import unittest
from calculator import Calculator

def test_add()->None:
    '''test add'''
    calc = Calculator()
    calc.add(10, 5)
    assert calc.add(10, 5) == 10


