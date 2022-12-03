# Задача 2
# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#  Пример:
#  [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19

import random

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def CreateArray(arrnum):
    l1 = []
    for i in range(0, num):
        l1.append(round(random.uniform(0.01, 19.99), 2))
    return l1

def CreateResult(arr):
    min = arr[0]
    max = arr[0]

    for i in range(1, len(arr)):
        if arr[i] % 1 < min % 1:
            min = arr[i]
        if arr[i] % 1 > max % 1:
            max = arr[i]
    print(f"Максимальное значение дробной части = {max}")
    print(f"Минимальное значение дробной части = {min}")
    print(f"Разница между максимальным и минимальным значением дробной части элементов = {round((max % 1) - (min % 1),2)}")

num = InputNumbers("Введите количество элементов списка: ")

array = CreateArray(num)

print("Список: ")
print(array)

result = CreateResult(array)
