import unittest
from string_calculator import add  # Importing the add function from string_calculator.py

class TestStringCalculator(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(add(""), 0)

if __name__ == "__main__":
    unittest.main()
