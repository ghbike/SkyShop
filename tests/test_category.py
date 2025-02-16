def test_category_init(first_category, second_category):
    assert first_category.name == "products for cycling"
    assert first_category.description == "Bikes, jerseys and more.."
    assert len(first_category.products) == 4

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 6
    assert second_category.product_count == 6
