from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data
import os, subprocess
import os


def greeting():
    print("Добрейшего Времни Суток!")

def input_data():
    name = input("Введите Имя: ")
    fam = input("Введите Фамилию: ")
    phone_number = input("Введите номер телефона: ")
    note = input("Введите комментарий: ")
    return [name, fam, phone_number, note]

def choice_sep():
    sep = ";"

def choice_todo():
    print("Выберерите действие:\n\
    1 - Создать контакт.\n\
    2 - Показать все контакты. \n\
    3 - Поиск и изменение контакта. \n\
    4 - Поиск и удаление контакта. ")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_data(input_data(), sep)
    elif ch == '2':
        data = export_data()
        print_data(data)
    elif ch == '3':
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print("Имя".center(20), "Фамилия".center(25), "Номер Телефона".center(30), "Комментарий".center(30))
            print("-"*100)
            print(item[0].center(20), item[1].center(25), item[2].center(30), item[3].center(30))
            def LineReplacement(File, FindThis, ReplaceByThis):
                TemporaryFile = File + '.tmp'
                with open(File, 'r') as f1, open(TemporaryFile, 'w') as f2:
                    lines = f1.readlines()
                    for line in lines:
                        line = line.strip()
                        if line == FindThis:
                            f2.write(ReplaceByThis + '\n')
                        else:
                            f2.write(line + '\n') 
                        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), File)
                os.remove(path)
                os.rename('phone.txt.tmp', 'phone.txt')
            File = "phone.txt"
            FindThis = input("Введите данные для замены: ")
            ReplaceByThis = input("Введите на какие данные меняете: ")
            LineReplacement(File, FindThis, ReplaceByThis)
        else:
            print("Данные не обнаружены")
    elif ch == '4':
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print("Имя".center(20), "Фамилия".center(25), "Номер Телефона".center(30), "Комментарий".center(30))
            print("-"*100)
            print(item[0].center(20), item[1].center(25), item[2].center(30), item[3].center(30))
            print('Для Удаления введите 1.\n\
Для выхода введите 2.')
            f_del = input('Ожидание ввода: ')
            if f_del == '1':
                def Delete_line(File, DelThis, ReplaceDelThis):
                    TemporaryFile = File + '.tmp'
                    with open(File, 'r') as f1, open(TemporaryFile, 'w') as f2:
                        lines = f1.readlines()
                        for line in lines:
                            line = line.strip()
                            if line == DelThis:
                                f2.write(ReplaceDelThis + '\n')
                            else:
                                f2.write(line + '\n') 
                            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), File)
                    os.remove(path)
                    os.rename('phone.txt.tmp', 'phone.txt')
                File = "phone.txt"
                DelThis = (item[0], item[1], item[2], item[3])
                ReplaceDelThis = exit #Здесь будет код на удаление строки в фйле
                Delete_line(File, DelThis, ReplaceDelThis)
            elif f_del == '2':
                    exit
        else:
            exit