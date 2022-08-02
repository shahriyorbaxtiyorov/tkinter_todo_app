from tkinter import Tk, Frame
from tkinter.ttk import Label, Button, Entry

from ui.settings.register import width, height, x, y


# Register Window
class RegisterForm(Frame):
    def __init__(self):
        super().__init__()

        # Main Window Settings
        self.title('Register Page')
        self.geometry(f'{width}x{height}+{x}+{y}')
        self.resizable(width=False, height=False)

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

    def run(self):
        self.mainloop()
