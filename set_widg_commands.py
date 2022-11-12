from set_interface import *
from mainmenu_interface import *
from generator_interface import gen_interface
from title_interface import *
from checkpas_interface import check_interface

def portal_tomain():
    settings_interface.place_forget()
    mmenu_interface.place()



settings_interface.leave_button['command'] = portal_tomain