from src.task4 import Student2

def test_przedstaw_sie():
    st = Student2("Ala", "Nowak", 1111)
    text = st.przedstaw_sie()
    assert "Ala Nowak" in text
    assert "1111" in text
