from tkinter import Tk, Listbox, Scrollbar
from tkinter.ttk import Label, Button, Entry

from ui.auth import LoginForm, RegisterForm
from ui.settings.main import width, height, x, y


# Main Window
class App(Tk):
    def __init__(self):
        super().__init__()

        # Main Window Settings
        self.title('Todo App')
        self.geometry(f'{width}x{height}+{x}+{y}')
        self.resizable(width=False, height=False)

        # Buttons foe Auth
        self.login_btn = Button()

        self.register_btn = Button()

        self.logout_btn = Button()

        # List box
        self.listbox = Listbox()

        # Scroll Bar
        self.scrollbar = Scrollbar()

        # Settings for listbox and scrollbar
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

    def login(self):
        LoginForm()

    def register(self):
        RegisterForm()

    def logout(self):
        pass

    def run(self):
        self.mainloop()
