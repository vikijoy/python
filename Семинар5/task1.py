# Задача 1
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

mytext = 'Напишите абвашки программу, удаляющую из текста все слова, содержащие "абв"'

def del_some_words(mytext):
    mytext = list(filter(lambda x: 'абв' not in x, mytext.split()))
    return " ".join(mytext)

mytext = del_some_words(mytext)
print(mytext)