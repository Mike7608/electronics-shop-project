import pytest

from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_init():
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5
    assert kb.language == "EN"


def test_change_lang():
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang().change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"

    with pytest.raises(AttributeError):
        kb.language = "EE"


def test___str__():
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
