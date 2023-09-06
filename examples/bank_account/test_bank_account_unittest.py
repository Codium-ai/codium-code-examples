
import unittest

from .bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount("John", True)
        self.account2 = BankAccount("Jane", False)

    def test_deposit_positive_amount(self):
        initial_balance = self.account1.balance()
        self.account1.deposit(100)
        self.assertEqual(self.account1.balance(), initial_balance + 97.5)

    def test_withdraw_positive_amount(self):
        self.account1.deposit(100)
        initial_balance = self.account1.balance()
        self.account1.withdraw(50)
        self.assertEqual(self.account1.balance(), initial_balance - 52.5)

    def test_withdraw_more_than_balance(self):
        self.account1.deposit(100)
        with self.assertRaises(ValueError):
            self.account1.withdraw(150)

    def test_transfer_more_than_balance(self):
        self.account1.deposit(100)
        with self.assertRaises(ValueError):
            self.account1.transfer_to_other_account(150, self.account2)

    def test_transfer_positive_amount(self):
        self.account1.deposit(100)
        initial_balance1 = self.account1.balance()
        initial_balance2 = self.account2.balance()
        self.account1.transfer_to_other_account(50, self.account2)
        self.assertEqual(self.account1.balance(), initial_balance1 - 52.5)
        self.assertEqual(self.account2.balance(), initial_balance2 + 50)

    def test_deposit_zero_amount(self):
        initial_balance = self.account1.balance()
        self.account1.deposit(0)
        self.assertEqual(self.account1.balance(), initial_balance)

if __name__ == '__main__':
    unittest.main()
