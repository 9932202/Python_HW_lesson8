def work_with_phonebook():
    choice = show_menu()

    phone_book = read_txt('book.txt')

    while (choice != 7):

        if choice == 1:
            print(*phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_subscr(phone_book, last_name, 0))
        elif choice == 3:
            tel_number = input('Введите номер:  ')
            print(find_by_subscr(phone_book, tel_number, 2))

        elif choice == 4:
            subscriber_data = []
            fields = ['Имя', 'Фамилия', 'Телефон', 'Описание']
            for i in range(0, 4):
                subscriber_data.append(str(input(f'{fields[i]}')))
            phone_book.append(add_new_subscriber(subscriber_data, phone_book))
            print(phone_book)
        elif choice == 5:
            number = input('number ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('new data ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)

        choice = show_menu()


def show_menu():
    print("\nВыберите действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти по фамилии\n"
          "3. Найти по номеру\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник\n")
    choice = int(input())
    return choice


def read_txt(filename):
    phone_book = []

    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))

        # dict(( (С„Р°РјРёР»РёСЏ,РРІР°РЅРѕРІ),(РёРјСЏ, РўРѕС‡РєР°),(РЅРѕРјРµСЂ,8928) ))

        phone_book.append(record)
    return phone_book



def write_txt(filename , phone_book):

    with open('book.txt','w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            for v in phone_book[i].values():

                s = s + v + ','

            phout.write(f'{s[:-1]}\n')


def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open('book.txt', 'r', encoding='utf-8') as phb:
        for line in phb:
            line = line.replace('\n', '')
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book


def find_by_subscr(phone_book, value, flag):
    if flag == 0:
        print("Поиск по фамилии")
    else:
        print("Поиск по номеру")
    for i in range(len(phone_book)):
        if [m for m in phone_book[i].values()][flag] == value:
            res = '--------/n'
            for teg1, teg2 in phone_book[i].items():
                res = f'{res} {teg1}: {teg2} \n'
            res = f'{res}-------\n'
    if res == '': res = 'Абонент не найден \n'
    return res



def add_new_subscriber(subscriber_data, phone_book):
    fields = ['Имя', 'Фамилия', 'Телефон', 'Описание']
    record = dict(zip(fields, subscriber_data))
    for ph_dic in phone_book:
        for teg1, teg2 in ph_dic.items():
            print(f'{teg1}: {teg2}')
        print('------')
    return record



work_with_phonebook()


# Иван, Иванов, 3333,  описание Иванова
# Василий, Васичкин, 444, описание Васичкина