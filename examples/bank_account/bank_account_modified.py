class BankAccount:
    """Bank account with deposit, withdrawal, and transfer capabilities.
    
    Attributes:
        _name (str): Account holder's name.
        _balance (float): Current account balance.
        _hasCommissionDiscount (bool): Whether account has commission discount.
        _commission_rate (float): Commission rate applied to transactions.
    """
    def __init__(self, name, hasCommissionDiscount):
        """Initialize a new bank account.
        
        Args:
            name (str): Account holder's name.
            hasCommissionDiscount (bool): Whether to apply discounted commission rate.
        """
        self._name = name
        self._hasCommissionDiscount = hasCommissionDiscount
        self._balance = 0
        self._commission_rate = BankAccount._calc_commission_rate(hasCommissionDiscount)

    def info(self):
        """Retrieve account information.
        
        Returns:
            dict: Dictionary containing account name and current balance.
        """
        return {
            "name": self._name,
            "current_balance": self._balance,
        }

    def deposit(self, amount):
        """Deposit money into the account.
        
        Commission is deducted from the deposited amount.
        
        Args:
            amount (float): Amount to deposit.
            
        Raises:
            ValueError: If amount is not greater than 0.
        """
        if amount > 0:
            self._balance += amount - self._calc_commission_rate(self._hasCommissionDiscount)
        else:
            raise ValueError("deposit amount must be larger than 0")
        
    def balance(self):
        """Get the current account balance.
        
        Returns:
            float: Current balance after all transactions and commissions.
        """
        return self._balance

    def withdraw(self, amount):
        """Withdraw money from the account.
        
        Commission is added to the withdrawal amount.
        
        Args:
            amount (float): Amount to withdraw.
            
        Raises:
            ValueError: If balance is insufficient or amount is not greater than 0.
        """
        if self._balance >= amount > 0:
            self._balance -= (amount + self._calc_commission_rate(self._hasCommissionDiscount))
        else:
            raise ValueError("Insufficient funds for withdraw")
    
    def can_withdraw(self, amount):
        """Check if withdrawal is possible without commission.
        
        Args:
            amount (float): Amount to check.
            
        Returns:
            bool: True if balance is sufficient and amount is positive, False otherwise.
        """
        return self._balance >= amount > 0

    def transfer_to_other_account(self, amount, other_account):
        """Transfer money to another account.
        
        Commission is deducted from the sender's account; recipient receives the full amount.
        
        Args:
            amount (float): Amount to transfer.
            other_account (BankAccount): Recipient account.
            
        Raises:
            ValueError: If amount is not positive or balance is insufficient.
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
        """Calculate commission rate based on discount eligibility.
        
        Args:
            hasCommisionDiscount (bool): Whether account qualifies for discount.
            
        Returns:
            float: Commission rate (2.5 with discount, 9 without).
        """
        if hasCommisionDiscount:
            return 2.5
        else:
            return 9
