from widget_classes import *
from other_classes import *


class MainUI(UI):
    main_frame = Frame()
    portal_savebox_button = ClassicButton(master=main_frame, text='Хранилище паролей', font='Helvetica 15', width=36)
    first_frame = Frame(master=main_frame)
    portal_generatepas_button = ClassicButton(master=first_frame, font='Helvetica 14', text='Сгенерировать пароль', width=19)
    portal_checkpas_button = ClassicButton(master=first_frame, font='Helvetica 14', text='Проверить пароль', width=16)
    second_frame = Frame(master=main_frame)
    portal_aboutus_button = ClassicButton(master=second_frame, text='О нас', width=13)
    portal_settings_button = ClassicButton(master=second_frame, text='Настройки', width=14)
    portal_leave_button = ClassicButton(master=second_frame, text='Выйти', width=14, command=quit)

    def __init__(self):
        super().__init__()
        self.widget_list = [MainUI.main_frame, MainUI.portal_savebox_button, MainUI.first_frame,
                            MainUI.portal_generatepas_button, MainUI.portal_checkpas_button, MainUI.second_frame,
                            MainUI.portal_aboutus_button, MainUI.portal_settings_button, MainUI.portal_leave_button]

    def place(self):
        MainUI.main_frame.place(anchor=CENTER, rely=0.4, relx=0.48125)
        MainUI.portal_savebox_button.pack(pady=2)
        MainUI.first_frame.pack()
        MainUI.portal_generatepas_button.pack(side=LEFT, pady=2, padx=2)
        MainUI.portal_checkpas_button.pack(side=LEFT, pady=2, padx=2)
        MainUI.second_frame.pack()
        MainUI.portal_aboutus_button.pack(side=LEFT, pady=2, padx=2)
        MainUI.portal_settings_button.pack(side=LEFT, pady=2, padx=2)
        MainUI.portal_leave_button.pack(side=LEFT, pady=2, padx=2)

    def place_forget(self):
        MainUI.main_frame.place_forget()


mmenu_interface = MainUI()


