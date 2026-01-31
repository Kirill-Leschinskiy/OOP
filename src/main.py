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
            response = input(f"Price is decreasing from {self.__price} to {new_price}. "
                             f"Confirm change (y/n): ").strip().lower()
            if response != 'y':
                print("Изменение цены отменено")
                return

        self.__price = new_price
        if hasattr(self, '_Product__price'):
            print(f"Цена успешно изменена на {new_price}")

    def __str__(self):
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


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



if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)