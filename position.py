# Работа со справочником должностей

from global_def import *


def pos_list(pos_id):   # Вывод списка Должностей
    conn, cur = conn_open()
    if pos_id:
        exec_str = f'select id_position, c_position from position where id_position = "{pos_id}"'
    else:
        exec_str = f'select id_position, c_position from position'
    cur.execute(exec_str)
    list_p = list((cur.fetchall()))
    for id, name in list_p:
        print(id, name)
    conn.close()


def comm_add_p():
    print('Добавление должности:')
    name = input('Введите должность: ')
    if name:
        conn, cur = conn_open()
        exec_str = f"insert into position (c_position) values ('{name}');"
        cur.execute(exec_str)
        last_row_id = cur.lastrowid
        conn.commit()
    pos_list(0)


def comm_del_p():
    print('Удаление должности:')
    pos_list(0)
    id = input('Введите id должности: ')
    if id:
        conn, cur = conn_open()
        exec_str = f"delete from position where id_position = ('{id}');"
        cur.execute(exec_str)
        conn.commit()
    pos_list(0)
