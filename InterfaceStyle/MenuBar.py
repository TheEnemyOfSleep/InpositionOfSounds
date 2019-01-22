# Menubar windows edition
from tkinter import ttk, Frame, PhotoImage
from Source import style, events
import os.path


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

    # Create array right menu frame
    list_rmf = []
    child_list_rmf = []

    # Add all right menu frame
    @classmethod
    def update(cls, lvl, value):
            cls.list_rmf.append(value)
        #print(cls.list_rmf)

    def __init__(self, master=None, button=None):
        super().__init__()
        self.master = master
        self.configure(bd=1)
        self.button = button
        self.lvl = 0

        # if menu button then bottom menu frame
        if str(button).find(".!menu.") is not -1:
            self.lvl = 0

            button.bind('<FocusIn>',
                        lambda event: self.place(x=button.winfo_x(), y=button.winfo_y() + button.winfo_height()-1))
            button.bind('<FocusOut>', lambda event: self.place_forget())

            self.master.bind('<Button-1>', lambda event: self.place_forget())

        # if menu frame button then right menu frame
        elif str(button).find('.!menuframe') is not -1:

            if str(button.master.button).find(".!menuframe") is -1:
                self.lvl = 1
            else:
                self.lvl = 2

            self.update(self.lvl, self)

            button.bind('<Enter>',
                        lambda event, root=self.master:
                        events.MenuBarEvents(event, root).entered_buttons_mf(
                            menu_frame=self, all_rmf=self.list_rmf, lvl=button.master.lvl
                        ))
            button.bind('<Unmap>', lambda event: self.place_forget())

        # print(str(self) + " -> " + str(self.lvl))

    def add_command(self, label="", command=None):
        # arrow_img = Image(file = './Source/InterfaceElement/bitmap.png'
        arrow_photo = PhotoImage(file='./Source/InterfaceElement/arrow.png')

        # init style and create command button for MenuBarFrame
        style.Theme().menu_frame_btn_style()
        command_btn = ttk.Button(self, text=str(label), style="MenuFrame.TButton")
        command_btn.config(image=arrow_photo, compound="right")
        command_btn.image = arrow_photo
        # Bind another function on the command button
        # test github
        if command is not None:
            command_btn.bind('<Button-1>', lambda event: command())

        command_btn.bind('<Enter>', lambda event, root=self.master:
                                    events.MenuBarEvents(events, root).forget_all_rmf(
                                        self.list_rmf, self.lvl, command_btn
                                    ))

        # pack command button on the SameMenuBar
        command_btn.pack(side="top", fill="x")
        return command_btn

    def add_separator(self):
        separator_mf = ttk.Separator(self)
        style.Theme().menu_separate_style(background=style.Theme().get_style_dict()['bg_separator'])
        separator_mf.config(style="Menu.TSeparator")
        separator_mf.pack(side="top", fill="x")