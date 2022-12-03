# Задача 1
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  *Пример:*
#  [2, 3, 4, 5, 6] => [12, 15, 16];
#  [2, 3, 5, 6] => [12, 15]

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
        l1.append(random.randint(0, 10))
    return l1

def CreateResult(arr):
    l1 = []
    if len(arr) % 2 == 0:
        num = int(len(arr) / 2)
    else:
        num = int(len(arr) // 2 +1)
    for i in range(0, num):
        l1.append(arr[i]*arr[len(arr)-i-1])
        #print (arr[i],len(arr)-i-1)
    return l1

num = InputNumbers("Введите количество элементов списка: ")

array = CreateArray(num)
result = CreateResult(array)

print("Список: ")
print(array)
print("Результат: ")
print(result) 