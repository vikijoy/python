# Задача 1
# Вычислить число ПИ c заданной точностью d
# Пример:
# при d = 0.0001, π = 3.1415. 10^-1 ≤ d ≤ 10^-10

import math

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            fl = float(input(f"{inputText}"))
            n1, n2 = str(fl).split('.')
            number = len(n2)
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def CreateResult(num):
    n1, n2 = str(math.pi).split('.')
    print(float(f'{n1}.{n2[:num]}'))

num = InputNumbers("Введите необходимую точность числа ПИ: ")

CreateResult(num)