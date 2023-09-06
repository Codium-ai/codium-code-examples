import pytest

from examples.bank_account_2.bank_account_2 import BankAccount2


def test_deposit_positive_amount():
    gandalf = BankAccount2("Gandalf", True)
    initial_balance = gandalf.balance()
    gandalf.deposit(100)
    assert gandalf.balance() == initial_balance + 97.5

def test_withdraw_positive_amount():
    frodo = BankAccount2("Frodo", True)
    frodo.deposit(100)
    initial_balance = frodo.balance()
    frodo.withdraw(50)
    assert frodo.balance() == initial_balance - 52.5

def test_withdraw_more_than_balance():
    gandalf = BankAccount2("Gandalf", True)
    gandalf.deposit(100)
    with pytest.raises(ValueError):
        gandalf.withdraw(150)
