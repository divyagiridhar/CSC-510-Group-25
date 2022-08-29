import sys

sys.path.insert(0, '../CSC-510_group-25/code')

import unittest

from setup import factorial
from fibo import fibonacci

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
