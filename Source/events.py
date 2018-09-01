from tkinter import messagebox, ttk


class MenuBarEvents(object):

    def __init__(self, event=None, master=None):
        self.event = event
        self.master = master

    # If one cascade button in the focus, another csd buttons automatly get focused too(when mouse hover their)
    def mouse_check_btn(self, csd_btn):
        if str(csd_btn.focus_get()).find("!menu.") != -1:
           self.event.widget.focus()

    # Remove focus from cascade button when it focused and click
    def unfocus_csd_btn(self, csd_btn):
        if str(csd_btn.focus_get()) == str(self.event.widget) and str(csd_btn.focus_get()).find("!menu") != -1:
            self.event.widget.configure(takefocus=0)
            self.master.focus_force()
        else:
            self.event.widget.configure(takefocus=1)

    def test(self):
        print("Noice")
