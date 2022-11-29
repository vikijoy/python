# Задача 5
# Реализуйте алгоритм генерации случайного числа.(Не используя библиотеки связанные с рандомом) (Доп задача, не влияющая на оценку )

import datetime

def gen_random_int(first, second):
    if first == second:  # Если числа одинаковые, просто возвращаем первое или второе, не важно.
        return first
    integer_for_gen = int(str(datetime.datetime.now())[-3:])  # Выбираем из даты милисекунды
    # print(integer_for_gen) # Выводим милисекунды для проверки
    while(True):
        integer_for_gen /= 17 # делим наши млсекунды на 17
        if integer_for_gen >= first and integer_for_gen <= second: # если в нашем диапозоне, прерываем цикл
            break
    return int(round(integer_for_gen))  # Приводим к int для отброса дробной части, округляем и возвращаем

print(gen_random_int(1, 100))