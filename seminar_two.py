
#* Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

number_of_coins = int(input('Введите количество монет: '))
eagle = 0
tails = 0

for i in range(number_of_coins):
    coin_selection = input('Введите один(орёл) или ноль(решка): ')
    if coin_selection == '1':
        eagle += 1
    if coin_selection == '0':
        tails += 1

print(f'кол-во монет с гербом {eagle}, кол-во монет с решкой {tails} -> ', end='')

if eagle < tails:
    print(f'орёл {eagle}')
else:
    print(f'решка {tails}')


#* Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
#* Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
#* а Катя должна их отгадать. Для этого Петя делает две подсказки.
#* Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

S = int(input('Сумма чисел: '))
P = int(input('Произведение чисел: '))

for X in range(1, 1001):
    for Y in range(1, 1001):
        if X + Y == S and X * Y == P:
            print(X, Y)


#* Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number_N = int(input('Введите число: '))
number_two = 2
index = 0

print(f'{number_N} -> ', end='')

for i in range(0, number_N):
    if index < number_N:
        index = number_two ** i
    if index >= number_N:
        break
    print(index, end=' ')

