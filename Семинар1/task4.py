# Задача 4
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def checkNumber(num):
    if num == 1:
        print("X > 0; Y > 0")
    elif num == 2:
        print("X < 0; Y > 0")
    elif num == 3:
        print("X < 0; Y < 0")
    elif num == 4:
        print("X > 0; Y < 0")
    else:
        print("Число должно быть от 1 до 4")


num = InputNumbers("Введите номер четверти: ")
checkNumber(num)