import pytest

from src.main import Category, Product


class TestCategory:
    """Тесты для класса Category"""

    def test_category_initialization(self, sample_category):
        """Тест корректности инициализации объекта Category"""
        assert sample_category.name == "Электроника"
        assert sample_category.description == "Техника и гаджеты"
        assert len(sample_category.products) == 3

    def test_category_with_empty_products(self):
        """Тест категории с пустым списком продуктов"""
        category = Category(
            name="Книги",
            description="Художественная литература",
            products=[]
        )

        assert category.name == "Книги"
        assert category.description == "Художественная литература"
        assert category.products == []
        assert len(category.products) == 0

    def test_category_with_single_product(self, sample_product):
        """Тест категории с одним продуктом"""
        category = Category(
            name="Литература",
            description="Книги разных жанров",
            products=[sample_product]
        )

        assert len(category.products) == 1
        assert category.products[0].name == "Телефон"
        assert category.products[0].price == 50000.0

    def test_category_products_are_correct_objects(self, sample_products):
        """Тест, что продукты в категории - правильные объекты"""
        category = Category("Категория", "Описание", sample_products)

        for i, product in enumerate(category.products):
            assert product.name == f"Товар{i + 1}"
            assert product.price == (i + 1) * 100.0

    @pytest.mark.parametrize("category_name,category_description,products_count", [
        ("Кат1", "Описание1", 0),
        ("Кат2", "Описание2", 1),
        ("Кат3", "Описание3", 5),
    ])
    def test_category_with_various_product_counts(self, category_name,
                                                  category_description,
                                                  products_count):
        """Параметризованный тест категорий с разным количеством продуктов"""
        products = [Product(f"Товар{i}", f"Описание{i}", i * 100.0, i)
                    for i in range(products_count)]

        category = Category(category_name, category_description, products)

        assert category.name == category_name
        assert category.description == category_description
        assert len(category.products) == products_count