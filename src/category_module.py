from src.product_module import Product

class Category:
    name: str
    description: str
    __products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        """
        инициализация экземпляра класса Category
        общее количество категорий увеличивается на единицу
        общее количество продуктов увеличивается на количество продуктов в новой категории
        новая категория добавляется в список категорий
        """
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        """
        создает строковое отображение экземпляра класса
        """
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f'{self.name}, количество продуктов: {total_quantity} шт.'

    def add_product(self, product):
        """
        добавляет продукт в список продуктов категории self
        увеличивает общее количество продуктов на единицу
        :param product: экземпляр класса Product
        """
        self.__products.append(product)
        self.product_count += 1

    @property
    def products(self):
        """
        геттер выводит список товаров этой категории в виде строк
        :return: в формате: Название продукта, 80 руб. Остаток: 15 шт.
        """
        products_lst = []
        for product in self.__products:
            # products_lst.append(f"{product.name}, {int(product.price)} руб. Остаток: {product.quantity} шт.")
            products_lst.append(str(product))
        return "\n".join(products_lst)


# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#     print(category1)
#
#     print('\n--------список товаров:')
#     print(category1.products)
#     print('\n--------список товаров:')
#     product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
#     category1.add_product(product4)
#     print(category1.products)
#     print(f'количество товаров: {category1.product_count}')
#     print()
#
#     new_product = Product.new_product(
#         {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
#          "quantity": 5})
#     print(f'новый продукт: {new_product.name}')
#     print(f'описание: {new_product.description}')
#     print(f'цена: {new_product.price}')
#     print(f'количество: {new_product.quantity}')
#
#     new_product.price = 800
#     print(f' цена: {new_product.price}')
#
#     new_product.price = -100
#     print(f' цена: {new_product.price}')
#     new_product.price = 0
#     print(f' цена: {new_product.price}')
