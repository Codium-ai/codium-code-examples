import pytest

from examples.bank_account.bank_account import BankAccount


def test_deposit_positive_amount():
    gandalf = BankAccount("Gandalf", True)
    initial_balance = gandalf.balance()
    gandalf.deposit(100)
    assert gandalf.balance() == initial_balance + 97.5

def test_withdraw_positive_amount():
    frodo = BankAccount("Frodo", True)
    frodo.deposit(100)
    initial_balance = frodo.balance()
    frodo.withdraw(50)
    assert frodo.balance() == initial_balance - 52.5

def test_withdraw_more_than_balance():
    gandalf = BankAccount("Gandalf", True)
    gandalf.deposit(100)
    with pytest.raises(ValueError):
        gandalf.withdraw(150)
