from src.product_module import Product


class Smartphone(Product):
    name: str
    description: str
    __price: float
    quantity: int
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """
        инициализация экземпляра класса Smartphone
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
