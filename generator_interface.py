from widget_classes import *
from other_classes import *

select_number, select_letter, select_gr_letter = IntVar(), IntVar(), IntVar()
select_sm_letter, select_other = IntVar(), IntVar()
select_number.set(1)
select_letter.set(1)
select_gr_letter.set(1)
select_sm_letter.set(1)
select_other.set(1)

select_symbolbet_action = IntVar()
select_symbolbet_action.set(1)

symbolbet = Symbolbet('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*')
required_symbolbet = Symbolbet()
range_len_pas = RangeLen()


class GenUI(UI):
    itog_frame = LabelFrame(text='Меню генератора', font='Helvetica 14')
    generate_pas_entry = ClassicEntry(itog_frame, font='Helvetica 15')
    generate_pas_button = ClassicButton(itog_frame, text='Сгенерировать', width=15, font='Helvetica 12')
    add_pas_storage_button = ClassicButton(itog_frame, text='Добавить в хранилище', width=20, font='Helvetica 12')

    settings_frame = Frame()
    first_frame = Frame(settings_frame)
    work_symbols_frame = LabelFrame(first_frame, text='Взаимодействие с символами', font='Helvetica 11')
    other_frame = LabelFrame(first_frame, text='Прочее', font='Helvetica 11')
    second_frame = Frame(settings_frame)
    select_symbolbet_frame = LabelFrame(second_frame, text='Выбор действия', font='Helvetica 11')
    work_lenrange_frame = LabelFrame(second_frame, text='Диапазон длины', font='Helvetica 11')

    usual_symbolbet_radiobutton = ClassicRadioButton(master=select_symbolbet_frame, text='Обычные символы',
                                                     variable=select_symbolbet_action, value=1)
    required_symbolbet_radiobutton = ClassicRadioButton(master=select_symbolbet_frame, text='Обязательные символы',
                                                        variable=select_symbolbet_action, value=2)

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

    letter_checkbutton = ClassicCheckButton(master=other_frame, text='Буквы', variable=select_letter, width=21)
    gr_letter_checkbutton = ClassicCheckButton(master=other_frame, text='Большие буквы', variable=select_gr_letter,
                                               width=21)
    sm_letter_checkbutton = ClassicCheckButton(master=other_frame, text='Маленькие буквы', variable=select_sm_letter,
                                               width=21)
    number_checkbutton = ClassicCheckButton(master=other_frame, text='Числа', variable=select_number, width=22)
    other_checkbutton = ClassicCheckButton(master=other_frame, text='Остальные', variable=select_other, width=22)
    settings_leave_button = ClassicButton(master=other_frame, text='Выйти', width=20)
    set_default_button = ClassicButton(master=other_frame, text='Сброс Настроек', width=20)
    set_checkpas_settings_button = ClassicButton(master=other_frame, text='Инициализация', width=20)

    def __init__(self):
        super().__init__()
        self.widget_list = [GenUI.itog_frame, GenUI.generate_pas_entry, GenUI.generate_pas_button,
                            GenUI.add_pas_storage_button, GenUI.settings_frame, GenUI.first_frame,
                            GenUI.work_symbols_frame,  GenUI.other_frame, GenUI.second_frame, GenUI.add_symbols_button, GenUI.delete_symbols_button,
                            GenUI.stay_symbols_button, GenUI.get_list_button, GenUI.add_symbols_entry,
                            GenUI.delete_symbols_entry, GenUI.stay_symbols_entry, GenUI.get_list_entry,
                            GenUI.letter_checkbutton, GenUI.gr_letter_checkbutton, GenUI.sm_letter_checkbutton,
                            GenUI.number_checkbutton, GenUI.other_checkbutton, GenUI.settings_leave_button,
                            GenUI.usual_symbolbet_radiobutton, GenUI.required_symbolbet_radiobutton, GenUI.select_range_button, GenUI.get_range_button,
                            GenUI.select_range_entry, GenUI.get_range_entry, GenUI.select_symbolbet_frame,
                            GenUI.work_lenrange_frame, GenUI.set_checkpas_settings_button, GenUI.set_default_button]

    def place(self):
        GenUI.itog_frame.pack()
        GenUI.generate_pas_entry.pack(side=LEFT, padx=3)
        GenUI.generate_pas_button.pack(side=LEFT, padx=3)
        GenUI.add_pas_storage_button.pack(side=LEFT, padx=3)

        GenUI.settings_frame.pack()
        frame_list = [GenUI.first_frame, GenUI.second_frame]
        for e in frame_list:
            e.pack(padx=1, side=LEFT)

        GenUI.work_symbols_frame.pack(pady=3)
        GenUI.other_frame.pack(pady=3)
        first_frame_list = [
            [[GenUI.add_symbols_button, GenUI.delete_symbols_button, GenUI.stay_symbols_button, GenUI.get_list_button],
             [GenUI.add_symbols_entry, GenUI.delete_symbols_entry, GenUI.stay_symbols_entry, GenUI.get_list_entry]],
            [[GenUI.letter_checkbutton, GenUI.gr_letter_checkbutton, GenUI.sm_letter_checkbutton, GenUI.settings_leave_button],
             [GenUI.number_checkbutton, GenUI.other_checkbutton, GenUI.set_default_button, GenUI.set_checkpas_settings_button]]]

        for elem_list in first_frame_list:
            for i in range(len(elem_list)):
                for j in range(len(elem_list[i])):
                    elem_list[i][j].grid(column=i, row=j, pady=1, padx=1)

        GenUI.select_symbolbet_frame.pack(pady=28)
        GenUI.work_lenrange_frame.pack(pady=28)
        second_frame_list = [[[GenUI.usual_symbolbet_radiobutton, GenUI.required_symbolbet_radiobutton]],
                             [[GenUI.select_range_button, GenUI.get_range_button],
                              [GenUI.select_range_entry, GenUI.get_range_entry]]]

        for elem_list in second_frame_list:
            for i in range(len(elem_list)):
                for j in range(len(elem_list[i])):
                    elem_list[i][j].grid(column=i, row=j, pady=1, padx=1)

    def place_forget(self):
        GenUI.itog_frame.pack_forget()
        GenUI.settings_frame.pack_forget()


gen_interface = GenUI()