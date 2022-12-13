# Семинар 3 Задача 4
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

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

#Было
#def CreateResult(num):
#    arr = []
#    for i in range(-num, num+1):
#        arr.append(int(round((((1+5**(1./2.))/2)**i-((1-5**(1./2.))/2)**i)/5**(1./2.),0)))
#    print("Последовательность негафибоначчи: ")
#    print(arr)

num = InputNumbers("Введите число: ")
print("Последовательность негафибоначчи: ", list(map(lambda i: int(round((((1+5**(1./2.))/2)**i-((1-5**(1./2.))/2)**i)/5**(1./2.),0)), [i for i in range(-num, num+1)])))
#CreateResult(num)