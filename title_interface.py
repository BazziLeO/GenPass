from other_classes import *
from widget_classes import *


class TitleUI(UI):
    main_frame = Frame()
    title_name = ClassicLabel(main_frame, text='Genpass 4.0 | Second Step', font='Helvetica 20')
    subtitle_name = ClassicLabel(main_frame, text='Check | Generate | Save')

    def __init__(self):
        super().__init__()
        self.widget_list = [TitleUI.main_frame, TitleUI.title_name, TitleUI.subtitle_name, TitleUI.main_frame]

    def place(self):
        TitleUI.main_frame.pack()
        TitleUI.title_name.pack()
        TitleUI.subtitle_name.pack()

    def place_forget(self):
        TitleUI.main_frame.pack_forget()


title_interface = TitleUI()
