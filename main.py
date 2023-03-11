from notes import *

# Начало работы

cont_work = True
print_menu()
while cont_work:
    sel_item = menu_select()
    command = sel_item[5:len(sel_item)]
    if sel_item == 'comm_end':
        cont_work = False
    elif command in dict_menu:
        eval(sel_item + '()')
    else:
        print('Неверная команда')

