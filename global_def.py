# Общие данные и функции

import inspect

dict_menu = {
            'list': ['- Список заметок', 'comm_list'],
            'add': ['- Добавить заметку', 'comm_add'],
            'del': ['- Удалить заметку', 'comm_del'],
            'upd': ['- Изменить заметку', 'comm_upd'],
            'help': ['- Помощь', 'comm_help'],
            'end': ['- Завершить работу', 'comm_end']
             }

# notes = {'1': ['Note1', 'text 1', '2023-03-11 13:34']}
notes = {}

ERROR_COMM = 'Нет такой команды'


def print_menu():  # Печать меню
    global dict_menu

    print('Заметки\n\n' + 'Команды:\n')
    for comm in dict_menu:
        print(comm, dict_menu[comm][0])


def menu_select():  # Выбор пункта меню
    global dict_menu

    comm = input('Введите команду:')
    try:
        func_comm = dict_menu[comm][1]
    except KeyError:
        return ERROR_COMM
    else:
        return func_comm


def comm_end():
    print('command ', inspect.stack()[0][3])
