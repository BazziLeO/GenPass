import savebox_password_interface
from mainmenu_interface import *
from checkpas_interface import *
from generator_interface import *
from set_interface import *
from savebox_password_interface import *

def entry_togenerator():
    mmenu_interface.place_forget()
    gen_interface.place()

def entry_tocheck():
    mmenu_interface.place_forget()
    check_interface.place()

def entry_toset():
    mmenu_interface.place_forget()
    settings_interface.place()

def entry_tosavebox():
    mmenu_interface.place_forget()
    savebox_password_frame.pack()

def leave_fromsavebox():
    mmenu_interface.place()
    savebox_password_frame.pack_forget()


mmenu_interface.portal_generatepas_button['command'] = entry_togenerator
mmenu_interface.portal_checkpas_button['command'] = entry_tocheck
mmenu_interface.portal_settings_button['command'] = entry_toset
mmenu_interface.portal_savebox_button["command"] = entry_tosavebox

savebox_password_interface.settings_interface.leave_button["command"] = leave_fromsavebox