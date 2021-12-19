import tkinter as tk
from tkinter import ttk

class View:
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label

        self.label = ttk.Label(self, text="Email:")
        self.label.grid(row=1, column=0)

        # email entry
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable = self.email_var, width=30)
        self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # Save button
        self.save_button = ttk.Button(self, text="Save", command=self.save_button.clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        # message
        self.message_label = ttk.Label(self, text="", foreground="red")
        self.message_label.grid(row=2, column=1, sticky=tk.w)

        # set controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def save_button_clicked(self):
        if self.controller:
            self.controller.save(self.email_var.get())

    def show_error(self, message):
        self.message_label["text"] = message
        self.message_label["foreground"] = "red"
        self.message_label.after(3000, self.hide_message)
        self.email_entry["foreground"] = "red"

    def show_success(self, message):
        self.message_label["text"] = message
        self.message_label["foreground"] = "green"
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry["foreground"] = "green"
        self.email_var.set("")

    def hide_message(self):
        self.message_label["text"] = ""