import unittest
from setup import factorial

class TestReturnValues(unittest.TestCase):
    def test_factorial(self):
        """
        Test for a known return value
        """
        self.assertEqual(factorial(5), 120)

