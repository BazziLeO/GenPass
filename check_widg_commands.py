from function_generator import *
from checkpas_interface import *
from mainmenu_interface import *

def check_password():
    password = CheckUI.check_password_entry.get()
    if selection_letters(only_type_symbols(password, 'letters'), 'great_letters') == '':
        result = 'Нет больших букв'
    elif selection_letters(only_type_symbols(password, 'letters'), 'small_letters') == '':
        result = 'Нет маленьких букв'
    elif only_type_symbols(password, 'numbers') == '':
        result = 'В пароле нет цифр'
    elif only_type_symbols(password, 'other') == '':
        result = 'В пароле нет символов помимо цифр и букв'
    elif not len_checkpas_range.get()[0] <= len(password) <= len_checkpas_range.get()[1]:
        result = f'Длина пароля не в рамках длины [{len_checkpas_range.get()[0]}, {len_checkpas_range.get()[1]}]'
    else:
        result = 'Проверка пройдена успешно'
        for e in password:
            if allowed_symbolbet.get().count(e) == 0:
                result = f'Символа "{e}" нету в разрешенном списке!'
    messagebox.showinfo("Результат", result)


def delete_symbols():
    def logic_delete_symbols(example_symbolbet):
        list_of_symbols = check_interface.delete_symbols_entry.get().split(' ')
        check_interface.delete_symbols_entry.delete(0)
        result = example_symbolbet.delete_symbols(list_of_symbols)
        messagebox.showinfo('Результат', result)
        automatically_update_list()
    if select_checksymbolbet_action.get() == 1:
        logic_delete_symbols(allowed_symbolbet)
    elif select_checksymbolbet_action.get() == 2:
        logic_delete_symbols(required_symbolbet)


def add_symbols():
    def logic_add_symbols(example_symbolbet):
        list_of_symbols = check_interface.add_symbols_entry.get().split(' ')
        check_interface.add_symbols_entry.delete(0)
        result = example_symbolbet.add_symbols(list_of_symbols)
        messagebox.showinfo('Результат', result)
    if select_checksymbolbet_action.get() == 1:
        logic_add_symbols(allowed_symbolbet)
    elif select_checksymbolbet_action.get() == 2:
        logic_add_symbols(required_symbolbet)



def stay_symbols():
    def logic_stay_symbols(example_symbolbet):
        list_of_symbols = check_interface.stay_symbols_entry.get().split(' ')
        check_interface.stay_symbols_entry.delete(0)
        result = example_symbolbet.stay_symbols(list_of_symbols)
        messagebox.showinfo("Результат", result)
    if select_checksymbolbet_action.get() == 1:
        logic_stay_symbols(allowed_symbolbet)
    elif select_checksymbolbet_action.get() == 2:
        logic_stay_symbols(required_symbolbet)


def select_range():
    diapason_list = check_interface.select_range_entry.get().split(' ')
    check_interface.select_range_entry.delete(0)
    if len(diapason_list) == 1:
        result = len_checkpas_range.set(diapason_list[0], diapason_list[0])
    elif len(diapason_list) > 1:
        result = len_checkpas_range.set(diapason_list[0], diapason_list[1])
    messagebox.showinfo("Результат", result)


def get_range():
    result = str(len_checkpas_range.get()[0]) + ' ' + str(len_checkpas_range.get()[1])
    check_interface.get_range_entry.delete(0)
    check_interface.get_range_entry.insert(0, result)


def stay_letters():
    if select_letter.get():
        symbolbet.delete_black_symbols(split(only_type_symbols(symbolbet.get_black(), 'letters')))
        check_interface.gr_letter_checkbutton['state'] = NORMAL
        check_interface.sm_letter_checkbutton['state'] = NORMAL
    else:
        symbolbet.add_black_symbols(split(only_type_symbols(symbolbet.get(), 'letters')))
        check_interface.gr_letter_checkbutton['state'] = DISABLED
        check_interface.sm_letter_checkbutton['state'] = DISABLED


def stay_sm_letters():
    if select_sm_letter.get():
        symbolbet.delete_black_symbols(
            split(selection_letters(only_type_symbols(symbolbet.get_black(), 'letters'), 'small_letters')))
        if select_gr_letter.get():
            check_interface.letter_checkbutton['state'] = NORMAL
    else:
        symbolbet.add_black_symbols(
            split(selection_letters(only_type_symbols(symbolbet.get(), 'letters'), 'small_letters')))
        check_interface.letter_checkbutton['state'] = DISABLED


def stay_gr_letters():
    if select_gr_letter.get():
        symbolbet.delete_black_symbols(
            split(selection_letters(only_type_symbols(symbolbet.get_black(), 'letters'), 'great_letters')))
        if select_sm_letter.get():
            check_interface.letter_checkbutton['state'] = NORMAL
    else:
        symbolbet.add_black_symbols(
            split(selection_letters(only_type_symbols(symbolbet.get(), 'letters'), 'great_letters')))
        check_interface.letter_checkbutton['state'] = DISABLED


def stay_numbers():
    if select_number.get():
        allowed_symbolbet.delete_black_symbols(split(only_type_symbols(symbolbet.get_black(), 'numbers')))
    else:
        allowed_symbolbet.add_black_symbols(split(only_type_symbols(symbolbet.get(), 'numbers')))


def stay_other():
    if select_other.get():
        allowed_symbolbet.delete_black_symbols(split(only_type_symbols(symbolbet.get_black(), 'other')))
    else:
        allowed_symbolbet.add_black_symbols(split(only_type_symbols(symbolbet.get(), 'other')))

def automatically_update_list():
    if check_interface.get_list_entry.get() != '':
        get_list()

def get_list():
    def logic_get_list(example_symbolbet):
        check_interface.get_list_entry.delete(0)
        check_interface.get_list_entry.insert(0, divide_word(example_symbolbet.get()))
    if select_checksymbolbet_action.get() == 1:
        logic_get_list(allowed_symbolbet)
    elif select_checksymbolbet_action.get() == 2:
        logic_get_list(required_symbolbet)


def leave():
    check_interface.place_forget()
    mmenu_interface.place()

check_interface.check_password_button['command'] = check_password
check_interface.add_symbols_button['command'] = add_symbols
check_interface.delete_symbols_button['command'] = delete_symbols
check_interface.stay_symbols_button['command'] = stay_symbols
check_interface.get_list_button['command'] = get_list
check_interface.select_range_button['command'] = select_range
check_interface.get_range_button['command'] = get_range
check_interface.letter_checkbutton['command'] = stay_letters
check_interface.gr_letter_checkbutton['command'] = stay_gr_letters
check_interface.sm_letter_checkbutton['command'] = stay_sm_letters
check_interface.number_checkbutton['command'] = stay_numbers
check_interface.other_checkbutton['command'] = stay_other

check_interface.leave_button['command'] = leave