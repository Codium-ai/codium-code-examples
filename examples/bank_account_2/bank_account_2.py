class BankAccount2:
    """ Create a new bank account """
    def __init__(self, name, hasCommissionDiscount):
        self._name = name
        self._hasCommissionDiscount = hasCommissionDiscount
        self._balance = 0
        self._commission_rate = BankAccount2._calc_commission_rate(hasCommissionDiscount)

    def info(self):
        """ Account information """
        return {
            "name": self._name,
            "current_balance": self._balance,
        }

    def deposit(self, amount):
        """ deposit money """
        if amount > 0:
            self._balance += amount + self._calc_commission_rate(self._hasCommissionDiscount)
        else:
            raise ValueError("deposit amount must be larger than 0")
        
    def balance(self):
        return self._balance

    def withdraw(self, amount):
        """ withdraw money """
        if self._balance >= amount > 0:
            self._balance -= (amount - self._calc_commission_rate(self._hasCommissionDiscount))
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
        else:
            raise ValueError("Insufficient funds for transfer")

    @staticmethod
    def _calc_commission_rate(hasCommisionDiscount):
        """ Get the rate of commission for this account """
        if hasCommisionDiscount:
            return 2.5
        else:
            return 5
