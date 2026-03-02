from factorial import factorial

def test_positive():
    assert factorial(5) == 120

def test_zero():
    assert factorial(0) == 1

def test_negative():
    assert factorial(-5) == "Invalid Input"

def test_string():
    assert factorial("abc") == "Invalid Input"