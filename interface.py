import os
from PyQt5.QtWidgets import QWidget, QAction, qApp, QTabWidget, QVBoxLayout
from PyQt5.QtCore import *
from source import style, sql, events

'Main class for UI'


class MainInterface(QWidget):

    def __init__(self, parent):
        super(MainInterface, self).__init__(parent)
        self.master = parent

        # Init all widgets
        self.init_menu_bar()
        self.init_main_interface_keyboard()

        # Init styles for all widgets
        self.init_styles()

    def init_styles(self):
        ssh = open('./interface-stylesheets/bluecyan.qss', 'r')

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
        new_project_act = QAction('New Project', self)
        new_project_act.setShortcut('Ctrl+N')
        open_project_act = QAction('Open...', self)

        fast_save_projcet_act = QAction('Save', self)
        fast_save_projcet_act.setShortcut('Ctrl+S')
        full_save_project_act = QAction('Save As...', self)
        full_save_project_act.setShortcut('Ctrl+Shift+S')

        pref_act = QAction('Preferences...', self)
        load_factory_act = QAction('Load Factory Settings', self)

        quit_act = QAction('Quit', self)
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
        self.list_widget = QWidget()
        self.tile_widget = QWidget()

        main_vbl = QVBoxLayout()

        switch_tabwidget = QTabWidget()
        switch_tabwidget.addTab(self.list_widget, "List")
        switch_tabwidget.addTab(self.tile_widget, "NumPad")

        main_vbl.addWidget(switch_tabwidget)

        self.setLayout(main_vbl)
        self.show()
