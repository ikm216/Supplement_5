import math
import pytest
from unittest.mock import patch
import random

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
    
def random_num():
    """
    Generates a random number between 1 and 100, does a process, and raises an exception if > 4.
    - If odd, multiply by 2.
    - If divisible by 3, divide by 3.
    - If divisible by 4, multiply by 4.
    - Raise ValueError if > 4 at any step.

    Args:
        rand: Generated random number to be process.

    Returns:
        processed number or raises ValueError: If the processed number is greater than 4.
    """
    rand = random.randint(1, 100)

    if rand % 2 != 0:  
        rand *= 2
        if rand > 4:
            raise ValueError("The random number is greater than 4")
    if rand % 3 == 0:  
        rand //= 3
        if rand > 4:
            raise ValueError("The random number is greater than 4")
    if rand % 4 == 0:  
        rand *= 4
        if rand > 4:
            raise ValueError("The random number is greater than 4")

    return rand

    

#Test for square_root    
def test_should_return_3_from_9():
    assert square_root(9) == 3

def test_should_return_exception_from_negative_num():
    with pytest.raises(ValueError, match = "A negative number cannot be calutaed to get square root"):
        square_root(-9)

#Test for random_num
def test_random_num_function_fully():
    with patch("random.randint", return_value=3):
        with pytest.raises(ValueError, match="greater than 4"):
            random_num()

#Test for divisibles_check
def test_should_return_divisibles_of_2():
    assert divisibles_check(2) == [2,4,6,8,10]
            
    