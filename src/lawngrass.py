from src.product_module import Product


class LawnGrass(Product):
    name: str
    description: str
    __price: float
    quantity: int
    country: str
    germination_period: int
    color: int

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """
        инициализация экземпляра класса LawnGrass
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
