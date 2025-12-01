from src.task7 import Pizza

def test_pineapple():
    p = Pizza()
    p.set_pineapple_allowed(True)
    assert p.pineapple_allowed is True
