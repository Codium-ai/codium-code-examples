import pytest

from examples.bank_account.bank_account import BankAccount

class TestBankAccount:
    def setup_method(self):
        self.account1 = BankAccount("John", True)
        self.account2 = BankAccount("Jane", False)

    # Tests that depositing a positive amount increases the account balance. 
    def test_deposit_positive_amount(self):
        initial_balance = self.account1.balance()
        self.account1.deposit(100)
        assert self.account1.balance() == initial_balance + 97.5

    # Tests that withdrawing a positive amount decreases the account balance. 
    def test_withdraw_positive_amount(self):
        self.account1.deposit(100)
        initial_balance = self.account1.balance()
        self.account1.withdraw(50)
        assert self.account1.balance() == initial_balance - 52.5

    # Tests that trying to withdraw more money than the account balance raises a ValueError. 
    def test_withdraw_more_than_balance(self):
        self.account1.deposit(100)
        with pytest.raises(ValueError):
            self.account1.withdraw(150)

    # Tests that trying to transfer more money than the account balance raises a ValueError. 
    def test_transfer_more_than_balance(self):
        self.account1.deposit(100)
        with pytest.raises(ValueError):
            self.account1.transfer_to_other_account(150, self.account2)

    
    # Tests that transferring a positive amount between two accounts decreases the balance of the sender and increases the balance of the receiver. 
    def test_transfer_positive_amount(self):
        self.account1.deposit(100)
        initial_balance1 = self.account1.balance()
        initial_balance2 = self.account2.balance()
        self.account1.transfer_to_other_account(50, self.account2)
        assert self.account1.balance() == initial_balance1 - 52.5
        assert self.account2.balance() == initial_balance2 + 50
