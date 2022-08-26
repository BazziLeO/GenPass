from widget_classes import *
from other_classes import *

choose_black_theme = IntVar()

class SetUI(UI):
    main_frame = Frame()
    portal_autosave_button = ClassicButton(main_frame, text='Настройка автосейва')
    portal_color_button = ClassicButton(main_frame, text='Настройка краски')
    portal_language_button = ClassicButton(main_frame, text='Выбор языка')
    portal_other_button = ClassicButton(main_frame, text='Прочее')
    leave_button = ClassicButton(main_frame, text='Выйти')
    select_theme_checkbutton = ClassicCheckButton(master=main_frame, text='Темная тема', variable=choose_black_theme)

    def __init__(self):
        super().__init__()
        self.widget_list = [SetUI.portal_autosave_button, SetUI.portal_color_button, SetUI.leave_button,
                            SetUI.portal_language_button, SetUI.portal_other_button, SetUI.select_theme_checkbutton, SetUI.main_frame]

    def place(self):
        SetUI.main_frame.place(anchor=CENTER, rely=0.4, relx=0.5)
        packing_portals_list = [[SetUI.portal_autosave_button, SetUI.portal_color_button, SetUI.leave_button],
                                [SetUI.portal_language_button, SetUI.portal_other_button, SetUI.select_theme_checkbutton]]
        for i in range(len(packing_portals_list)):
            for j in range(len(packing_portals_list[i])):
                packing_portals_list[i][j].grid(column=i, row=j, padx=2, pady=1)


    def place_forget(self):
        SetUI.main_frame.place_forget()

settings_interface = SetUI()


