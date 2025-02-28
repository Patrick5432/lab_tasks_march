class Passport:
    def __init__(self, first_name, last_name, country, date_of_birth, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.date_of_birth = date_of_birth
        self.passport_number = passport_number

    def print_info(self):
        print("\Полное имя:", self.first_name, self.last_name)
        print("Дата рождения:", self.date_of_birth)
        print("Страна:", self.country)
        print("Паспорт:", self.passport_number)


class ForeignPassport(Passport):
    def __init__(self, first_name, last_name, country, date_of_birth, passport_number, visa):
        super().__init__(first_name, last_name, country, date_of_birth, passport_number)
        self.visa = visa

    def print_info(self):
        super().print_info()
        print("Visa:", self.visa)


def main():
    passport_list = []

    request1 = ForeignPassport("Максим", "Мерзкой", "Русский", "23.05.1999", "1231233", "Россия")
    passport_list.append(request1)

    request2 = Passport("Контенье", "Нитье", "Испания", "12.02.2001", "21423232")
    passport_list.append(request2)

    request3 = ForeignPassport("Некит", "Некитич", "ЮСА", "13.12.2010", "12312332", "Италияя")
    passport_list.append(request3)

    for emp in passport_list:
        emp.print_info()

    input("Нажмите Enter, чтобы выйти...")  # Чтобы консоль не закрывалась сразу


if __name__ == "__main__":
    main()