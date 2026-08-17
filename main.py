class Product:
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def show_info(self):
        print(f"Товар: {self.name}")
        print(f"Цена: {self.price:.2f} сом")
        print(f"На складе: {self.stock} шт.")
        print(f"Категория: {self.category}")
        print("-" * 30)

    def change_price(self, new_price):
        if new_price >= 0:
            self.price = new_price
        else:
            print("Цена не может быть отрицательной.")

    def increase_stock(self, amount):
        if amount > 0:
            self.stock += amount
        else:
            print("Количество должно быть положительным.")

    def decrease_stock(self, amount):
        if amount > 0 and amount <= self.stock:
            self.stock -= amount
        else:
            print("Недостаточно товара на складе.")

    def is_available(self):
        return self.stock > 0

class User:
    def __init__(self, name, email, balance=0):
        self.name = name
        self.email = email
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Баланс пополнен на {amount:.2f} сом.")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Недостаточно средств.")
            return False

    def show_info(self):
        print(f"Пользователь: {self.name}")
        print(f"Email: {self.email}")
        print(f"Баланс: {self.balance:.2f} сом")
        print("-" * 30)

class Order:
    def __init__(self, user):
        self.user = user
        self.products = []
        self.status = "Новый"

    def add_product(self, product):
        if product.is_available():
            self.products.append(product)
            print(f"Товар «{product.name}» добавлен в заказ.")
        else:
            print(f"Товар «{product.name}» отсутствует на складе.")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Товар «{product.name}» удалён из заказа.")

    def get_total(self):
        return sum(product.price for product in self.products)

    def change_status(self, new_status):
        self.status = new_status

    def show_info(self):
        print("===== ЗАКАЗ =====")
        print(f"Покупатель: {self.user.name}")
        print(f"Статус: {self.status}")

        for product in self.products:
            print(f"- {product.name}: {product.price:.2f} сом")

        print(f"Итого: {self.get_total():.2f} сом")

    def checkout(self):
        total = self.get_total()

        if not self.products:
            print("Заказ пуст.")
            return

        for product in self.products:
            if not product.is_available():
                print(f"Товар {product.name} закончился.")
                return

        if self.user.withdraw(total):
            for product in self.products:
                product.decrease_stock(1)

            self.change_status("Оплачен")
            print(f"Заказ оформлен на сумму {total:.2f} сом.")
        else:
            print("Недостаточно средств.")


class Electronics(Product):
    def __init__(self, name, price, stock, category, warranty_months, manufacturer):
        super().__init__(name, price, stock, category)
        self.warranty_months = warranty_months
        self.manufacturer = manufacturer

    def show_info(self):
        print("===== ЭЛЕКТРОНИКА =====")
        print(f"Название: {self.name}")
        print(f"Цена: {self.price:.2f} сом")
        print(f"Количество: {self.stock} шт.")
        print(f"Категория: {self.category}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Гарантия: {self.warranty_months} мес.")
        print()


class Clothing(Product):
    def __init__(self, name, price, stock, category, size, material, color):
        super().__init__(name, price, stock, category)
        self.size = size
        self.material = material
        self.color = color

    def show_info(self):
        print("===== ОДЕЖДА =====")
        print(f"Название: {self.name}")
        print(f"Цена: {self.price:.2f} сом")
        print(f"Количество: {self.stock} шт.")
        print(f"Категория: {self.category}")
        print(f"Размер: {self.size}")
        print(f"Материал: {self.material}")
        print(f"Цвет: {self.color}")
        print()


class Food(Product):
    def __init__(self, name, price, stock, category, expiration_date, weight):
        super().__init__(name, price, stock, category)
        self.expiration_date = expiration_date
        self.weight = weight

    def show_info(self):
        print("===== ПРОДУКТ =====")
        print(f"Название: {self.name}")
        print(f"Цена: {self.price:.2f} сом")
        print(f"Количество: {self.stock} шт.")
        print(f"Категория: {self.category}")
        print(f"Срок годности: {self.expiration_date}")
        print(f"Вес: {self.weight} кг")
        print()



