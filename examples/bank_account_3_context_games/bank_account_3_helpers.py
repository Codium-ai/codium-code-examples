MAX_DEPOSIT_PREMIUM = 1_000_000
MAX_DEPOSIT_NON_PREMIUM = 10_000

MAX_BALANCE_PREMIUM = 10_000_000
MAX_BALANCE_NON_PREMIUM = 100_000

def calc_commission_rate(is_premium_account):
    if is_premium_account:
        return 1.5
    else:
        return 8


def is_more_than_max_deposit(is_premium_account, deposit_amount):
    if is_premium_account:
        return deposit_amount > MAX_DEPOSIT_PREMIUM
    else:
        return deposit_amount > MAX_DEPOSIT_NON_PREMIUM


def is_deposit_over_balance(is_premium_account, deposit_amount, balance):
    expected_balance = balance + deposit_amount - calc_commission_rate(is_premium_account)

    if is_premium_account:
        return expected_balance > MAX_BALANCE_PREMIUM
    else:
        return expected_balance > MAX_BALANCE_NON_PREMIUM
