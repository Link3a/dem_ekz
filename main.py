from avto_csv import file_open, insert, show_rows, save, drop_by_arg, find, avg_age, find1, find2

FILENAME = "Data.csv"

MENU = {
    '1': 'Открыть файл',
    '2': 'Добавить',
    '3': 'Удалить',
    '4': 'Найти по номеру',
    '5': 'Найти по модели',
    '6': 'Вывести по году',
    '7': 'Сохранить в файл',
    '8': 'Вывести записи',
    '9': 'Средний пробег',
    '0': '<-Меню',
    'exit': 'Выход'
}
for k, v in MENU.items():
    print(k, '-', v)

while True:

    action = input('>_')
    if action == '1':
        file_open(FILENAME)
    elif action == '2':
        insert(input('vin: '), input('номер: '), input('модель: '), input('год: '),
               input('мощность: '), input('пробег: '), input('владелец: '), input('стоимость: '))
    elif action == '3':
        print(drop_by_arg(input("Значение: "), input("Колонка: ")))
    elif action == '4':
        col = input('Колонка: ')
        val = input('Значение: ')
        find(val, col_name=col)
    elif action == '5':
        find1(input("Значение: "), input("Колонка: "))
    elif action == '6':
        find2(input("Значение: "), input("Колонка: "))
    elif action == '7':
        save(FILENAME)
    elif action == '8':
        show_rows()
    elif action == '9':
        avg_age()
    elif action == '0':
        for k, v in MENU.items():
            print(k, '-', v)
    elif action == 'exit':
        break
