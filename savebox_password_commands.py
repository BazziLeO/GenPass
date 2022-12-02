from savebox_password_interface import *
from mainmenu_interface import mmenu_interface

def open_stigma_creator():
    savebox_interface.stigma_frame.pack_forget()
    creator_stigma.pack()

def protect_passwords():
    blocked_list = [savebox_interface.place_ofpassword_entry, savebox_interface.place_ofdescription_text,
                    savebox_interface.add_password_button, savebox_interface.delete_password_button]
    if protect_passwords_state.get():
        new_key_list, new_value_list = [], []
        update_boxes_information()
        savebox_interface.place_ofpassword_entry["show"] = "*"
        for e in operational_password_box.key_list:
            new_key_list.append(add_symbols_in_random(word=e, chance=r(51, 97)))
            new_value_list.append("")
        for e in blocked_list:
            e["state"] = DISABLED
    else:
        load_boxes_information()
        savebox_interface.place_ofpassword_entry["show"] = ""
        for e in blocked_list:
            e["state"] = NORMAL
    update_passwordbox_information()


def add_password():
    operational_password_box.add("", "")
    update_passwordbox_information()
    if operational_password_box.length() > 1:
        savebox_interface.delete_password_button["state"] = NORMAL


def delete_password():
    if password_box.length() == 2:
        savebox_interface.delete_password_button["state"] = DISABLED
        operational_password_box.delete(operational_password_box.length-1)
        update_passwordbox_information()


def save_password_information():
    index = scroll_password_box.index
    password = savebox_interface.place_ofpassword_entry.get()
    description = savebox_interface.place_ofdescription_text.get(0.0, END)
    operational_password_box.set_by_index(key=password, value=description, index=index)


def search_by_index():
    new_index = savebox_interface.search_bynumber_entry.get()
    scroll_password_box.set_index(new_index, "by user")
    update_passwordbox_information()


def update_passwordbox_information():
    savebox_interface.place_ofpassword_entry.delete(0, END)
    savebox_interface.place_ofdescription_text.delete(0.0, END)
    scroll_password_box.set_length(operational_password_box.length())
    savebox_interface.place_ofpassword_entry.insert(0, operational_password_box.key_list[scroll_password_box.index])
    savebox_interface.place_ofdescription_text.insert(0.0, operational_password_box.value_list[scroll_password_box.index])
    savebox_interface.show_number_of_password_button["text"] = f"Страница {scroll_password_box.index+1} из {scroll_password_box.length}"


def turn_right():
    scroll_password_box.turn_right()
    update_passwordbox_information()


def turn_left():
    scroll_password_box.turn_left()
    update_passwordbox_information()


def update_boxes_information():
    password_box.set_new_dict(operational_password_box.key_list, operational_password_box.value_list)


def load_boxes_information():
    operational_password_box.set_new_dict(password_box.key_list, password_box.value_list)


def deleting_password_elements():
    word = savebox_interface.search_bypassword_entry.get()
    for i in range(len(operational_password_box.key_list)):
        if operational_password_box.key_list[i].count(word) == 0:
            operational_password_box.delete(i)
            deleting_password_elements()
            break


def search_by_password():
    savebox_interface.save_new_information_button["state"] = DISABLED
    savebox_interface.add_password_button["state"] = DISABLED
    savebox_interface.delete_password_button["state"] = DISABLED
    savebox_interface.search_bypassword_button["state"] = DISABLED
    savebox_interface.search_bypassword_entry["state"] = DISABLED
    savebox_interface.search_bydescription_button["state"] = DISABLED
    savebox_interface.break_search_bydescrp_button["state"] = DISABLED

    update_boxes_information()
    deleting_password_elements()
    if not operational_password_box.key_list:
        stop_searching()
        messagebox.showinfo("Поиск совершен неудачно", "Паролей с заданными настройками вы не сохранили!")
    else:
        scroll_password_box.set_index(0)
        scroll_password_box.set_length(operational_password_box.length())
    update_passwordbox_information()


def deleting_description_elements():
    word = savebox_interface.search_bydescription_entry.get()
    for i in range(len(operational_password_box.value_list)):
        if operational_password_box.value_list[i].count(word) == 0:
            operational_password_box.delete(i)
            deleting_description_elements()
            break


def search_by_description():
    savebox_interface.save_new_information_button["state"] = DISABLED
    savebox_interface.add_password_button["state"] = DISABLED
    savebox_interface.delete_password_button["state"] = DISABLED
    savebox_interface.search_bydescription_button["state"] = DISABLED
    savebox_interface.search_bydescription_entry["state"] = DISABLED
    savebox_interface.search_bypassword_button["state"] = DISABLED
    savebox_interface.break_search_bypassword_button["state"] = DISABLED

    update_boxes_information()
    deleting_description_elements()
    if not operational_password_box.key_list:
        stop_searching()
        messagebox.showinfo("Поиск совершен неудачно", "Паролей с заданными настройками вы не сохранили!")
    else:
        scroll_password_box.set_index(0)
        scroll_password_box.set_length(operational_password_box.length())
    update_passwordbox_information()


def stop_searching():
    savebox_interface.save_new_information_button["state"] = NORMAL
    savebox_interface.add_password_button["state"] = NORMAL
    if password_box.length() > 1:
        savebox_interface.delete_password_button["state"] = NORMAL
    savebox_interface.search_bypassword_button["state"] = NORMAL
    savebox_interface.search_bypassword_entry["state"] = NORMAL
    savebox_interface.search_bydescription_button["state"] = NORMAL
    savebox_interface.search_bydescription_entry["state"] = NORMAL
    savebox_interface.break_search_bypassword_button["state"] = NORMAL
    savebox_interface.break_search_bydescrp_button["state"] = NORMAL
    load_boxes_information()
    update_passwordbox_information()


def leave_from_savebox():
    if savebox_interface.search_bydescription_entry["state"] and savebox_interface.search_bypassword_entry["state"] == NORMAL:
        update_boxes_information()
    savebox_interface.place_forget()
    mmenu_interface.place()


savebox_interface.add_password_button["command"] = add_password
savebox_interface.delete_password_button["command"] = delete_password
savebox_interface.search_bypassword_button["command"] = search_by_password
savebox_interface.break_search_bypassword_button["command"] = stop_searching
savebox_interface.search_bydescription_button["command"] = search_by_description
savebox_interface.break_search_bydescrp_button["command"] = stop_searching
savebox_interface.search_bynumber_button["command"] = search_by_index
savebox_interface.turn_toleft_button["command"] = turn_left
savebox_interface.turn_toright_button["command"] = turn_right
savebox_interface.save_new_information_button["command"] = save_password_information
savebox_interface.leave_button["command"] = leave_from_savebox
savebox_interface.protect_passwords_checkbutton["command"] = protect_passwords
savebox_interface.change_stigma_button["command"] = open_stigma_creator
update_passwordbox_information()



