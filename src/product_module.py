from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """
        инициализация экземпляра класса Product
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        """
        создает строковое отображение экземпляра класса
        """
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """
        реализована возможность складывать продукты
        :param other: другой продукт
        :return: полная стоимость всех товаров на складе
        """
        if type(other) is type(self):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, product_dct):
        """
        создает новый экземпляр класса продукт
        :param product_dct: параметры нового продукта в словаре
        :return: новый экземпляр класса продукт
        """
        return cls(*product_dct.values())

    @property
    def price(self):
        """
        Геттер
        :return: цена товара
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Сеттер
        :param new_price:
        :return: устанавливает новую цену
        """
        if new_price > 0:
            if new_price < self.__price:
                user_decision = input("новая цена ниже. подтверждаете?\n")
                if user_decision == 'y':
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


if __name__ == '__main__':
    dct = {"name": "Colnago", "description": "Best cycle for Giro", "price": 500_000.00, "quantity": 1}
    product2 = Product.new_product(dct)
    product11 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product12 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    print(f'сумма продуктов:  {product11 + product12}')
    print("\n------name--description--price--quantity-----product2")
    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print('\n--------------new big price----------')
    product2.price = 999_999.00
    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print('\n--------------new small price----------')
    product2.price = 777.77
    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print('\n--------------negative price------------')
    product2.price = -777.77
    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)
