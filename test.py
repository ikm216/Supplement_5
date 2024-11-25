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