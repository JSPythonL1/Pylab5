from src.task2 import Student

def test_student_creation():
    s = Student("Adam", 12345)
    assert s.imie == "Adam"
    assert s.numer_albumu == 12345
