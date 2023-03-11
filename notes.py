# Заметка должна содержать идентификатор, заголовок, тело заметки
# и дату/время создания или последнего изменения заметки.
import datetime
from global_def import *
from notes_json import notes_write, notes_read


def comm_list():    # Список заметок
    notes_read()
    print()
    for key, value in notes.items():
        print(f"id: {key}")
        print(f"Заголовок: {value[0]}\nТекст: {value[1]}\nИзменен: {value[2]}\n")


def comm_add():
    print('Добавление заметки:')
    id_note = input('Введите id заметки: ')
    if id_note in notes:
        print(f"Значение id {id_note} уже существует")
    else:
        name_note = input('Введите заголовок: ')
        text_note = input('Введите содержание: ')
        date_note = datetime.datetime.now().strftime("%d-%m-%y %I:%M")
        notes[id_note] = [name_note, text_note, date_note]
        comm_save()


def comm_upd():
    print('Изменение заметки:')
    id_note = input('Введите id заметки: ')
    if id_note in notes:
        name_note = input('Введите заголовок: ')
        text_note = input('Введите содержание: ')
        date_note = datetime.datetime.now().strftime("%d-%m-%y %I:%M")
        notes[id_note] = [name_note, text_note, date_note]
        comm_save()
    else:
        print(f"Значение id {id_note} не существует")


def comm_del():
    print('Удаление заметки:')
    id_note = input('Введите id заметки: ')
    if id_note in notes:
        del notes[id_note]
        comm_save()
    else:
        print(f"Значение id {id_note} не существует")


def comm_save():
    notes_write()

