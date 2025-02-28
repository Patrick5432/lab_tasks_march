def main():
    # Задача 1
    print("--- Задача 1 ---")
    matrix1 = [
        [1, -2, 3],
        [-4, 5, -6],
        [7, -8, 9]
    ]

    print("Исходная матрица:")
    print_matrix(matrix1)

    transformed_matrix1 = transform_matrix(matrix1)
    print("Преобразованная матрица:")
    print_matrix(transformed_matrix1)

    # Задача 2
    print("\n--- Задача 2 ---")
    magic_square1 = [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1]
    ]

    not_magic_square = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Матрица 1:")
    print_matrix(magic_square1)
    print("Является магическим квадратом?", is_magic_square(magic_square1))

    print("Матрица 2:")
    print_matrix(not_magic_square)
    print("Является магическим квадратом?", is_magic_square(not_magic_square))

    # Задача 3
    print("\n--- Задача 3 ---")
    matrix2 = [
        [5, 2, 8, 1],
        [9, 4, 6, 3],
        [7, 10, 2, 5]
    ]
    print("Исходная матрица:")
    print_matrix(matrix2)

    sorted_matrix = sort_rows(matrix2)
    print("Матрица с отсортированными строками:")
    print_matrix(sorted_matrix)


# Вспомогательная функция для вывода матрицы
def print_matrix(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))


# Задача 1: Замена положительных элементов на 1, отрицательных на 0
def transform_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transformed_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] > 0:
                transformed_matrix[i][j] = 1
            else:
                transformed_matrix[i][j] = 0
    return transformed_matrix


# Задача 2: Проверка, является ли матрица магическим квадратом
def is_magic_square(matrix):
    n = len(matrix)
    if n != len(matrix[0]):
        return False  # Не квадратная матрица

    magic_sum = sum(matrix[0])  # Сумма первой строки

    # Проверяем строки
    for i in range(1, n):
        if sum(matrix[i]) != magic_sum:
            return False

    # Проверяем столбцы
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += matrix[i][j]
        if col_sum != magic_sum:
            return False

    return True


# Задача 3: Сортировка элементов в каждой строке
def sort_rows(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    sorted_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        row = matrix[i].copy()
        row.sort()
        for j in range(cols):
            sorted_matrix[i][j] = row[j]
    return sorted_matrix


if __name__ == "__main__":
    main()