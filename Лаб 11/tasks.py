import random

class Soldier:
    def __init__(self, name="Noname", health=100):
        self._name = name
        self.health = health

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def make_kick(self, enemy):
        enemy.health -= 20
        if enemy.health < 0:
            enemy.health = 0
        self.health += 10
        print(f"{self.name} бьет {enemy.name}")
        print(f"{enemy.name} = {enemy.health}")


class Battle:
    def __init__(self, u1, u2):
        self._u1 = u1
        self._u2 = u2
        self.result = "Сражения не было"

    def battle_start(self):
        while self._u1.health > 0 and self._u2.health > 0:
            n = random.randint(1, 2)  # Генерируем случайное число 1 или 2

            if n == 1:
                self._u1.make_kick(self._u2)
            else:
                self._u2.make_kick(self._u1)

        if self._u1.health > self._u2.health:
            self.result = f"{self._u1.name} ПОБЕДА"
        elif self._u2.health > self._u1.health:
            self.result = f"{self._u2.name} ПОБЕДА"
        else:
            self.result = "Ничья"

    def who_win(self):
        print(self.result)


def main():
    first = Soldier("Mr. First", 140)
    second = Soldier()
    second.name = "Mr. Second"

    b = Battle(first, second)
    b.battle_start()
    b.who_win()

    input("Нажмите Enter, чтобы выйти...")  # Чтобы консоль не закрывалась сразу


if __name__ == "__main__":
    main()