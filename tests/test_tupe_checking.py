import pytest

from src.main import Product, Smartphone, LawnGrass


class TestAddProductTypeChecking:
    """Тесты проверки типов при добавлении продуктов (Задание 3)"""

    def test_add_product_success(self, sample_category_empty, sample_product):
        """Тест успешного добавления обычного продукта"""
        sample_category_empty.add_product(sample_product)

        assert len(sample_category_empty) == 1
        assert isinstance(sample_category_empty.get_products()[0], Product)
        assert sample_category_empty.get_products()[0].name == "Телефон"

    def test_add_smartphone_success(self, sample_category_empty, sample_smartphone):
        """Тест успешного добавления смартфона"""
        sample_category_empty.add_product(sample_smartphone)

        assert len(sample_category_empty) == 1
        assert isinstance(sample_category_empty.get_products()[0], Smartphone)
        assert isinstance(sample_category_empty.get_products()[0], Product)
        assert sample_category_empty.get_products()[0].model == "S23 Ultra"

    def test_add_lawn_grass_success(self, sample_category_empty, sample_lawn_grass):
        """Тест успешного добавления газонной травы"""
        sample_category_empty.add_product(sample_lawn_grass)

        assert len(sample_category_empty) == 1
        assert isinstance(sample_category_empty.get_products()[0], LawnGrass)
        assert isinstance(sample_category_empty.get_products()[0], Product)
        assert sample_category_empty.get_products()[0].country == "Россия"

    def test_add_mixed_products_success(self, sample_category_empty):
        """Тест успешного добавления продуктов разных типов"""
        product = Product("Продукт", "Описание", 100.0, 5)
        smartphone = Smartphone("Смартфон", "Описание", 50000.0, 2,
                                "Высокая", "Модель", "256", "Черный")
        lawn_grass = LawnGrass("Трава", "Описание", 1500.0, 50,
                               "Россия", "14 дней", "Зеленый")

        sample_category_empty.add_product(product)
        sample_category_empty.add_product(smartphone)
        sample_category_empty.add_product(lawn_grass)

        assert len(sample_category_empty) == 3

        products = sample_category_empty.get_products()
        assert isinstance(products[0], Product)
        assert isinstance(products[1], Smartphone)
        assert isinstance(products[2], LawnGrass)


class TestAddInvalidTypeErrors:
    """Тесты ошибок при добавлении некорректных типов (Задание 3)"""

    def test_add_string_error(self, sample_category_empty):
        """Тест ошибки при добавлении строки"""
        with pytest.raises(TypeError) as exc_info:
            sample_category_empty.add_product("Не продукт")

        error_message = str(exc_info.value)
        assert "Можно добавлять только объекты класса Product или его наследников" in error_message
        assert len(sample_category_empty) == 0

    def test_add_integer_error(self, sample_category_empty):
        """Тест ошибки при добавления числа"""
        with pytest.raises(TypeError) as exc_info:
            sample_category_empty.add_product(123)

        error_message = str(exc_info.value)
        assert "Можно добавлять только объекты класса Product или его наследников" in error_message
        assert len(sample_category_empty) == 0

    def test_add_list_error(self, sample_category_empty):
        """Тест ошибки при добавлении списка"""
        with pytest.raises(TypeError) as exc_info:
            sample_category_empty.add_product(["продукт1", "продукт2"])

        error_message = str(exc_info.value)
        assert "Можно добавлять только объекты класса Product или его наследников" in error_message
        assert len(sample_category_empty) == 0

    def test_add_dict_error(self, sample_category_empty):
        """Тест ошибки при добавлении словаря"""
        with pytest.raises(TypeError) as exc_info:
            sample_category_empty.add_product({"name": "Продукт", "price": 100})

        error_message = str(exc_info.value)
        assert "Можно добавлять только объекты класса Product или его наследников" in error_message
        assert len(sample_category_empty) == 0

    def test_add_none_error(self, sample_category_empty):
        """Тест ошибки при добавлении None"""
        with pytest.raises(TypeError) as exc_info:
            sample_category_empty.add_product(None)

        error_message = str(exc_info.value)
        assert "Можно добавлять только объекты класса Product или его наследников" in error_message
        assert len(sample_category_empty) == 0


class TestCustomClassTypeChecking:
    """Тесты с пользовательскими классами (Задание 3)"""

    def test_add_custom_class_not_inherited_error(self, sample_category_empty):
        """Тест ошибки при добавлении класса, не наследующего Product"""

        class NotAProduct:
            def __init__(self):
                self.name = "Не продукт"
                self.price = 100

        not_product = NotAProduct()

        with pytest.raises(TypeError) as exc_info:
            sample_category_empty.add_product(not_product)

        error_message = str(exc_info.value)
        assert "Можно добавлять только объекты класса Product или его наследников" in error_message
        assert len(sample_category_empty) == 0

    def test_add_custom_class_inherited_success(self, sample_category_empty):
        """Тест успешного добавления пользовательского класса, наследующего Product"""

        class CustomProduct(Product):
            def __init__(self, name, description, price, quantity, custom_attr):
                super().__init__(name, description, price, quantity)
                self.custom_attr = custom_attr

        custom_product = CustomProduct(
            name="Кастомный продукт",
            description="Описание",
            price=1000.0,
            quantity=3,
            custom_attr="специальный атрибут"
        )

        sample_category_empty.add_product(custom_product)

        assert len(sample_category_empty) == 1
        product = sample_category_empty.get_products()[0]
        assert isinstance(product, CustomProduct)
        assert isinstance(product, Product)
        assert product.name == "Кастомный продукт"
        assert product.custom_attr == "специальный атрибут"


class TestIssubclassAndIsinstanceCheck:
    """Тесты использования issubclass и isinstance (Задание 3)"""

    def test_isinstance_check_works(self, sample_category_empty, sample_smartphone):
        """Тест что isinstance проверяет корректно"""
        # Smartphone является экземпляром Product
        assert isinstance(sample_smartphone, Product)

        # И его можно добавить
        sample_category_empty.add_product(sample_smartphone)
        assert len(sample_category_empty) == 1

    def test_issubclass_check_works(self):
        """Тест что issubclass проверяет корректно"""
        # Smartphone является подклассом Product
        assert issubclass(Smartphone, Product)

        # LawnGrass является подклассом Product
        assert issubclass(LawnGrass, Product)

        # Product является подклассом самого себя
        assert issubclass(Product, Product)


class TestMixedValidInvalidAdditions:
    """Тесты смешанных сценариев добавления"""

    def test_add_valid_then_invalid(self, sample_category_empty, sample_product):
        """Тест добавления валидного, затем невалидного объекта"""
        # Добавляем валидный продукт
        sample_category_empty.add_product(sample_product)
        assert len(sample_category_empty) == 1

        # Пытаемся добавить невалидный (должна быть ошибка)
        with pytest.raises(TypeError) as exc_info:
            sample_category_empty.add_product("неправильный тип")

        error_message = str(exc_info.value)
        assert "Можно добавлять только объекты класса Product или его наследников" in error_message

        # Количество продуктов не должно измениться
        assert len(sample_category_empty) == 1

    def test_add_invalid_then_valid(self, sample_category_empty, sample_smartphone):
        """Тест попытки добавить невалидный, затем валидный объект"""
        # Пытаемся добавить невалидный
        with pytest.raises(TypeError):
            sample_category_empty.add_product(123)

        # Категория должна остаться пустой
        assert len(sample_category_empty) == 0

        # Добавляем валидный
        sample_category_empty.add_product(sample_smartphone)
        assert len(sample_category_empty) == 1

    def test_multiple_valid_additions(self, sample_category_empty):
        """Тест множественных валидных добавлений"""
        products_to_add = [
            Product("Продукт1", "Описание", 100, 5),
            Smartphone("Смартфон1", "Описание", 50000, 2,
                       "Высокая", "Модель1", "128", "Черный"),
            LawnGrass("Трава1", "Описание", 1500, 50,
                      "Россия", "14 дней", "Зеленый"),
            Smartphone("Смартфон2", "Описание", 60000, 1,
                       "Средняя", "Модель2", "256", "Белый"),
            Product("Продукт2", "Описание", 200, 10),
        ]

        for product in products_to_add:
            sample_category_empty.add_product(product)

        assert len(sample_category_empty) == len(products_to_add)

        # Проверяем типы
        for i, product in enumerate(sample_category_empty.get_products()):
            assert isinstance(product, Product)
            assert product.name == products_to_add[i].name