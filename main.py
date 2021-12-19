import tkinter as tk
from model import Model
from controller import Controller
from view import View


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Python Tkinter MVC Application")

        model = Model("dave@tkinter.net")

        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        controller = Controller(model, view)

        view.set_controller(controller)

if __name__ == "__main__":
    app = App()
    app.mainloop()