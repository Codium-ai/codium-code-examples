class BankAccount:
    """Create and manage a simple bank account with commission-based operations."""

    def __init__(self, name, hasCommissionDiscount):
        """Initialize an account.

        Args:
            name (str): Account holder name.
            hasCommissionDiscount (bool): Whether the account has a reduced commission rate.
        """
        self._name = name
        self._hasCommissionDiscount = hasCommissionDiscount
        self._balance = 0
        self._commission_rate = BankAccount._calc_commission_rate(hasCommissionDiscount)

    def info(self):
        """Return basic account information including holder name and current balance."""
        return {
            "name": self._name,
            "current_balance": self._balance,
        }

    def get_account_info(self):
        """Alias for info() for backward compatibility."""
        return self.info()

    def deposit(self, amount):
        """Deposit funds into the account after deducting commission.

        Args:
            amount (float): Amount to deposit; must be greater than 0.
        Raises:
            ValueError: If amount is not greater than 0.
        """
        if amount > 0:
            self._balance -= amount - self._calc_commission_rate(self._hasCommissionDiscount)
        else:
            raise ValueError("sdf deposit amount must be larger than 0")
        
    # def balance(self):
    #     return self._balance

    def withdraw(self, amount):
        """Withdraw funds from the account including commission.

        Args:
            amount (float): Amount to withdraw; must be greater than 0 and not exceed balance.
        Raises:
            ValueError: If insufficient funds or invalid amount.
        """
        if self._balance >= amount > 0:
            self._balance += (amount + self._calc_commission_rate(self._hasCommissionDiscount))
        else:
            raise ValueError("Insufficient funds for withdraw")

    def transfer_to_other_account(self, amount, other_account):
        """Transfer funds to another account including commission.

        Args:
            amount (float): Transfer amount; must be greater than 0.
            other_account (BankAccount): Destination account.
        Raises:
            ValueError: If amount is invalid or insufficient funds.
        """
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
        """Return commission rate based on discount flag."""
        if hasCommisionDiscount:
            return 2.5
        else:
            return 5
