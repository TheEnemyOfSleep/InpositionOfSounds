from tkinter import ttk, Frame, messagebox
from Source import style, events



class Menu(Frame):
    def __init__(self, master=None):
        self.master = master
        super().__init__()
        self.create_menu_frame()

    def create_menu_frame(self):
        self.configure(background=style.Theme().get_style_dict()['bg_window'])
        self.menu_separator = ttk.Separator(self)
        style.Theme().menu_separate_style(background=style.Theme().get_style_dict()['bg_separator'])
        self.menu_separator.config(style="Menu.TSeparator")

    def to_window(self):
        self.pack(fill="x", side="top")
        self.menu_separator.pack(fill="x", side="bottom")

    def add_cascade(self, label=""):
        style.Theme().menu_btn_style()
        self.cascade_btn = ttk.Button(self, text=str(label), style="Menu.TButton")
        self.cascade_btn.bind('<FocusOut>', events.MenuBarEvents().mouse_change_btn())
        self.cascade_btn.pack(side="left")
        return self.cascade_btn