from src.main import Category, Product


def test_string_representation():
    """Тест строкового представления (Задание 1)"""
    print("\n=== Тест строкового представления ===")

    product = Product("Телефон", "Смартфон", 10000, 5)
    print(f"Строковое представление продукта: {product}")

    category = Category("Электроника", "Техника", [product])
    print(f"Строковое представление категории: {category}")


def test_product_addition():
    """Тест сложения продуктов (Задание 2)"""
    print("\n=== Тест сложения продуктов ===")

    product1 = Product("Ноутбук", "Игровой", 50000, 3)
    product2 = Product("Ноутбук", "Игровой", 45000, 2)

    print(f"Продукт 1: {product1}")
    print(f"Продукт 2: {product2}")

    try:
        product3 = product1 + product2
        print(f"Суммарный продукт: {product3}")
        print(f"Общее количество: {product3.quantity}")
        print(f"Выбранная цена: {product3.price}")
    except ValueError as e:
        print(f"Ошибка: {e}")

    product4 = Product("Телефон", "Смартфон", 20000, 4)
    try:
        result = product1 + product4
    except ValueError as e:
        print(f"Ожидаемая ошибка при сложении разных продуктов: {e}")


def test_total_value_calculation():
    """Тест расчета общей стоимости"""
    print("\n=== Тест расчета общей стоимости ===")

    product = Product("Планшет", "10 дюймов", 25000, 4)
    total_value = product.calculate_total_value()
    print(f"Продукт: {product}")
    print(f"Общая стоимость на складе: {total_value} руб.")


def test_category_iterator():
    """Тест итератора по категории (Дополнительное задание)"""
    print("\n=== Тест итератора по категории ===")

    product1 = Product("Монитор", "27 дюймов", 15000, 3)
    product2 = Product("Клавиатура", "Механическая", 5000, 10)
    product3 = Product("Мышь", "Беспроводная", 3000, 15)

    category = Category("Компьютерная периферия", "Устройства ввода-вывода",
                        [product1, product2, product3])

    print("Перебор товаров в категории через цикл for:")
    for product in category:
        print(f"  - {product}")

    print("\nПрямое использование итератора:")
    iterator = iter(category)
    try:
        while True:
            product = next(iterator)
            print(f"  - {product}")
    except StopIteration:
        print("Конец списка товаров")


def test_optimized_products_getter():
    """Тест оптимизированного геттера продуктов"""
    print("\n=== Тест оптимизированного геттера ===")

    product1 = Product("Наушники", "Беспроводные", 8000, 7)
    product2 = Product("Колонка", "Портативная", 12000, 5)

    category = Category("Аудиотехника", "Устройства для воспроизведения звука",
                        [product1, product2])

    print("Список продуктов через геттер:")
    for product_str in category.products:
        print(f"  - {product_str}")


def test_previous_functionality():
    """Тест предыдущей функциональности"""
    print("\n=== Тест предыдущей функциональности ===")

    product = Product("Тест", "Описание", 100, 10)
    assert product.name == "Тест"
    assert product.quantity == 10

    product.price = 150
    assert product.price == 150

    category = Category("Тест категория", "Описание", [product])
    assert len(category) == 1

    products_list = []
    data = {'name': 'Новый', 'description': 'Описание', 'price': 200, 'quantity': 5}
    new_product = Product.new_product(data, products_list)
    assert new_product.name == "Новый"
    assert new_product.price == 200

    print("Все предыдущие тесты пройдены успешно!")