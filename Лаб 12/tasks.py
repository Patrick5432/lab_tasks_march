from abc import ABC, abstractmethod

class Class1(ABC):
    def __init__(self, val):
        self.x = val

    @abstractmethod
    def func(self):
        pass


class Class2(Class1):
    def __init__(self, val):
        super().__init__(val)

    def another_func(self):
        print(-self.x)


class Class3(Class2):
    def __init__(self, val):
        super().__init__(val)

    def func(self):
        print(self.x)


def main():
    c = Class3(10)
    c.func()          # Вывод: 10
    c.another_func()  # Вывод: -10

    input("Нажмите Enter, чтобы выйти...")  # Чтобы консоль не закрывалась сразу


if __name__ == "__main__":
    main()