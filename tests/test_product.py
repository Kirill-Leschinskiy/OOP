import pytest

from src.main import Product


class TestProduct:
    """Тесты для класса Product"""

    def test_product_initialization(self):
        """Тест корректности инициализации объекта Product"""
        product = Product(
            name="Ноутбук",
            description="Игровой ноутбук",
            price=150000.99,
            quantity=5
        )

        assert product.name == "Ноутбук"
        assert product.description == "Игровой ноутбук"
        assert product.price == 150000.99
        assert product.quantity == 5

    def test_product_attributes_types(self):
        """Тест типов атрибутов продукта"""
        product = Product("Товар", "Описание", 100.50, 10)

        assert isinstance(product.name, str)
        assert isinstance(product.description, str)
        assert isinstance(product.price, float)
        assert isinstance(product.quantity, int)

    @pytest.mark.parametrize("name,description,price,quantity", [
        ("Товар А", "Описание А", 99.99, 50),
        ("Товар Б", "Описание Б", 0.0, 0),
        ("Товар В", "Описание В", 999999.99, 1),
    ])
    def test_product_with_different_values(self, name, description, price, quantity):
        """Параметризованный тест с разными значениями"""
        product = Product(name, description, price, quantity)

        assert product.name == name
        assert product.description == description
        assert product.price == price
        assert product.quantity == quantity