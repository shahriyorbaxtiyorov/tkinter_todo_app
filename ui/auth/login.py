from tkinter import Tk, Checkbutton, StringVar, W
from tkinter.ttk import Label, Button, Entry, Frame, Checkbutton

from ui.settings.login import width, height, x, y


# Login Window
class LoginForm(Frame):
    def __init__(self, container):
        super().__init__(container)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # Username:
        self.username = StringVar()
        self.username_label = Label()
        self.username_entry = Entry(self, width=30)

        # Password:
        self.password = StringVar()
        self.password_label = Label()
        self.password_entry = Entry(self, width=30)

        # Login Button
        self.login_btn = Button()

        # Exit Button
        self.exit_btn = Button()

    def run(self):
        return self