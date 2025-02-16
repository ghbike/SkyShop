def test_product_init(product):
    assert product.name == "Iphone"
    assert product.description == "Iphone 10 pro max"
    assert product.price == 200_000.00
    assert product.quantity == 3
