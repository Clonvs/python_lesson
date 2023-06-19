
FILE_PATH = r'telephonedirectory/contact_details.txt'

def get_info_contact():
    with open(FILE_PATH, 'r', encoding='utf-8') as cont:
        for line in cont:
            print(line.strip())


def search_lastname_contact():
    with open(FILE_PATH, 'r', encoding='utf-8') as cont:
        surname_name = input('Введите фамилию: ')
        text = cont.read().splitlines()
        new_list = [text[i:i + 3] for i in range(0, len(text), 3)]    
        for i in new_list:
            if surname_name in i:
                print(*i)


def change_phone_contact():
    with open(FILE_PATH, 'r', encoding='utf-8') as cont:
        all_contact_info = cont.readlines()

    old_contact = input('Изменить контакт: ')
    
    for i in range(len(all_contact_info)):
        if old_contact in all_contact_info[i]:
            info = input('введите новые данные: ')
            all_contact_info[i] = info + '\n'
            break

    with open(FILE_PATH, 'w', encoding='utf-8') as cont:
            for line in all_contact_info:
                cont.write(line)
            
           
def add_phone_contact():
    with open(FILE_PATH, 'a', encoding='utf-8') as cont:
        contact_surname = input('Добавить фамилию: ')
        contact_name = input('Добавить имя: ')
        contact_number = input('Добавить номер : ')
        cont.write(f'\n{contact_surname}\n{contact_name}\n{contact_number}')
       

def start_menu():
    while True:
        change = int(input('\n1. Список контактов'
                    '\n2. Поиск по фамилии'
                    '\n3. Изменить контакт'
                    '\n4. Добавить контакт'
                    '\n5. Выйти'
                    '\n'))
        match change:
            case 1:
                get_info_contact( )
            case 2:
                search_lastname_contact()
            case 3:
                change_phone_contact()
            case 4:
                add_phone_contact()
            case 5:
                break

start_menu()
