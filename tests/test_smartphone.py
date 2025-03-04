def test_smartphone_init(first_smartphone, second_smartphone):
    assert first_smartphone.name == "Nokia"
    assert first_smartphone.description == "for classic lovers"
    assert first_smartphone.price == 12_000.00
    assert first_smartphone.quantity == 1
    assert first_smartphone.efficiency == 0.5
    assert first_smartphone.model == "8800"
    assert first_smartphone.memory == 8
    assert first_smartphone.color == 'Silver'

    assert second_smartphone.name == "Iphone"
    assert second_smartphone.description == "hit of selling"
    assert second_smartphone.price == 120_000.00
    assert second_smartphone.quantity == 10
    assert second_smartphone.efficiency == 01.7
    assert second_smartphone.model == "16 Max"
    assert second_smartphone.memory == 128
    assert second_smartphone.color == 'Ultramarine'
