# Задача 3
# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
# Пример:
# Для n = 3: {1: 2, 2: 2.25 , 3: 2.37}
# Необходимо сложить все значения словаря и вывести сумму на экран.


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            dct = {i: (1+(1/i))**i for i in range(1,number+1)}
            print(dct)
            print(f"Сумма значений: ")
            print(sum(dct.values()))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")

InputNumbers("Введите число: ")