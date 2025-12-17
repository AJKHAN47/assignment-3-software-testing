import unittest
from src.login import login

class TestLogin(unittest.TestCase):

    def test_valid_login(self):
        self.assertEqual(login("admin", "admin123"), "Login successful")

    def test_invalid_password(self):
        self.assertEqual(login("admin", "wrong123"), "Invalid credentials")

    def test_empty_fields(self):
        self.assertEqual(login("", ""), "Fields cannot be empty")

if __name__ == "__main__":
    unittest.main()
