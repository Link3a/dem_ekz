import csv

csv_file = []


# Открыть файл
def file_open(file_name):
    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            print(row)
            csv_file.append(row)
        print("Файл открыт. Записей: ", len(csv_file))


# Добавление
def insert(vin, nom, mod, age, mog, prob, hoz, st):
    try:
        csv_file.append({'vin': vin,
                         'номер': nom,
                         'модель': mod,
                         'год': age,
                         'мощность': mog,
                         'пробег': prob,
                         'владелец': hoz,
                         'стоимость': st})
    except Exception as e:
        return f"Ошибка при добавлении новой записи {e}"
    print("Данные добавлены")


# Удаление
def drop_by_arg(val, col_name="номер"):
    global csv_file
    try:
        csv_file = list(filter(lambda x: x[col_name] != val, csv_file))
    except Exception as e:
        return f"Строка со значением {val} поля {col_name} не найдена"
    return f"Строка со значением {val} поля {col_name} удалена!"


# Поиск по номеру
def find(val, col_name='номер'):
    print(*list(filter(lambda x: x[col_name] == val, csv_file)))


# Поиск по модели
def find1(val, col_name: str = 'модель'):
    print(*list(filter(lambda x: x[col_name] == val, csv_file)))


# поиск по году
def find2(val, col_name='год'):
    print(*list(filter(lambda x: x[col_name] == val, csv_file)))

def avg_age():
    print("Средний пробег:",
        sum([int(row['пробег']) for row in csv_file]) // len(csv_file))


# Функция Сохранить
def save(fine_name):
    with open(fine_name, 'w', encoding='utf-8', newline='') as file:
        columns = ['vin', 'номер', 'модель', 'год', 'мощность', 'пробег', 'владелец', 'стоимость']
        writer = csv.DictWriter(file, delimiter=";", fieldnames=columns)
        writer.writeheader()
        writer.writerows(csv_file)
        print("Данные сохранены")


# Вывод списка записей
def show_rows():
    if len(csv_file) > 0:
        print('{:<5}{:<15}{:<25}{:<8}{:<12}{:<12}{:<25}{:<12}'.format('vin', 'номер', 'модель', 'год', 'мощность',
                                                                      'пробег', 'владелец', 'стоимость'))
        for el in csv_file:
            print('{:<5}{:<15}{:<25}{:<8}{:<12}{:<12}{:<25}{:<12}'.format(el['vin'], el['номер'], el['модель'],
                                                                          el['год'], el['мощность'], el['пробег'],
                                                                          el['владелец'], el['стоимость']))
