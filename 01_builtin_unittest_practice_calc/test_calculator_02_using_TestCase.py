'''Test for calculator using built-in unittest'''

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    '''Inherit TestCase and implement test cases'''

    def test_add(self,):
        '''Test add function'''
        calc = Calculator()
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)


    def test_subtract(self):
        '''Test subtract function'''
        calc = Calculator()
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)


    def test_multiply(self):
        '''Test multiply function'''
        calc = Calculator()
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)


    def test_divide(self):
        '''Test divide function'''
        calc = Calculator()
        self.assertEqual(calc.divide(10, 5), 3)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)


if __name__=='__main__':
    unittest.main()
