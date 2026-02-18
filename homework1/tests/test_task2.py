from src import task2

def test_integer():
    assert isinstance(task2.get_integer(), int)

def test_float():
    assert isinstance(task2.get_float(), float)

def test_string():
    assert isinstance(task2.get_string(), str)

def test_boolean():
    assert isinstance(task2.get_boolean(), bool)

