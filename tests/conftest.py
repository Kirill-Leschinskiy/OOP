import pytest

from src.main import Category, Product


@pytest.fixture
def reset_counters():
    """Фикстура для сброса счетчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_product():
    """Фикстура для создания тестового продукта"""
    return Product(
        name="Телефон",
        description="Смартфон с хорошей камерой",
        price=50000.0,
        quantity=10
    )


@pytest.fixture
def sample_products():
    """Фикстура для создания списка продуктов"""
    return [
        Product("Товар1", "Описание1", 100.0, 5),
        Product("Товар2", "Описание2", 200.0, 3),
        Product("Товар3", "Описание3", 300.0, 7)
    ]


@pytest.fixture
def sample_category(sample_products):
    """Фикстура для создания тестовой категории"""
    return Category(
        name="Электроника",
        description="Техника и гаджеты",
        products=sample_products
    )