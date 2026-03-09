import pytest

from src.main import Product, Smartphone, LawnGrass


class TestAdditionSameClassRestriction:
    """Тесты ограничения сложения только одинаковых классов (Задание 2)"""

    def test_smartphone_addition_same_class_success(self):
        """Тест успешного сложения смартфонов одного класса"""
        smartphone1 = Smartphone(
            name="iPhone",
            description="Смартфон",
            price=100000.0,
            quantity=3,
            efficiency="Высокая",
            model="15 Pro",
            memory="256",
            color="Титан"
        )

        smartphone2 = Smartphone(
            name="iPhone",
            description="Смартфон",
            price=90000.0,
            quantity=2,
            efficiency="Высокая",
            model="15 Pro",
            memory="256",
            color="Титан"
        )

        result = smartphone1 + smartphone2

        assert isinstance(result, Smartphone), \
            "Результат сложения смартфонов должен быть Smartphone"
        assert result.quantity == 5, \
            f"Ожидалось количество 5, получено {result.quantity}"
        assert result.price == 100000.0, \
            f"Ожидалась цена 100000.0, получено {result.price}"
        assert result.name == "iPhone", \
            f"Ожидалось имя 'iPhone', получено {result.name}"

    def test_lawn_grass_addition_same_class_success(self):
        """Тест успешного сложения газонной травы одного класса"""
        grass1 = LawnGrass(
            name="Трава спортивная",
            description="Для полей",
            price=2000.0,
            quantity=50,
            country="Германия",
            germination_period="10 дней",
            color="Темно-зеленый"
        )

        grass2 = LawnGrass(
            name="Трава спортивная",
            description="Для полей",
            price=1800.0,
            quantity=30,
            country="Германия",
            germination_period="10 дней",
            color="Темно-зеленый"
        )

        result = grass1 + grass2

        assert isinstance(result, LawnGrass), \
            "Результат сложения газонной травы должен быть LawnGrass"
        assert result.quantity == 80, \
            f"Ожидалось количество 80, получено {result.quantity}"
        assert result.price == 2000.0, \
            f"Ожидалась цена 2000.0, получено {result.price}"
        assert result.country == "Германия", \
            f"Ожидалась страна 'Германия', получено {result.country}"

    def test_product_addition_same_class_success(self):
        """Тест успешного сложения обычных продуктов одного класса"""
        product1 = Product(
            name="Ноутбук",
            description="Игровой",
            price=50000.0,
            quantity=3
        )

        product2 = Product(
            name="Ноутбук",
            description="Игровой",
            price=45000.0,
            quantity=2
        )

        result = product1 + product2

        assert isinstance(result, Product), \
            "Результат сложения продуктов должен быть Product"
        assert result.quantity == 5, \
            f"Ожидалось количество 5, получено {result.quantity}"
        assert result.price == 50000.0, \
            f"Ожидалась цена 50000.0, получено {result.price}"


class TestAdditionDifferentClassRestriction:
    """Тесты ошибок при сложении разных классов (Задание 2)"""

    def test_smartphone_plus_lawn_grass_error(self, sample_smartphone, sample_lawn_grass):
        """Тест ошибки при сложении смартфона и газонной травы"""
        with pytest.raises(TypeError) as exc_info:
            sample_smartphone + sample_lawn_grass

        error_message = str(exc_info.value)
        assert "Можно складывать только объекты одного класса" in error_message
        assert "Smartphone" in error_message

    def test_lawn_grass_plus_smartphone_error(self, sample_lawn_grass, sample_smartphone):
        """Тест ошибки при сложении газонной травы и смартфона"""
        with pytest.raises(TypeError) as exc_info:
            sample_lawn_grass + sample_smartphone

        error_message = str(exc_info.value)
        assert "Можно складывать только объекты одного класса" in error_message
        assert "LawnGrass" in error_message

    def test_smartphone_plus_product_error(self, sample_smartphone):
        """Тест ошибки при сложении смартфона и обычного продукта"""
        product = Product(
            name="Телефон",
            description="Обычный телефон",
            price=5000.0,
            quantity=10
        )

        with pytest.raises(TypeError) as exc_info:
            sample_smartphone + product

        error_message = str(exc_info.value)
        assert "Можно складывать только объекты одного класса" in error_message
        assert "Smartphone" in error_message

    def test_lawn_grass_plus_product_error(self, sample_lawn_grass):
        """Тест ошибки при сложении газонной травы и обычного продукта"""
        product = Product(
            name="Трава",
            description="Обычная трава",
            price=500.0,
            quantity=20
        )

        with pytest.raises(TypeError) as exc_info:
            sample_lawn_grass + product

        error_message = str(exc_info.value)
        assert "Можно складывать только объекты одного класса" in error_message
        assert "LawnGrass" in error_message

    def test_product_plus_smartphone_error(self):
        """Тест ошибки при сложении обычного продукта и смартфона"""
        product = Product(
            name="Устройство",
            description="Описание",
            price=10000.0,
            quantity=5
        )

        smartphone = Smartphone(
            name="Устройство",
            description="Описание",
            price=50000.0,
            quantity=2,
            efficiency="Высокая",
            model="Модель",
            memory="128",
            color="Черный"
        )




class TestAdditionWithDifferentNames:
    """Тесты сложения с разными именами продуктов"""

    def test_smartphone_addition_different_names_error(self):
        """Тест ошибки при сложении смартфонов с разными именами"""
        smartphone1 = Smartphone(
            name="iPhone",
            description="Смартфон",
            price=100000.0,
            quantity=3,
            efficiency="Высокая",
            model="15 Pro",
            memory="256",
            color="Титан"
        )

        smartphone2 = Smartphone(
            name="Samsung",
            description="Смартфон",
            price=90000.0,
            quantity=2,
            efficiency="Высокая",
            model="S23",
            memory="256",
            color="Черный"
        )

        with pytest.raises(ValueError) as exc_info:
            smartphone1 + smartphone2

        error_message = str(exc_info.value)
        assert "Можно складывать только одинаковые продукты" in error_message

    def test_smartphone_addition_same_name_different_case(self):
        """Тест сложения смартфонов с одинаковым именем в разном регистре"""
        smartphone1 = Smartphone(
            name="iPhone",
            description="Смартфон",
            price=100000.0,
            quantity=3,
            efficiency="Высокая",
            model="15 Pro",
            memory="256",
            color="Титан"
        )

        smartphone2 = Smartphone(
            name="IPHONE",  # Верхний регистр
            description="Смартфон",
            price=90000.0,
            quantity=2,
            efficiency="Высокая",
            model="15 Pro",
            memory="256",
            color="Титан"
        )

        # Должна быть ошибка, так как имена различаются регистром
        with pytest.raises(ValueError) as exc_info:
            smartphone1 + smartphone2

        error_message = str(exc_info.value)
        assert "Можно складывать только одинаковые продукты" in error_message


class TestAdditionPreservesAttributes:
    """Тесты сохранения атрибутов при сложении"""

    def test_smartphone_addition_preserves_attributes(self):
        """Тест что сложение смартфонов сохраняет их атрибуты"""
        smartphone1 = Smartphone(
            name="Xiaomi",
            description="Смартфон",
            price=30000.0,
            quantity=5,
            efficiency="Средняя",
            model="Redmi Note 12",
            memory="128",
            color="Синий"
        )

        smartphone2 = Smartphone(
            name="Xiaomi",
            description="Смартфон",
            price=28000.0,
            quantity=3,
            efficiency="Средняя",
            model="Redmi Note 12",
            memory="128",
            color="Синий"
        )

        result = smartphone1 + smartphone2

        # Проверяем что специфичные атрибуты сохранились
        assert result.efficiency == "Средняя"
        assert result.model == "Redmi Note 12"
        assert result.memory == "128"
        assert result.color == "Синий"

        # Проверяем что базовые атрибуты правильные
        assert result.quantity == 8
        assert result.price == 30000.0
        assert result.name == "Xiaomi"

    def test_lawn_grass_addition_preserves_attributes(self):
        """Тест что сложение газонной травы сохраняет их атрибуты"""
        grass1 = LawnGrass(
            name="Трава элитная",
            description="Для гольф-полей",
            price=5000.0,
            quantity=25,
            country="США",
            germination_period="7 дней",
            color="Изумрудный"
        )

        grass2 = LawnGrass(
            name="Трава элитная",
            description="Для гольф-полей",
            price=4500.0,
            quantity=15,
            country="США",
            germination_period="7 дней",
            color="Изумрудный"
        )

        result = grass1 + grass2

        # Проверяем что специфичные атрибуты сохранились
        assert result.country == "США"
        assert result.germination_period == "7 дней"
        assert result.color == "Изумрудный"

        # Проверяем что базовые атрибуты правильные
        assert result.quantity == 40
        assert result.price == 5000.0
        assert result.name == "Трава элитная"