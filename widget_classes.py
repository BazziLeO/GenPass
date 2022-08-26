from root_description import *


class ClassicButton(Button):
    def __init__(self, master=root, text='', width=20, height=1, font='Helvetica 13', command=do_nothing):
        super().__init__(command=command, text=text, master=master, width=width, height=height, font=font)


class ClassicLabel(Label):
    def __init__(self, master=root, text='', font='Helvetica 13'):
        super().__init__(master=master, text=text, font=font)


class ClassicEntry(Entry):
    def __init__(self, master=root, width=20, font='Helvetica 14', cursor='mouse'):
        super().__init__(master=master, width=width, font=font, cursor=cursor)


class ClassicRadioButton(Radiobutton):
    def __init__(self, variable, value, master=root, text='', font='Helvetica 13', width=28, command=do_nothing):
        super().__init__(variable=variable, value=value, command=command, master=master, text=text, width=width, font=font)


class ClassicCheckButton(Checkbutton):
    def __init__(self, variable, master=root, text='', font='Helvetica 11', width=20, command=do_nothing):
        super().__init__(variable=variable, command=command, master=master, text=text, font=font, width=width)


class EraseWidget:
    def __init__(self, master=root, font='Helvetica 11', width=20, distance=2):
        self.frame = Frame(master=master)
        self.eraseentry = ClassicEntry(self.frame, width=width)
        self.erasebutton = ClassicButton(command=lambda: self.eraseentry.delete(0, END), master=self.frame, width=2,
                                         height=1, font=font, text='X')
        self.eraseentry.pack(side=LEFT, padx=distance)
        self.erasebutton.pack(side=LEFT, padx=distance)

    def grid(self, column, row, padx=0, pady=0):
        self.frame.grid(column=column, row=row, padx=padx, pady=pady)

    def pack(self, padx=0, pady=0, side=BOTTOM):
        self.frame.pack(padx=padx, pady=pady, side=side)

    def get(self):
        return self.eraseentry.get()

    def get_widgets(self):
        return [self.frame, self.eraseentry, self.erasebutton]

    def delete(self, index):
        self.eraseentry.delete(index, END)

    def insert(self, index, text):
        self.eraseentry.insert(index, text)

