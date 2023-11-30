import pytest
from examples.bank_account_3_context_games.bank_account_3 import BankAccount3


class TestBankAccountSimpson:
    def setup_method(self):
        self.homer = BankAccount3("Homer", True)
        self.marge = BankAccount3("Marge", False)
    
    def test_deposit_with_commission_discount_true(self):
        initial_balance = self.homer.balance()
        deposit_amount = 100
        expected_commission = 1.5
        expected_balance = initial_balance + deposit_amount - expected_commission
        
        self.homer.deposit(deposit_amount)

        assert self.homer.balance() == expected_balance
