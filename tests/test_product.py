import pytest

from src.main import Product, Category


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

    def test_product_price_setter(self):
        """Тест сеттера цены продукта"""
        print("\n=== Тест сеттера цены ===")

        product = Product("Test", "Test desc", 100, 10)
        print(f"Начальная цена: {product.price}")

        product.price = -50

        product.price = 0

        product.price = 150
        print(f"Новая цена: {product.price}")

    def test_new_product_method(self):
        """Тест метода создания нового продукта"""
        print("\n=== Тест new_product ===")

        products_list = []

        data1 = {'name': 'Телефон', 'description': 'Смартфон', 'price': 10000, 'quantity': 5}
        product1 = Product.new_product(data1, products_list)
        products_list.append(product1)
        print(f"Создан продукт 1: {product1}")

        data2 = {'name': 'телефон', 'description': 'Другой смартфон', 'price': 12000, 'quantity': 3}
        product2 = Product.new_product(data2, products_list)
        print(f"После добавления дубликата: {product2}")
        print(f"Количество продуктов в списке: {len(products_list)}")

    def test_category_products(self):
        """Тест работы с продуктами в категории"""
        print("\n=== Тест категории и продуктов ===")

        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray", 210000.0, 8)

        category = Category("Смартфоны", "Описание", [product1, product2])

        print(f"Категория: {category.name}")
        print(f"Количество продуктов: {len(category)}")
        print("Список продуктов:")
        for product in category.products:
            print(f"  - {product}")

        product3 = Product("Xiaomi Redmi", "1024GB, Синий", 31000.0, 14)
        category.add_product(product3)

        print(f"\nПосле добавления нового продукта:")
        print(f"Количество продуктов: {len(category)}")
        for product in category.products:
            print(f"  - {product}")

    def test_duplicate_products(self):
        """Тест обработки дубликатов продуктов"""
        print("\n=== Тест дубликатов ===")

        product1 = Product("Ноутбук", "Игровой", 50000, 3)
        product2 = Product("ноутбук", "Офисный", 45000, 2)

        category = Category("Электроника", "Техника", [product1])

        print("До добавления дубликата:")
        for product in category.products:
            print(f"  - {product}")

        category.add_product(product2)

        print("\nПосле добавления дубликата:")
        for product in category.products:
            print(f"  - {product}")