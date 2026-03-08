from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    def __init__(self, name, description, price, quantity):
        """Инициализация продукта"""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        """Строковое представление продукта"""
        pass

    @abstractmethod
    def calculate_total_value(self):
        """Рассчитывает общую стоимость товара на складе"""
        pass

    @property
    def price(self):
        """Геттер для цены"""
        return self._price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены"""
        self._price = new_price

    @classmethod
    @abstractmethod
    def new_product(cls, product_data, products_list=None):
        """Создает новый продукт или обновляет существующий"""
        pass

    @abstractmethod
    def __add__(self, other):
        """Сложение продуктов"""
        pass


class ReprMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        """Инициализация с логированием"""

        super().__init__(*args, **kwargs)

        if hasattr(self, '_init_params'):
            class_name = self.__class__.__name__
            params = self._init_params
            param_str = ', '.join([f"{k}={v!r}" for k, v in params.items()])
            print(f"Создан объект: {class_name}({param_str})")



    def __repr__(self):
        """Представление объекта для отладки"""
        if hasattr(self, '_init_params'):
            params = self._init_params
            param_str = ', '.join([f"{k}={v!r}" for k, v in params.items()])
            return f"{self.__class__.__name__}({param_str})"
        return super().__repr__()


class BaseEntity(ABC):
    """Абстрактный базовый класс для сущностей с общими свойствами"""

    def __init__(self, name):
        """Инициализация сущности"""
        self._name = name

    @property
    def name(self):
        """Геттер для имени"""
        return self._name

    @name.setter
    def name(self, value):
        """Сеттер для имени"""
        if not value:
            raise ValueError("Имя не может быть пустым")
        self._name = value

    @abstractmethod
    def __str__(self):
        """Строковое представление"""
        pass

    @abstractmethod
    def __repr__(self):
        """Представление для отладки"""
        pass


class Order(BaseEntity):
    """Класс для заказа"""

    def __init__(self, product, quantity):
        """
        Инициализация заказа
        param product - объект продукта
        param quantity - количество
        """
        super().__init__(f"Заказ: {product.name}")
        self.product = product
        self.quantity = quantity
        self.total_cost = self.calculate_total()

    def calculate_total(self):
        """Рассчитывает итоговую стоимость заказа"""
        return self.product.price * self.quantity

    def __str__(self):
        """Строковое представление заказа"""
        return (f"{self.name}, товар: {self.product.name}, "
                f"количество: {self.quantity}, сумма: {self.total_cost} руб.")

    def __repr__(self):
        """Представление для отладки"""
        return f"Order(product={self.product!r}, quantity={self.quantity})"

    @property
    def total(self):
        """Геттер для общей стоимости"""
        return self.total_cost

    @total.setter
    def total(self, value):
        """Сеттер для общей стоимости (пересчитывает при изменении)"""
        if value != self.calculate_total():
            self.total_cost = value

class Product(ReprMixin, BaseProduct):
    name: str
    description: str
    quantity: int
    color: str

    def __init__(self, name, description, price, quantity, color=None):
        if not hasattr(self, '_init_params'):
            self._init_params = {
                'name': name,
                'description': description,
                'price': price,
                'quantity': quantity,
                'color': color
            }

        super().__init__(name, description, price, quantity)
        self.color = color

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
        return self._price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if hasattr(self, '_price') and new_price < self._price:
            try:
                response = input(f"Price is decreasing from {self._price} to {new_price}. "
                                 f"Confirm change (y/n): ").strip().lower()
                if response != 'y':
                    print("Изменение цены отменено")
                    return
            except:
                print("Изменение цены отменено")
                return

        self._price = new_price


    def __str__(self):
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        """Представление для отладки"""
        return f"Product({self.name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        """Сложение продуктов (Задание 2)"""
        if not isinstance(other, type(self)):
            raise TypeError("Можно складывать только объекты одного класса: {type(self).__name__}")

        if self.name != other.name:
            raise ValueError("Можно складывать только одинаковые продукты")

        total_quantity = self.quantity + other.quantity
        max_price = max(self.price, other.price)

        return type(self)(
            self.name,
            self.description,
            max_price,
            total_quantity,
            self.color
        )

    def calculate_total_value(self):
        """Рассчитывает общую стоимость товара на складе"""
        return self.price * self.quantity


class Smartphone(Product):
    """Класс для смартфонов"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        self._init_params = {
            'name': name,
            'description': description,
            'price': price,
            'quantity': quantity,
            'efficiency': efficiency,
            'model': model,
            'memory': memory,
            'color': color
        }

        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory

    def __repr__(self):
        """Представление для отладки"""
        return (f"Smartphone('{self.name}', {self.price}, {self.quantity}, "
                f"efficiency='{self.efficiency}', model='{self.model}', "
                f"memory='{self.memory}', color='{self.color}')")

    def __str__(self):
        return f"{self.name} {self.model}, {self.memory} ГБ, цвет {self.color}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение смартфонов (Задание 2)"""
        if not isinstance(other, type(self)):
            raise TypeError(f"Можно складывать только объекты одного класса: {type(self).__name__}")

        if self.name != other.name:
            raise ValueError("Можно складывать только одинаковые продукты")

        total_quantity = self.quantity + other.quantity
        max_price = max(self.price, other.price)

        return type(self)(
            self.name,
            self.description,
            max_price,
            total_quantity,
            self.efficiency,
            self.model,
            self.memory,
            self.color
        )




class LawnGrass(Product):
    """Класс для газонной травы"""

    country: str
    germination_period: int


    def __init__(self, name, description, price, quantity,
                 country, germination_period, color):
        self._init_params = {
            'name': name,
            'description': description,
            'price': price,
            'quantity': quantity,
            'country': country,
            'germination_period': germination_period,
            'color': color
        }

        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period

    def __repr__(self):
        """Представление для отладки"""
        return (f"LawnGrass('{self.name}', {self.price}, {self.quantity}, "
                f"country='{self.country}', germination_period='{self.germination_period}', "
                f"color='{self.color}')")

    def __str__(self):
        """Строковое представление газонной травы"""
        return f"{self.name}, {self.country}, цвет: {self.color}, прорастание: {self.germination_period}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение газонной травы (Задание 2)"""
        if not isinstance(other, type(self)):
            raise TypeError(f"Можно складывать только объекты одного класса: {type(self).__name__}")

        if self.name != other.name:
            raise ValueError("Можно складывать только одинаковые продукты")

        total_quantity = self.quantity + other.quantity
        max_price = max(self.price, other.price)

        return type(self)(
            self.name,
            self.description,
            max_price,
            total_quantity,
            self.country,
            self.germination_period,
            self.color
        )


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
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        if not issubclass(type(product), Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        for existing_product in self.__products:
            if existing_product.name.lower() == product.name.lower():
                existing_product.quantity += product.quantity
                if product.price > existing_product.price:
                    existing_product.price = product.price
                return

        self.__products.append(product)
        Category.product_count += 1

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