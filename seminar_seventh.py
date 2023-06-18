
#* Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def get_num_syllables(phrase):
    vowels = "aeiouyAEIOUYаоеуёыиэюя"
    return sum(1 for char in phrase if char in vowels)

def check_rhythm(poem):
    phrases = poem.split(" ")
    num_syllables = get_num_syllables(phrases[0])
    for phrase in phrases:
        phrase_syllables = get_num_syllables(phrase)
        if phrase_syllables != num_syllables:
            return "Пам парам"
    return "Парам пам-пам"
    
poem = input("Введите стихотворение: ")
print(check_rhythm(poem))


#* Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6): 

    for i in range(1, num_rows + 1):  
        for j in range(1, num_columns + 1):
            print(round(operation(i, j), 1), end=' ')
        print()

print_operation_table(lambda x, y: x * y)
