import pytest

from src.category import Category
from src.product import Product


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
def product():
    return Product("Cube", "Road Bicycle Cube Peloton", 150_000.00, 1)
