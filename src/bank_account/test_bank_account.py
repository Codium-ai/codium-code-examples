from .BankAccount import BankAccount

def test_sanity():
    bank_account = BankAccount("foo bar", True)
    assert bank_account.balance() == 0
