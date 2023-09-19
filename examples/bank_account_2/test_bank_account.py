import pytest

from examples.bank_account_2.bank_account_2 import BankAccount2

class TestBankAccount2:
    def setup_method(self):
        self.account1 = BankAccount2("John", True)
        self.account2 = BankAccount2("Jane", False)

    # Tests that depositing a positive amount increases the account balance. 
    def test_deposit_positive_amount(self):
        initial_balance = self.account1.balance()
        self.account1.deposit(100)
        assert self.account1.balance() == initial_balance + 97.5

    def test_withdraw_positive_amount(self):
        self.account1.deposit(100)
        initial_balance = self.account1.balance()
        self.account1.withdraw(50)
        assert self.account1.balance() == initial_balance - 52.5

    def test_withdraw_more_than_balance(self):
        self.account1.deposit(100)
        with pytest.raises(ValueError):
            self.account1.withdraw(150)

    def test_transfer_more_than_balance(self):
        self.account1.deposit(100)
        with pytest.raises(ValueError):
            self.account1.transfer_to_other_account(150, self.account2)

    
    def test_transfer_positive_amount(self):
        self.account1.deposit(100)
        initial_balance1 = self.account1.balance()
        initial_balance2 = self.account2.balance()
        self.account1.transfer_to_other_account(50, self.account2)
        assert self.account1.balance() == initial_balance1 - 52.5
        assert self.account2.balance() == initial_balance2 + 50



class TestBankAccountSimpson:
    def setup_method(self):
        self.homer = BankAccount2("Homer", True)
        self.marge = BankAccount2("Marge", False)
    
    def test_deposit_negative_amount(self):
        with pytest.raises(ValueError):
            self.homer.deposit(-100)
