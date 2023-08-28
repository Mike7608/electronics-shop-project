"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Наименование", 23.6, 11)


def test_init():
    assert item1.price == 23.6
    assert item1.name == "Наименование"
    assert item1.quantity == 11


def test_calculate_total_price():
    assert item1.calculate_total_price() == 259.6


def test_apply_discount():
    item1.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 18.880000000000003


def test_name_getter_setter():
    item1.name = "Наименование"
    assert item1.name == "Наименован"
    item1.name = "Товар"
    assert item1.name == "Товар"


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_string_to_number():
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.5") == 5

def test___repr__():
    assert item1.__repr__() == "Item('Товар', 18.880000000000003, 11)"


def test___str__():
    assert item1.__str__() == "Товар"
