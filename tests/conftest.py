import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_category():
    return Category(
        name="products for cycling",
        description="Bikes, jerseys and more..",
        products=[
            Product("bike", "Peloton road bike Cube", 100_000.00, 1),
            Product("helmet", "Guro velo helmet", 10_000.00, 2),
            Product("jersey", "Men's Pro Cycling Jersey", 100_000.00, 5),
            Product("Bicycle tube", "Continental Race Bicycle Tube", 3_000.00, 3)
        ]
    )


@pytest.fixture
def second_category():
    return Category(
        name="Apple products",
        description="Iphones, airpods etc",
        products=[
            Product("Iphone", "Iphone 10 pro max", 200_000.00, 3),
            Product("Macbook", "Macbook pro", 300_000.00, 1)
        ]
    )


@pytest.fixture
def product():
    return Product("Iphone", "Iphone 10 pro max", 200_000.00, 3)
