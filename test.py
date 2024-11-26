import math
import pytest

def square_root(num):
    """
    Calculates the square root of a number and raises ValueError if the number is negative.
    
    Args:
        num: The number to calculate the square root for.
    
    Returns:
        The square root of the number or the exception if the number is negative
    """
    if num >= 0:
        return math.sqrt(num)
    else:
        raise  ValueError("A negative number cannot be calutaed to get square root")
    
def test_should_return_3_from_9():
    assert square_root(9) == 3

def test_should_return_exception_from_negative_num():
    with pytest.raises(ValueError, match = "A negative number cannot be calutaed to get square root"):
        square_root(-9)

def test_should_return_nothing_from_2_even():
    assert random_num(2) is True

def test_should_return_6_from_3_odd():
    assert random_num(3) == 6

def test_should_return_4_from_12_divisble_three():
    assert random_num(12) == 4

def test_should_return_3_from_12_divisble_four():
    assert random_num(12) == 3