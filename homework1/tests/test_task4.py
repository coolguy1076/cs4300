from src.task4 import calculate_discount

def test_discount_int():
    assert calculate_discount(100, 10) == 90

def test_discount_float():
    assert calculate_discount(100.0, 10.0) == 90.0

