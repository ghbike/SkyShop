from src.product_module import Product
from src.category_module import Category

class MyIterator:
    def __init__(self, category):
        self.category = category

    def __iter__(self):
        self.currant_index = -1

    def __next__(self):
        lst = self.category.product_list
        print(len(lst))
        if self.currant_index + 1 < len(lst):
            next_product = lst[self.currant_index]
            self.currant_index += 1
            return next_product
        else:
            raise StopIteration

# if __name__ == '__main__':
#     category1 = Category(
#         name="Bicycling",
#         description="Everything for bicycling",
#         products=[
#             Product("Cube", "Road Bicycle Cube Peloton", 150_000.00, 1),
#             Product("Giro", "Helmet Giro for road cycling", 10_000.00, 3),
#             Product("Wahoo", "Wahoo velo computer", 30_000.00, 2),
#             Product("jersey", "Man's long sleeve jersey", 5_000.00, 5),
#             Product("Rockbros", "Glasses for cycling", 2_000.00, 11)
#         ]
#     )
#
#     iter1 = MyIterator(category1)
#     for i in iter1:
#         print(i)
