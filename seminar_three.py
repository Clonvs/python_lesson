
#* Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

number_X = int(input('Введите число, которое надо найти: '))
number_N = int(input('Введите кол-во элементов в массиве: '))
list_A = []

for _ in range(number_N):
    list_A.append(int(input('Введите элементы списка: ')))
print(*list_A)

count = 0

for i in range(len(list_A)):
    if list_A[i] == number_X:
        count += 1
print(number_X)
print('->', count)


#* Задача 18: Требуется найти в списке A самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

number_X = int(input('Введите число, которое надо найти: '))
number_N = int(input('Введите кол-во элементов в списке: '))
list_A = []

for _ in range(number_N):
    list_A.append(int(input('Введите элементы списка: ')))
print(*list_A)

new_list = list_A[0]

for i in list_A:

    if abs(i - number_X) < abs(new_list - number_X):
        if i != number_X:
            new_list = i
print(f'{number_X} -> {new_list}')