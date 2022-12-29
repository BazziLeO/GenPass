import savebox_password_interface
from function_generator import *
from generator_interface import *
from mainmenu_interface import *
from checkpas_interface import *
from savebox_password_interface import *


def select_translation(translation_pairs, language='russian'):
    if language == 'russian':
        return list(translation_pairs.keys())[0]
    elif language == 'english':
        return list(translation_pairs.values())[0]


def generate():
    number = range_len_pas.get_random()
    req_symbol_string = required_symbolbet.get()
    need_symbol_string = select_symbols(only_type_symbols(symbolbet.get(), 'numbers'))
    need_symbol_string += select_symbols(only_type_symbols(symbolbet.get(), 'other'))
    need_symbol_string += select_symbols(
        selection_letters(only_type_symbols(symbolbet.get(), 'letters'), 'small_letters'))
    need_symbol_string += select_symbols(
        selection_letters(only_type_symbols(symbolbet.get(), 'letters'), 'great_letters'))
    result = need_symbol_string + req_symbol_string
    if number > len(result):
        result = shuffle_symbols(result)
        result += select_symbols(symbolbet.get(), number - len(result))
    elif range_len_pas.get()[1] > len(result):
        result = shuffle_symbols(result)
        result += select_symbols(symbolbet.get(), range_len_pas.get()[1] - len(result))
    else:
        result = shuffle_symbols(req_symbol_string)
        if number > len(req_symbol_string):
            result += select_symbols(symbolbet.get(), number - len(req_symbol_string))
        elif int(range_len_pas.get()[1]) > len(req_symbol_string):
            result += select_symbols(symbolbet.get(), range_len_pas.get()[1] - len(req_symbol_string))
    gen_interface.generate_pas_entry.delete(0, END)
    gen_interface.generate_pas_entry.insert(0, result)

def send_to_savebox():
    gen_interface.place_forget()
    savebox_password_interface.settings_interface.add_password()
    savebox_password_interface.main_interface.place_ofpassword_entry.insert(0, gen_interface.generate_pas_entry.get())
    savebox_password_interface.savebox_password_frame.pack()


def delete_symbols():
    def logic_delete_symbols(example_symbolbet):
        list_of_symbols = gen_interface.delete_symbols_entry.get().split(' ')
        gen_interface.delete_symbols_entry.delete(0)
        result = example_symbolbet.delete_symbols(list_of_symbols)
        messagebox.showinfo('Результат', result)
        automatically_update_list()
    if select_symbolbet_action.get() == 1:
        logic_delete_symbols(symbolbet)
    elif select_symbolbet_action.get() == 2:
        logic_delete_symbols(required_symbolbet)


def add_symbols():
    def logic_add_symbols(example_symbolbet):
        list_of_symbols = gen_interface.add_symbols_entry.get().split(' ')
        gen_interface.add_symbols_entry.delete(0)
        result = select_translation(example_symbolbet.add_symbols(list_of_symbols))
        messagebox.showinfo('Результат', result)
    if select_symbolbet_action.get() == 1:
        logic_add_symbols(symbolbet)
    elif select_symbolbet_action.get() == 2:
        logic_add_symbols(required_symbolbet)



def stay_symbols():
    def logic_stay_symbols(example_symbolbet):
        list_of_symbols = gen_interface.stay_symbols_entry.get().split(' ')
        gen_interface.stay_symbols_entry.delete(0)
        result = example_symbolbet.stay_symbols(list_of_symbols)
        messagebox.showinfo("Результат", result)

    if select_symbolbet_action.get() == 1:
        logic_stay_symbols(symbolbet)
    elif select_symbolbet_action.get() == 2:
        logic_stay_symbols(required_symbolbet)


def select_range():
    diapason_list = gen_interface.select_range_entry.get().split(' ')
    gen_interface.select_range_entry.delete(0)
    if len(diapason_list) == 1:
        result = range_len_pas.set(diapason_list[0], diapason_list[0])
    elif len(diapason_list) > 1:
        result = range_len_pas.set(diapason_list[0], diapason_list[1])
    messagebox.showinfo("Результат", result)


def get_range():
    result = str(range_len_pas.get()[0]) + ' ' + str(range_len_pas.get()[1])
    gen_interface.get_range_entry.delete(0)
    gen_interface.get_range_entry.insert(0, result)


def stay_letters():
    if select_letter.get() and gen_interface.letter_checkbutton['state'] == NORMAL:
        symbolbet.delete_black_symbols(split(only_type_symbols(symbolbet.get_black(), 'letters')))
        gen_interface.gr_letter_checkbutton['state'] = NORMAL
        gen_interface.sm_letter_checkbutton['state'] = NORMAL
    elif not select_letter.get() and gen_interface.letter_checkbutton['state'] == NORMAL:
        symbolbet.add_black_symbols(split(only_type_symbols(symbolbet.get(), 'letters')))
        gen_interface.gr_letter_checkbutton['state'] = DISABLED
        gen_interface.sm_letter_checkbutton['state'] = DISABLED


def stay_sm_letters():
    if select_sm_letter.get() and gen_interface.sm_letter_checkbutton['state'] == NORMAL:
        symbolbet.delete_black_symbols(
            split(selection_letters(only_type_symbols(symbolbet.get_black(), 'letters'), 'small_letters')))
        if select_gr_letter.get():
            gen_interface.letter_checkbutton['state'] = NORMAL
    elif not select_sm_letter.get() and gen_interface.sm_letter_checkbutton['state'] == NORMAL:
        symbolbet.add_black_symbols(
            split(selection_letters(only_type_symbols(symbolbet.get(), 'letters'), 'small_letters')))
        gen_interface.letter_checkbutton['state'] = DISABLED


def stay_gr_letters():
    if select_gr_letter.get() and gen_interface.gr_letter_checkbutton['state'] == NORMAL:
        symbolbet.delete_black_symbols(
            split(selection_letters(only_type_symbols(symbolbet.get_black(), 'letters'), 'great_letters')))
        if select_sm_letter.get():
            gen_interface.letter_checkbutton['state'] = NORMAL
    elif not select_gr_letter.get() and gen_interface.gr_letter_checkbutton['state'] == NORMAL:
        symbolbet.add_black_symbols(
            split(selection_letters(only_type_symbols(symbolbet.get(), 'letters'), 'great_letters')))
        gen_interface.letter_checkbutton['state'] = DISABLED


def stay_numbers():
    if select_number.get() and gen_interface.number_checkbutton['state'] == NORMAL:
        symbolbet.delete_black_symbols(split(only_type_symbols(symbolbet.get_black(), 'numbers')))
    elif not select_number.get() and gen_interface.number_checkbutton['state'] == NORMAL:
        symbolbet.add_black_symbols(split(only_type_symbols(symbolbet.get(), 'numbers')))


def stay_other():
    if select_other.get() and gen_interface.other_checkbutton['state'] == NORMAL:
        symbolbet.delete_black_symbols(split(only_type_symbols(symbolbet.get_black(), 'other')))
    elif not select_other.get() and gen_interface.other_checkbutton['state'] == NORMAL:
        symbolbet.add_black_symbols(split(only_type_symbols(symbolbet.get(), 'other')))


def automatically_update_list():
    if gen_interface.get_list_entry.get() != '':
        get_list()


def get_list():
    def logic_get_list(example_symbolbet):
        gen_interface.get_list_entry.delete(0)
        gen_interface.get_list_entry.insert(0, divide_word(example_symbolbet.get()))
    if select_symbolbet_action.get() == 1:
        logic_get_list(symbolbet)
    elif select_symbolbet_action.get() == 2:
        logic_get_list(required_symbolbet)


def set_standart():
    symbolbet.delete_symbols(split(symbolbet.get()))
    symbolbet.add_symbols(split('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*'))
    symbolbet.delete_black_symbols(split(symbolbet.get_black()))
    symbolbet.update_reserve()
    required_symbolbet.delete_symbols(split(required_symbolbet.get()))
    range_len_pas.set()
    automatically_update_list()
    select_number.set(1)
    select_letter.set(1)
    select_gr_letter.set(1)
    select_sm_letter.set(1)
    select_other.set(1)
    gen_interface.letter_checkbutton['state'] = NORMAL
    gen_interface.gr_letter_checkbutton['state'] = NORMAL
    gen_interface.sm_letter_checkbutton['state'] = NORMAL

def set_checkpas_settings():
    symbolbet.delete_symbols(split(symbolbet.get()))
    required_symbolbet.delete_symbols(split(required_symbolbet.get()))
    symbolbet.delete_black_symbols(split(symbolbet.get_black()))
    symbolbet.add_symbols(split(allowed_symbolbet.get()))
    required_symbolbet.add_symbols(split(required_check_symbolbet.get()))
    symbolbet.add_black_symbols(split(allowed_symbolbet.get_black()))
    range_len_pas.set(len_checkpas_range.get()[0], len_checkpas_range.get()[1])
    select_number.set(allow_number.get())
    select_letter.set(allow_letter.get())
    select_gr_letter.set(allow_gr_letter.get())
    select_sm_letter.set(allow_sm_letter.get())
    select_other.set(allow_other.get())
    stay_numbers()
    stay_letters()
    stay_gr_letters()
    stay_sm_letters()
    stay_other()


def settings_window_leave():
    gen_interface.place_forget()
    mmenu_interface.place()



gen_interface.generate_pas_button['command'] = generate
gen_interface.add_symbols_button['command'] = add_symbols
gen_interface.delete_symbols_button['command'] = delete_symbols
gen_interface.stay_symbols_button['command'] = stay_symbols
gen_interface.get_list_button['command'] = get_list
gen_interface.select_range_button['command'] = select_range
gen_interface.get_range_button['command'] = get_range
gen_interface.letter_checkbutton['command'] = stay_letters
gen_interface.gr_letter_checkbutton['command'] = stay_gr_letters
gen_interface.sm_letter_checkbutton['command'] = stay_sm_letters
gen_interface.number_checkbutton['command'] = stay_numbers
gen_interface.other_checkbutton['command'] = stay_other
gen_interface.set_default_button['command'] = set_standart
gen_interface.settings_leave_button['command'] = settings_window_leave
gen_interface.set_checkpas_settings_button['command'] = set_checkpas_settings
gen_interface.add_pas_storage_button["command"] = send_to_savebox
