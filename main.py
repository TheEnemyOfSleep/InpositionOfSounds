from tkinter import Tk
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
import interface


class Application(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ImpositionsOfSounds")

    def init_ui(self):
        # Create ui form for working and manipulating program
        form_widget = interface.MainInterface(self)
        self.setCentralWidget(form_widget)

app = QApplication(sys.argv)
root = Application()
root.init_ui()
root.show()
sys.exit(app.exec_())


