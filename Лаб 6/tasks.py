def main():
    # Задача 1
    number1 = 12345
    digit_count1 = count_digits(number1)
    print(f"Количество цифр в числе {number1}: {digit_count1}")  # Вывод: 5

    number2 = 0
    digit_count2 = count_digits(number2)
    print(f"Количество цифр в числе {number2}: {digit_count2}")  # Вывод: 1

    number3 = -123
    digit_count3 = count_digits(number3)
    print(f"Количество цифр в числе {number3}: {digit_count3}")  # Вывод: 3

    # Задача 2
    n1 = 5
    factorial1 = calculate_factorial(n1)
    print(f"Факториал числа {n1}: {factorial1}")  # Вывод: 120

    n2 = 0
    factorial2 = calculate_factorial(n2)
    print(f"Факториал числа {n2}: {factorial2}")  # Вывод: 1

    n3 = 10
    factorial3 = calculate_factorial(n3)
    print(f"Факториал числа {n3}: {factorial3}")  # Вывод: 3628800

    try:
        n4 = -5
        factorial4 = calculate_factorial(n4)  # вызовет исключение
    except ValueError as ex:
        print(ex)


# Задача 1: Функция для вычисления количества цифр числа
def count_digits(number):
    # Обрабатываем отрицательные числа, беря их абсолютное значение
    number = abs(number)

    if number == 0:
        return 1  # Особый случай для числа 0

    count = 0
    while number > 0:
        number //= 10  # Делим на 10, чтобы избавиться от последней цифры
        count += 1
    return count


# Задача 2: Функция для вычисления факториала числа
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел.")

    if n == 0:
        return 1  # Факториал 0 равен 1

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


if __name__ == "__main__":
    main()