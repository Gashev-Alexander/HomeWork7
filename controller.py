from import_data import import_data
from export_data import export_data
from print_data import print_data


def greeting():
    print("Добрейшего Времни Суток!")

def input_data():
    name = input("Введите Имя Контакта: ")
    phone_number = input("Введите номер телефона: ")
    note = input("Введите комментарий: ")
    return [name, phone_number, note]

def choice_sep():
    sep = ";"

def choice_todo():
    print("Выберерите действие:\n\
    1 - Создать контакт.\n\
    2 - Показать все контакты.")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_data(input_data(), sep)
    elif ch == '2':
        data = export_data()
        print_data(data)