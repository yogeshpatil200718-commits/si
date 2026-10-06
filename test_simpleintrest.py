from simpleinterest import calculate_simple_interest

def test_simple_interest():
    assert calculate_simple_interest(1000, 5, 2) == 100

def test_zero_principal():
    assert calculate_simple_interest(0, 5, 2) == 0

def test_zero_rate():
    assert calculate_simple_interest(1000, 0, 2) == 0

def test_zero_time():
    assert calculate_simple_interest(1000, 5, 0) == 0

def test_decimal_values():
    assert calculate_simple_interest(5000, 7.5, 1) == 375


    