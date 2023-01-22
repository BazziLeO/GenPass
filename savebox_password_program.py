from widget_classes import *
from other_classes import *


def update_boxes_information():
    settings_interface.password_box.set_new_dict(settings_interface.operational_password_box.key_list,
                                                 settings_interface.operational_password_box.value_list)
    stigma_interface.stigma_list.clear()
    stigma_interface.stigma_list = [e for e in stigma_interface.operational_stigma_list]


def load_boxes_information():
    settings_interface.operational_password_box.set_new_dict(settings_interface.password_box.key_list,
                                                             settings_interface.password_box.value_list)
    stigma_interface.operational_stigma_list.clear()
    stigma_interface.operational_stigma_list = [e for e in stigma_interface.stigma_list]


def update_passwordbox_information():
    main_interface.place_ofpassword_entry.delete(0, END)
    main_interface.place_ofdescription_text.delete(0.0, END)
    main_interface.place_ofpassword_entry.insert(0, settings_interface.operational_password_box.key_list[
        settings_interface.password_index])
    main_interface.place_ofdescription_text.insert(0.0, settings_interface.operational_password_box.value_list[
        settings_interface.password_index])
    main_interface.show_number_of_password_button[
        "text"] = f"Страница {settings_interface.password_index + 1} из " \
                  f"{settings_interface.operational_password_box.length()} "


class SetUI(UI):

    def __init__(self, master=None, text="Настройки"):  # Description + packing
        super().__init__(master=master, text=text)
        self.password_index = 0
        self.protect_passwords_variable = IntVar()
        self.password_box = MyDict([""], [""])
        self.operational_password_box = MyDict([""], [""])

        self.settings_frame = LabelFrame(self, text="Настройки", font="Helvetica 12")

        self.action_frame = LabelFrame(self, text="Действия с паролями", font="Helvetica 11")
        self.save_new_information_button = ClassicButton(self.action_frame, text="Сохранить изменения", width=24,
                                                         font="Helvetica 13")
        self.add_password_button = ClassicButton(self.action_frame, text="Добавить пароль", width=28,
                                                 font="Helvetica 13", command=self.add_password)
        self.delete_password_button = ClassicButton(self.action_frame, text="Удалить пароль", width=28,
                                                    font="Helvetica 13",
                                                    state=DISABLED, command=self.delete_password)

        self.search_frame = LabelFrame(self, text="Поиск", font="Helvetica 11")
        self.search_bypassword_button = ClassicButton(self.search_frame, text="По названию", width=13,
                                                      command=self.search_by_password)
        self.search_bypassword_entry = ClassicEntry(self.search_frame, width=10, font="Helvetica 14")
        self.break_search_bypassword_button = ClassicButton(self.search_frame, text="X", width=2, height=1,
                                                            font="Helvetica 11",
                                                            command=self._stop_searching)
        self.search_bydescription_button = ClassicButton(self.search_frame, text="По описанию", width=13,
                                                         command=self.search_by_description)
        self.search_bydescription_entry = ClassicEntry(self.search_frame, width=10, font="Helvetica 14")
        self.break_search_bydescr_button = ClassicButton(self.search_frame, text="X", width=2, height=1,
                                                         font="Helvetica 11",
                                                         command=self._stop_searching)
        self.search_bynumber_button = ClassicButton(self.search_frame, text="По номеру", width=13,
                                                    command=self.search_by_index)
        self.search_bynumber_entry = ClassicEntry(self.search_frame, width=10, font="Helvetica 14")

        self.leave_button = ClassicButton(self, text="Выйти", width=13)

        self.action_frame.pack()
        self.add_password_button.pack(pady=1, padx=4)
        self.delete_password_button.pack(pady=1)

        self.search_frame.pack(pady=2)
        self.search_bypassword_button.grid(column=0, row=0, padx=1, pady=1)
        self.search_bypassword_entry.grid(column=1, row=0, padx=1, pady=1)
        self.break_search_bypassword_button.grid(column=2, row=0, padx=1, pady=1)
        self.search_bydescription_button.grid(column=0, row=1, padx=1, pady=1)
        self.search_bydescription_entry.grid(column=1, row=1, padx=1, pady=1)
        self.break_search_bydescr_button.grid(column=2, row=1, padx=1, pady=1)
        self.search_bynumber_button.grid(column=0, row=2, padx=1, pady=1)
        self.search_bynumber_entry.grid(column=1, row=2, padx=1, pady=1)

        self.leave_button.pack(side=LEFT, pady=1)

    def set_new_index(self, new_index, type="non-by-user"):
        try:
            if type == "by-user":
                new_index = int(new_index) - 1
            elif type == "non-by-user":
                new_index = int(new_index)
            if -1 < new_index < self.operational_password_box.length():
                self.password_index = new_index
        except:
            return "Index is not correct!"

    def add_password(self):
        self.operational_password_box.add("", "")
        stigma_interface.stigma_placed_forget()
        stigma_interface.operational_stigma_list.append([])
        self.set_new_index(self.operational_password_box.length() - 1)
        stigma_interface.stigma_placed()
        update_passwordbox_information()
        if self.operational_password_box.length() > 1:
            self.delete_password_button["state"] = NORMAL

    def delete_password(self):
        stigma_interface.stigma_placed_forget()
        if self.operational_password_box.length() == 2:
            self.delete_password_button["state"] = DISABLED
        self.set_new_index(self.operational_password_box.length() - 1)
        stigma_interface.operational_stigma_list.pop(self.operational_password_box.length() - 1)
        stigma_interface.stigma_placed()
        update_passwordbox_information()

    def _deleting_password_elements(self, word, type="key"):
        clearing_list = []
        if type == "key":
            clearing_list = self.operational_password_box.key_list
        elif type == "value":
            clearing_list = self.operational_password_box.value_list
        for i in range(len(clearing_list)):
            if clearing_list[i].count(word) == 0:
                self.operational_password_box.delete(i)
                stigma_interface.operational_stigma_list.pop(i)
                self._deleting_password_elements(word=word, type=type)
                break

    def _stop_searching(self):
        searching_list = [main_interface.save_new_information_button, self.add_password_button,
                          self.delete_password_button, self.search_bypassword_button, self.search_bypassword_entry,
                          self.break_search_bypassword_button, self.search_bydescription_button,
                          self.search_bydescription_entry, self.break_search_bydescr_button]
        for e in searching_list:
            if e == self.delete_password_button:
                if self.password_box.length() > 1:
                    self.delete_password_button["state"] = NORMAL
            else:
                e["state"] = NORMAL
        load_boxes_information()
        self.set_new_index(0)
        update_passwordbox_information()

    def search_by_password(self):
        stigma_interface.stigma_placed_forget()
        disabled_list = [main_interface.save_new_information_button, self.add_password_button,
                         self.delete_password_button, self.search_bydescription_button, self.search_bypassword_entry,
                         self.search_bydescription_button, self.break_search_bydescr_button]
        update_boxes_information()
        self._deleting_password_elements(word=self.search_bypassword_entry.get(), type="key")
        if not self.operational_password_box.key_list:
            messagebox.showinfo("Поиск совершен неудачно", "Паролей с заданными настройками вы не сохранили!")
            self._stop_searching()
        else:
            for e in disabled_list:
                e["state"] = DISABLED
            self.set_new_index(self.operational_password_box.length() - 1)
            update_passwordbox_information()
        stigma_interface.stigma_placed()

    def search_by_description(self):
        disabled_list = [main_interface.save_new_information_button, self.add_password_button,
                         self.delete_password_button, self.search_bydescription_button,
                         self.search_bydescription_entry, self.search_bydescription_button,
                         self.break_search_bypassword_button]
        stigma_interface.stigma_placed_forget()
        update_boxes_information()
        self._deleting_password_elements(word=self.search_bydescription_entry.get(), type="value")
        if not self.operational_password_box.key_list:
            messagebox.showinfo("Поиск совершен неудачно", "Паролей с заданными настройками вы не сохранили!")
            self._stop_searching()
        else:
            for e in disabled_list:
                e["state"] = DISABLED
            self.set_new_index(self.operational_password_box.length() - 1)
            update_passwordbox_information()
        stigma_interface.stigma_placed()

    def search_by_index(self):
        stigma_interface.stigma_placed_forget()
        new_index = self.search_bynumber_entry.get()
        self.set_new_index(new_index, "by-user")
        stigma_interface.stigma_placed()
        update_passwordbox_information()


class ProtectUI(UI):

    def __init__(self, master=None, text="Входной контроль"):
        super().__init__(master=master, text=text)
        self._key_gate = ""

        self.write_key_frame = LabelFrame(self, text="Вход в хранилище", font="Helvetica 12")
        self.confirm_key_button = ClassicButton(self.write_key_frame, text="Потвердить ключ", width=24,
                                                command=self.entry_to_savebox)
        self.write_key_entry = ClassicEntry(self.write_key_frame)

        self.or_label = ClassicLabel(self, text="ИЛИ")

        self.update_key_frame = LabelFrame(self, text="Обновление ключа", font="Helvetica 12")
        self.inside_frame = Frame(self.update_key_frame)
        self.check_old_key_label = ClassicLabel(self.inside_frame, text="Старый ключ")
        self.check_old_key_entry = ClassicEntry(self.inside_frame, width=10)
        self.check_new_key_label = ClassicLabel(self.inside_frame, text="Новый ключ")
        self.check_new_key_entry = ClassicEntry(self.inside_frame, width=10)
        self.confirm_change_button = ClassicButton(self.update_key_frame, text="Потвердить изменения", width=24, command=self.confirm_changes)

        self.write_key_frame.pack(pady=1)
        self.write_key_entry.pack(padx=2, pady=2)
        self.confirm_key_button.pack(padx=2, pady=2)

        self.or_label.pack()

        self.update_key_frame.pack(pady=1)
        self.inside_frame.pack()
        self.check_old_key_label.grid(column=0, row=0, padx=1, pady=1)
        self.check_old_key_entry.grid(column=0, row=1, padx=1, pady=1)
        self.check_new_key_label.grid(column=1, row=0, padx=1, pady=1)
        self.check_new_key_entry.grid(column=1, row=1, padx=1, pady=1)

        self.confirm_change_button.pack(pady=2)

    def entry_to_savebox(self):
        if self.write_key_entry.get() == self._key_gate:
            self.grid_forget()
            settings_interface.grid(column=0, row=0)
            main_interface.grid(column=1, row=0)
            stigma_interface.grid(column=2, row=0)
        else:
            self.grid(column=1, row=0)
            self.write_key_entry.delete(0, END)
            self.write_key_entry.insert(0, "Введенный пароль неправилен!")

    def confirm_changes(self):
        if self.check_old_key_entry.get() == self._key_gate:
            self._key_gate = self.check_new_key_entry.get()




class MainUI(UI):
    def __init__(self, master=None, text="Пароль"):
        super().__init__(master=master, text=text)
        self.place_ofpassword_entry = ClassicEntry(self, width=25)
        self.place_ofdescription_text = Text(self, font="Helvetica 11", width=35, height=10)

        self.navigation_frame = Frame(self)
        self.turn_toleft_button = ClassicButton(self.navigation_frame, text="<", width=2, command=self.turn_left)
        self.show_number_of_password_button = ClassicLabel(self.navigation_frame,
                                                           text=f"Страница {settings_interface.password_index + 1} из {settings_interface.operational_password_box.length}")
        self.turn_toright_button = ClassicButton(self.navigation_frame, text=">", width=2, command=self.turn_right)
        self.save_new_information_button = ClassicButton(self.navigation_frame, text="Сохранить", width=9,
                                                         command=self.save_password_information)

        self.place_ofpassword_entry.pack(pady=6)
        self.place_ofdescription_text.pack()

        self.navigation_frame.pack(pady=8)
        self.turn_toleft_button.pack(side=LEFT, padx=1)
        self.show_number_of_password_button.pack(side=LEFT, padx=1)
        self.turn_toright_button.pack(side=LEFT, padx=1)
        self.save_new_information_button.pack(side=LEFT, padx=1)

    def turn_right(self):
        stigma_interface.stigma_placed_forget()
        if settings_interface.password_index == settings_interface.operational_password_box.length() - 1:
            settings_interface.set_new_index(0)
        else:
            settings_interface.set_new_index(settings_interface.password_index + 1)
        stigma_interface.stigma_placed()
        update_passwordbox_information()

    def turn_left(self):
        stigma_interface.stigma_placed_forget()
        if settings_interface.password_index == 0:
            settings_interface.set_new_index(settings_interface.operational_password_box.length() - 1)
        else:
            settings_interface.set_new_index(settings_interface.password_index - 1)
        stigma_interface.stigma_placed()
        update_passwordbox_information()

    def save_password_information(self):
        index = settings_interface.password_index
        password = self.place_ofpassword_entry.get()
        description = self.place_ofdescription_text.get(0.0, END)
        settings_interface.operational_password_box.set_by_index(key=password, value=description, index=index)


class StigmaUI(UI):
    def __init__(self, master=None, text="Метки"):
        super().__init__(master=master, text=text)

        self.stigma_place_frame = Frame(self)

        self.stigma_list = [[Stigma(self.stigma_place_frame, text="Метка 1")]]
        self.operational_stigma_list = [e for e in self.stigma_list]
        self.stigma_index = 0

        self.stigma_settings_frame = Frame(self.stigma_place_frame)
        self.move_down_button = ClassicButton(self.stigma_settings_frame, text="v", font="Helvetica 12", width=2,
                                              height=1, command=self.swap_stigmas)
        self.change_stigma_button = ClassicButton(self.stigma_settings_frame, text="⭯", font="Helvetica 12", width=2,
                                                  height=1, command=self.open_stigma_creator)
        self.delete_stigma_button = ClassicButton(self.stigma_settings_frame, text="X", font="Helvetica 12", width=2,
                                                  height=1, command=self.delete_stigma)
        self.stigma_navigation_frame = Frame(self)
        self.go_up_button = ClassicButton(self.stigma_navigation_frame, text="˄", width=2, height=1, command=self.go_up)
        self.selected_stigma_label = ClassicLabel(self.stigma_navigation_frame)
        self.go_down_button = ClassicButton(self.stigma_navigation_frame, text="˅", width=2, height=1,
                                            command=self.go_down)
        self.add_stigma_button = ClassicButton(self.stigma_navigation_frame, text="Добавить", font="Helvetica 13",
                                               width=13,
                                               height=1, command=self.add_stigma)

        self.stigma_place_frame.pack()
        self.stigma_settings_frame.grid(column=1, row=0)
        self.move_down_button.pack(side=LEFT, padx=1)
        self.change_stigma_button.pack(side=LEFT, padx=1)
        self.delete_stigma_button.pack(side=LEFT, padx=1)

        self.stigma_navigation_frame.pack(pady=7)
        self.go_up_button.pack(side=LEFT)
        self.selected_stigma_label.pack(side=LEFT)
        self.go_down_button.pack(side=LEFT)
        self.add_stigma_button.pack(side=LEFT, padx=3)

        self.stigma_placed()

    def set_new_index(self, new_index, type="non-by-user"):
        try:
            if type == "by-user":
                new_index = int(new_index) - 1
            elif type == "non-by-user":
                new_index = int(new_index)
            if -1 < new_index < len(self.operational_stigma_list[settings_interface.password_index]):
                self.stigma_index = new_index
        except:
            return "Index is not correct!"

    def stigma_placed_forget(self):
        stigma_list = self.operational_stigma_list[settings_interface.password_index]
        for i in range(len(stigma_list)):
            stigma_list[i].grid_forget()
        self.stigma_settings_frame.grid_forget()

    def stigma_placed(self):
        stigma_list = self.operational_stigma_list[settings_interface.password_index]
        for i in range(len(stigma_list)):
            stigma_list[i].grid(column=0, row=i)
        self._show_stigma_settings_frame()
        self._update_selected_stigma_label()
        self._check_disable_on_add_button()

    def _update_selected_stigma_label(self):
        stigma_list = self.operational_stigma_list[settings_interface.password_index]
        if len(stigma_list) > 0:
            self.selected_stigma_label["text"] = f"Номер {self.stigma_index + 1} из {len(stigma_list)}"
        else:
            self.selected_stigma_label["text"] = "Меток нет"

    def _show_stigma_settings_frame(self):
        stigma_list = self.operational_stigma_list[settings_interface.password_index]
        if len(stigma_list) > 0:
            self.stigma_settings_frame.grid(column=1, row=self.stigma_index)
        else:
            self.stigma_settings_frame.grid_forget()

    def _check_disable_on_add_button(self):
        stigma_list = self.operational_stigma_list[settings_interface.password_index]
        if len(stigma_list) > 9:
            self.add_stigma_button["state"] = DISABLED
        else:
            self.add_stigma_button["state"] = NORMAL

    def add_stigma(self):
        stigma_list = self.operational_stigma_list[settings_interface.password_index]
        self.stigma_placed_forget()
        stigma_list.append(Stigma(self.stigma_place_frame, text=f"Метка {len(stigma_list) + 1}"))
        self.set_new_index(len(stigma_list) - 1)
        self.stigma_placed()

    def delete_stigma(self):
        stigma_list = self.operational_stigma_list[settings_interface.password_index]
        self.stigma_placed_forget()
        stigma_list.pop(self.stigma_index)
        if self.stigma_index > 0:
            self.set_new_index(len(stigma_list) - 1)
        self.stigma_placed()

    def swap_stigmas(self):
        stigma_list = self.operational_stigma_list[settings_interface.password_index]

        def logic_of_swap(first_index, step):
            self.stigma_placed_forget()
            k = stigma_list[first_index]
            stigma_list[first_index] = stigma_list[(first_index + step) % len(stigma_list)]
            stigma_list[(first_index + step) % len(stigma_list)] = k
            self.set_new_index((first_index + step) % len(stigma_list))
            self.stigma_placed()

        logic_of_swap(self.stigma_index, 1)

    def open_stigma_creator(self):
        self.grid_forget()
        stigma_creator_interface.grid(column=2, row=0)

    def go_up(self):
        self.stigma_placed_forget()
        if self.stigma_index == 0:
            self.set_new_index(len(self.operational_stigma_list[settings_interface.password_index]) - 1)
        else:
            self.set_new_index(self.stigma_index - 1)
        self.stigma_placed()

    def go_down(self):
        self.stigma_placed_forget()
        if self.stigma_index == len(self.operational_stigma_list[settings_interface.password_index]) - 1:
            self.set_new_index(0)
        else:
            self.set_new_index(self.stigma_index + 1)
        self.stigma_placed()


class CreatorStigmaUI(UI):
    red_scale_variable, blue_scale_variable, green_scale_variable = IntVar(), IntVar(), IntVar()

    def __init__(self, master=None):
        super().__init__(master=master)

        self.first_frame = Frame(self)

        self.example_frame = LabelFrame(self.first_frame, text="Пример", font="Helvetica 12")
        self.example = Stigma(self.example_frame)
        self.confirm_stigma = ClassicButton(self.example_frame, text="Потвердить", width=15, height=1,
                                            command=self.confirm_changes)

        self.select_name_frame = LabelFrame(self.first_frame, text="Выбор имени", font="Helvetica 12")
        self.write_name_entry = ClassicEntry(self.select_name_frame, font="helvetica 12", width=15)
        self.confirm_name_button = ClassicButton(self.select_name_frame, text="Потвердить", font="Helvetica 11",
                                                 width=15, command=self.config_name)
        self.leave_from_creator_button = ClassicButton(self.first_frame, text="Выйти", width=15, height=1,
                                                       command=self.leave_from_creator)

        self.color_frame = LabelFrame(self, text="Выбор цвета", font="Helvetica 12")
        self.red_scale = ClassicScale(self.color_frame, text="Красный", width=128, command=self.config_color)
        self.green_scale = ClassicScale(self.color_frame, text="Зеленый", width=128, command=self.config_color)
        self.blue_scale = ClassicScale(self.color_frame, text="Синий", width=128, command=self.config_color)

        self.widget_list = [self, self.example, self.red_scale,
                            self.green_scale, self.blue_scale, self.write_name_entry, self.confirm_name_button]

        self.first_frame.pack(side=LEFT)

        self.example_frame.pack(pady=2)
        self.example.pack()
        self.confirm_stigma.pack(side=LEFT, padx=2)

        self.select_name_frame.pack(pady=2)
        self.write_name_entry.pack(pady=2)
        self.confirm_name_button.pack(pady=2)
        self.leave_from_creator_button.pack(pady=2)

        self.color_frame.pack(pady=2)
        self.red_scale.pack(pady=1)
        self.green_scale.pack(pady=1)
        self.blue_scale.pack(pady=1)

    def config_name(self):
        self.example.change_name(new_name=self.write_name_entry.get())

    def config_color(self, value):
        self.example.change_color(red=self.red_scale.get(), green=self.green_scale.get(), blue=self.blue_scale.get())

    def confirm_changes(self):
        password_index = settings_interface.password_index
        stigma_index = stigma_interface.stigma_index
        stigma = stigma_interface.operational_stigma_list[password_index][stigma_index]
        stigma_interface.stigma_placed_forget()
        stigma.change_color(self.example.color.green, self.example.color.blue, self.example.color.red)
        stigma.change_name(self.example.get("name"))
        stigma_interface.stigma_placed()
        self.leave_from_creator()

    def leave_from_creator(self):
        self.grid_forget()
        stigma_interface.grid(column=2, row=0)


savebox_password_frame = Frame()
settings_interface = SetUI(savebox_password_frame)
main_interface = MainUI(savebox_password_frame)
stigma_interface = StigmaUI(savebox_password_frame)

stigma_creator_interface = CreatorStigmaUI(savebox_password_frame)
protect_interface = ProtectUI(savebox_password_frame)

protect_interface.grid(column=1, row=0)


update_passwordbox_information()
