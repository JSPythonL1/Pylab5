from src.task3 import Osoba, Student2

def test_student2_inheritance():
    st = Student2("Ala", "Kowalska", 9988)
    assert isinstance(st, Osoba)
    assert st.imie == "Ala"
    assert st.nazwisko == "Kowalska"
    assert st.numer_albumu == 9988
