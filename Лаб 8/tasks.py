class Student:
    def __init__(self, full_name="", group_number=0, progress=None):
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress if progress is not None else []

    def __str__(self):
        return f"Студент: {self.full_name} Группа: {self.group_number} Оценки: {' '.join(map(str, self.progress))}"


def main():
    st_size = 2  # Количество студентов (уменьшено для удобства тестирования)
    students = []

    for i in range(st_size):
        print(f"Введите полное имя студента {i + 1}:")
        full_name = input()

        while True:
            try:
                print("Введите номер группы:")
                group_number = int(input())
                break
            except ValueError:
                print("Некорректный ввод. Введите целое число для номера группы:")

        print("Введите 5 оценок в столбик:")
        progress = []
        n = 5  # Количество оценок у каждого студента
        for j in range(n):
            while True:
                try:
                    score = int(input())
                    if score < 1 or score > 5:
                        print("Введите оценку от 1 до 5:")
                        continue
                    break
                except ValueError:
                    print("Некорректный ввод. Введите целое число для оценки:")
            progress.append(score)

        st = Student(full_name, group_number, progress)
        students.append(st)

    print("\Список студентов:")
    for st in students:
        print(st)

    # Сортировка по фамилии (используем sorted)
    sorted_students = sorted(students, key=lambda s: s.full_name)

    print("\nОтсортированные студенты:")
    for st in sorted_students:
        print(st)

    print("\nСтуденты с плохими оценками:")
    n0 = 0  # Счетчик неуспевающих
    for st in students:
        if any(val < 3 for val in st.progress):
            # Есть плохая оценка
            print(st)
            n0 += 1

    if n0 == 0:
        print("Ничего не нашлось.")

    input("Нажмите Enter, чтобы выйти...")  # Чтобы консоль не закрывалась сразу


if __name__ == "__main__":
    main()