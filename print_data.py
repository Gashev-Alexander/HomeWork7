def print_data(data):
    if len(data) > 0:
        print("Имя".center(20), "Фамилия".center(25), "Номер телефона".center(30), "Комментарий".center(20))
        print("-"*100)
        for item in data:
            print(item[0].center(20), item[1].center(25), item[2].center(30), item[3].center(20))
    else:
        print("Телефонный справочник пуст...")