# Задача 4
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

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

num = InputNumbers("Введите количество элементов списка: ")
l1 = []
for i in range(0, num):
    l1.append(random.randint(-num, num))

print("Список: ")
print(l1)

prv = 1

print("Позиции из файла: ")
file1 = open("file.txt", "r")
while True:
    # считываем строку
    line = file1.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    line1 = int(line)
    prv = prv * l1[line1]
    print(line1)
# закрываем файл
file1.close

print(f"Произведение чисел = {prv}")