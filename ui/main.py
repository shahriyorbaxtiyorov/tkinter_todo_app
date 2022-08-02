from PIL import Image, ImageTk
from tkinter import Tk, Listbox, Scrollbar
from tkinter.ttk import Label, Button, Entry

from ui.auth import LoginForm, RegisterForm
from ui.settings.main import width, height, x, y


class MainForm(Tk):

    def __init__(self):
        super().__init__()
        # Main Window Settings
        self.title('Todo App')
        self.attributes('-fullscreen', True)
        self.resizable(width=False, height=False)

        # Set Up Background
        self.image = Image.open('ui/img/home.jpg')
        self.image = self.image.resize((800, 500), Image.ANTIALIAS)
        self.tkImage = ImageTk.PhotoImage(
            image=self.image,
            width=800,
            height=500
        )
        self.background = Label(image=self.tkImage)
        self.background.place(x=0, y=0)

        # List box
        self.listbox = Listbox()

        # Scroll Bar
        self.scrollbar = Scrollbar()

        # Settings for listbox and scrollbar
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Logout Button
        self.logout_btn = Button(
            self,
            text='Logout',
            command=lambda: self.logout()
        )
        self.logout_btn.place(
            width=80,
            height=30,
            x=700,
            y=410
        )

    def logout(self):
        self.logout_btn.state(['disabled'])

    def run(self):
        self.mainloop()
