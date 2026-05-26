import pytest

from examples.bank_account_2.bank_account_2 import (
    BankAccount2,
    InsufficientFundsError,
    InvalidAmountError,
)

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


# New tests added below to cover additional behaviors
class TestBankAccountAdditional:
    def setup_method(self):
        self.acc_discount = BankAccount2("Alice", True)
        self.acc_no_discount = BankAccount2("Bob", False)

    def test_deposit_zero_raises(self):
        with pytest.raises(ValueError):
            self.acc_discount.deposit(0)

    def test_withdraw_zero_raises(self):
        with pytest.raises(ValueError):
            self.acc_discount.withdraw(0)

    def test_calc_commission_rate_values(self):
        # Using internal static method to ensure commission values are as expected
        assert BankAccount2._calc_commission_rate(True) == 2.5
        assert BankAccount2._calc_commission_rate(False) == 5.0

    def test_failed_transfer_does_not_change_other_account(self):
        # Ensure other account balance is unchanged if transfer fails
        self.acc_discount.deposit(10)  # after commission: 7.5
        other = BankAccount2("Other", False)
        before = other.balance()
        with pytest.raises(ValueError):
            self.acc_discount.transfer_to_other_account(100, other)
        assert other.balance() == before

    def test_info_includes_name_and_balance(self):
        self.acc_no_discount.deposit(50)
        info = self.acc_no_discount.info()
        assert info["name"] == "Bob"
        assert info["current_balance"] == self.acc_no_discount.balance()

    def test_get_commission_rate(self):
        assert self.acc_discount.get_commission_rate() == 2.5
        assert self.acc_no_discount.get_commission_rate() == 5.0

    def test_can_withdraw_sufficient_funds(self):
        self.acc_discount.deposit(100)  # balance: 97.5
        assert self.acc_discount.can_withdraw(50) is True
        assert self.acc_discount.can_withdraw(95) is True

    def test_can_withdraw_insufficient_funds(self):
        self.acc_discount.deposit(100)  # balance: 97.5
        assert self.acc_discount.can_withdraw(100) is False
        assert self.acc_discount.can_withdraw(150) is False

    def test_can_withdraw_invalid_amount(self):
        assert self.acc_discount.can_withdraw(0) is False
        assert self.acc_discount.can_withdraw(-50) is False

    def test_can_transfer_sufficient_funds(self):
        self.acc_discount.deposit(100)  # balance: 97.5
        assert self.acc_discount.can_transfer(50) is True

    def test_can_transfer_insufficient_funds(self):
        self.acc_discount.deposit(100)  # balance: 97.5
        assert self.acc_discount.can_transfer(100) is False

    def test_invalid_amount_error_on_deposit(self):
        with pytest.raises(InvalidAmountError):
            self.acc_discount.deposit(-10)

    def test_insufficient_funds_error_on_withdraw(self):
        self.acc_discount.deposit(10)  # balance: 7.5
        with pytest.raises(InsufficientFundsError):
            self.acc_discount.withdraw(100)

    def test_insufficient_funds_error_on_transfer(self):
        self.acc_discount.deposit(10)  # balance: 7.5
        with pytest.raises(InsufficientFundsError):
            self.acc_discount.transfer_to_other_account(100, self.acc_no_discount)
