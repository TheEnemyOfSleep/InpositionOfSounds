import os
from PyQt5.QtWidgets import QWidget, QAction, QTabWidget, QTableWidget, QHBoxLayout, QVBoxLayout,\
    QHeaderView, QLabel, QSlider, QPushButton, QSizePolicy, QGridLayout, QFrame, QTableView

from PyQt5.QtGui import QFontDatabase, QIcon
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
        # install custom fonts
        QFontDatabase.addApplicationFont('./interface-stylesheets/Fonts/Ubuntu-B.ttf')

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
        self.list_widget.setObjectName('listWidget')
        self.init_list_widget()

        self.tile_widget = QWidget()

        main_vbl = QVBoxLayout()

        switch_tabwidget = QTabWidget()
        switch_tabwidget.addTab(self.list_widget, "List")
        switch_tabwidget.addTab(self.tile_widget, "NumPad")

        main_vbl.addWidget(switch_tabwidget)

        self.setLayout(main_vbl)
        self.show()

    def init_list_widget(self):
        list_vbl = QVBoxLayout()
        master_btn_hbl = QHBoxLayout()

        list_table = QTableWidget()
        list_table.setColumnCount(4)
        list_table.setRowCount(5)
        list_table.setSelectionBehavior(QTableView.SelectRows)
        # Set headers parameter
        list_table.setHorizontalHeaderLabels(['Name', 'Sound Volume', 'Key', 'Settings'])
        list_table.verticalHeader().setVisible(False)

        list_table.verticalHeader().resizeSections(100)

        # Resize header table widget
        list_header = list_table.horizontalHeader()
        list_header.setSectionResizeMode(0, QHeaderView.Stretch)
        list_header.setSectionResizeMode(1, QHeaderView.Fixed)
        list_header.setSectionResizeMode(2, QHeaderView.Fixed)
        list_header.setSectionResizeMode(3, QHeaderView.Fixed)

        list_header.resizeSection(1, 250)
        list_header.resizeSection(2, 120)
        list_header.resizeSection(3, 100)

        # Name of sounds
        label_name = QLabel()
        label_name.setObjectName('NameLblList')
        label_name.setAlignment(Qt.AlignCenter)
        label_name.setText(str(os.getcwd()))

        # Volume setting slider
        master_volumme = QSlider(Qt.Horizontal)
        master_volumme.setMinimum(0)
        master_volumme.setMaximum(100)
        master_volumme.setValue(100)
        master_volumme.setTickInterval(1)

        # Hotkey label
        label_hotkey = QLabel()
        label_hotkey.setObjectName('HotkeyLblList')
        label_hotkey.setAlignment(Qt.AlignCenter)
        label_hotkey.setText('Ctrl+Shift+N')

        settings_hbl = QHBoxLayout()
        settings_hbl.setSpacing(0)

        settings_sound_pbtn = QPushButton()
        settings_sound_pbtn.setObjectName("SoundSettingsButton")
        settings_sound_pbtn.setIcon(QIcon('./interface-stylesheets/interface-element/gear_night.png'))
        settings_sound_pbtn.setIconSize(QSize(24, 24))
        settings_sound_pbtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        list_table.setCellWidget(0, 0, label_name)
        list_table.setCellWidget(0, 1, master_volumme)
        list_table.setCellWidget(0, 2, label_hotkey)
        list_table.setCellWidget(0, 3, settings_sound_pbtn)

        list_vbl.addWidget(list_table)
        self.list_widget.setLayout(list_vbl)

    def init_tile_widget(self):
        pass
