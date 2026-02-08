import pytest

from src.main import Product, Smartphone, LawnGrass


class TestInheritance:
    """Тесты для проверки наследования"""

    def test_smartphone_is_subclass_of_product(self):
        """Тест что Smartphone является наследником Product"""
        assert issubclass(Smartphone, Product), \
            "Smartphone должен быть наследником класса Product"

    def test_lawn_grass_is_subclass_of_product(self):
        """Тест что LawnGrass является наследником Product"""
        assert issubclass(LawnGrass, Product), \
            "LawnGrass должен быть наследником класса Product"

    def test_smartphone_instance_of_product(self, sample_smartphone):
        """Тест что объект Smartphone является экземпляром Product"""
        assert isinstance(sample_smartphone, Product), \
            "Объект Smartphone должен быть экземпляром класса Product"

    def test_lawn_grass_instance_of_product(self, sample_lawn_grass):
        """Тест что объект LawnGrass является экземпляром Product"""
        assert isinstance(sample_lawn_grass, Product), \
            "Объект LawnGrass должен быть экземпляром класса Product"


class TestSmartphoneAttributes:
    """Тесты для атрибутов класса Smartphone (Задание 1)"""

    def test_smartphone_has_additional_attributes(self, sample_smartphone):
        """Тест что Smartphone имеет дополнительные атрибуты"""
        assert hasattr(sample_smartphone, 'efficiency'), \
            "Smartphone должен иметь атрибут 'efficiency' (производительность)"
        assert hasattr(sample_smartphone, 'model'), \
            "Smartphone должен иметь атрибут 'model' (модель)"
        assert hasattr(sample_smartphone, 'memory'), \
            "Smartphone должен иметь атрибут 'memory' (объем памяти)"
        assert hasattr(sample_smartphone, 'color'), \
            "Smartphone должен иметь атрибут 'color' (цвет)"

    def test_smartphone_attributes_values(self, sample_smartphone):
        """Тест значений атрибутов Smartphone"""
        assert sample_smartphone.efficiency == "Высокая"
        assert sample_smartphone.model == "S23 Ultra"
        assert sample_smartphone.memory == "256"
        assert sample_smartphone.color == "Серый"

    @pytest.mark.parametrize("efficiency,model,memory,color", [
        ("Низкая", "Model A", "64", "Черный"),
        ("Средняя", "Model B", "128", "Белый"),
        ("Высокая", "Model C", "512", "Синий"),
    ])
    def test_smartphone_with_different_attributes(self, efficiency, model, memory, color):
        """Параметризованный тест создания смартфонов с разными атрибутами"""
        smartphone = Smartphone(
            name="Смартфон",
            description="Тестовый смартфон",
            price=50000.0,
            quantity=5,
            efficiency=efficiency,
            model=model,
            memory=memory,
            color=color
        )

        assert smartphone.efficiency == efficiency
        assert smartphone.model == model
        assert smartphone.memory == memory
        assert smartphone.color == color


class TestLawnGrassAttributes:
    """Тесты для атрибутов класса LawnGrass (Задание 1)"""

    def test_lawn_grass_has_additional_attributes(self, sample_lawn_grass):
        """Тест что LawnGrass имеет дополнительные атрибуты"""
        assert hasattr(sample_lawn_grass, 'country'), \
            "LawnGrass должен иметь атрибут 'country' (страна-производитель)"
        assert hasattr(sample_lawn_grass, 'germination_period'), \
            "LawnGrass должен иметь атрибут 'germination_period' (срок прорастания)"
        assert hasattr(sample_lawn_grass, 'color'), \
            "LawnGrass должен иметь атрибут 'color' (цвет)"

    def test_lawn_grass_attributes_values(self, sample_lawn_grass):
        """Тест значений атрибутов LawnGrass"""
        assert sample_lawn_grass.country == "Россия"
        assert sample_lawn_grass.germination_period == "14 дней"
        assert sample_lawn_grass.color == "Зеленый"

    @pytest.mark.parametrize("country,germination_period,color", [
        ("Россия", "10 дней", "Темно-зеленый"),
        ("Германия", "14 дней", "Светло-зеленый"),
        ("США", "7 дней", "Изумрудный"),
    ])
    def test_lawn_grass_with_different_attributes(self, country, germination_period, color):
        """Параметризованный тест создания газонной травы с разными атрибутами"""
        lawn_grass = LawnGrass(
            name="Трава газонная",
            description="Тестовая трава",
            price=2000.0,
            quantity=50,
            country=country,
            germination_period=germination_period,
            color=color
        )

        assert lawn_grass.country == country
        assert lawn_grass.germination_period == germination_period
        assert lawn_grass.color == color


class TestStringRepresentationInheritance:
    """Тесты строкового представления наследников (Задание 1)"""

    def test_smartphone_str_representation(self, sample_smartphone):
        """Тест строкового представления Smartphone"""
        result = str(sample_smartphone)

        # Проверяем что содержит все важные атрибуты
        assert "Samsung Galaxy S23" in result
        assert "S23 Ultra" in result
        assert "256" in result
        assert "Серый" in result
        assert "180000.0" in result
        assert "Остаток: 5 шт." in result

    def test_lawn_grass_str_representation(self, sample_lawn_grass):
        """Тест строкового представления LawnGrass"""
        result = str(sample_lawn_grass)

        # Проверяем что содержит все важные атрибуты
        assert "Трава газонная Премиум" in result
        assert "Россия" in result
        assert "Зеленый" in result
        assert "прорастание: 14 дней" in result
        assert "1500.0" in result
        assert "Остаток: 100 шт." in result

    def test_different_str_formats(self):
        """Тест что разные классы имеют разное строковое представление"""
        product = Product("Товар", "Описание", 100.0, 10)
        smartphone = Smartphone("Смартфон", "Описание", 50000.0, 2,
                                "Высокая", "Модель", "256", "Черный")
        lawn_grass = LawnGrass("Трава", "Описание", 1500.0, 50,
                               "Россия", "14 дней", "Зеленый")

        product_str = str(product)
        smartphone_str = str(smartphone)
        lawn_grass_str = str(lawn_grass)

        # Все три представления должны быть разными
        assert product_str != smartphone_str
        assert product_str != lawn_grass_str
        assert smartphone_str != lawn_grass_str


class TestMethodInheritance:
    """Тесты наследования методов"""

    def test_inherited_methods_work(self, sample_smartphone, sample_lawn_grass):
        """Тест что унаследованные методы работают в наследниках"""
        # Проверяем метод calculate_total_value
        smartphone_total = sample_smartphone.calculate_total_value()
        assert smartphone_total == 180000.0 * 5

        lawn_grass_total = sample_lawn_grass.calculate_total_value()
        assert lawn_grass_total == 1500.0 * 100

        # Проверяем свойство price
        assert sample_smartphone.price == 180000.0
        assert sample_lawn_grass.price == 1500.0

        # Проверяем сеттер price
        sample_smartphone.price = 190000.0
        assert sample_smartphone.price == 190000.0

        sample_lawn_grass.price = 1600.0
        assert sample_lawn_grass.price == 1600.0