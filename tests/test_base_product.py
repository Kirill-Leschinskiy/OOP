import pytest
from src.main import BaseProduct, Product, Smartphone, LawnGrass, ReprMixin, Order


class TestBaseProduct:
    """Тесты для абстрактного базового класса"""

    def test_base_product_is_abstract(self):
        """Тест что BaseProduct является абстрактным классом"""
        with pytest.raises(TypeError):
            BaseProduct("name", "desc", 100, 5)

    def test_product_inherits_from_base_product(self):
        """Тест что Product наследуется от BaseProduct"""
        assert issubclass(Product, BaseProduct)

    def test_smartphone_inherits_from_base_product(self):
        """Тест что Smartphone наследуется от BaseProduct"""
        assert issubclass(Smartphone, BaseProduct)

    def test_lawn_grass_inherits_from_base_product(self):
        """Тест что LawnGrass наследуется от BaseProduct"""
        assert issubclass(LawnGrass, BaseProduct)


class TestReprMixin:
    """Тесты для миксина логирования"""

    def test_product_creation_logging(self, capsys):
        """Тест логирования при создании продукта"""
        product = Product("Тест", "Описание", 100, 5)
        captured = capsys.readouterr()
        assert "Создан объект: Product" in captured.out
        assert "name='Тест'" in captured.out
        assert "description='Описание'" in captured.out
        assert "price=100" in captured.out
        assert "quantity=5" in captured.out

    def test_smartphone_creation_logging(self, capsys):
        """Тест логирования при создании смартфона"""
        smartphone = Smartphone(
            "iPhone", "Смартфон", 100000, 3,
            "Высокая", "15 Pro", "256", "Черный"
        )
        captured = capsys.readouterr()
        assert "Создан объект: Smartphone" in captured.out
        assert "name='iPhone'" in captured.out
        assert "description='Смартфон'" in captured.out
        assert "price=100000" in captured.out
        assert "quantity=3" in captured.out
        assert "efficiency='Высокая'" in captured.out
        assert "model='15 Pro'" in captured.out
        assert "memory='256'" in captured.out
        assert "color='Черный'" in captured.out

    def test_lawn_grass_creation_logging(self, capsys):
        """Тест логирования при создании газонной травы"""
        grass = LawnGrass(
            "Трава", "Описание", 1500, 100,
            "Россия", "14 дней", "Зеленый"
        )
        captured = capsys.readouterr()
        assert "Создан объект: LawnGrass" in captured.out
        assert "name='Трава'" in captured.out
        assert "description='Описание'" in captured.out
        assert "price=1500" in captured.out
        assert "quantity=100" in captured.out
        assert "country='Россия'" in captured.out
        assert "germination_period='14 дней'" in captured.out
        assert "color='Зеленый'" in captured.out


class TestOrder:
    """Тесты для класса заказа"""

    def test_order_initialization(self, sample_product):
        """Тест инициализации заказа"""
        order = Order(sample_product, 3)
        assert order.product == sample_product
        assert order.quantity == 3
        assert order.total_cost == sample_product.price * 3

    def test_order_name_property(self, sample_product):
        """Тест свойства name заказа"""
        order = Order(sample_product, 2)
        assert order.name == f"Заказ: {sample_product.name}"

    def test_order_name_setter(self, sample_product):
        """Тест сеттера name"""
        order = Order(sample_product, 2)
        order.name = "Новое имя"
        assert order.name == "Новое имя"

        with pytest.raises(ValueError):
            order.name = ""

    def test_order_total_property(self, sample_product):
        """Тест свойства total"""
        order = Order(sample_product, 4)
        assert order.total == sample_product.price * 4

    def test_order_str_representation(self, sample_product):
        """Тест строкового представления заказа"""
        order = Order(sample_product, 2)
        order_str = str(order)
        assert "Заказ: Телефон" in order_str
        assert "количество: 2" in order_str
        assert f"сумма: {sample_product.price * 2}" in order_str

    def test_order_repr_representation(self, sample_product):
        """Тест представления заказа для отладки"""
        order = Order(sample_product, 3)
        repr_str = repr(order)
        assert "Order(" in repr_str
        assert "quantity=3" in repr_str