from widget_classes import *
from other_classes import *
allow_number, allow_letter, allow_gr_letter = IntVar(), IntVar(), IntVar()
allow_sm_letter, allow_other = IntVar(), IntVar()
allow_number.set(1)
allow_letter.set(1)
allow_gr_letter.set(1)
allow_sm_letter.set(1)
allow_other.set(1)
select_checksymbolbet_action = IntVar()
select_checksymbolbet_action.set(1)

allowed_symbolbet = Symbolbet('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*')
required_check_symbolbet = Symbolbet()
len_checkpas_range = RangeLen()





class CheckUI(UI):
    main_frame = Frame()
    itog_frame = LabelFrame(main_frame, text='Проверка пароля', font='Helvetica 14')
    check_password_button = ClassicButton(itog_frame, text='Проверить')
    check_password_entry = EraseWidget(itog_frame)
    add_pas_storage_button = ClassicButton(itog_frame, text='Добавить в хранилище', width=20)

    settings_frame = Frame(main_frame)
    first_frame = Frame(settings_frame)
    work_symbols_frame = LabelFrame(first_frame, text='Взаимодействие с символами', font='Helvetica 11')
    other_frame = LabelFrame(first_frame, text='Прочее', font='Helvetica 11')
    second_frame = Frame(settings_frame)
    select_symbolbet_frame = LabelFrame(second_frame, text='Выбор действия', font='Helvetica 11')
    work_lenrange_frame = LabelFrame(second_frame, text='Диапазон длины', font='Helvetica 11')

    allowed_symbolbet_radiobutton = ClassicRadioButton(master=select_symbolbet_frame, text='Разрешенные символы', variable=select_checksymbolbet_action, value=1)
    required_symbolbet_radiobutton = ClassicRadioButton(master=select_symbolbet_frame, text='Обязательные символы', variable=select_checksymbolbet_action, value=2)
    delete_symbols_button = ClassicButton(work_symbols_frame, text='Удалить символы')
    stay_symbols_button = ClassicButton(work_symbols_frame, text='Оставить символы')
    add_symbols_button = ClassicButton(work_symbols_frame, text='Добавить символы')
    get_list_button = ClassicButton(work_symbols_frame, text='Показать список')
    delete_symbols_entry = EraseWidget(work_symbols_frame)
    stay_symbols_entry = EraseWidget(work_symbols_frame)
    add_symbols_entry = EraseWidget(work_symbols_frame)
    get_list_entry = EraseWidget(work_symbols_frame)

    select_range_button = ClassicButton(work_lenrange_frame, text='Определить диапазон')
    get_range_button = ClassicButton(work_lenrange_frame, text='Показать диапазон')
    select_range_entry = EraseWidget(work_lenrange_frame, width=5)
    get_range_entry = EraseWidget(work_lenrange_frame, width=5)

    letter_checkbutton = ClassicCheckButton(master=other_frame, text='Буквы', variable=allow_letter, width=21)
    gr_letter_checkbutton = ClassicCheckButton(master=other_frame, text='Большие буквы', variable=allow_gr_letter, width=21)
    sm_letter_checkbutton = ClassicCheckButton(master=other_frame, text='Маленькие буквы', variable=allow_sm_letter, width=21)
    number_checkbutton = ClassicCheckButton(master=other_frame, text='Числа', variable=allow_number, width=22)
    other_checkbutton = ClassicCheckButton(master=other_frame, text='Остальные', variable=allow_other, width=22)
    set_default_button = ClassicButton(master=other_frame, text='Сброс настроек', width=20)
    set_gen_settings_button = ClassicButton(master=other_frame, text='Инициализация', width=20)
    leave_button = ClassicButton(master=other_frame, text='Выйти', width=20)

    def __init__(self):
        super().__init__()
        self.widget_list = [CheckUI.main_frame, CheckUI.itog_frame, CheckUI.add_pas_storage_button, CheckUI.check_password_button,
                            CheckUI.first_frame, CheckUI.second_frame, CheckUI.add_symbols_button, CheckUI.delete_symbols_button,
                            CheckUI.stay_symbols_button, CheckUI.get_list_button, CheckUI.letter_checkbutton, CheckUI.gr_letter_checkbutton,
                            CheckUI.sm_letter_checkbutton, CheckUI.number_checkbutton, CheckUI.other_checkbutton, CheckUI.leave_button,
                            CheckUI.work_symbols_frame, CheckUI.select_symbolbet_frame, CheckUI.work_lenrange_frame,
                            CheckUI.allowed_symbolbet_radiobutton, CheckUI.required_symbolbet_radiobutton,
                            CheckUI.select_range_button, CheckUI.get_range_button, CheckUI.select_range_entry,
                            CheckUI.get_range_entry, CheckUI.add_symbols_entry, CheckUI.delete_symbols_entry,
                            CheckUI.stay_symbols_entry, CheckUI.get_list_entry, CheckUI.check_password_entry,
                            CheckUI.other_frame, CheckUI.settings_frame, CheckUI.set_default_button, CheckUI.set_gen_settings_button]

    def place(self):
        CheckUI.main_frame.pack()
        CheckUI.itog_frame.pack()
        CheckUI.add_pas_storage_button.pack(side=LEFT, padx=2)
        CheckUI.check_password_button.pack(side=LEFT, padx=2)
        CheckUI.check_password_entry.pack(side=LEFT, padx=2)


        CheckUI.settings_frame.pack()
        frame_list = [CheckUI.first_frame, CheckUI.second_frame]
        for e in frame_list:
            e.pack(padx=1, side=LEFT)

        CheckUI.work_symbols_frame.pack(pady=3)
        CheckUI.other_frame.pack(pady=3)
        first_frame_list = [
            [[CheckUI.add_symbols_button, CheckUI.delete_symbols_button, CheckUI.stay_symbols_button, CheckUI.get_list_button],
             [CheckUI.add_symbols_entry, CheckUI.delete_symbols_entry, CheckUI.stay_symbols_entry, CheckUI.get_list_entry]],
            [[CheckUI.letter_checkbutton, CheckUI.gr_letter_checkbutton, CheckUI.sm_letter_checkbutton, CheckUI.leave_button],
              [CheckUI.number_checkbutton, CheckUI.other_checkbutton, CheckUI.set_default_button, CheckUI.set_gen_settings_button]]]

        for elem_list in first_frame_list:
             for i in range(len(elem_list)):
                 for j in range(len(elem_list[i])):
                  elem_list[i][j].grid(column=i, row=j, pady=1, padx=1)

        CheckUI.select_symbolbet_frame.pack(pady=28)
        CheckUI.work_lenrange_frame.pack(pady=28)
        second_frame_list = [[[CheckUI.allowed_symbolbet_radiobutton, CheckUI.required_symbolbet_radiobutton]],
                              [[CheckUI.select_range_button, CheckUI.get_range_button],
                               [CheckUI.select_range_entry, CheckUI.get_range_entry]]]

        for elem_list in second_frame_list:
            for i in range(len(elem_list)):
                for j in range(len(elem_list[i])):
                    elem_list[i][j].grid(column=i, row=j, pady=1, padx=1)

    def place_forget(self):
        CheckUI.main_frame.pack_forget()


check_interface = CheckUI()
