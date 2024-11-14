def bubble_sort(arr):
    n = len(arr)
    # Проходим через каждый элемент массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n - i - 1):
            # Меняем местами, если элемент найден меньше, чем следующий
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    # Запрашиваем у пользователя количество чисел
    n = int(input("Введите количество чисел: "))
    numbers = []

    # Запрашиваем у пользователя ввод чисел
    for i in range(n):
        num = float(input(f"Введите число {i + 1}: "))  # Используем float для работы с дробными числами
        numbers.append(num)

    # Сортируем массив чисел
    bubble_sort(numbers)

    # Выводим отсортированный массив
    print("Отсортированные числа по возрастанию:")
    for number in numbers:
        print(number)

if __name__ == "__main__":
    main()