from savebox_password_interface import *
from mainmenu_interface import mmenu_interface

def turn_left():
    scroll.turn_left()
    savebox_interface.show_number_of_password_button[
        "text"] = f"Страница {scroll.get('index')} из {scroll.get('length')}"


def turn_right():
    scroll.turn_right()
    savebox_interface.show_number_of_password_button[
        "text"] = f"Страница {scroll.get('index')} из {scroll.get('length')}"

def select_index():
    new_index = savebox_interface.search_bynumber_entry.get()
    scroll.set_index(new_index)
    savebox_interface.show_number_of_password_button[
        "text"] = f"Страница {scroll.get('index')} из {scroll.get('length')}"

def leave_from_savebox():
    savebox_interface.place_forget()
    mmenu_interface.place()

savebox_interface.turn_toleft_button["command"] = turn_left
savebox_interface.turn_toright_button["command"] = turn_right
savebox_interface.search_bynumber_button["command"] = select_index
savebox_interface.leave_button["command"] = leave_from_savebox
