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

    # If entered on the rmf button, then add right menu frame
    def forget_all_rmf(self, all_rmf, lvl=None, button=None):
        for rmf in all_rmf:
            # Check lvl rmf for forgetting place
            if lvl+1 is rmf.lvl:
                rmf.place_forget()

    def entered_buttons_mf(self, menu_frame=None, all_rmf=None, lvl=None):
        self.forget_all_rmf(all_rmf, lvl, self.event.widget)
        if lvl is 1:
            menu_frame.place(x=self.event.widget.winfo_x() + self.event.widget.winfo_width() * 1.95,
                             y=self.event.widget.winfo_y() + self.event.widget.winfo_height() * 3)
        else:
            menu_frame.place(x=self.event.widget.winfo_x() + self.event.widget.winfo_width(),
                       y=self.event.widget.winfo_y() + self.event.widget.winfo_height())

    def test(self):
        print("Noice")
