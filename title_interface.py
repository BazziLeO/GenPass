from other_classes import *
from widget_classes import *


class TitleUI(UI):
    main_frame = Frame()
    title_name = ClassicLabel(main_frame, text='Genpass 4.0 | Second Step', font='Helvetica 20')
    subtitle_name = ClassicLabel(main_frame, text='Check | Generate | Save')

    def place(self):
        TitleUI.main_frame.pack()
        TitleUI.title_name.pack()
        TitleUI.subtitle_name.pack()

    def place_forget(self):
        TitleUI.main_frame.pack_forget()


title_interface = TitleUI()
