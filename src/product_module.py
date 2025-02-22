class Product:
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
        return self.__price

    @price.setter
    def price(self, new_price):
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
    product1 = Product("Cube", "Road Bicycle Cube Peloton", 150_000.00, 11)
    print("\n------name--description--price--quantity-----product1")
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    dct = {"name": "Colnago", "description": "Best cycle for Giro", "price": 500_000.00, "quantity": 1}
    product2 = Product.new_product(dct)
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
