import tkinter as ttk
from tkinter import ttk, Menu

from Source import style, sql
from InterfaceStyle import MenuBar

'Main class for UI'


class MainMenu:

    def __init__(self, master):
        self.master = master
        self.create_menu()
        'Import modules (style.py, sql.py) by path'
        style.Theme()

        self.style_dict = style.Theme().get_style_dict()

    def create_menu(self):
        menu = MenuBar.Menu(self.master)
        menu.to_window()
        menu.add_cascade(label="Уууууеееее")
        menu.add_cascade(label="Новый интерфейс")

    """def create_menu(self):
        # Add default parameter for working
        menu_dict = {'relief': "flat", 'bg_menu': "#202533", 'fg_menu': "#a4a4a5"}

        # Create menu bar
        menu = Menu(self.master, background='#000099', foreground='white',
                    activebackground='#004c99', activeforeground='white')
        print(self.master.config())
        self.master.config(menu=menu)

        file_menu = Menu(menu, tearoff=0)
        file_menu.configure(bg=menu_dict['bg_menu'], relief=menu_dict['relief'], fg=menu_dict['fg_menu'],
                            borderwidth=0)

        menu.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="Create config")
        file_menu.add_command(label="Open config")
        file_menu.add_command(label="Load config")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)"""

