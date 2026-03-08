import pytest
from src.main import Product, Category, Order, ZeroQuantityError


class TestZeroQuantityProduct:
    """Тесты для проверки создания продукта с нулевым количеством"""

    def test_product_with_zero_quantity_raises_error(self):
        """Тест что создание продукта с нулевым количеством вызывает ValueError"""
        with pytest.raises(ValueError) as exc_info:
            Product("Тест", "Описание", 100, 0)

        assert "Товар с нулевым количеством не может быть добавлен" in str(exc_info.value)

    def test_product_with_negative_quantity_raises_error(self):
        """Тест что создание продукта с отрицательным количеством вызывает ValueError"""
        with pytest.raises(ValueError) as exc_info:
            Product("Тест", "Описание", 100, -5)

        assert "Товар с нулевым количеством не может быть добавлен" in str(exc_info.value)

    def test_smartphone_with_zero_quantity_raises_error(self):
        """Тест что создание смартфона с нулевым количеством вызывает ValueError"""
        with pytest.raises(ValueError) as exc_info:
            from src.main import Smartphone
            Smartphone("iPhone", "Смартфон", 100000, 0, "Высокая", "15 Pro", "256", "Черный")

        assert "Товар с нулевым количеством не может быть добавлен" in str(exc_info.value)

    def test_lawn_grass_with_zero_quantity_raises_error(self):
        """Тест что создание газонной травы с нулевым количеством вызывает ValueError"""
        with pytest.raises(ValueError) as exc_info:
            from src.main import LawnGrass
            LawnGrass("Трава", "Описание", 1500, 0, "Россия", "14 дней", "Зеленый")

        assert "Товар с нулевым количеством не может быть добавлен" in str(exc_info.value)

    def test_product_with_positive_quantity_success(self):
        """Тест что создание продукта с положительным количеством успешно"""
        product = Product("Тест", "Описание", 100, 5)
        assert product.quantity == 5
        assert product.name == "Тест"


class TestCategoryAveragePrice:
    """Тесты для метода подсчета среднего ценника в категории"""

    def test_average_price_with_products(self, sample_category):
        """Тест подсчета среднего ценника в категории с товарами"""
        # В sample_category 3 товара с ценами 100, 200, 300
        expected_average = (100 + 200 + 300) / 3
        assert sample_category.get_average_price() == expected_average

    def test_average_price_with_empty_category(self, sample_category_empty):
        """Тест подсчета среднего ценника в пустой категории"""
        assert sample_category_empty.get_average_price() == 0

    def test_average_price_with_single_product(self, sample_product):
        """Тест подсчета среднего ценника в категории с одним товаром"""
        category = Category("Один товар", "Описание", [sample_product])
        assert category.get_average_price() == sample_product.price

    def test_average_price_with_different_products(self):
        """Тест подсчета среднего ценника с разными товарами"""
        products = [
            Product("Товар1", "Описание1", 150.0, 5),
            Product("Товар2", "Описание2", 250.0, 3),
            Product("Товар3", "Описание3", 350.0, 7),
            Product("Товар4", "Описание4", 450.0, 2)
        ]
        category = Category("Тест", "Описание", products)
        expected_average = (150 + 250 + 350 + 450) / 4
        assert category.get_average_price() == expected_average


class TestZeroQuantityError:
    """Тесты для пользовательского исключения ZeroQuantityError"""

    def test_zero_quantity_error_initialization(self):
        """Тест инициализации исключения ZeroQuantityError"""
        error = ZeroQuantityError()
        assert str(error) == "Товар с нулевым количеством не может быть добавлен"

        custom_error = ZeroQuantityError("Кастомное сообщение")
        assert str(custom_error) == "Кастомное сообщение"

    def test_zero_quantity_error_inheritance(self):
        """Тест что ZeroQuantityError наследуется от Exception"""
        assert issubclass(ZeroQuantityError, Exception)

    def test_add_product_with_zero_quantity_to_category(self, sample_category_empty, sample_product):
        """Тест добавления товара с нулевым количеством в категорию"""
        sample_product.quantity = 0

        with pytest.raises(ZeroQuantityError) as exc_info:
            sample_category_empty.add_product(sample_product)

        assert "Товар с нулевым количеством не может быть добавлен в категорию" in str(exc_info.value)

    def test_create_order_with_zero_quantity(self, sample_product):
        """Тест создания заказа с нулевым количеством"""
        with pytest.raises(ZeroQuantityError) as exc_info:
            Order(sample_product, 0)

        assert "Товар с нулевым количеством не может быть добавлен в заказ" in str(exc_info.value)

    def test_create_order_with_negative_quantity(self, sample_product):
        """Тест создания заказа с отрицательным количеством"""
        with pytest.raises(ZeroQuantityError) as exc_info:
            Order(sample_product, -5)

        assert "Товар с нулевым количеством не может быть добавлен в заказ" in str(exc_info.value)

    def test_add_product_with_zero_quantity_to_existing_category(self, sample_category):
        """Тест добавления товара с нулевым количеством в существующую категорию"""
        from src.main import Smartphone

        smartphone = Smartphone(
            "iPhone", "Смартфон", 100000, 5,
            "Высокая", "15 Pro", "256", "Черный"
        )

        smartphone.quantity = 0

        with pytest.raises(ZeroQuantityError) as exc_info:
            sample_category.add_product(smartphone)

        assert "Товар с нулевым количеством не может быть добавлен в категорию" in str(exc_info.value)