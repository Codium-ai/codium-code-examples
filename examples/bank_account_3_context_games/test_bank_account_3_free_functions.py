from examples.bank_account_3_context_games.bank_account_3 import BankAccount3

def test_deposit_with_premium_account_true():
    homer = BankAccount3("Homer", True)
    initial_balance = homer.balance()
    deposit_amount = 100
    expected_commission = 1.5
    expected_balance = initial_balance + deposit_amount - expected_commission
    
    homer.deposit(deposit_amount)

    assert homer.balance() == expected_balance
