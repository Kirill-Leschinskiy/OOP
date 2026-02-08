class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data, products_list=None):
        """Создает новый продукт или обновляет существующий"""
        name = product_data.get('name', '')
        description = product_data.get('description', '')
        price = product_data.get('price', 0)
        quantity = product_data.get('quantity', 0)

        if products_list:
            for product in products_list:
                if product.name.lower() == name.lower():
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
                    return product

        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if hasattr(self, '_Product__price') and new_price < self.__price:
            try:
                response = input(f"Price is decreasing from {self.__price} to {new_price}. "
                                 f"Confirm change (y/n): ").strip().lower()
                if response != 'y':
                    print("Изменение цены отменено")
                    return
            except:
                print("Изменение цены отменено")
                return

        self.__price = new_price


    def __str__(self):
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        """Представление для отладки"""
        return f"Product({self.name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        """Сложение продуктов (Задание 2)"""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")

        if self.name != other.name:
            raise ValueError("Можно складывать только одинаковые продукты")

        total_quantity = self.quantity + other.quantity
        max_price = max(self.price, other.price)

        return Product(self.name, self.description, max_price, total_quantity)

    def calculate_total_value(self):
        """Рассчитывает общую стоимость товара на складе"""
        return self.price * self.quantity


class CategoryIterator:
    """Итератор для перебора товаров в категории (Дополнительное задание)"""

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.get_products()):
            product = self.category.get_products()[self.index]
            self.index += 1
            return product
        raise StopIteration



class Category:
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product):
        """Добавляет продукт в категорию"""
        if isinstance(product, Product):
            for existing_product in self.__products:
                if existing_product.name.lower() == product.name.lower():
                    existing_product.quantity += product.quantity
                    if product.price > existing_product.price:
                        existing_product.price = product.price
                    return

            self.__products.append(product)
            Category.product_count += 1
        else:
            print("Можно добавлять только объекты класса Product")

    @property
    def products(self):
        """Геттер для списка продуктов"""
        return [str(product) for product in self.__products]

    def get_products(self):
        """Возвращает список объектов продуктов"""
        return self.__products

    def __len__(self):
        """Возвращает количество продуктов в категории"""
        return len(self.__products)

    def __str__(self):
        """Строковое представление категории (Задание 1)"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __repr__(self):
        """Представление для отладки"""
        return f"Category(name='{self.name}', products={len(self.__products)})"

    def __iter__(self):
        """Возвращает итератор для категории (Дополнительное задание)"""
        return CategoryIterator(self)



if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print("Продукты:")
    print(product1)
    print(product2)
    print(product3)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print("\nКатегория 1:")
    print(category1)
    print(f"Описание: {category1.description}")
    print(f"Количество уникальных продуктов: {len(category1)}")

    print("\nТовары в категории:")
    for product in category1.products:
        print(f"  - {product}")

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print("\nКатегория 2:")
    print(category2)
    print(f"Описание: {category2.description}")

    print(f"\nОбщее количество категорий: {Category.category_count}")
    print(f"Общее количество продуктов: {Category.product_count}")

    print("\n=== Демонстрация сложения продуктов ===")
    samsung1 = Product("Samsung S23", "Флагман", 80000, 3)
    samsung2 = Product("Samsung S23", "Флагман", 75000, 2)

    print(f"Партия 1: {samsung1}")
    print(f"Партия 2: {samsung2}")

    total_samsung = samsung1 + samsung2
    print(f"Общая партия: {total_samsung}")

    print("\n=== Демонстрация перебора товаров в категории ===")
    for idx, product in enumerate(category1, 1):
        print(f"{idx}. {product}")