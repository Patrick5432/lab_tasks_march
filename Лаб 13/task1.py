class Furniture:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        self.price = price

    def print_details(self):
        print(f"Бренд: {self.brand}, Название: {self.name}, Цена: {self.price}")


class Table(Furniture):
    def __init__(self, brand, name, price, has_backrest, number_of_legs):
        super().__init__(brand, name, price)
        self.has_backrest = has_backrest
        self.number_of_legs = number_of_legs

    def print_details(self):
        super().print_details()
        print(f"Спинка сиденья: {self.has_backrest}, Количество ножек: {self.number_of_legs}")


# Пример использования
furniture = Furniture("Фантом", "Мышка", 1500.00)
table = Table("Ардор", "Клавиатура", 2500.00, True, 4)

print("Описание мышки:")
furniture.print_details()

print("\nОписание клавиатуры:")
table.print_details()