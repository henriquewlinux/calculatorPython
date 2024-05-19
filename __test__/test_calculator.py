from calculator import Calculator
from main import main
import pytest
from unittest.mock import patch
from io import StringIO
import builtins

def test_add_value_positive():
    x = 5
    y = 2
    expected = 7
    actual = Calculator.add(x,y)
    assert actual == expected

def test_add_value_negative():
    x = 5
    y = -9
    expectd = -4
    actual = Calculator.add(x,y)
    assert actual == expectd
    

def test_subtract_value_positive():
    x = 2
    y = 1
    expectd = 1
    actual = Calculator.subtract(x,y)
    assert actual == expectd

def test_subtrair_valor_negative():
    x = 2
    y = -5
    expectd = 7
    actual = Calculator.subtract(x,y)
    assert actual == expectd

def test_divide():
    x = 2
    y = 10
    expected = 0.2
    actual = Calculator.divide(x,y)
    assert actual == expected

def test_divide_for_zero():
    x = 10
    y = 0
    expected = "Error: Divide for zero"
    actual = Calculator.divide(x,y)
    assert actual == expected

def test_multiply():
    x = 5
    y = 3
    expected = 15
    actual = Calculator.multiply(x,y)
    assert actual == expected