from src.item import Item


class Phone(Item):
    """
    Класс Phone наследуемый от Item содержащий информацию о мобильных телефонных аппаратах
    """
    def __init__(self,  name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            return None

    @property
    def number_of_sim(self):
        """
        Количество физических SIM-карт
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if type(value) != int or value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self.__number_of_sim = value
