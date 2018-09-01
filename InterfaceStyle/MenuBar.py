# Menubar windows edition
from tkinter import ttk, Frame
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
        self.menu_separator.pack(fill="x", side="bottom")
        self.pack(fill="x", side="top")

    def add_cascade(self, label=""):
        # init style and create button for MenuBar
        style.Theme().menu_btn_style()
        cascade_btn = ttk.Button(self, text=str(label), style="Menu.TButton")

        # pack cascade button on the MenuBar(Frame)
        cascade_btn.pack(side="left")

        # create default binds for cascade button
        cascade_btn.bind('<Enter>', lambda event, root=self.master: events.MenuBarEvents(event, root)
                              .mouse_check_btn(cascade_btn))
        cascade_btn.bind('<Button-1>', lambda event, root=self.master:
                              events.MenuBarEvents(event, root).unfocus_csd_btn(cascade_btn))

        # cascade_btn.bind('<FocusIn>', lambda event, root=self.master)

        return cascade_btn


class MenuFrame(Frame):
    def __init__(self, master=None, button=None):
        super().__init__()
        self.master = master
        self.master.update()
        button.bind('<FocusIn>', lambda event: self.place(x=button.winfo_x(), y=button.winfo_y()+button.winfo_height()-1))
        button.bind('<FocusOut>', lambda event: self.place_forget())

    def add_command(self, label="", command=None):
        # init style and create command button for MenuBarFrame
        style.Theme().menu_frame_btn_style()
        command_btn = ttk.Button(self, text=str(label), style="MenuFrame.TButton")

        # Bind another function on the command button
        if command is not None:
            command_btn.bind('<Button-1>', lambda event: command())

        # pack command button on the SameMenuBar
        command_btn.pack(side="top", fill="x")

        #

