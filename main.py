import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import interface
import contextlib
__author__ = "TheEnemyOfSleep"
__version__ = "0.0.1"



class Application(QMainWindow):

    def __init__(self):
        super(Application, self).__init__()
        self.form_widget = interface.MainInterface(self)
        self.init_ui()

        self.setWindowTitle("Sonic")

        #TileWindowSettings(self)

    def init_ui(self):
        # Create ui form for working and manipulating program
        self.setCentralWidget(self.form_widget)


app = QApplication(sys.argv)
root = Application()
root.setGeometry(app.desktop().screenGeometry().width()/3.2, app.desktop().screenGeometry().height()/4, 800, 500)
root.show()
sys.exit(app.exec_())
