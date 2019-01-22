from tkinter import ttk, Menu
from Source import style, sql, events
from InterfaceStyle import MenuBar

'Main class for UI'


class MainMenu:

    def __init__(self, master):
        self.master = master
        self.create_menu()
        'Import modules (style.py, sql.py) by path'

        self.style_dict = style.Theme().get_style_dict()

    def create_menu(self):

        menu = MenuBar.Menu(self.master)
        menu.to_window()
        file = menu.add_cascade(label="File")
        edit = menu.add_cascade(label="Edit")

        menu_file = MenuBar.MenuFrame(self.master, button=file)
        menu_file.add_command(label="New project", command=events.MenuBarEvents().test)
        menu_file.add_separator()
        menu_edit = MenuBar.MenuFrame(self.master, button=edit)
        menu_edit.add_command(label="Preferences")
        create_btn = menu_file.add_command(label="Create")
        import_btn = menu_file.add_command(label="Import")
        export_btn = menu_file.add_command(label="Export")
        menu_file.add_command(label="Quit", command=self.master.quit)

        # Import right menu frame
        import_menu_frame = MenuBar.MenuFrame(self.master, button=import_btn)
        import_menu_frame.add_command(label="Import sound file...")
        import_menu_frame.add_command(label="Import color palette...")
        # Create right menu frame
        side_menu_frm = MenuBar.MenuFrame(self.master, button=create_btn)
        new_file = side_menu_frm.add_command(label="New File")

    def create_entry(self):
        test = ttk.Entry(self.master)
        test.pack()
        test.insert(0, "Label")



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

