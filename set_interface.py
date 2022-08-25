from widget_classes import *
from other_classes import *

class SetUI(UI):
    main_frame = Frame()
    portal_autosave_button = ClassicButton(main_frame, text='Настройка автосейва')
    portal_color_button = ClassicButton(main_frame, text='Настройка краски')
    portal_language_button = ClassicButton(main_frame, text='Выбор языка')
    portal_other_button = ClassicButton(main_frame, text='Прочее')
    leave_button = ClassicButton(text='Выйти')

    def place(self):
        SetUI.main_frame.pack()
        packing_portals_list = [[SetUI.portal_autosave_button, SetUI.portal_color_button],
                                [SetUI.portal_language_button, SetUI.portal_other_button]]
        for i in range(len(packing_portals_list)):
            for j in range(len(packing_portals_list[i])):
                packing_portals_list[i][j].grid(column=i, row=j, padx=2, pady=1)
        SetUI.leave_button.pack()

    def place_forget(self):
        SetUI.main_frame.pack_forget()
        SetUI.leave_button.pack_forget()




