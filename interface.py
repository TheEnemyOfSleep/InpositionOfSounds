import os
from PyQt5.QtWidgets import QWidget, QMenuBar, QAction, qApp, QComboBox, QVBoxLayout
from source import style, sql, events

'Main class for UI'


class MainInterface(QWidget):

    def __init__(self, master):
        super(MainInterface, self).__init__(master)
        self.master = master

        # Init all widgets
        self.init_menu_bar()

        # Init styles for all widgets
        self.init_styles()

    def init_styles(self):
        ssh = open('./interface-stylesheets/bluecyan.css', 'r')

        self.master.setStyleSheet(ssh.read())

    def test(self):
        print("Noice")

    def init_menu_bar(self):

        menu_bar_events = events.MenuBarEvents(self.master)

        # Create menu bar
        self.bar = self.master.menuBar()

        # Create root menus
        file = self.bar.addMenu('File')

        # Create action to menus
        new_project_act = QAction('New Project', self.master)
        new_project_act.setShortcut('Ctrl+N')
        open_project_act = QAction('Open...', self.master)

        fast_save_projcet_act = QAction('Save', self.master)
        fast_save_projcet_act.setShortcut('Ctrl+S')
        full_save_project_act = QAction('Save As...', self.master)
        full_save_project_act.setShortcut('Ctrl+Shift+S')

        pref_act = QAction('Preferences...', self.master)
        load_factory_act = QAction('Load Factory Settings', self.master)

        quit_act = QAction('Quit', self.master)
        quit_act.setShortcut('Ctrl+Q')

        # Add actions to menus
        file.addAction(new_project_act)
        file.addAction(open_project_act)

        file.addSeparator()

        file.addAction(fast_save_projcet_act)
        file.addAction(full_save_project_act)

        file.addSeparator()

        file.addAction(pref_act)
        file.addAction(load_factory_act)

        file.addSeparator()

        file.addAction(quit_act)

        # Menu bar events
        quit_act.triggered.connect(lambda: menu_bar_events.quit_trigger())

    def init_main_interface_keyboard(self):

        main_box_layout = QVBoxLayout(self)

        switch_main_interface_cmb = QComboBox()
        switch_main_interface_cmb.addItems("Keyboard", "NumPad")
        main_box_layout.addWidget(switch_main_interface_cmb)
        self.setLayout(main_box_layout)
