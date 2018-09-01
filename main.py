from tkinter import Tk
import interface


class Application(Tk):
    def init_ui(self):
        # Create ui form for working and manipulating program
        interface.MainMenu(self)

    def sel_win_style(self):
        # Style parameters for main window
        root_dict = {'relief': "flat", 'bg_window': "#202533"}
        self.configure(background=root_dict['bg_window'], relief=root_dict['relief'])


root = Application()
root.init_ui()
root.sel_win_style()
root.mainloop()


