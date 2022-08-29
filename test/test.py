import unittest

from CSC-510-Group-25.code.setup import factorial
from CSC-510-Group-25.code.fibo import fibonacci

class TestReturnValues(unittest.TestCase):
    
    def test_factorial(self):
        """
        Test for a known return value
        """
        self.assertEqual(factorial(5), 120)

    def test_fibonacci(self):
        """
        Test for a known return value
        """
        self.assertEqual(fibonacci(9), 34)
