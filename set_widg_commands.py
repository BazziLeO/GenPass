from set_interface import *
from mainmenu_interface import *
from generator_interface import gen_interface
from title_interface import *
from checkpas_interface import check_interface

def portal_tomain():
    settings_interface.place_forget()
    mmenu_interface.place()

def set_black_theme():
    def set_theme(widget_list):
        if choose_black_theme.get():
            for element in widget_list:
                if type(element).__name__ == 'LabelFrame':
                    element.config(fg='white', bg='gray10')
                elif type(element).__name__ == 'Frame':
                    element.config(bg='gray10')
                elif type(element).__name__ == 'ClassicButton':
                    element.config(fg='white', activeforeground='white', bg='gray21', activebackground='gray20')
                elif type(element).__name__ == 'ClassicLabel':
                    element.config(fg='white', bg='gray10')
                elif type(element).__name__ == 'ClassicEntry':
                    element.config(fg='white', bg='gray19', insertbackground='white')
                elif type(element).__name__ == 'EraseWidget':
                    set_theme(element.get_widgets())
                elif type(element).__name__ == 'ClassicRadioButton' or 'ClassicCheckButton':
                    element.config(fg='white', activeforeground='white', bg='gray10', activebackground='gray10',
                                       selectcolor='gray7')
            root.config(bg='gray10')
        else:
            for element in widget_list:
                if type(element).__name__ == 'LabelFrame':
                    element.config(fg='black', bg='gray94')
                elif type(element).__name__ == 'Frame':
                    element.config(bg='gray94')
                elif type(element).__name__ == 'ClassicButton':
                    element.config(fg='black', bg='gray94')
                elif type(element).__name__ == 'ClassicLabel':
                    element.config(fg='black', bg='gray94')
                elif type(element).__name__ == 'ClassicEntry':
                    element.config(fg='black', bg='white', insertbackground='black')
                elif type(element).__name__ == 'EraseWidget':
                    set_theme(element.get_widgets())
                elif type(element).__name__ == 'ClassicRadioButton' or 'ClassicCheckButton':
                    element.config(fg='black', activeforeground='black', bg='gray94', activebackground='gray94', selectcolor='white')
            root.config(bg='gray94')
    set_theme(gen_interface.get_widgets())
    set_theme(mmenu_interface.get_widgets())
    set_theme(settings_interface.get_widgets())
    set_theme(title_interface.get_widgets())
    set_theme(check_interface.get_widgets())

settings_interface.select_theme_checkbutton['command'] = set_black_theme
settings_interface.leave_button['command'] = portal_tomain