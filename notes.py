# Заметка должна содержать идентификатор, заголовок, тело заметки
# и дату/время создания или последнего изменения заметки.
# При чтении списка заметок реализовать фильтрацию по дате.
import datetime

import global_def
from notes_json import notes_write, notes_read


def comm_list():  # Список заметок
    global_def.notes = notes_read()
    print("Диапазон дат:")
    s_date = datetime.datetime.strptime("01-01-01 00:00", "%d-%m-%y %H:%M")
    e_date = datetime.datetime.now()

    str_date = input("Начальная дата (ДД-ММ-ГГ, пусто - все): ")
    if len(str_date) != 0:
        try:
            s_date = datetime.datetime.strptime(str_date, "%d-%m-%y")
        except ValueError:
            print("Ошибка ввода даты!")
            return
        str_date = input("Конечная дата (ДД-ММ-ГГ, пусто - сегодня): ")
        if len(str_date) != 0:
            try:
                e_date = datetime.datetime.strptime(str_date, "%d-%m-%y")
            except ValueError:
                print("Ошибка ввода даты!")
                return
    start_date = s_date
    end_date = e_date

    for key, value in global_def.notes.items():
        date1 = datetime.datetime.strptime(value[2], "%d-%m-%y %H:%M")
        if (date1 >= start_date) and (date1 <= end_date):
            print(f"id: {key}")
            print(f"Заголовок: {value[0]}\nТекст: {value[1]}\nИзменен: {value[2]}\n")


def comm_add():
    print('Добавление заметки:')
    id_note = input('Введите id заметки: ')
    if id_note in global_def.notes:
        print(f"Значение id {id_note} уже существует")
    else:
        name_note = input('Введите заголовок: ')
        text_note = input('Введите содержание: ')
        date_note = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
        global_def.notes[id_note] = [name_note, text_note, date_note]
        comm_save()


def comm_upd():
    print('Изменение заметки:')
    id_note = input('Введите id заметки: ')
    if id_note in global_def.notes:
        name_note = input('Введите заголовок: ')
        if len(name_note) == 0:
            name_note = global_def.notes[id_note][0]
        text_note = input('Введите содержание: ')
        if len(text_note) == 0:
            text_note = global_def.notes[id_note][1]
        date_note = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
        global_def.notes[id_note] = [name_note, text_note, date_note]
        comm_save()
    else:
        print(f"Значение id {id_note} не существует")


def comm_del():
    print('Удаление заметки:')
    id_note = input('Введите id заметки: ')
    if id_note in global_def.notes:
        del global_def.notes[id_note]
        comm_save()
    else:
        print(f"Значение id {id_note} не существует")


def comm_save():
    notes_write()
    print("Заметка успешно сохранена")


def comm_help():
    global_def.print_menu()

