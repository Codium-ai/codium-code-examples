from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Dict, List, Optional


@dataclass(frozen=True)
class Transaction:
    type: str
    gross_amount: Decimal
    commission: Decimal
    net_amount: Decimal
    balance_after: Decimal
    timestamp: datetime


class BankAccount:
    """Bank account with deposit, withdrawal and transfer support.

    Args:
        name (str): Account holder name.
        has_commission_discount (bool): Whether the account uses a discounted commission.
        currency (str): Currency code (e.g. "USD"). Transfers between accounts with
            different currencies are rejected.
    """

    _STANDARD_COMMISSION_FEE = Decimal("5.00")
    _DISCOUNTED_COMMISSION_FEE = Decimal("2.50")

    def __init__(self, name: str, has_commission_discount: bool, currency: str = "USD") -> None:
        self._name: str = name
        self._has_commission_discount: bool = has_commission_discount
        self._balance: Decimal = Decimal("0.00")
        self._commission_fee: Decimal = (
            BankAccount._calc_commission_fee(self._has_commission_discount)
        )
        # store Transaction instances (immutable)
        self._transactions: List[Transaction] = []
        # currency code for the account
        self._currency: str = currency

    def info(self) -> Dict[str, object]:
        return {"name": self._name, "current_balance": self._balance, "currency": self._currency}

    def _record_transaction(self, type_: str, gross: Decimal, commission: Decimal, balance_after: Decimal) -> None:
        tx = Transaction(
            type=type_,
            gross_amount=gross,
            commission=commission,
            net_amount=(gross - commission),
            balance_after=balance_after,
            timestamp=datetime.now(timezone.utc),
        )
        # store the immutable Transaction instance
        self._transactions.append(tx)

    def get_transaction_history(self, last_n: Optional[int] = None) -> List[Dict]:
        """Return a list of transactions as dicts (copies) in chronological order.

        We keep the public API returning dicts for backward compatibility, but
        internally transactions are immutable Transaction instances to prevent
        accidental mutation.
        """
        txs = self._transactions if last_n is None else self._transactions[-last_n:]
        # return shallow dict copies converted from dataclass to keep types like Decimal and datetime
        return [asdict(t) for t in txs]

    def _to_decimal(self, amount) -> Decimal:
        """Convert amount to Decimal rounded to 2 decimal places.

        Accepts Decimal, int, float or numeric string. If a Decimal is passed,
        it will be quantized to 2 decimal places. Raises ValueError for invalid input.
        """
        try:
            if isinstance(amount, Decimal):
                d = amount
            else:
                # Convert through str to avoid binary float issues
                d = Decimal(str(amount))
            # ensure two decimal places with HALF_UP rounding
            return d.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        except (InvalidOperation, ValueError, TypeError):
            raise ValueError("Amount must be a numeric value convertible to Decimal with 2 fractional digits")

    def deposit(self, amount) -> None:
        gross = self._to_decimal(amount)
        if gross <= Decimal("0.00"):
            raise ValueError("Deposit amount must be greater than 0.")
        if gross < self._commission_fee:
            raise ValueError("Deposit amount must be at least equal to the commission fee.")
        commission = self._commission_fee
        net = gross - commission
        self._balance += net
        self._record_transaction("deposit", gross, commission, self._balance)

    def balance(self) -> Decimal:
        return self._balance

    def withdraw(self, amount) -> None:
        gross = self._to_decimal(amount)
        if gross <= Decimal("0.00"):
            raise ValueError("Withdrawal amount must be greater than 0.")
        commission = self._commission_fee
        total = gross + commission
        if self._balance < total:
            raise ValueError("Insufficient funds for withdrawal.")
        self._balance -= total
        self._record_transaction("withdraw", gross, commission, self._balance)

    def receive(self, amount, from_account: Optional["BankAccount"] = None) -> None:
        gross = self._to_decimal(amount)
        if gross <= Decimal("0.00"):
            raise ValueError("Receive amount must be greater than 0.")
        # if sender provided, ensure currency matches
        if from_account is not None and from_account._currency != self._currency:
            raise ValueError("Currency mismatch: cannot receive funds from account with different currency")
        self._balance += gross
        self._record_transaction("transfer_in", gross, Decimal("0.00"), self._balance)

    def transfer(self, amount, other_account: "BankAccount") -> None:
        gross = self._to_decimal(amount)
        if gross <= Decimal("0.00"):
            raise ValueError("Transfer amount must be greater than 0.")
        # ensure currency matches
        if other_account._currency != self._currency:
            raise ValueError("Currency mismatch: cannot transfer between different currencies")
        commission = self._commission_fee
        total = gross + commission
        if self._balance < total:
            raise ValueError("Insufficient funds for transfer.")
        self._balance -= total
        other_account.receive(gross, from_account=self)
        self._record_transaction("transfer_out", gross, commission, self._balance)

    def currency(self) -> str:
        return self._currency

    @staticmethod
    def _calc_commission_fee(has_commission_discount: bool) -> Decimal:
        return BankAccount._DISCOUNTED_COMMISSION_FEE if has_commission_discount else BankAccount._STANDARD_COMMISSION_FEE
