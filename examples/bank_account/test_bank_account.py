import pytest
from decimal import Decimal
from examples.bank_account.bank_account import BankAccount


def test_deposit_applies_commission_and_records_transaction():
    acc = BankAccount("Alice2", has_commission_discount=False)
    acc.deposit("100.00")
    assert acc.balance() == Decimal("95.00")
    history = acc.get_transaction_history()
    assert history[-1]["type"] == "deposit"
    assert history[-1]["gross_amount"] == Decimal("100.00")
    assert history[-1]["commission"] == Decimal("5.00")


def test_withdraw_requires_sufficient_funds_and_records_transaction():
    acc = BankAccount("Bob", has_commission_discount=True)
    acc.deposit("50.00")  # net will be 47.50
    acc.withdraw("10.00")
    # after withdraw: 47.50 - (10 + 2.5) = 35.00
    assert acc.balance() == Decimal("35.00")
    history = acc.get_transaction_history()
    assert history[-1]["type"] == "withdraw"


def test_transfer_moves_funds_between_accounts_and_records_both_sides():
    a = BankAccount("A", has_commission_discount=False)
    b = BankAccount("B", has_commission_discount=False)
    a.deposit("200.00")
    a.transfer("50.00", b)
    assert a.balance() == Decimal("140.00")  # 200-5 deposit ->195 then - (50+5)=140
    # validate transfer resulted in received gross on B
    bh = b.get_transaction_history()
    assert bh[-1]["type"] == "transfer_in"
    assert bh[-1]["gross_amount"] == Decimal("50.00")


def test_amount_parsing_rejects_invalid_input():
    acc = BankAccount("Eve", has_commission_discount=False)
    with pytest.raises(ValueError):
        acc.deposit("not-a-number")
    with pytest.raises(ValueError):
        acc.withdraw(None)


def test_get_transaction_history_last_n_returns_recent_items():
    acc = BankAccount("Zed", has_commission_discount=False)
    acc.deposit("100.00")
    acc.deposit("50.00")
    acc.deposit("25.00")
    hist = acc.get_transaction_history(last_n=2)
    assert len(hist) == 2
    assert hist[0]["gross_amount"] == Decimal("50.00")
    assert hist[1]["gross_amount"] == Decimal("25.00")


# New tests added below

def test_deposit_zero_or_negative_raises():
    acc = BankAccount("Min", has_commission_discount=False)
    with pytest.raises(ValueError):
        acc.deposit("0.00")
    with pytest.raises(ValueError):
        acc.deposit("-10.00")


def test_withdraw_zero_or_negative_raises():
    acc = BankAccount("MinW", has_commission_discount=False)
    with pytest.raises(ValueError):
        acc.withdraw("0.00")
    with pytest.raises(ValueError):
        acc.withdraw("-5")


def test_transfer_zero_or_negative_raises():
    a = BankAccount("T1", has_commission_discount=False)
    b = BankAccount("T2", has_commission_discount=False)
    a.deposit("100.00")
    with pytest.raises(ValueError):
        a.transfer("0.00", b)
    with pytest.raises(ValueError):
        a.transfer("-1", b)


def test_commission_fee_respects_discount_flag():
    std = BankAccount("Std", has_commission_discount=False)
    disc = BankAccount("Disc", has_commission_discount=True)
    # deposit same gross amount and inspect commission in last transaction
    std.deposit("100.00")
    disc.deposit("100.00")
    sh = std.get_transaction_history()
    dh = disc.get_transaction_history()
    assert sh[-1]["commission"] == Decimal("5.00")
    assert dh[-1]["commission"] == Decimal("2.50")


def test_transaction_history_is_copied_on_get():
    acc = BankAccount("Copy", has_commission_discount=False)
    acc.deposit("100.00")
    hist = acc.get_transaction_history()
    # Mutate returned history copy and ensure internal history is unchanged
    hist.append({"type": "fake", "gross_amount": Decimal("1.00")})
    internal = acc.get_transaction_history()
    # last real transaction should still be deposit with 100.00
    assert internal[-1]["type"] == "deposit"
    assert internal[-1]["gross_amount"] == Decimal("100.00")
