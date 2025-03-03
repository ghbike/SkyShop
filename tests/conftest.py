import pytest

from src.category_module import Category
from src.my_iterator import MyIterator
from src.product_module import Product


@pytest.fixture
def first_category():
    return Category(
        name="Bicycling",
        description="Everything for bicycling",
        products=[
            Product("Cube", "Road Bicycle Cube Peloton", 150_000.00, 1),
            Product("Giro", "Helmet Giro for road cycling", 10_000.00, 3),
            Product("Wahoo", "Wahoo velo computer", 30_000.00, 2),
            Product("jersey", "Man's long sleeve jersey", 5_000.00, 5)
        ]
    )


@pytest.fixture
def second_category():
    return Category(
        name="Apple",
        description="Everything from Apple",
        products=[
            Product("iphone", "iphone 16 pro max", 200_000.00, 2),
            Product("Macbook", "Macbook pro 16 inch", 250_000.00, 3)
        ]
    )


@pytest.fixture
def third_category():
    return Category(
        name="Bicycling",
        description="Everything for bicycling",
        products=[
            Product("Cube", "Road Bicycle Cube Peloton", 150_000.00, 1),
            Product("Giro", "Helmet Giro for road cycling", 10_000.00, 3),
            Product("Wahoo", "Wahoo velo computer", 30_000.00, 2),
            Product("jersey", "Man's long sleeve jersey", 5_000.00, 5),
            Product("Rockbros", "Glasses for cycling", 2_000.00, 11)
        ]
    )


@pytest.fixture
def first_product():
    return Product("Cube", "Road Bicycle Cube Peloton", 150_000.00, 1)


@pytest.fixture
def second_product():
    return Product("Rockbros", "Glasses for cycling", 2_000.00, 11)


@pytest.fixture
def new_product_dict():
    return Product.new_product({"name": "Rockbros", "description": "Glasses for cycling", "price": 2_000.00, "quantity": 11})
