from simpleinterest import simInt

def test_simple_interest():
    assert simInt(1000, 5, 2) == 100

def test_zero_principal():
    assert simInt(0, 5, 2) == 0

def test_zero_rate():
    assert simInt(1000, 0, 2) == 0

def test_zero_time():
    assert simInt(1000, 5, 0) == 0

def test_decimal_values():
    assert simInt(5000, 7.5, 1) == 375


    