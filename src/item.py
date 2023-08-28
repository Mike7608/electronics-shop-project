import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @property
    def name(self):
        """Наименование товара"""
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls):
        """Получить базу данных из csv-файла,
        пока по жестко привязанному пути ))"""

        # current_directory = os.getcwd()
        # parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
        # path = parent_directory + "\\src\\items.csv"
        file = os.path.join('..', 'src', 'items.csv')
        with open(file, 'r') as file:  # "../src/items.csv" здесь pytest coverage ругается на путь, но тесты проходят!!!
            reader = csv.DictReader(file)
            for row in reader:
                i = Item(str(row['name']), float(row['price']), int(row['quantity']))
                Item.all.append(i)

    @staticmethod
    def string_to_number(value: str):
        """Преобразовать строковое число в число int"""
        d = float(value)
        return int(d)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
