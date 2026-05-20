# Simple Python Hello World example

def main():
    print("Hello, world!")

if __name__ == "__main__":
    main()
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Dict, List, Optional

"""Simple in-memory BankAccount example.

Provides a BankAccount class with deposit, withdraw, transfer and transaction
history tracking. Amounts use Decimal for monetary precision and all timestamps
are recorded in UTC and timezone-aware.
"""


@dataclass
class Transaction:
    """Lightweight record describing a single account transaction.

    Attributes:
        type (str): A short transaction type (e.g., "deposit", "withdraw",
            "transfer_in", "transfer_out").
        gross_amount (Decimal): The gross amount involved in the transaction
            before commission.
        commission (Decimal): Commission charged for the transaction.
        net_amount (Decimal): Gross minus commission (amount that affected balance).
        balance_after (Decimal): Account balance after applying the transaction.
        timestamp (datetime): UTC timestamp when the transaction was recorded.
    """
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
    """

    # Fixed fees (Decimal) for clarity — name uses "fee" not "rate" because these are absolute amounts
    _STANDARD_COMMISSION_FEE = Decimal("5.00")
    _DISCOUNTED_COMMISSION_FEE = Decimal("2.50")

    def __init__(self, name: str, has_commission_discount: bool) -> None:
        self._name: str = name
        self._has_commission_discount: bool = has_commission_discount
        self._balance: Decimal = Decimal("0.00")
        self._commission_fee: Decimal = (
            BankAccount._calc_commission_fee(self._has_commission_discount)
        )
        self._transactions: List[Dict] = []

    def info(self) -> Dict[str, object]:
        """Return basic account info as a dict.

        Returns:
            dict: name and current_balance.
        """
        return {"name": self._name, "current_balance": self._balance}

    def _record_transaction(self, type_: str, gross: Decimal, commission: Decimal, balance_after: Decimal) -> None:
        """Append a transaction entry to the in-memory history.

        Transactions store both gross and commission so consumers know the breakdown.
        Timestamps are recorded in UTC and are timezone-aware.
        """
        tx = Transaction(
            type=type_,
            gross_amount=gross,
            commission=commission,
            net_amount=(gross - commission),
            balance_after=balance_after,
            timestamp=datetime.now(timezone.utc),
        )
        # store plain dicts to keep simple serializable structures
        self._transactions.append({
            "type": tx.type,
            "gross_amount": tx.gross_amount,
            "commission": tx.commission,
            "net_amount": tx.net_amount,
            "balance_after": tx.balance_after,
            "timestamp": tx.timestamp,
        })

    def get_transaction_history(self, last_n: Optional[int] = None) -> List[Dict]:
        """Return a deep copy of transaction history. If last_n is provided, return the most recent N entries.

        Copies are returned to prevent external mutation of internal state.
        """
        # return copies so callers cannot mutate internal state
        copied = [t.copy() for t in self._transactions]
        if last_n is None:
            return copied
        return copied[-last_n:]

    def _to_decimal(self, amount) -> Decimal:
        """Convert numeric input to Decimal with two decimal places precision.

        Raises ValueError on invalid input.
        """
        try:
            d = Decimal(str(amount)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        except (InvalidOperation, ValueError, TypeError):
            raise ValueError("Amount must be a numeric value")
        return d

    def deposit(self, amount) -> None:
        """Deposit amount into the account after deducting commission.

        Raises:
            ValueError: if amount is not positive.
        """
        gross = self._to_decimal(amount)
        if gross <= Decimal("0.00"):
            raise ValueError("Deposit amount must be greater than 0.")
        commission = self._commission_fee
        net = gross - commission
        self._balance += net
        self._record_transaction("deposit", gross, commission, self._balance)

    def balance(self) -> Decimal:
        """Return current balance."""
        return self._balance

    def withdraw(self, amount) -> None:
        """Withdraw amount plus commission from the account.

        Raises:
            ValueError: if amount is not positive or funds are insufficient.
        """
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
        """Receive funds from another account. Public method to preserve encapsulation.

        Records a transfer_in transaction. The sender is responsible for deducting commission.
        """
        gross = self._to_decimal(amount)
        if gross <= Decimal("0.00"):
            raise ValueError("Receive amount must be greater than 0.")
        self._balance += gross
        self._record_transaction("transfer_in", gross, Decimal("0.00"), self._balance)

    def transfer(self, amount, other_account: "BankAccount") -> None:
        """Transfer amount to another account. Sender pays commission; recipient gets full amount.

        Raises:
            ValueError: if amount is not positive or funds are insufficient.
        """
        gross = self._to_decimal(amount)
        if gross <= Decimal("0.00"):
            raise ValueError("Transfer amount must be greater than 0.")
        commission = self._commission_fee
        total = gross + commission
        if self._balance < total:
            raise ValueError("Insufficient funds for transfer.")
        self._balance -= total
        # Use public API to give money to the other account
        other_account.receive(gross, from_account=self)
        self._record_transaction("transfer_out", gross, commission, self._balance)

    @staticmethod
    def _calc_commission_fee(has_commission_discount: bool) -> Decimal:
        """Calculate and return the commission fee for account operations.

        This internal helper chooses between a standard and a discounted fixed
        commission fee based on the account's discount flag. The method always
        returns a Decimal with two-decimal-place precision representing the
        absolute fee amount (not a percentage).

        Args:
            has_commission_discount (bool): If True, return the discounted fee;
                otherwise return the standard fee.

        Returns:
            Decimal: The commission fee to apply to transactions.
        """
        return BankAccount._DISCOUNTED_COMMISSION_FEE if has_commission_discount else BankAccount._STANDARD_COMMISSION_FEE