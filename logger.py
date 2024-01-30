


from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    
    with open('data_phonebook.csv', 'a', encoding='utf-8') as f:
        f.write(f"{name}; {surname}; {phone}; {address}\n")



def delete_data():
     with open('data_phonebook.csv', 'r', encoding='utf-8') as f:
        data_phone = f.readlines() # первым действием считаем все строки файла f в список с помощью встроенной функции readlines
        for i, line in enumerate(data_phone, 1):
            print(f'{i}: {line}')

        print("Введите номер строки удаляемого контакта: ")
        d = int(input())
        if d <= len(data_phone):
            with open('data_phonebook.csv', 'w', encoding='utf-8') as f:
                for i, line in enumerate(data_phone, 1):
                    if i != d:
                        f.write(line)
                print(f'Выбранный номер: {data_phone[d - 1]} успешно удален')
        else:
            print(f'Ошибка: в справочнике нет номера {d}')



def print_data():
    print('Вывод данных из телефонной книги: \n')
    with open('data_phonebook.csv', 'r', encoding='utf-8') as f:
        data_phone = f.readlines() # первым действием считаем все строки файла f в список с помощью встроенной функции readlines
        for i, line in enumerate(data_phone, 1):
            print(f'{i}: {line}')
        


    
def change_data():
    with open('data_phonebook.csv', 'r', encoding='utf-8') as f:
        data_phone = f.readlines()
        for i, line in enumerate(data_phone, 1):
            print(f"{i}: {line}")
    print('Введите номер строки, которую хотите изменить: ')
    n = int(input())
    if n <= len(data_phone):
        print(f'Выбранная строка: {data_phone[n-1]}')
        print('Введите новые данные\n')
        name1 = name_data()
        surname1 = surname_data()
        phone1 = phone_data()
        address1 = address_data()
        new_data = f"{name1}; {surname1}; {phone1}; {address1}\n"
        data_phone[n-1] = f'{new_data}'
        with open('data_phonebook.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_phone)
        print(f'Строка с номером {n} успешно изменена')
    else:
        print(f'Ошибка ввода: в телефонной книге нет строки с номером {n}')
