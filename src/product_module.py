class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """
        инициализация экземпляра класса Product
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    # @classmethod
    # def check_product_list(cls, name):
    #     """
    #     проверяет не встречалось ли name  в списке продуктов ранее
    #     :param name:
    #     :return: product or None
    #     """
    #     print("check_product_list in process")
    #     for category in cls.categories:
    #         for product in category.products:
    #             if name == product.name:
    #                 return product
    #     return None

    # @staticmethod
    # def merge_products(price, quantity, product_doublet):
    #     """
    #     соединяет два продукта в один. Их количество складывается, цена выбирается максимальной.
    #     :param price: Цена нового продукта.
    #     :param quantity: Количество нового продукта.
    #     :param product_doublet: Продукт из списка продуктов с одинаковым именем.
    #     """
    #     product_doublet.quantity += quantity
    #     product_doublet.price = max(product_doublet.price, price)


    @classmethod
    def new_product(cls, product_dct):
        """
        создает новый экземпляр класса продукт
        :param product_dct: параметры нового продукта в словаре
        :return: новый экземпляр класса продукт
        """
        return cls(*product_dct.values())


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
