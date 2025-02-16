class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# if __name__ == '__main__':
#     product = Product("bike", "Peloton road bike Cube", 100_000.00, 1)
#
#     print(product.name)
#     print(product.description)
#     print(product.price)
#     print(product.quantity)
#     print(product)
