# Задача 2
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 (N) конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 (M) конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

def play_game(n, m, players):
    messages = 'возьмите конфеты'
    count = 0
    if n % 10 == 1 and 9 > n > 10:
        letter = 'а'
    elif 1 < n % 10 < 5 and 9 > n > 10:
        letter = 'ы'
    else:
        letter = ''
    while n > 0:
        print(f'{players[count % 2]}, {messages}')
        move = int(input())
        if move > n or move > m:
            print(f'Можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
            attempt = 3
            while attempt > 0:
                if n >= move <= m:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -= 1
            else:
                return print(f'Попытки кончились. Тупите меньше!!!')
        n = n - move
        if n > 0:
            print(f'Осталось {n} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[not count % 2]

player1 = input('Первый игрок, представтесь: \n')
player2 = input('Второй игрок, представтесь: \n')

# Случайно выбираем кто ходит первым
if random.randint(0,1) == 1:
    players = [player1, player2]
else:
    players = [player2, player1]

n = int(input('Сколько конфет разыгрывается?\n '))
m = int(input('Максимальное количество конфет за один ход?\n '))

winer = play_game(n, m, players)
if not winer:
    print('У нас нет победителя.')
else:
    print(f'Победил {winer}!')