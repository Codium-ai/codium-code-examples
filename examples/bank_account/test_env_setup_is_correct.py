from .bank_account import BankAccount

def test_bank_account_env_setup_correct():
    """
    This is a sanity test to make sure that imports and paths work.
    Just create an instance of the class.
    """
    BankAccount("foo bar", True)
