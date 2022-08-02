from PIL import Image, ImageTk  # type: ignore
from tkinter import Tk, Listbox, Scrollbar
from tkinter.ttk import Label, Button, Entry

from ui.auth import LoginForm, RegisterForm
from ui.settings.home import width, height, x, y, img_width, img_height


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
        self.image = self.image.resize((img_width, img_height), Image.ANTIALIAS)
        self.tkImage = ImageTk.PhotoImage(
            image=self.image,
            width=img_width,
            height=img_height
        )
        self.background = Label(image=self.tkImage)
        self.background.place(x=0, y=0)

        # Login Button
        self.login_btn = Button(
            self,
            text='Login',
            command=lambda: self.login()
        )
        self.login_btn.place(
            width=80,
            height=30,
            x=1300,
            y=570
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
            x=1300,
            y=610
        )

        # Exit Button
        self.exit_button = Button(
            self,
            text='Exit',
            command=lambda: self.quit()
        )
        self.exit_button.place(
            width=80,
            height=30,
            x=1300,
            y=650
        )

    def login(self):
        self.login_btn.state(['disabled'])
        login_form = LoginForm(self).run()
        login_form.place(x=20, y=20)

    def register(self):
        # self.register_btn.state(['disabled'])
        RegisterForm()

    def run(self):
        self.mainloop()
