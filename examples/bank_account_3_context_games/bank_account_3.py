from examples.bank_account_3_context_games.bank_account_3_helpers import calc_commission_rate, is_deposit_over_balance, is_more_than_max_deposit


class BankAccount3:
    """ Create a new bank account """
    def __init__(self, name, is_premium_account):
        self._name = name
        self._is_premium_account = is_premium_account
        self._balance = 0

    def deposit(self, amount):
        """ deposit money """
        if amount <= 0:
            raise IOError("deposit amount must be larger than 0")
        
        if is_more_than_max_deposit(self._is_premium_account, amount):
            raise ValueError("deposit amount exceeds maximum allowed")
        
        if is_deposit_over_balance(self._is_premium_account, amount, self._balance):
            raise ValueError("deposit amount will exceed maximum allowed balance")
        
        self._balance += amount - calc_commission_rate(self._is_premium_account)

    def balance(self):
        return self._balance
