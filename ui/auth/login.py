from tkinter import Tk
from tkinter.ttk import Label, Button, Entry

from ui.settings.login import width, height, x, y


# Login Window
class LoginForm(Tk):
    def __init__(self):
        super().__init__()

        # Main Window Settings
        self.title('Login Page')
        self.geometry(f'{width}x{height}+{x}+{y}')
        self.resizable(width=False, height=False)
