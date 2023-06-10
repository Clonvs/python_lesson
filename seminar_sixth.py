
#* Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#* Каждое число вводится с новой строки.7 9 11 13 15

def arithmetic_progression(eleement_n, difference, number_of_element):
    lst = []
    intermediate_variable = 0
    n = 1
    for _ in range(number_of_element):
        intermediate_variable = eleement_n + (n - 1) * difference
        lst.append(intermediate_variable)
        n += 1
    return lst

first_element = int(input('Введите первый элемент: '))
range_of_element = int(input('Введите разность: '))
count_element = int(input('Введите кол-во элементов: '))
print(arithmetic_progression(first_element, range_of_element, count_element))


#* Задача 32: Определить индексы элементов массива (списка),
#* значения которых принадлежат заданному диапазону (т.е. не
#* меньше заданного минимума и не больше заданного
#* максимума)

def index_definition(start_index, end_index):
    lst = []
    count_elements = int(input('Введите кол-во элементов: '))
    for _ in range(count_elements):
        lst.append(int(input('Введите элементы списка: '))) 
    new_list = [i for i in range(len(lst)) if end_index >= lst[i] >= start_index]
    return new_list
minimum = int(input('Введите минимальный элемент: '))
maximum = int(input('Введите максимальный элемент: '))
print(index_definition(minimum, maximum))    