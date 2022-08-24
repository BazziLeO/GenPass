from mainmenu_interface import *
from checkpas_interface import *
from generator_interface import *


def entry_togenerator():
    mmenu_interface.place_forget()
    gen_interface.place()

def entry_tocheck():
    mmenu_interface.place_forget()
    check_interface.place()

mmenu_interface.portal_generatepas_button['command'] = entry_togenerator
mmenu_interface.portal_checkpas_button['command'] = entry_tocheck