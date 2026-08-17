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