from src.main import Category


class TestCategoryCounters:
    """Тесты для счетчиков категорий и продуктов"""

    def test_category_counter_increment(self, reset_counters):
        """Тест подсчета количества категорий"""
        category1 = Category("Кат1", "Описание1", [])
        category2 = Category("Кат2", "Описание2", [])
        category3 = Category("Кат3", "Описание3", [])

        assert Category.category_count == 3

    def test_product_counter_in_categories(self, reset_counters, sample_products):
        """Тест подсчета общего количества продуктов в категориях"""
        Category("Кат1", "Описание1", sample_products[:2])  # 2 продукта
        Category("Кат2", "Описание2", sample_products[2:])  # 1 продукт

        assert Category.product_count == 3

    def test_empty_category_counter(self, reset_counters):
        """Тест счетчика для категории без продуктов"""
        Category("Пустая категория", "Без продуктов", [])

        assert Category.category_count == 1
        assert Category.product_count == 0

    def test_single_product_category_counter(self, reset_counters, sample_product):
        """Тест счетчика для категории с одним продуктом"""
        Category("Категория", "Описание", [sample_product])

        assert Category.category_count == 1
        assert Category.product_count == 1

    def test_product_counter_with_duplicate_products(self, reset_counters, sample_product):
        """Тест счетчика продуктов с одинаковыми продуктами в разных категориях"""
        Category("Кат1", "Описание1", [sample_product])
        Category("Кат2", "Описание2", [sample_product])

        assert Category.product_count == 2
        assert Category.category_count == 2

    def test_mixed_counters(self, reset_counters, sample_products):
        """Тест одновременного подсчета категорий и продуктов"""
        Category("Кат1", "Описание1", sample_products[:1])  # 1 продукт
        Category("Кат2", "Описание2", sample_products[1:])  # 2 продукта

        assert Category.category_count == 2
        assert Category.product_count == 3