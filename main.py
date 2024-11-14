def bubble_sort(arr, ascending=True):
    n = len(arr)
    # Проходим через каждый элемент массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n - i - 1):
            # Меняем местами, в зависимости от направления сортировки
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    # Запрашиваем у пользователя количество чисел
    n = int(input("Введите количество чисел: "))
    numbers = []

    # Запрашиваем у пользователя ввод чисел
    for i in range(n):
        num = float(input(f"Введите число {i + 1}: "))  # Используем float для работы с дробными числами
        numbers.append(num)

    # Запрашиваем направление сортировки
    direction = input("Введите направление сортировки (возрастание/убывание): ").strip().lower()

    if direction == "возрастание":
        ascending = True
    elif direction == "убывание":
        ascending = False
    else:
        print("Некорректный ввод направления сортировки. Используем по возрастанию по умолчанию.")
        ascending = True

    # Сортируем массив чисел
    bubble_sort(numbers, ascending)

    # Выводим отсортированный массив
    if ascending:
        print("Отсортированные числа по возрастанию:")
    else:
        print("Отсортированные числа по убыванию:")

    for number in numbers:
        print(number)


if __name__ == "__main__":
    main()