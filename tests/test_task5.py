from src.task5 import Liczba

def test_liczba_magic_add():
    a = Liczba(2)
    b = Liczba(3)
    assert (a + b) == 19
