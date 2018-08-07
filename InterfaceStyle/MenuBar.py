from tkinter import ttk, Frame
from Source import style


class Menu(Frame):
    def __init__(self, master=None):
        self.master = master
        super().__init__()
        self.create_menu_style()

    def create_menu_style(self):
        self.configure(background=style.Theme().get_style_dict()['bg_window'])

    def to_window(self):
        self.pack(fill="x", side="top")

    def add_cascade(self, label=""):
        style.Theme().menu_btn_style()
        self.cascade_btn = ttk.Button(self, text=str(label), style="Menu.TButton")

        self.cascade_btn.pack(side="left")
