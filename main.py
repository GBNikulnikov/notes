from notes import *
import global_def
# Начало работы

cont_work = True
global_def.notes = notes_read()
global_def.print_menu()
while cont_work:
    sel_item = global_def.menu_select()
    command = sel_item[5:len(sel_item)]
    if sel_item == 'comm_end':
        cont_work = False
    elif command in global_def.dict_menu:
        eval(sel_item + '()')
    else:
        print('Неверная команда')
