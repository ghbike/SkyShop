import pytest

from tests.conftest import first_category, second_category, third_category, first_product, second_product, new_product_dict


def test_category_init(first_category, second_category):
    assert first_category.name == "Bicycling"
    assert first_category.description == "Everything for bicycling"
    assert len(first_category.products.split('\n')) == 4

    assert second_category.name == "Apple"
    assert second_category.description == "Everything from Apple"
    assert len(second_category.products.split('\n')) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 6
    assert second_category.product_count == 6


def test_products_getter(first_category):
    assert  first_category.products == ('Cube, 150000.0 руб. Остаток: 1 шт.\nGiro, 10000.0 руб. Остаток: 3 шт.\nWahoo, 30000.0 руб. Остаток: 2 шт.\njersey, 5000.0 руб. Остаток: 5 шт.')


def test_add_product(first_category, second_product):
    assert len(first_category.products.split('\n')) == 4
    first_category.add_product(second_product)
    assert len(first_category.products.split('\n')) == 5
    assert first_category.products.split('\n')[4] == "Rockbros, 2000.0 руб. Остаток: 11 шт."


def test_add_smartphone(first_category, first_smartphone):
    assert len(first_category.products.split('\n')) == 4
    first_category.add_product(first_smartphone)
    assert len(first_category.products.split('\n')) == 5
    assert first_category.products.split('\n')[4] == "Nokia, 12000.0 руб. Остаток: 1 шт."


def test_add_lawngrass(first_category, first_lawngrass):
    assert len(first_category.products.split('\n')) == 4
    first_category.add_product(first_lawngrass)
    assert len(first_category.products.split('\n')) == 5
    assert first_category.products.split('\n')[4] == "Ландшафтный бонсай, 100.0 руб. Остаток: 15 шт."


def test_add_product_error(first_category):
    with pytest.raises(TypeError):
        first_category.add_product(1)


def test_category_str(first_category, second_category):
    assert str(first_category) == 'Bicycling, количество продуктов: 11 шт.'
    assert str(second_category) == 'Apple, количество продуктов: 5 шт.'
