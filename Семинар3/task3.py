# Задача 3
# Напишите программу, которая будет преобразовывать десятичное число в двоичное

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

def CreateResult(num):
    b = ''
    n = num
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    print(f"Десятичное число = {num}, двоичное = {b}")

num = InputNumbers("Введите число: ")

CreateResult(num)
