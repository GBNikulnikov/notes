# Работа со справочником отделов

from global_def import *
from position import pos_list


def dep_list(dep_id):   # Вывод списка отделов
    conn, cur = conn_open()
    if dep_id:
        exec_str = f'SELECT id_department, c_department FROM department where id_department = "{dep_id}";'
    else:
        exec_str = f'SELECT id_department, c_department FROM department;'
    cur.execute(exec_str)
    list_p = list((cur.fetchall()))
    for id, name in list_p:
        print(id, name)
    conn.close()


def comm_add_d():
    print('Добавление отдела:')
    name = input('Введите отдел: ')
    if name:
        conn, cur = conn_open()
        exec_str = f"insert into department (c_department) values ('{name}');"
        cur.execute(exec_str)
        last_row_id = cur.lastrowid
        conn.commit()
    dep_list(0)


def comm_del_d():
    print('Удаление отдела:')
    pos_list(0)
    id = input('Введите id отдела: ')
    if id:
        conn, cur = conn_open()
        exec_str = f"delete from position where id_position = ('{id}');"
        cur.execute(exec_str)
        conn.commit()
    pos_list(0)


def pd_list(dp_id):   # Вывод списка Должностей в отделах
    conn, cur = conn_open()
    if dp_id:
        exec_str = f'SELECT * FROM pd_list where id_depart_pos = "{dp_id}";'
    else:
        exec_str = f'SELECT * FROM pd_list;'
    cur.execute(exec_str)
    list_p = list((cur.fetchall()))

    for id_depart_pos, c_department, c_position in list_p:
        print(id_depart_pos, c_department, c_position)
    conn.close()


def comm_add_pd():  # Добавление должности в отдел
    id_dep = 0
    id_pos = 0

    print('Добавление должности в отдел')
    dep_list(0)
    id_dep = input('Введите id отдела: ')
    pos_list(0)
    id_pos = input('Введите id должности в отделе: ')
    if id_pos and id_dep:
        conn, cur = conn_open()
        exec_str = f"insert into depart_pos (id_department, id_position) values ({id_dep}, {id_pos});"
        cur.execute(exec_str)
        last_row_id = cur.lastrowid
        conn.commit()
    pd_list(0)


def comm_del_pd():
    id = 0
    print('Удаление должности из отдела:')
    pd_list(0)
    id = input('Введите id должности в отделе: ')
    if id:
        conn, cur = conn_open()
        exec_str = f"delete from depart_pos where id_depart_pos = ('{id}');"
        cur.execute(exec_str)
        conn.commit()
    pd_list(0)
