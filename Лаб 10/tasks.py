class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def action(self):
        return "Не определено"

    def __str__(self):
        return f"{self.name} {self.make} {self.year}"


class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def __str__(self):
        return f"{self.name} {self.series} {self.make} {self.year}"

    def action(self):
        return "Печатает"


class Scanner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return "Сканирует"


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return "Копирует"


def main():
    sklad = []

    scanner = Scanner("ХП", "СупримМодель", 2025)
    sklad.append(scanner)

    xerox = Xerox("Пулевое", "НаЛегке", 2023)
    sklad.append(xerox)

    printer = Printer("Ножевой", "Нията", "Скандалист", 2021)
    sklad.append(printer)

    print("На складе имеются:")
    for x in sklad:
        print(x, x.action())

    # Удаляем все принтеры
    sklad = [x for x in sklad if not isinstance(x, Printer)]

    print("\nHa складе осталось:")
    for x in sklad:
        print(x, x.action())

    input("Нажмите Enter, чтобы выйти...")  # Чтобы консоль не закрывалась сразу


if __name__ == "__main__":
    main()