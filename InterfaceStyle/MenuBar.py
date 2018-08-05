from tkinter import ttk, Button, Frame, SEPARATOR, Canvas
from Source import style


class Menu(ttk.Frame):
    def __init__(self, master):
        self.master = master
        super(Menu, self).__init__(self.master)
        self.create_menu_style()

    def create_menu_style(self):
        style.Theme().menu_bar_style()
        self.configure(style="Menu.TFrame")

    def to_window(self):
        self.pack(fill="x", side="top")

    def add_cascade(self, label=""):
        style.Theme().menu_btn_style()
        self.cascade_btn = ttk.Button(self, text=str(label), style="Menu.TButton")

        self.cascade_btn.pack(side="left")
