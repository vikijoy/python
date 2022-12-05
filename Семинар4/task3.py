# Задача 3
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. 

import math

def InputNumbers( ):
    is_OK = False
    while not is_OK:
        try:
            lst = list(map(int, input("Введите числа через пробел:\n").split()))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return lst

def CreateResult(lst):
    print(f"Исходный список: {lst}")
    dup = [x for x in lst if lst.count(x) == 1]
    print(f"Список из неповторяющихся элементов: {dup}")

l1 = InputNumbers()

CreateResult(l1)