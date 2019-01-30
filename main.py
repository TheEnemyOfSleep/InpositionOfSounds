from tkinter import Tk
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QWidget
import interface

__author__ = "TheEnemyOfSleep"
__version__ = "0.0.2"

class Application(QMainWindow):

    def __init__(self):
        super(Application, self).__init__()
        self.form_widget = interface.MainInterface(self)
        self.init_ui()

        self.setWindowTitle("Sonic")

    def init_ui(self):
        # Create ui form for working and manipulating program
        self.setCentralWidget(self.form_widget)


app = QApplication(sys.argv)
root = Application()
root.show()
sys.exit(app.exec_())


