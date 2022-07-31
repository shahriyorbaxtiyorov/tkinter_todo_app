from PIL import Image, ImageTk
from tkinter import Tk, Listbox, Scrollbar
from tkinter.ttk import Label, Button, Entry

from ui.auth import LoginForm, RegisterForm
from ui.settings.home import width, height, x, y


# Main Window
class App(Tk):
    def __init__(self):
        super().__init__()
        # Main Window Settings
        self.title('Todo App')
        self.geometry(f'{width}x{height}+{x}+{y}')
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

        # Buttons foe Auth
        # Login Button
        self.login_btn = Button(
            self,
            text='Login',
            command=lambda: self.login()
        )
        self.login_btn.place(
            width=80,
            height=30,
            x=20,
            y=20
        )

        # Register Button
        self.register_btn = Button(
            self,
            text='Register',
            command=lambda: self.register()
        )
        self.register_btn.place(
            width=80,
            height=30,
            x=225,
            y=245
        )

        # Logout Button
        self.logout_btn = Button(
            self,
            text='Logout',
            command=lambda: self.logout()
        )

        # List box
        self.listbox = Listbox()

        # Scroll Bar
        self.scrollbar = Scrollbar()

        # Settings for listbox and scrollbar
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Exit Button
        self.exit_button = Button(
            self,
            text='Exit',
            command=lambda: self.quit()
        )

        self.exit_button.place(
            width=80,
            height=30,
            x=700,
            y=450
        )

    def login(self):
        self.login_btn.state(['disabled'])
        LoginForm()

    def register(self):
        RegisterForm()

    def logout(self):
        pass

    def run(self):
        self.mainloop()
