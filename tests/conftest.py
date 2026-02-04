import pytest

from src.main import Category, Product, Smartphone, LawnGrass


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

@pytest.fixture
def sample_category_empty():
    """Фикстура для создания пустой категории"""
    return Category(
        name="Пустая категория",
        description="Описание пустой категории",
        products=[]
    )

@pytest.fixture
def sample_smartphone():
    """Фикстура для создания смартфона"""
    return Smartphone(
        name="Samsung Galaxy S23",
        description="Флагманский смартфон",
        price=180000.0,
        quantity=5,
        efficiency="Высокая",
        model="S23 Ultra",
        memory="256",
        color="Серый"
    )


@pytest.fixture
def sample_lawn_grass():
    """Фикстура для создания газонной травы"""
    return LawnGrass(
        name="Трава газонная Премиум",
        description="Мягкая и густая трава",
        price=1500.0,
        quantity=100,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый"
    )


@pytest.fixture
def sample_mixed_products(sample_product, sample_smartphone, sample_lawn_grass):
    """Фикстура для смешанного списка продуктов"""
    return [sample_product, sample_smartphone, sample_lawn_grass]