# Задача 2
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def CreateResult(num):
    Ans = []
    d = 2
    while d * d <= num:
        if num % d == 0:
            Ans.append(d)
            num //= d
        else:
            d += 1
    if num > 1:
        Ans.append(num)
    print(Ans)

num = InputNumbers("Введите число: ")

CreateResult(num)