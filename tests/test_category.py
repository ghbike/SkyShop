def test_category_init(first_category, second_category):
    assert first_category.name == "Bicycling"
    assert first_category.description == "Everything for bicycling"
    assert len(first_category.products) == 4

    assert second_category.name == "Apple"
    assert second_category.description == "Everything from Apple"
    assert len(second_category.products) == 2


    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 6
    assert second_category.product_count == 6
