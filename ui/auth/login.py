from tkinter import Tk, Checkbutton, StringVar, W
from tkinter.ttk import Label, Button, Entry, Frame

from ui.settings.login import width, height, x, y


# Login Window
class LoginForm(Frame):
    def __init__(self, container):
        super().__init__(container)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        self.__create_widgets()

    def __create_widgets(self):
        # Username:
        username = StringVar()
        username_label = Label().grid(column=0, row=0)
        username_entry = Entry(self, width=30).grid(column=1, row=0, sticky=W)

        # Password:
        password = StringVar()
        password_label = Label().grid(column=0, row=1)
        password_entry = Entry(self, width=30).grid(column=1, row=2, sticky=W)

        # Login Button
        login_btn = Button().grid()

        # Exit Button
        exit_btn = Button()

    def run(self):
        return self
