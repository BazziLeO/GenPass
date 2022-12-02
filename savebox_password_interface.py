from widget_classes import *
from other_classes import *

protect_passwords_state = IntVar()
password_box = MyDict([""], [""])
operational_password_box = MyDict([""], [""])
scroll_password_box = ScrollList(length=operational_password_box.length(), scroll="circled")


class CreatorStigmaUI(UI):
    red_scale_variable, blue_scale_variable, green_scale_variable = IntVar(), IntVar(), IntVar()

    def __init__(self, master=None):
        super().__init__(master=master)

        self.first_frame = Frame(self)

        self.example_frame = LabelFrame(self.first_frame, text="Пример", font="Helvetica 10")
        self.example = Stigma(self.example_frame)
        self.leave_from_creator_button = ClassicButton(self.example_frame, text="X", width=2, height=1, command=self.leave_from_creator)
        self.confirm_stigma = ClassicButton(self.example_frame, text="Потвердить", width=12, height=1)

        self.select_name_frame = LabelFrame(self.first_frame, text="Выбор имени", font="Helvetica 12")
        self.write_name_entry = ClassicEntry(self.select_name_frame, font="helvetica 12", width=15)
        self.confirm_name_button = ClassicButton(self.select_name_frame, text="Потвердить", font="Helvetica 11",
                                                 width=15, command=self.config_name)

        self.color_frame = LabelFrame(self, text="Выбор цвета", font="Helvetica 12")
        self.red_scale = ClassicScale(self.color_frame, text="Красный", command=self.config_color)
        self.green_scale = ClassicScale(self.color_frame, text="Зеленый", command=self.config_color)
        self.blue_scale = ClassicScale(self.color_frame, text="Синий", command=self.config_color)

        self.widget_list = [self, self.example, self.red_scale,
                            self.green_scale, self.blue_scale, self.write_name_entry, self.confirm_name_button]

        self.first_frame.pack(side=LEFT)

        self.example_frame.pack(pady=2)
        self.example.pack()

        self.confirm_name_button.pack(pady=2)
        self.confirm_stigma.pack(side=LEFT, padx=2)
        self.leave_from_creator_button.pack(side=LEFT, padx=2)

        self.color_frame.pack(pady=2)
        self.red_scale.pack(pady=1)
        self.green_scale.pack(pady=1)
        self.blue_scale.pack(pady=1)

        self.select_name_frame.pack(pady=2)
        self.write_name_entry.pack(pady=2)

    def config_name(self):
        self.example.change_name(new_name=self.write_name_entry.get())

    def config_color(self, value):
        self.example.change_color(red=self.red_scale.get(), green=self.green_scale.get(), blue=self.blue_scale.get())

    def leave_from_creator(self):
        self.pack_forget()
        savebox_interface.place()


class SaveBoxUI(UI):
    def __init__(self, master=None):
        super().__init__(master=master)

    main_frame = Frame()

    settings_frame = LabelFrame(main_frame, text="Настройки", font="Helvetica 12")

    search_frame = LabelFrame(settings_frame, text="Поиск", font="Helvetica 11")
    search_bypassword_button = ClassicButton(search_frame, text="По названию", width=13)
    search_bypassword_entry = ClassicEntry(search_frame, width=10, font="Helvetica 14")
    break_search_bypassword_button = ClassicButton(search_frame, text="X", width=2, height=1, font="Helvetica 11")
    search_bydescription_button = ClassicButton(search_frame, text="По описанию", width=13)
    search_bydescription_entry = ClassicEntry(search_frame, width=10, font="Helvetica 14")
    break_search_bydescrp_button = ClassicButton(search_frame, text="X", width=2, height=1, font="Helvetica 11")
    search_bynumber_button = ClassicButton(search_frame, text="По номеру", width=13)
    search_bynumber_entry = ClassicEntry(search_frame, width=10, font="Helvetica 14")

    action_frame = LabelFrame(settings_frame, text="Действия с паролями", font="Helvetica 11")
    save_new_information_button = ClassicButton(action_frame, text="Сохранить изменения", width=24, font="Helvetica 13")
    add_password_button = ClassicButton(action_frame, text="Добавить пароль", width=28, font="Helvetica 13")
    delete_password_button = ClassicButton(action_frame, text="Удалить пароль", width=28, font="Helvetica 13",
                                           state=DISABLED)

    other_frame = LabelFrame(settings_frame, text="Прочее", font="Helvetica 11")
    leave_button = ClassicButton(other_frame, text="Выйти", width=13)
    protect_passwords_checkbutton = ClassicCheckButton(other_frame, text="Защитить пароли", width=13,
                                                       variable=protect_passwords_state)

    password_frame = LabelFrame(main_frame, text="Пароль", font="Helvetica 12")
    place_ofpassword_entry = ClassicEntry(password_frame, width=25)
    place_ofdescription_text = Text(password_frame, font="Helvetica 11", width=35, height=10)

    navigation_frame = Frame(password_frame)
    turn_toleft_button = ClassicButton(navigation_frame, text="<", width=2)
    show_number_of_password_button = ClassicLabel(navigation_frame,
                                                  text=f"Страница {scroll_password_box.index + 1} из {scroll_password_box.length}")
    turn_toright_button = ClassicButton(navigation_frame, text=">", width=2)
    save_new_information_button = ClassicButton(navigation_frame, text="Сохранить", width=9)

    stigma_frame = LabelFrame(main_frame, text="Метки", font="Helvetica 12")
    stigma_place_frame = Frame(stigma_frame)
    stigma_settings_frame = Frame(stigma_place_frame)
    move_down_button = ClassicButton(stigma_settings_frame, text="v", font="Helvetica 12", width=2, height=1)
    change_stigma_button = ClassicButton(stigma_settings_frame, text="⭯", font="Helvetica 12", width=2, height=1)
    delete_stigma_button = ClassicButton(stigma_settings_frame, text="X", font="Helvetica 12", width=2, height=1)
    example_stigma = Stigma(stigma_place_frame)
    example_stigma_sec = Stigma(stigma_place_frame)
    stigma_navigation_frame = Frame(stigma_frame)
    go_up_button = ClassicButton(stigma_navigation_frame, text="˄", width=2, height=1)
    selected_stigma_label = ClassicLabel(stigma_navigation_frame, text="Номер 1 из 2")
    go_down_button = ClassicButton(stigma_navigation_frame, text="˅", width=2, height=1)
    add_stigma_button = ClassicButton(stigma_navigation_frame, text="Добавить", font="Helvetica 13", width=13, height=1)

    def place(self):
        SaveBoxUI.main_frame.pack()

        SaveBoxUI.settings_frame.pack(side=LEFT)

        SaveBoxUI.action_frame.pack()
        SaveBoxUI.add_password_button.pack(pady=1, padx=4)
        SaveBoxUI.delete_password_button.pack(pady=1)

        SaveBoxUI.search_frame.pack(pady=2)
        SaveBoxUI.search_bypassword_button.grid(column=0, row=0, padx=1, pady=1)
        SaveBoxUI.search_bypassword_entry.grid(column=1, row=0, padx=1, pady=1)
        SaveBoxUI.break_search_bypassword_button.grid(column=2, row=0, padx=1, pady=1)
        SaveBoxUI.search_bydescription_button.grid(column=0, row=1, padx=1, pady=1)
        SaveBoxUI.search_bydescription_entry.grid(column=1, row=1, padx=1, pady=1)
        SaveBoxUI.break_search_bydescrp_button.grid(column=2, row=1, padx=1, pady=1)
        SaveBoxUI.search_bynumber_button.grid(column=0, row=2, padx=1, pady=1)
        SaveBoxUI.search_bynumber_entry.grid(column=1, row=2, padx=1, pady=1)

        SaveBoxUI.other_frame.pack()
        SaveBoxUI.leave_button.pack(side=LEFT, padx=1)
        SaveBoxUI.protect_passwords_checkbutton.pack(side=LEFT, padx=1)

        SaveBoxUI.password_frame.pack(side=LEFT)
        SaveBoxUI.place_ofpassword_entry.pack(pady=6)
        SaveBoxUI.place_ofdescription_text.pack()

        SaveBoxUI.navigation_frame.pack(pady=8)
        SaveBoxUI.turn_toleft_button.pack(side=LEFT, padx=1)
        SaveBoxUI.show_number_of_password_button.pack(side=LEFT, padx=1)
        SaveBoxUI.turn_toright_button.pack(side=LEFT, padx=1)
        SaveBoxUI.save_new_information_button.pack(side=LEFT, padx=1)

        SaveBoxUI.stigma_frame.pack(side=LEFT)
        SaveBoxUI.stigma_place_frame.pack()

        SaveBoxUI.example_stigma.grid(column=0, row=0)
        SaveBoxUI.example_stigma_sec.grid(column=0, row=1)

        SaveBoxUI.stigma_settings_frame.grid(column=1, row=1)
        SaveBoxUI.move_down_button.pack(side=LEFT, padx=1)
        SaveBoxUI.change_stigma_button.pack(side=LEFT, padx=1)
        SaveBoxUI.delete_stigma_button.pack(side=LEFT, padx=1)

        SaveBoxUI.stigma_navigation_frame.pack(pady=7)
        SaveBoxUI.go_up_button.pack(side=LEFT)
        SaveBoxUI.selected_stigma_label.pack(side=LEFT)
        SaveBoxUI.go_down_button.pack(side=LEFT)
        SaveBoxUI.add_stigma_button.pack(side=LEFT, padx=3)

    def place_forget(self):
        SaveBoxUI.main_frame.pack_forget()


savebox_interface = SaveBoxUI()
creator_stigma = CreatorStigmaUI(savebox_interface.main_frame)
