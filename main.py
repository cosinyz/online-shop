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
