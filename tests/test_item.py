"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Товар", 23.6, 11)


def test_init():
    assert item1.price == 23.6
    assert item1.name == "Товар"
    assert item1.quantity == 11


def test_calculate_total_price():
    assert item1.calculate_total_price() == 259.6


def test_apply_discount():
    item1.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 18.880000000000003
