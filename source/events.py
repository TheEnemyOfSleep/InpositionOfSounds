from PyQt5.QtWidgets import QPushButton, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QVariantAnimation
from source import media


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
        sound = media.FileSound()

        if self.play_pbtn is True:

            self.play_pbtn = False
            btn.setIcon(QIcon('./interface-stylesheets/interface-element/play.gif'))
            sound.pause_sound()
        else:
            self.play_pbtn = True
            btn.setIcon(QIcon('./interface-stylesheets/interface-element/end.gif'))
            sound.play_sound()


class TileInterfaceEvent(object):
    play_pbtn = False
    active_btn = None

    @classmethod
    def update(cls, btn):
        if cls.play_pbtn is True:
            if cls.active_btn is not None and btn.accessibleName() == cls.active_btn.accessibleName():
                btn.setIcon(QIcon('./interface-stylesheets/interface-element/play.gif'))
                cls.active_btn = None
                cls.play_pbtn = False
            else:
                cls.active_btn.setIcon(QIcon('./interface-stylesheets/interface-element/play.gif'))
                btn.setIcon(QIcon('./interface-stylesheets/interface-element/end.gif'))
                cls.active_btn = btn

        else:
            btn.setIcon(QIcon('./interface-stylesheets/interface-element/end.gif'))
            cls.active_btn = btn
            cls.play_pbtn = True

    def __init__(self, master=None):
        self.master = master

    def switch_play_pbtn(self, btn):
        self.update(btn)

    def press_settings_buttonEvent(self, main_interface):
        main_interface.TileSettingsSound.show()


class WindowSettingsEvent(object):
    play_pbtn = False
    repeat_pbtn = False

    def __init__(self, master=None):
        self.master = master

        # Animation
        self.timeline_info = None
        self.timeline = None
        self.animation = QVariantAnimation()
        self.animation.setProperty('Play', False)
        self.animation.setProperty('MovePlayed', False)
        self.animation.valueChanged.connect(self.play_slider_sound)

    def play_slider_sound(self):
        self.timeline.setValue(self.animation.currentValue())

    def event_play_slider(self):
        if self.animation.property('Play') == True:
            self.animation.stop()
        self.animation.setDuration((self.timeline_info['duration']))
        self.animation.setStartValue(self.timeline_info['start'])
        self.animation.setEndValue(self.timeline_info['end'])
        self.animation.setProperty('Play', True)
        self.animation.start()

    def event_start_paused_animation(self):
        self.animation.start()

    def event_move_stop_slider(self):
        if self.animation.property('Play') is True:
            self.animation.stop()
            self.animation.setProperty('Play', False)
            self.animation.setProperty('MovePlayed', True)

    def switch_play_pbtn(self, btn, timeline, timeline_info):
        self.timeline = timeline

        self.timeline_info = self.timeline.update_slider_info()

        if self.play_pbtn is True:
            self.event_move_stop_slider()
            self.animation.setProperty('MovePlayed', False)
            self.play_pbtn = False
            btn.setIcon(QIcon('./interface-stylesheets/interface-element/play.gif'))
            btn.setToolTip('Play music')
        else:
            self.event_play_slider()
            self.play_pbtn = True
            btn.setIcon(QIcon('./interface-stylesheets/interface-element/end.gif'))
            btn.setToolTip('Stop music')

    def switch_repeat_pbtn(self, btn):

        if self.repeat_pbtn is True:

            self.repeat_pbtn = False
            btn.setStyleSheet("""QPushButton{background: #202533;}
                                 QPushButton:hover{background:  #262B39;}
                                 QPushButton:pressed{background:  #16a4b5;}""")
            btn.setToolTip('Play music')
        else:
            self.repeat_pbtn = True
            btn.setStyleSheet("""QPushButton{background: #16a4b5;}
                                 QPushButton:hover{background:  #2AB8C9;}
                                 QPushButton:pressed{background:  #202533;}""")
            btn.setToolTip('Stop music')

    def set_lbl_time(self, timeline, time_lbl, timeline_val):
        if timeline.value() == timeline.maximum():
            print('Max')
        if timeline_val % 60 < 10:
            time_lbl.setText(str(timeline_val // 60) + ":0" + str(timeline_val % 60))
        else:
            time_lbl.setText(str(timeline_val // 60) + ":" + str(timeline_val % 60))

    def update_release_slider(self, timeline):
        self.timeline_info = timeline
        if self.animation.property('Play') is True or self.animation.property('MovePlayed') is True:
            self.animation.setProperty('MovePlayed', False)
            self.event_play_slider()
        # print(('Duration: ' + str(self.timeline_info['duration']) + '\nStart Value: '
        #       + str(self.timeline_info['start']) + '\nEnd Value: ' + str(self.timeline_info['end'])) + '\n')
