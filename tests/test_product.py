def test_product_init(product):
    assert product.name == "Cube"
    assert product.description == "Road Bicycle Cube Peloton"
    assert product.price == 150_000.00
    assert product.quantity == 1
