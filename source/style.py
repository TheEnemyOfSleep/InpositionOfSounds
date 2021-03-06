from tkinter import ttk, PhotoImage
from tkinter.font import Font

# Theme bluecyan class for change interface


class Theme(ttk.Style):
    def __init__(self, master=None):
        self.master = master
        super(Theme, self).__init__()
        self.style_dict = {'relief': "flat", 'bg_window': "#202533", 'bg_frame': "#181c26",
                           'fg_frame': "#a4a4a5", 'bg_btn_def': "#c8c8c846", 'bg_btn_point': "#ffffff46",
                           'bg_btn_sel': "#32323246", 'bg_separator': "#181b26", 'font_family': "Sans Sherif",
                           'font_size': 8, 'font_weight': "bold", 'selected_bg': "#16a4b5"}

    def menu_separate_style(self, background="#181b26"):
        self.configure("Menu.TSeparator", background=background)

    def menu_btn_style(self, foreground="white", background="#202533", relief="flat",
                       focus_background="#16a4b5", font_family="Sans Sherif", font_size=8, font_weight="bold"):

        # Set flat theme "clam"
        self.theme_use("clam")

        # set configuration for button
        self.configure("Menu.TButton", foreground=foreground, relief=relief, font=(font_family, font_size, font_weight),
                             background=background, width=0, height=0)

        # remove focus ring for button
        self.layout("Menu.TButton", [
            ("Button.focus", None), # Del focus ring
            ("Button.background", {"children": # get children background
                                   [("Button.button", {"children": # get children button
                                                       [("Button.padding", {"children": # get children padding
                                                                            [("Button.label", {"side": "left", "expand": 1})]
                                                                            })]
                                                       })]
                                   })
        ])

        # set background focus color for button
        self.map("Menu.TButton", background=[('focus', focus_background)])

    def menu_frame_main_btn_style(self, foreground="white", background="#202533", relief="flat",
                                  focus_background="#16a4b5"):

        # Set flat theme "clam"
        self.theme_use("clam")

        # set configuration for frame_mainbtns
        self.configure("MenuFrame.TLabel", foreground=foreground, relief=relief, font=("Sans Sherif", 8, "bold"),
                       background=background, anchor='w')

        self.configure("MenuFrame.TFrame", foreground=foreground, relief=relief,
                       background=background)

        self.configure("ActiveMenuFrame.TLabel", foreground=foreground, relief=relief, font=("Sans Sherif", 8, "bold"), background=focus_background)

        self.configure("ActiveMenuFrame.TFrame", foreground=foreground, relief=relief, background=focus_background)

        self.layout("MenuFrame.TLabel", [
            ("Label.focus", None), # Del focus ring
            ("Label.background", {"children": # get children background
                                                       [("Label.padding", {"children": # get children padding
                                                                            [("Label.label", {"side": "left", "expand": 1})]
                                                                            })]
                                   })
        ])

        self.layout("ActiveMenuFrame.TLabel", [
            ("Label.focus", None), # Del focus ring
            ("Label.background", {"children": # get children background
                                                       [("Label.padding", {"children": # get children padding
                                                                            [("Label.label", {"side": "left", "expand": 1})]
                                                                            })]
                                   })
        ])


    def menu_frame_btn_style(self, foreground="white", background="#202533", relief="flat", focus_background="#16a4b5"):

        # Set flat theme "clam"
        self.theme_use("clam")

        # set configuration for button
        self.configure("MenuFrame.TButton", foreground=foreground, relief=relief, font=("Sans Sherif", 8, "bold"),
                             background=background, width=0, height=0, anchor='w')

        self.configure("FocusedMenuFrame.TButton", foreground=foreground, relief=relief, font=("Sans Sherif", 8, "bold"),
                             background=focus_background, width=0, height=0, anchor='w')

        # remove focus ring for button
        self.layout("MenuFrame.TButton", [
            ("Button.focus", None), # Del focus ring
            ("Button.background", {"children": # get children background
                                   [("Button.button", {"children": # get children button
                                                       [("Button.padding", {"children": # get children padding
                                                                            [("Button.label", {"side": "left", "expand": 1})]
                                                                            })]
                                                       })]
                                   })
        ])

        # set background focus color for button
        self.map("MenuFrame.TButton", background=[('active', focus_background)])
        self.map("FocusedMenuFrame.TButton", background=[('active', focus_background)])

    def main_frames(self):
        background_image = PhotoImage(file=
                                      "E:\File\PythonProgramm\ImpositionOfSounds\Reference&Images\FidgetPicture.png")
        self.configure("Tile.MTFrame", background=self.style_dict['bg_frame'], image=background_image)

    def get_style_dict(self):
        return  self.style_dict