from widget_classes import *
from other_classes import *

protect_passwords = IntVar()
scroll = ScrollList(length=17, scroll="circled")

class SaveBoxUI(UI):
    main_frame = Frame()

    settings_frame = LabelFrame(main_frame, text="Настройки", font="Helvetica 12")

    search_frame = LabelFrame(settings_frame, text="Поиск", font="Helvetica 11")
    search_bypassword_button = ClassicButton(search_frame, text="По названию", width=13)
    search_bypassword_entry = ClassicEntry(search_frame, width=10, font="Helvetica 14")
    search_bydescription_button = ClassicButton(search_frame, text="По описанию", width=13)
    search_bydescription_entry = ClassicEntry(search_frame, width=10, font="Helvetica 14")
    search_bynumber_button = ClassicButton(search_frame, text="По номеру", width=13)
    search_bynumber_entry = ClassicEntry(search_frame, width=10, font="Helvetica 14")

    action_frame = LabelFrame(settings_frame, text="Действия с паролями", font="Helvetica 11")
    add_password_button = ClassicButton(action_frame, text="Добавить пароль", width=24, font="Helvetica 13")
    delete_password_button = ClassicButton(action_frame, text="Удалить пароль", width=24, font="Helvetica 13")

    other_frame = LabelFrame(settings_frame, text="Прочее", font="Helvetica 11")
    leave_button = ClassicButton(other_frame, text="Выйти", width=10)
    protect_passwords_checkbutton = ClassicCheckButton(other_frame, text="Защитить пароли", width=13)

    password_frame = LabelFrame(main_frame, text="Пароль", font="Helvetica 12")
    place_ofpassword_entry = ClassicEntry(password_frame, width=25)
    place_ofdescription_text = Text(password_frame, font="Helvetica 11", width=35, height=10)

    navigation_frame = Frame(password_frame)
    turn_toleft_button = ClassicButton(navigation_frame, text="<", width=2)
    show_number_of_password_button = ClassicLabel(navigation_frame, text=f"Страница {scroll.get('index')} из {scroll.get('length')}")
    turn_toright_button = ClassicButton(navigation_frame, text=">", width=2)
    clear_all_button = ClassicButton(navigation_frame, text="C", width=2)

    stigma_frame = LabelFrame(main_frame, text="Метки", font="Helvetica 12")
    example_stigma = Stigma(stigma_frame)
    example_stigma_sec = Stigma(stigma_frame)
    add_stigma_button = ClassicButton(stigma_frame, text="Создать метку")

    def place(self):
        SaveBoxUI.main_frame.pack()

        SaveBoxUI.settings_frame.pack(side=LEFT)

        SaveBoxUI.action_frame.pack()
        SaveBoxUI.add_password_button.pack(pady=1, padx=8)
        SaveBoxUI.delete_password_button.pack(pady=1)

        SaveBoxUI.search_frame.pack(pady=2)
        SaveBoxUI.search_bypassword_button.grid(column=0, row=0, padx=1, pady=1)
        SaveBoxUI.search_bypassword_entry.grid(column=1, row=0, padx=1, pady=1)
        SaveBoxUI.search_bydescription_button.grid(column=0, row=1, padx=1, pady=1)
        SaveBoxUI.search_bydescription_entry.grid(column=1, row=1, padx=1, pady=1)
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
        SaveBoxUI.clear_all_button.pack(side=LEFT, padx=1)

        SaveBoxUI.stigma_frame.pack(side=LEFT)
        SaveBoxUI.example_stigma.pack()
        SaveBoxUI.example_stigma_sec.pack()
        SaveBoxUI.add_stigma_button.pack()
    def place_forget(self):
        SaveBoxUI.main_frame.pack_forget()

savebox_interface = SaveBoxUI()

