class InsufficientFundsError(ValueError):
    """Raised when account has insufficient funds for an operation."""
    pass


class InvalidAmountError(ValueError):
    """Raised when transaction amount is invalid (zero or negative)."""
    pass


class BankAccount2:
    """Bank account with commission handling.
    
    This class manages a bank account with transaction fees (commissions).
    Accounts can have a commission discount, reducing fees from 5.0 to 2.5 units.
    
    Attributes:
        name: Account holder's name
        has_commission_discount: Whether the account has reduced commission rates
        
    Example:
        >>> account = BankAccount2("Alice", has_commission_discount=True)
        >>> account.deposit(100)  # Balance increases by 97.5 (100 - 2.5 commission)
        >>> account.balance()
        97.5
    """

    def __init__(self, name: str, has_commission_discount: bool):
        self._name = name
        self._has_commission_discount = has_commission_discount
        self._balance = 0.0
        self._commission_rate = self._calc_commission_rate(has_commission_discount)

    def info(self) -> dict:
        """Return account information.
        
        Returns:
            Dictionary with account name and current balance.
        """
        return {"name": self._name, "current_balance": self._balance}

    def deposit(self, amount: float) -> None:
        """Deposit money into the account.
        
        The deposited amount is reduced by the commission fee.
        
        Args:
            amount: Amount to deposit (must be positive)
            
        Raises:
            InvalidAmountError: If amount is not positive
        """
        self._validate_amount(amount)
        self._balance += amount - self._commission_rate

    def balance(self) -> float:
        """Get the current account balance.
        
        Returns:
            Current balance as a float
        """
        return self._balance

    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account.
        
        The withdrawn amount plus commission fee is deducted from the balance.
        
        Args:
            amount: Amount to withdraw (must be positive)
            
        Raises:
            InvalidAmountError: If amount is not positive
            InsufficientFundsError: If balance is insufficient for withdrawal + commission
        """
        self._validate_amount(amount)
        total = amount + self._commission_rate
        if self._balance < total:
            raise InsufficientFundsError(
                f"Insufficient funds for withdraw: need {total}, have {self._balance}"
            )
        self._balance -= total

    def transfer_to_other_account(self, amount: float, other_account: "BankAccount2") -> None:
        """Transfer money to another account.
        
        The sender pays the commission; the receiver gets the full amount.
        
        Args:
            amount: Amount to transfer (must be positive)
            other_account: Target BankAccount2 instance
            
        Raises:
            InvalidAmountError: If amount is not positive
            InsufficientFundsError: If balance is insufficient for transfer + commission
        """
        self._validate_amount(amount)
        total = amount + self._commission_rate
        if self._balance < total:
            raise InsufficientFundsError(
                f"Insufficient funds for transfer: need {total}, have {self._balance}"
            )
        self._balance -= total
        other_account._balance += amount

    def get_commission_rate(self) -> float:
        """Get the commission rate for this account.
        
        Returns:
            Commission rate (2.5 with discount, 5.0 without)
        """
        return self._commission_rate

    def can_withdraw(self, amount: float) -> bool:
        """Check if withdrawal is possible without raising an exception.
        
        Args:
            amount: Amount to check (must be positive)
            
        Returns:
            True if withdrawal is possible, False otherwise
        """
        if amount <= 0:
            return False
        return self._balance >= amount + self._commission_rate

    def can_transfer(self, amount: float) -> bool:
        """Check if transfer is possible without raising an exception.
        
        Args:
            amount: Amount to check (must be positive)
            
        Returns:
            True if transfer is possible, False otherwise
        """
        if amount <= 0:
            return False
        return self._balance >= amount + self._commission_rate

    def _validate_amount(self, amount: float) -> None:
        """Validate that amount is positive.
        
        Args:
            amount: Amount to validate
            
        Raises:
            InvalidAmountError: If amount is not positive
        """
        if amount <= 0:
            raise InvalidAmountError("Amount must be larger than 0")

    @staticmethod
    def _calc_commission_rate(has_commission_discount: bool) -> float:
        """Calculate commission rate based on discount status.
        
        Args:
            has_commission_discount: Whether account has commission discount
            
        Returns:
            Commission rate (2.5 with discount, 5.0 without)
        """
        return 2.5 if has_commission_discount else 5.0
