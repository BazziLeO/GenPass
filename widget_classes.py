from root_description import *


class ClassicButton(Button):
    def __init__(self, master=None, text='', width=20, height=1, font='Helvetica 13', command=None):
        super().__init__(command=command, text=text, master=master, width=width, height=height, font=font)


class ClassicLabel(Label):
    def __init__(self, master=None, text='', font='Helvetica 13'):
        super().__init__(master=master, text=text, font=font)


class ClassicEntry(Entry):
    def __init__(self, master=None, width=20, font='Helvetica 14', cursor='mouse'):
        super().__init__(master=master, width=width, font=font, cursor=cursor)


class ClassicRadioButton(Radiobutton):
    def __init__(self, variable, value=None, master=None, text='', font='Helvetica 13', width=28, command=None):
        super().__init__(variable=variable, value=value, command=command, master=master, text=text, width=width, font=font)


class ClassicCheckButton(Checkbutton):
    def __init__(self, master=None, variable=None, text='', font='Helvetica 11', width=20, command=None):
        super().__init__(variable=variable, command=command, master=master, text=text, font=font, width=width)


class ClassicScale(Scale):
    def __init__(self, master=None, text='', font='Helvetica 12', width=128, from_=0, to=0, orient=HORIZONTAL, command=None):
        super().__init__(master=master, label=text, font=font, length=width, from_=from_, to=to, orient=orient, command=command)


class EraseWidget(Frame):
    def __init__(self, master=root, font='Helvetica 11', width=20, distance=2):
        super().__init__(master=master)
        self.eraseentry = ClassicEntry(self, width=width)
        self.erasebutton = ClassicButton(command=lambda: self.eraseentry.delete(0, END), master=self, width=2,
                                         height=1, font=font, text='X')
        self.eraseentry.pack(side=LEFT, padx=distance)
        self.erasebutton.pack(side=LEFT, padx=distance)

    def get(self):
        return self.eraseentry.get()

    def get_widgets(self):
        return [self.frame, self.eraseentry, self.erasebutton]

    def delete(self, index):
        self.eraseentry.delete(index, END)

    def insert(self, index, text):
        self.eraseentry.insert(index, text)

    def show(self, symbol=""):
        self.eraseentry["show"] = symbol

class Stigma(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.color_point = ClassicLabel(master=self, text="●")
        self.stigma_name = ClassicLabel(master=self, text="Hello world!!!")
        self.color_point.pack(side=LEFT)
        self.stigma_name.pack(side=LEFT)
    def get_widgets(self):
        return [self.color_point, self.stigma_name]


