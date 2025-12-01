from src.task6 import Dog

def test_dog_static():
    Dog.count = 0
    Dog.dogs = []

    d1 = Dog("Reksio")
    d2 = Dog("Burek")

    count, names = Dog.show_dogs()

    assert count == 2
    assert "Reksio" in names
    assert "Burek" in names
