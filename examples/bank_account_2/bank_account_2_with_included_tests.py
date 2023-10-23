class BankAccount2:
    """ Create a new bank account """
    def __init__(self, name, hasCommissionDiscount):
        self._name = name
        self._hasCommissionDiscount = hasCommissionDiscount
        self._balance = 0
        self._commission_rate = BankAccount2._calc_commission_rate(hasCommissionDiscount)

    def info(self):
        """ Account information """
        return {
            "name": self._name,
            "current_balance": self._balance,
        }

    def deposit(self, amount):
        """ deposit money """
        if amount > 0:
            self._balance += amount - self._calc_commission_rate(self._hasCommissionDiscount)
        else:
            raise ValueError("deposit amount must be larger than 0")
        
    def balance(self):
        return self._balance

    def withdraw(self, amount):
        """ withdraw money """
        if self._balance >= amount > 0:
            self._balance -= (amount + self._calc_commission_rate(self._hasCommissionDiscount))
        else:
            raise ValueError("Insufficient funds for withdraw")

    def transfer_to_other_account(self, amount, other_account):
        """ transfer money """
        if amount <= 0:
            raise ValueError("Transfer amount must be larger than 0")
        amount_including_commission = amount + self._commission_rate
        if self._balance >= amount_including_commission > 0:
            self._balance -= amount_including_commission
            other_account._balance += amount
        else:
            raise ValueError("Insufficient funds for transfer")

    @staticmethod
    def _calc_commission_rate(hasCommisionDiscount):
        """ Get the rate of commission for this account """
        if hasCommisionDiscount:
            return 2.5
        else:
            return 5


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

    # Cannot transfer a negative amount from one bank account to another
def test_transfer_negative_amount():
    gandalf = BankAccount2("Gandalf", True)
    aragorn = BankAccount2("Aragorn", False)
    gandalf.deposit(200)
    with pytest.raises(ValueError):
        gandalf.transfer_to_other_account(-100, aragorn)

    # Can transfer a positive amount from one bank account to another
def test_transfer_positive_amount():
    frodo = BankAccount2("Frodo", True)
    gandalf = BankAccount2("Gandalf", False)
    frodo.deposit(200)
    gandalf.deposit(0)
    initial_frodo_balance = frodo.balance()
    initial_gandalf_balance = gandalf.balance()
    frodo.transfer_to_other_account(100, gandalf)
    assert frodo.balance() == initial_frodo_balance - 102.5
    assert gandalf.balance() == initial_gandalf_balance + 100

    # Cannot deposit a negative amount into the bank account
def test_deposit_negative_amount():
    gandalf = BankAccount2("Gandalf", True)
    with pytest.raises(ValueError):
        gandalf.deposit(-50)

    # Cannot withdraw a negative amount from the bank account
def test_withdraw_negative_amount():
    frodo = BankAccount2("Frodo", True)
    frodo.deposit(100)
    with pytest.raises(ValueError):
        frodo.withdraw(-50)


