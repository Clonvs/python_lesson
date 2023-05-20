
# *Найдите сумму цифр трехзначного числа.

numbres = int(input('Введите трёхзначное число: '))
sum_of_numbers = 0

print(f'{numbres} -> ', end='')

if not 0 < numbres // 100 <= 9:
    print('Число не трёхзначное')
else:
    while numbres > 0:
        sum_of_numbers = sum_of_numbers + numbres % 10
        numbres //= 10
    print(sum_of_numbers)


# *Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе? *Пример:*6 -> 1  4  1

quantity_cranes = int(input('Введите кол-во журавликов: '))

if quantity_cranes % 3!=0 or quantity_cranes < 0:
    print(False)
else:
    variable = quantity_cranes // 3
    pety = variable // 2
    sergey = variable // 2
    katya = quantity_cranes - variable
    print(f'Из {quantity_cranes} собранных журавликов, Петя собрал -> {pety}, Катя собрала -> {katya}, Сережа собрал {sergey}')


# *Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

ticket_number = input('Введите номер билета: ')
half_numbers_one = ticket_number[:3]
half_numbers_two = ticket_number[3:]
sum_numbers_one = 0
sum_numbers_two = 0

for i in half_numbers_one:
    sum_numbers_one += int(i)
    print(f'{i}', end='')
for i in half_numbers_two:
    sum_numbers_two += int(i)
    print(f'{i}', end='')
if sum_numbers_one == sum_numbers_two:
    print(f' -> {sum_numbers_one} = {sum_numbers_two} Ура, билет счастливый!!!')
else:
    print( f' -> {sum_numbers_one} != {sum_numbers_two} Опять не повезло(')


# *Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать 
# *один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

length_chocolate = int(input('Введите длину шоколада: '))
widht_chocolate = int(input('Введите ширину шоколада: '))
slice_chocolate = int(input('Введите количество долек: '))

if slice_chocolate == length_chocolate and widht_chocolate or (slice_chocolate % length_chocolate == 0 or 
slice_chocolate % widht_chocolate == 0):                            
    print('yes')
else:
    print('no')