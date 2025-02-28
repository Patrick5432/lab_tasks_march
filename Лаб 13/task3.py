class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def print_info(self):
        print(f"Имя: {self.name}, Порода: {self.species}")


class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name, "Собака")
        self.breed = breed

    def print_info(self):
        super().print_info()
        print(f"Разведена: {self.breed}")


# Пример использования
dog = Dog("Чавчик", "Пит-Вбуль")
dog.print_info()