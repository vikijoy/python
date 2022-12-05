# Задача 4
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k(до 6 степени).*
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# *Значения коэффициентов от -100 до 100

from random import randint
import itertools

def get_ratios(k):
    ratios = [randint(-100, 100) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 100)
    return ratios

def get_polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' + -',' - ').replace('-1*x','-x').replace(' 1*x',' x')

k = randint(2, 6)

ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)

with open('4_4.txt', 'w') as data:
    data.write(polynom1)


# Второй многочлен для следующей задачи:

k = randint(2, 6)

ratios = get_ratios(k)
polynom2 = get_polynomial(k, ratios)
print(polynom2)

with open('4_4_2.txt', 'w') as data:
    data.write(polynom2)