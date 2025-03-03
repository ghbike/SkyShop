def test_product_init(first_product, second_product):
    assert first_product.name == "Cube"
    assert first_product.description == "Road Bicycle Cube Peloton"
    assert first_product.price == 150_000.00
    assert first_product.quantity == 1

    assert second_product.name == "Rockbros"
    assert second_product.description == "Glasses for cycling"
    assert second_product.price == 2_000.00
    assert second_product.quantity == 11


def test_new_product(new_product_dict, second_product):
    assert new_product_dict.name == "Rockbros"
    assert new_product_dict.description == "Glasses for cycling"
    assert new_product_dict.price == 2_000.00
    assert new_product_dict.quantity == 11


def test_price_getter(first_product, second_product):
    assert first_product.price == 150000
    assert second_product.price == 2000


def test_price_setter(first_product, second_product):
    first_product.price = 333_000
    assert first_product.price == 333_000
    second_product.price = -1000
    assert second_product.price == 2000


def test_product_str(first_product, second_product):
    assert str(first_product) == 'Cube, 150000.0 руб. Остаток: 1 шт.'
    assert str(second_product) == 'Rockbros, 2000.0 руб. Остаток: 11 шт.'


def test_product_add(first_product, second_product):
    assert first_product + second_product == 172_000.0
