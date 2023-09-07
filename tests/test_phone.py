import pytest

from src.phone import Phone
from src.item import Item
phone1 = Phone("Смартфон 111", 2630.3, 10, 2)
item1 = Item("Смартфон 001", 369.7, 5,)

def test_init():
    assert phone1.price == 2630.3
    assert phone1.name == "Смартфон 111"
    assert phone1.quantity == 10
    assert phone1.number_of_sim == 2

def test___repr__():
    assert phone1.__repr__() == "Phone('Смартфон 111', 2630.3, 10, 2)"

def test___add__():
    assert phone1 + phone1 == 20
    assert phone1 + 10 is None

def test_number_of_sim():
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3

    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


