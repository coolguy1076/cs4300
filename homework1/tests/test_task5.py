from src import task5

def test_first_three_books():
    assert len(task5.first_three_books()) == 3

def test_student_db():
    assert task5.student_db["Alice"] == 1001

