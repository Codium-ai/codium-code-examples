from datetime import datetime


class BankAccount2:
    """ Create a new bank account """
    def __init__(self, name, hasCommissionDiscount):
        self._name = name
        self._hasCommissionDiscount = hasCommissionDiscount
        self._balance = 0
        self._commission_rate = BankAccount2._calc_commission_rate(hasCommissionDiscount)
        self._transactions = []

    def info(self):
        """ Account information """
        return {
            "name": self._name,
            "current_balance": self._balance,
        }

    def info_test(self):
        """ Account information """
        # Deprecated test helper: return same info as `info()` and close the dict properly
        return {
            "name": self._name,
            "current_balance": self._balance,
        }

    def _record_transaction(self, type, amount, balance_after):
        """ Record a transaction in the history """
        self._transactions.append({
            "type": type,
            "amount": amount,
            "balance_after": balance_after,
            "timestamp": datetime.now(),
        })

    def get_transaction_history(self, last_n=None):
        """ Return transaction history, optionally limited to the last N entries """
        if last_n is None:
            return list(self._transactions)
        return list(self._transactions[-last_n:])

    def deposit(self, amount):
        """ deposit money """
        if amount > 0:
            self._balance += amount - self._calc_commission_rate(self._hasCommissionDiscount)
            self._record_transaction("deposit", amount, self._balance)
        else:
            raise ValueError("deposit amount must be larger than 0")
        
    def balance(self):
        return self._balance

    def withdraw(self, amount):
        """ withdraw money """
        if self._balance >= amount > 0:
            self._balance -= (amount + self._calc_commission_rate(self._hasCommissionDiscount))
            self._record_transaction("withdrawal", amount, self._balance)
        else:
            raise ValueError("Insufficient funds for withdraw")

    def transfer_to_other_account(self, amount, other_account):
        """ transfer money """
        if amount <= 0:
            raise ValueError("Transfer amount must be larger than 0")
        amount_including_commission = amount + self._commission_rate
        if self._balance >= amount_including_commission > 0:
            self._balance -= amount_including_commission
            other_account._balance += amount
            self._record_transaction("transfer_out", amount, self._balance)
            other_account._record_transaction("transfer_in", amount, other_account._balance)
        else:
            raise ValueError("Insufficient funds for transfer")

    @staticmethod
    def _calc_commission_rate(hasCommisionDiscount):
        """ Get the rate of commission for this account """
        if hasCommisionDiscount:
            return 2.5
        else:
            return 5
