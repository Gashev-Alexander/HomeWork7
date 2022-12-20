def print_data(data):
    if len(data) > 0:
        print("Имя Контакта".center(20), "Номер телефона".center(20), "Комментарий".center(20))
        print("-"*60)
        for item in data:
            print(item[0].center(20), item[1].center(20), item[2].center(15))
    else:
        print("Телефонный справочник пуст...")