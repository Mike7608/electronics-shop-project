from src.item import Item


class MixinKey:
    __language = "EN"

    @property
    def language(self):
        return self.__language

    def __str__(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class Keyboard(Item, MixinKey):
    pass
