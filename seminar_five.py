
#* Задача №35

#* Напишите функцию, которая принимает одно число и
#* проверяет, является ли оно простым

number = int(input('Введите число: '))
def is_prime(number):
    if number < 2:
        return False

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return 'No'

        divider += 1

    return 'Yes'

print(is_prime(number))


#* Задача №37.

# * Дано натуральное число N и
# * последовательность из N элементов.
# * Требуется вывести эту последовательность в
# * обратном порядке.
# * Примечание. В программе запрещается
# * объявлять массивы и использовать циклы
# * (даже для ввода и вывода).
# * Input: 2 -> 3 4
# * Output: 4 3


def rec_N(number_N):
    if number_N > 0:
        user_input = int(input('Введите числа: '))
        rec_N(number_N - 1)
        print(user_input, end=' ')

numbers = int(input('Введите число: '))
rec_N(numbers)
