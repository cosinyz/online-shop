from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, price, stock, category):
        self.name = name
        self._price = 0
        self._stock = 0
        self.category = category

        self.set_price(price)
        self.set_stock(stock)

    @abstractmethod
    def show_info(self):
        pass

    @abstractmethod
    def calculate_discount(self):
        pass

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self._price = new_price

    def get_stock(self):
        return self._stock

    def set_stock(self, new_stock):
        if new_stock < 0:
            raise ValueError("Количество товара не может быть отрицательным.")
        self._stock = new_stock

    def change_price(self, new_price):
        self.set_price(new_price)

    def increase_stock(self, amount):
        if amount <= 0:
            raise ValueError("Количество должно быть положительным.")
        self._stock += amount

    def decrease_stock(self, amount):
        if amount <= 0:
            raise ValueError("Количество должно быть положительным.")

        if amount > self._stock:
            raise ValueError("Недостаточно товара на складе.")

        self._stock -= amount

    def is_available(self):
        return self._stock > 0

    def get_final_price(self):
        discount = self.calculate_discount()
        return self._price * (1 - discount)



class User:
    def __init__(self, name, email, balance=0):
        self.name = name
        self.email = email
        self._balance = 0
        self.set_balance(balance)

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Баланс не может быть отрицательным.")
        self._balance = new_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")

        self._balance += amount
        print(f"Баланс пополнен на {amount:.2f} сом.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма списания должна быть положительной.")

        if amount > self._balance:
            print("Недостаточно средств.")
            return False

        self._balance -= amount
        return True

    def show_info(self):
        print(f"Пользователь: {self.name}")
        print(f"Email: {self.email}")
        print(f"Баланс: {self._balance:.2f} сом")
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
        return sum(product.get_final_price() for product in self.products)



    def change_status(self, new_status):
        self.status = new_status

    def show_info(self):
        print("===== ЗАКАЗ =====")
        print(f"Покупатель: {self.user.name}")
        print(f"Статус: {self.status}")

        for product in self.products:
            print(f"- {product.name}: {product.get_price()
} сом")

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

    def calculate_discount(self):
     return 0.20


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

    def calculate_discount(self):
     return 0.20


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

    def calculate_discount(self):
     return 0.05


    def show_info(self):
        print("===== ПРОДУКТ =====")
        print(f"Название: {self.name}")
        print(f"Цена: {self.price:.2f} сом")
        print(f"Количество: {self.stock} шт.")
        print(f"Категория: {self.category}")
        print(f"Срок годности: {self.expiration_date}")
        print(f"Вес: {self.weight} кг")
        print()



