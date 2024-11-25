import pytest

def test_should_return_3_from_9():
    assert square_root(9) == 3

def test_should_return_exception_from_negative_num():
    with pytest.raises(ValueError, match = "A negative number cannot be calutaed to get square root"):
        square_root(-9)