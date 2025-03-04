def test_lawngrass_init(first_lawngrass, second_lawngrass):
    assert first_lawngrass.name == "Ландшафтный бонсай"
    assert first_lawngrass.description == "износоустойчивый"
    assert first_lawngrass.price == 100.00
    assert first_lawngrass.quantity == 15
    assert first_lawngrass.country == "Russia"
    assert first_lawngrass.germination_period == 8
    assert first_lawngrass.color == 'green'

    assert second_lawngrass.name == "Городской изумруд"
    assert second_lawngrass.description == "низкорастущий"
    assert second_lawngrass.price == 120.00
    assert second_lawngrass.quantity == 17
    assert second_lawngrass.country == "Iran"
    assert second_lawngrass.germination_period == 12
    assert second_lawngrass.color == 'emerald'
