# from src.product import Product


class Category:
    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        """
        инициализация экземпляра класса Category
        """
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


# if __name__ == '__main__':
#     product1 = Product("Cube", "Road Bicycle Cube Peloton", 150_000.00, 1)
#     product2 = Product("Giro", "Helmet Giro for road cycling", 10_000.00, 3)
#     product3 = Product("Wahoo", "Wahoo velo computer", 30_000.00, 2)
#     product4 = Product("jersey", "Man's long sleeve jersey", 5_000.00, 5)
#
#     category1 = Category("Bicycling", "Everything for bicycling", [product1, product2, product3, product4])
#
#     print(category1.name)
#     print(category1.description)
#     print(category1.products)
#
#     print(category1.category_count)
#     print(category1.product_count)
