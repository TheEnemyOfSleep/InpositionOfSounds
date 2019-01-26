from PyQt5.QtWidgets import qApp


class MenuBarEvents(object):

    def __init__(self, master=None):
        self.master = master

    def quit_trigger(self):
        qApp.quit()
