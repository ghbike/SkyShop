from src.product_module import Product
from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Product("Cube", "Road Bicycle Cube Peloton", 150_000.00, 1)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Cube, Road Bicycle Cube Peloton, 150000.0, 1)"

    Smartphone("Nokia", "for classic lovers", 12_000.00, 1, 0.5, "8800", 8, 'Silver')
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Nokia, for classic lovers, 12000.0, 1)"

    LawnGrass("Ландшафтный бонсай", "износоустойчивый", 100.00, 15, "Russia", 8, 'green')
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Ландшафтный бонсай, износоустойчивый, 100.0, 15)"
