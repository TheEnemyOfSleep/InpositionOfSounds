import os, time
from PyQt5.QtWidgets import QWidget, QAction, QTabWidget, QTableWidget, QLabel, \
    QSlider, QPushButton, QSpacerItem, QMainWindow  # import main widgets for app
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout  # import layouts
from PyQt5.QtWidgets import QSizePolicy, QHeaderView, QAbstractItemView, QGraphicsBlurEffect, \
    QGraphicsOpacityEffect, QStyleOptionSlider, QStyle  # import other elements graphics and views
from PyQt5.QtGui import QFontDatabase, QIcon, QPixmap, QMouseEvent
from PyQt5.QtCore import *
from source import events

'Main class for UI'
class MainInterface(QWidget):

    def __init__(self, parent):
        super(MainInterface, self).__init__(parent)
        self.master = parent

        # Init all widgets
        self.init_menu_bar()
        self.init_main_interface_keyboard()

        # Create other frames
        self.TileSettingsSound = TileWindowSettings(self.master)

        # Init styles for all widgets
        self.init_styles()

    def init_styles(self):
        # install custom fonts
        QFontDatabase.addApplicationFont('./interface-stylesheets/interface-element/Fonts/Ubuntu-B.ttf')

        ssh = open('./interface-stylesheets/bluecyan.qss', 'r')
        self.master.setStyleSheet(ssh.read())

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
        self.init_tile_widget()

        main_vbl = QVBoxLayout()

        switch_tabwidget = QTabWidget()
        switch_tabwidget.addTab(self.list_widget, "List")
        switch_tabwidget.addTab(self.tile_widget, "NumPad")

        main_vbl.addWidget(switch_tabwidget)

        self.setLayout(main_vbl)
        self.show()

    def init_list_widget(self):
        list_events = events.ListInterfaceEvent(self.master)

        list_vbl = QVBoxLayout()

        master_btn_frame = QWidget()
        master_btn_frame.setObjectName('MasterBtnsList')
        master_btn_hbl = QHBoxLayout()

        # Add master btns
        add_sound_pbtn = QPushButton()
        add_sound_pbtn.setObjectName('ListBtn')
        add_sound_pbtn.setText("Add new Sound...")

        play_sound_pbtn = QPushButton()
        play_sound_pbtn.setObjectName('PlayBtns')
        play_sound_pbtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        play_sound_pbtn.setIcon(QIcon('./interface-stylesheets/interface-element/play.gif'))
        play_sound_pbtn.clicked.connect(lambda: list_events.switch_play_pbtn(play_sound_pbtn))

        begin_sound_pbtn = QPushButton()
        begin_sound_pbtn.setObjectName('PlayBtns')
        begin_sound_pbtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        begin_sound_pbtn.setIcon(QIcon('./interface-stylesheets/interface-element/end.gif'))

        end_sound_pbtn = QPushButton()
        end_sound_pbtn.setObjectName('PlayBtns')
        end_sound_pbtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        end_sound_pbtn.setIcon(QIcon('./interface-stylesheets/interface-element/begin.gif'))

        m_settings_sound_pbtn = QPushButton()
        m_settings_sound_pbtn.setObjectName('ListBtn')
        m_settings_sound_pbtn.setText('Settings')

        delete_sound_pbtn = QPushButton()
        delete_sound_pbtn.setObjectName('ListBtn')
        delete_sound_pbtn.setText('Remove')

        list_table = QTableWidget()
        list_table.setColumnCount(4)
        list_table.setRowCount(1)

        # Set selections for single row and all columns and delete dotted select row
        list_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        list_table.setSelectionMode(QAbstractItemView.SingleSelection)
        list_table.setFocusPolicy(Qt.NoFocus)

        # Set headers parameter
        list_table.setHorizontalHeaderLabels(['Name', 'Sound Volume', 'Key', 'Settings'])
        list_table.verticalHeader().setVisible(False)

        list_table.verticalHeader().resizeSections(100)

        # Resize header table widget
        list_header = list_table.horizontalHeader()
        list_header.setSectionResizeMode(0, QHeaderView.Stretch)
        list_header.setSectionResizeMode(1, QHeaderView.Stretch)
        list_header.setSectionResizeMode(2, QHeaderView.Fixed)
        list_header.setSectionResizeMode(3, QHeaderView.Fixed)

        list_header.resizeSection(1, 250)
        list_header.resizeSection(2, 120)
        list_header.resizeSection(3, 80)

        """Start test elements"""
        # Name of sounds
        label_name = QLabel()
        label_name.setObjectName('NameLblList')
        label_name.setAlignment(Qt.AlignCenter)
        label_name.setText(str(os.getcwd()))

        # Volume setting slider
        sound_volumme = QVolumeSlider(self.list_widget, self.master, list_table)

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
        settings_sound_pbtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Set widget in the table widget

        list_table.setCellWidget(0, 0, label_name)
        list_table.setCellWidget(0, 1, sound_volumme)
        list_table.setCellWidget(0, 2, label_hotkey)
        list_table.setCellWidget(0, 3, settings_sound_pbtn)
        """End test elements"""

        # Set layouts and add widgets
        master_btn_hbl.addWidget(add_sound_pbtn, 50)
        master_btn_hbl.addWidget(begin_sound_pbtn)
        master_btn_hbl.addWidget(play_sound_pbtn)
        master_btn_hbl.addWidget(end_sound_pbtn)
        master_btn_hbl.addWidget(m_settings_sound_pbtn, 25)
        master_btn_hbl.addWidget(delete_sound_pbtn, 25)

        master_btn_frame.setLayout(master_btn_hbl)

        list_vbl.addWidget(list_table)
        list_vbl.addWidget(master_btn_frame)

        self.list_widget.setLayout(list_vbl)

    def init_tile_widget(self):
        master_layout = QGridLayout()
        nums = 9
        text_labels_list = ['PGUP', 8, 'HOME', 6, None, 4, 'PGDN', 2, 'END']
        num_pads_list = []
        i = 0
        for y in range(0, 3):
            for x in range(3, 0, -1):
                num_pad = NumPadWidget(nums, self)

                num_pads_list.append(num_pad)
                num_pad.set_text_lbl_icons(text_labels_list[i])

                master_layout.addWidget(num_pad.return_widget(), y, x)

                nums -= 1
                i += 1

        del i, nums, text_labels_list
        self.tile_widget.setLayout(master_layout)


# Num pad widget and buttons class
class NumPadWidget(object):
    def __init__(self, nums, parent):
        super().__init__()
        self.nums = nums
        self.parent = parent

        self.tile_events = events.TileInterfaceEvent()
        # Init main widget for master-controlling NumPad
        self.widget = QWidget()
        self.widget.setObjectName('NumPad')
        # Create blur effect for widgets
        self.blur_top_lbl = QGraphicsBlurEffect()
        self.blur_top_lbl.setBlurRadius(0.0)

        self.blur_bottom_lbl = QGraphicsBlurEffect()
        self.blur_bottom_lbl.setBlurRadius(0.0)

        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.0)

        # Create animation classes
        self.blur_anim = QVariantAnimation()
        self.blur_anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.blur_anim.valueChanged.connect(self.play_animation)

        self.opacity_anim = QPropertyAnimation(self.opacity_effect, b'opacity')
        self.opacity_anim.setEasingCurve(QEasingCurve.InOutQuad)

        elements_hbl = QVBoxLayout()

        # Top label of NumPad
        self.top_lbl = QLabel()
        self.top_lbl.setGraphicsEffect(self.blur_top_lbl)
        self.top_lbl.setText(str(nums))
        self.top_lbl.setObjectName('NumPad')
        self.top_lbl.setAlignment(Qt.AlignCenter)

        # Bottom label of NumPad
        self.bottom_lbl = QLabel()
        self.bottom_lbl.setGraphicsEffect(self.blur_bottom_lbl)
        self.bottom_lbl.setObjectName('NumPad')
        self.bottom_lbl.setAlignment(Qt.AlignCenter)

        elements_hbl.addWidget(self.top_lbl, 50)
        elements_hbl.addWidget(self.bottom_lbl, 50)

        self.widget.setLayout(elements_hbl)

        self.create_master_numpad()

        # Events and signals widget
        self.widget.enterEvent = lambda event: self.enter_event()
        self.widget.leaveEvent = lambda event: self.leave_event()

    def create_master_numpad(self):
        self.overlay_widget = QWidget(self.widget)
        self.overlay_widget.setObjectName("OverlayNumPadWidget")

        sound_pbtn_widget = QWidget(self.overlay_widget)
        # sound_pbtn_widget.setAttribute(Qt.WA_TranslucentBackground)

        # NumPad widgets, layouts and items
        sound_name_lbl = QLabel(self.overlay_widget)
        sound_name_lbl.setObjectName('NumPadName')
        sound_name_lbl.setAlignment(Qt.AlignCenter)
        sound_name_lbl.setText('Name of Sound')

        numpad_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        settings_numpad_pbtn = QPushButton(self.overlay_widget)
        settings_numpad_pbtn.setObjectName('NumPad')
        settings_numpad_pbtn.setText('Settings')

        add_numpad_pbtn = QPushButton(self.overlay_widget)
        add_numpad_pbtn.setObjectName('NumPad')
        add_numpad_pbtn.setText('Add Sound')

        remove_numpad_pbtn = QPushButton(self.overlay_widget)
        remove_numpad_pbtn.setObjectName('NumPad')
        remove_numpad_pbtn.setText('Remove Sound')

        # Master sound buttons
        play_sound_pbtn = QPushButton()
        play_sound_pbtn.setObjectName('PlayBtns')
        play_sound_pbtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        play_sound_pbtn.setIcon(QIcon('./interface-stylesheets/interface-element/play.gif'))
        play_sound_pbtn.setAccessibleName('NumPadPushButton_%d' % self.nums)

        begin_sound_pbtn = QPushButton()
        begin_sound_pbtn.setObjectName('PlayBtns')
        begin_sound_pbtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        begin_sound_pbtn.setIcon(QIcon('./interface-stylesheets/interface-element/end.gif'))

        end_sound_pbtn = QPushButton()
        end_sound_pbtn.setObjectName('PlayBtns')
        end_sound_pbtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        end_sound_pbtn.setIcon(QIcon('./interface-stylesheets/interface-element/begin.gif'))

        overlay_pbtn_hbl = QVBoxLayout()
        overlay_pbtn_hbl.setContentsMargins(0, 0, 0, 0)
        overlay_pbtn_hbl.setSpacing(0)

        # Create and set layouts and add widgets
        play_sound_hbl = QHBoxLayout()
        play_sound_hbl.setContentsMargins(0, 0, 0, 0)

        play_sound_hbl.addWidget(begin_sound_pbtn)
        play_sound_hbl.addWidget(play_sound_pbtn)
        play_sound_hbl.addWidget(end_sound_pbtn)

        overlay_pbtn_hbl.addWidget(sound_name_lbl)
        overlay_pbtn_hbl.addItem(numpad_spacer)
        overlay_pbtn_hbl.addWidget(sound_pbtn_widget)
        overlay_pbtn_hbl.addWidget(add_numpad_pbtn)
        overlay_pbtn_hbl.addWidget(remove_numpad_pbtn)
        overlay_pbtn_hbl.addWidget(settings_numpad_pbtn)

        sound_pbtn_widget.setLayout(play_sound_hbl)
        self.overlay_widget.setLayout(overlay_pbtn_hbl)

        # Custom parameters
        self.overlay_widget.setGraphicsEffect(self.opacity_effect)

        # Events and signals widget
        self.widget.resizeEvent = lambda event: self.resize_event()
        play_sound_pbtn.clicked.connect(lambda: self.tile_events.switch_play_pbtn(play_sound_pbtn))
        settings_numpad_pbtn.mousePressEvent = lambda event: self.tile_events.press_settings_buttonEvent(self.parent)

    def set_text_lbl_icons(self, bottom_text_lbl):

        if type(bottom_text_lbl) is str:
            self.bottom_lbl.setText(bottom_text_lbl)
        elif bottom_text_lbl is not None:
            pixmap_lbl = QPixmap('./interface-stylesheets/interface-element/%d_numpad_night.png' % bottom_text_lbl)
            pixmap_lbl.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.bottom_lbl.setPixmap(pixmap_lbl)

    # If mouse pointer on the widget then play animate widget buttons and blur master widget
    def enter_event(self):
        self.blur_anim.setDirection(QPropertyAnimation.Forward)
        self.blur_anim.setDuration(500)
        self.blur_anim.setStartValue(self.blur_top_lbl.blurRadius())
        self.blur_anim.setEndValue(8.0)
        self.blur_anim.start()

        self.opacity_anim.setDirection(QPropertyAnimation.Forward)
        self.opacity_anim.setDuration(500)
        self.opacity_anim.setStartValue(self.opacity_effect.opacity())
        self.opacity_anim.setEndValue(0.6)
        self.opacity_anim.start()

    # If mouse pointer out the widget then play reverse animate widget buttons and unblur master widget
    def leave_event(self):
        self.blur_anim.setDirection(QPropertyAnimation.Backward)
        self.blur_anim.setDuration(500)
        self.blur_anim.setStartValue(0.0)
        self.blur_anim.setEndValue(self.blur_top_lbl.blurRadius())
        self.blur_anim.start()

        self.opacity_anim.setDirection(QPropertyAnimation.Backward)
        self.opacity_anim.setDuration(500)
        self.opacity_anim.setStartValue(0.0)
        self.opacity_anim.setEndValue(self.opacity_effect.opacity())
        self.opacity_anim.start()

    def play_animation(self):
        self.blur_top_lbl.setBlurRadius(self.blur_anim.currentValue())
        self.blur_bottom_lbl.setBlurRadius(self.blur_anim.currentValue())

    def resize_event(self):
        self.overlay_widget.setGeometry(0, 0, self.widget.geometry().width(), self.widget.geometry().height())

    def return_top_lbl(self):
        return self.top_lbl

    def return_bottom_lbl(self):
        return self.bottom_lbl

    def return_widget(self):
        return self.widget


# Create setting window
class TileWindowSettings(QMainWindow):
    def __init__(self, parent, master=None):
        super(TileWindowSettings, self).__init__(parent)
        self.master = master

        self.event_command = events.WindowSettingsEvent()

        self.init_interface()

        self.setMaximumHeight(300)

        self.setObjectName('ChildWindows')
        self.setWindowTitle('NumPad sound settings')

    def init_interface(self):
        master_widget = QWidget()
        master_widget.setObjectName('SettingsWidget')
        master_layout = QGridLayout()
        master_layout.setContentsMargins(0, 20, 0, 0)

        sound_name_lbl = QLabel()
        sound_name_lbl.setText('Name')
        sound_name_lbl.setObjectName('SettingsWidget')
        sound_name_lbl.setAlignment(Qt.AlignCenter)

        settings_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        sound_volume_lbl = QLabel('volume:')
        sound_volume_lbl.setObjectName('SettingsWidgetSub')
        sound_volume_lbl.setAlignment(Qt.AlignCenter)
        sound_volume_lbl.setFixedSize(QSize(140, 22))

        sound_volume_slider = QVolumeSlider(sub_widget=sound_volume_lbl)

        time_lbl = QLabel('0:00')
        time_lbl.setObjectName('SettingsWidgetSub')
        time_lbl.setAlignment(Qt.AlignCenter)
        time_lbl.setFixedSize(QSize(60, 34))

        timeline = SSTimelineSlider()
        timeline.valueChanged.connect(
            lambda: self.event_command.set_lbl_time(timeline, time_lbl, timeline.value()))
        timeline.slider_moved.connect(lambda: self.event_command.event_move_stop_slider())
        timeline.sliderReleased.connect(lambda: self.event_command.update_release_slider(timeline.slider_info_anim))

        start_pbtn = QPushButton()
        start_pbtn.setObjectName('SettingsWidgetIgm')
        start_pbtn.setIcon(QIcon('./interface-stylesheets/interface-element/end.gif'))
        start_pbtn.setToolTip('Beginning start play music')

        backward_pbtn = QPushButton()
        backward_pbtn.setObjectName('SettingsWidgetIgm')
        backward_pbtn.setIcon(QIcon('./interface-stylesheets/interface-element/backward.png'))
        backward_pbtn.setToolTip('Go back 10 seconds')

        play_stop_pbtn = QPushButton()
        play_stop_pbtn.setObjectName('SettingsWidgetIgm')
        play_stop_pbtn.setIcon(QIcon('./interface-stylesheets/interface-element/play.gif'))
        play_stop_pbtn.clicked.connect(lambda: self.event_command.switch_play_pbtn(play_stop_pbtn, timeline,
                                                                                   timeline.slider_info_anim))
        play_stop_pbtn.setToolTip('Play music')

        forward_pbtn = QPushButton()
        forward_pbtn.setObjectName('SettingsWidgetIgm')
        forward_pbtn.setIcon(QIcon('./interface-stylesheets/interface-element/forward.png'))
        forward_pbtn.setToolTip('Go forward 10 seconds')

        repeat_pbtn = QPushButton()
        repeat_pbtn.setObjectName('SettingsWidgetIgm')

        # repeat_palette = repeat_pbtn.palette()
        # repeat_palette.setColor(repeat_pbtn.backgroundRole(), QColor('red'))
        # repeat_pbtn.setPalette(repeat_palette)
        # repeat_pbtn.setAutoFillBackground(True)

        repeat_pbtn.setIcon(QIcon('./interface-stylesheets/interface-element/repeat_night.png'))
        repeat_pbtn.clicked.connect(lambda: self.event_command.switch_repeat_pbtn(repeat_pbtn))

        cancel_pbtn = QPushButton('Cancel')
        cancel_pbtn.setObjectName('SettingsWidget')

        save_pbtn = QPushButton('Save')
        save_pbtn.setObjectName('SettingsWidget')

        master_layout.setHorizontalSpacing(0)
        master_layout.setVerticalSpacing(12)

        master_layout.addWidget(sound_name_lbl, 0, 0, 1, 100)
        # master_layout.addItem(settings_spacer)
        master_layout.addWidget(sound_volume_lbl, 1, 0, 1, 3)
        master_layout.addWidget(sound_volume_slider, 1, 3, 1, 97)

        master_layout.addWidget(timeline, 2, 0, 1, 90)
        master_layout.addWidget(time_lbl, 2, 90, 1, 5)
        master_layout.addWidget(start_pbtn, 2, 95)
        master_layout.addWidget(backward_pbtn, 2, 96)
        master_layout.addWidget(play_stop_pbtn, 2, 97)
        master_layout.addWidget(forward_pbtn, 2, 98)
        master_layout.addWidget(repeat_pbtn, 2, 99)

        master_layout.addWidget(save_pbtn, 3, 0, 1, 50)
        master_layout.setAlignment(save_pbtn, Qt.AlignLeft)
        master_layout.addWidget(cancel_pbtn, 3, 51, 1, 50)

        master_layout.setAlignment(cancel_pbtn, Qt.AlignRight)

        master_widget.setLayout(master_layout)
        self.setCentralWidget(master_widget)


# Sound volume slider class
class QVolumeSlider(QSlider):
    def __init__(self, parent=None, master=None, sub_widget=None):
        super(QVolumeSlider, self).__init__(parent)

        # System variables
        self.l_click = False

        # Another initialization
        self.master = master
        self.sub_widget = sub_widget

        self.setOrientation(Qt.Horizontal)
        self.setObjectName('SoundSettings')
        self.setMinimum(0)
        self.setMaximum(100)
        self.setValue(100)
        self.setTickInterval(1)

        # self.value_lbl = QLabel(str(self.value()), self)
        # self.value_lbl.setObjectName('SoundSettings')

        if str(type(self.sub_widget)) == "<class 'PyQt5.QtWidgets.QTableWidget'>":
            self.valueChanged.connect(self.list_slider_changed)
        elif str(type(self.sub_widget)) == "<class 'PyQt5.QtWidgets.QLabel'>":
            self.valueChanged.connect(self.label_slider_changed)

    def list_slider_changed(self):
        self.sub_widget.setHorizontalHeaderLabels(['Name', str(self.value()), 'Key', 'Settings'])

    def list_slider_release(self):
        self.sub_widget.setHorizontalHeaderLabels(['Name', 'Sound Volume', 'Key', 'Settings'])

    def label_slider_changed(self):
        self.sub_widget.setText(str(self.value()))

    def label_slider_release(self):
        self.sub_widget.setText('volume')

    # Set custom events for slider widget
    def mousePressEvent(self, ev: QMouseEvent):
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        sr = QRect(self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self))
        self.l_click = False
        if ev.button() == Qt.LeftButton and sr.contains(ev.pos()) is False:

            if (ev.button() == Qt.Vertical):
                n_val = self.minimum() + ((self.maximum() - self.minimum()
                                           * (self.height() - ev.y())) / self.height())
            else:
                n_val = self.minimum() + ((self.maximum() - self.minimum())
                                          * ev.x()) / self.width()

            if self.invertedAppearance() is True:
                self.setValue(self.maximum() - n_val)
            else:
                self.setValue(n_val)

            n_val = None
            self.l_click = True
            ev.accept()
        elif ev.button() == Qt.LeftButton:
            self.l_click = True
        else:
            self.l_click = False

    def mouseMoveEvent(self, ev: QMouseEvent):
        if self.l_click:
            if (ev.button() == Qt.Vertical):
                n_val = self.minimum() + ((self.maximum() - self.minimum()
                                           * (self.height() - ev.y())) / self.height())
            else:
                n_val = self.minimum() + ((self.maximum() - self.minimum())
                                          * ev.x()) / self.width()

            if self.invertedAppearance() is True:
                self.setValue(self.maximum() - n_val)
            else:
                self.setValue(n_val)

            n_val = None
            ev.accept()

    def mouseReleaseEvent(self, ev: QMouseEvent):

        if str(type(self.sub_widget)) == "<class 'PyQt5.QtWidgets.QTableWidget'>":
            self.list_slider_release()
        elif str(type(self.sub_widget)) == "<class 'PyQt5.QtWidgets.QLabel'>":
            self.label_slider_release()


# Create Timeline
class SSTimelineSlider(QSlider):
    # System variables
    l_click = False
    slider_released = pyqtSignal(name='sliderReleased')
    slider_moved = pyqtSignal(name='slider_moved')

    def __init__(self, parent=None, master=None):
        super(SSTimelineSlider, self).__init__(parent)

        # Another initialization
        self.master = master

        self.setObjectName('SettingsWidget')

        self.setOrientation(Qt.Horizontal)
        self.setMinimum(0)
        self.setMaximum(120)
        self.setValue(0)
        self.setTickInterval(1)

        self.slider_info_anim = {'duration': (self.maximum() - self.value()) * 1000,
                                 'start': self.value(), 'end': self.maximum()}

    def update_slider_info(self):
        self.slider_info_anim = {'duration': (self.maximum() - self.value()) * 1000,
                                 'start': self.value(), 'end': self.maximum()}
        return self.slider_info_anim

    def mousePressEvent(self, ev: QMouseEvent):
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        sr = QRect(self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self))
        self.l_click = False
        if ev.button() == Qt.LeftButton and sr.contains(ev.pos()) is False:

            if (ev.button() == Qt.Vertical):
                n_val = self.minimum() + ((self.maximum() - self.minimum()
                                           * (self.height() - ev.y())) / self.height())
            else:
                n_val = self.minimum() + ((self.maximum() - self.minimum())
                                          * ev.x()) / self.width()

            if self.invertedAppearance() is True:
                self.setValue(self.maximum() - n_val)
            else:
                self.setValue(n_val)

            n_val = None
            self.l_click = True
            ev.accept()
        elif ev.button() == Qt.LeftButton:
            self.l_click = True
        else:
            self.l_click = False

    def mouseMoveEvent(self, ev: QMouseEvent):
        if self.l_click:
            if (ev.button() == Qt.Vertical):
                n_val = self.minimum() + ((self.maximum() - self.minimum()
                                           * (self.height() - ev.y())) / self.height())
            else:
                n_val = self.minimum() + ((self.maximum() - self.minimum())
                                          * ev.x()) / self.width()

            if self.invertedAppearance() is True:
                self.setValue(self.maximum() - n_val)
                self.slider_moved.emit()
            else:
                self.setValue(n_val)
                self.slider_moved.emit()

            n_val = None
            ev.accept()
        self.update_slider_info()

    def mouseReleaseEvent(self, ev: QMouseEvent):
        self.update_slider_info()
        self.slider_released.emit()
