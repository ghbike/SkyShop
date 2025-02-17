class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """
        инициализация объекта класса Product
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == '__main__':
    product = Product("bicycle", "Road Bicycle Cube Peloton", 150_000.00, 1)

    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)
