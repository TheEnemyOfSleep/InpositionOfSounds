from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon

class MenuBarEvents(object):

    def __init__(self, master=None):
        self.master = master

    def quit_trigger(self):
        qApp.quit()


class ListInterfaceEvent(object):
    play_pbtn = False

    def __init__(self, master=None):
        self.master = master

    def switch_play_pbtn(self, btn):

        if self.play_pbtn is True:

            self.play_pbtn = False
            btn.setIcon(QIcon('./interface-stylesheets/interface-element/play.gif'))
        else:
            self.play_pbtn = True
            btn.setIcon(QIcon('./interface-stylesheets/interface-element/end.gif'))