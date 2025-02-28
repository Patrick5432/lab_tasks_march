def main():
    # Задача 1
    print("--- Задача 1 ---")
    list1 = [1, 2, 3, 4, 5]
    print("Исходный список:", ", ".join(map(str, list1)))

    print("Элемент с индексом 2:", list1[2])

    list1[1] = 10
    print("Список после замены элемента:", ", ".join(map(str, list1)))

    list1.append(6)
    print("Список после добавления элемента:", ", ".join(map(str, list1)))

    list1.pop(3)
    print("Список после удаления элемента:", ", ".join(map(str, list1)))

    list2 = list1.copy()
    print("Дублированный список:", ", ".join(map(str, list2)))

    # Задача 2
    print("\n--- Задача 2 ---")
    list3 = [5, 2, 8, 1, 9, 4]
    min_index = find_min_index(list3)
    print("Список:", ", ".join(map(str, list3)))
    print("Индекс минимального элемента:", min_index)

    # Задача 3
    print("\n--- Задача 3 ---")
    list4 = [5, -2, 8, -1, 9, 0, -4, 3]
    positive_list, negative_zero_list = split_list(list4)
    print("Исходный список:", ", ".join(map(str, list4)))
    print("Положительные элементы:", ", ".join(map(str, positive_list)))
    print("Остальные элементы:", ", ".join(map(str, negative_zero_list)))

    # Задача 4
    print("\n--- Задача 4 ---")
    list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_sum = sum_of_odd_indexes(list5)
    print("Список:", ", ".join(map(str, list5)))
    print("Сумма элементов с нечетными индексами:", odd_sum)

    # Задача 5
    print("\n--- Задача 5 ---")
    list6 = [10, 20, 5, 15, 8, 25, 12, 3]
    transform_list(list6)
    print("Преобразованный список:", ", ".join(map(str, list6)))

    # Задача 6
    print("\n--- Задача 6 ---")
    list7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list8 = [5, 7, 9, 11, 13, 2, 4, 14, 15]
    common_elements = find_common_elements(list7, list8)
    print("Список 1:", ", ".join(map(str, list7)))
    print("Список 2:", ", ".join(map(str, list8)))
    print("Общие элементы в порядке возрастания:", ", ".join(map(str, common_elements)))


def find_min_index(lst):
    if not lst:
        raise ValueError("Список не может быть пустым")

    min_index = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
    return min_index


def split_list(lst):
    positive_list = [num for num in lst if num > 0]
    negative_zero_list = [num for num in lst if num <= 0]
    return positive_list, negative_zero_list


def sum_of_odd_indexes(lst):
    return sum(lst[i] for i in range(1, len(lst), 2))


def transform_list(lst):
    for i in range(len(lst)):
        if lst[i] < 15:
            lst[i] *= 2


def find_common_elements(list1, list2):
    set1 = set(list1)
    common = [x for x in list2 if x in set1]
    common.sort()
    return common


if __name__ == "__main__":
    main()