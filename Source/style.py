from tkinter import ttk, PhotoImage


class Theme:
    def __init__(self, master=None):
        self.master = master
        self.style_dict = {'relief': "flat", 'bg_window': "#202533", 'bg_frame': "#181c26",
                           'fg_frame': "#a4a4a5", 'bg_btn_def': "#c8c8c846", 'bg_btn_point': "#ffffff46",
                           'bg_btn_sel': "#32323246"}
        self.style = ttk.Style()

    def menu_btn_style(self, foreground="white", background="#202533", relief="flat",
                       focus_background="blue"):
        self.style.theme_use("clam")
        self.style.configure("Menu.TButton", foreground=foreground, relief=relief, font=("Sans Sherif", 8, "bold"),
                             background=background)
        self.style.map("Menu.TButton", background=[('focus', focus_background)])

    def main_frames(self):
        background_image = PhotoImage(file=
                                      "E:\File\PythonProgramm\ImpositionOfSounds\Reference&Images\FidgetPicture.png")
        self.style.configure("Tile.MTFrame", background=self.style_dict['bg_frame'], image=background_image)

    def get_style(self):
        return self.style

    def get_style_dict(self):
        return  self.style_dict