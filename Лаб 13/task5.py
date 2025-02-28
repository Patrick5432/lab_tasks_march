class Man:
    def __init__(self, last_name, initials, phone, address, age):
        self.last_name = last_name
        self.initials = initials
        self.phone = phone
        self.address = address
        self.age = age

    def print_info(self):
        print(f"Фамилия: {self.last_name}, Инициалы: {self.initials}, Телефон: {self.phone}, Адрес: {self.address}, Возраст: {self.age}")


class Manager(Man):
    def __init__(self, last_name, initials, phone, address, age, department_number, number_of_subordinates):
        super().__init__(last_name, initials, phone, address, age)
        self.department_number = department_number
        self.number_of_subordinates = number_of_subordinates

    def print_info(self):
        super().print_info()
        print(f"Номер департамента: {self.department_number}, Номер Сотрудника: {self.number_of_subordinates}")


# Пример использования
manager = Manager("Шелков", "А.Ф.", "8999999999", "Сосновая 5", 23, 20, 2221)
manager.print_info()