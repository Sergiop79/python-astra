#!/usr/bin/env python
"""
    amixer set Master mute
    amixer set Master unmute
    amixer -c 1 set PCM 2dB+
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):

    def __init__(self, app, parent=None):
        super(Form, self).__init__(parent)

        # PyQT Code
        volumeLabel = QLabel("Volumen")
        self.volumeDial = QDial()
        self.volumeDial.setMinimum(0)
        self.volumeDial.setMaximum(100)
        self.volumePosition = 0

        muteLabel = QLabel("Silencio")
        self.muteCheck = QCheckBox()

        testLabel = QLabel("Test")
        self.testButton = QPushButton('Test')

        self.statusLabel = QLabel("Este es el volumen")

        grid = QGridLayout()
        grid.addWidget(self.statusLabel, 0, 0, 1, 3, alignment=Qt.AlignCenter)
        grid.addWidget(volumeLabel, 1, 0, alignment=Qt.AlignCenter)
        grid.addWidget(muteLabel, 1, 1, alignment=Qt.AlignCenter)
        grid.addWidget(testLabel, 1, 2, alignment=Qt.AlignCenter)
        grid.addWidget(self.volumeDial, 2, 0, alignment=Qt.AlignCenter)
        grid.addWidget(self.muteCheck, 2, 1, alignment=Qt.AlignCenter)
        grid.addWidget(self.testButton, 2, 2, alignment=Qt.AlignCenter)
        self.setLayout(grid)

        self.connect(self.testButton,
                     SIGNAL("pressed()"), self.startTest)

        self.connect(self.testButton,
                     SIGNAL("released()"), self.stopTest)

        self.connect(self.volumeDial,
                     SIGNAL("valueChanged(int)"), self.updateVolume)

        self.connect(app,
                     SIGNAL("lastWindowClosed()"), self.cleanup)

        self.connect(self.muteCheck,
                     SIGNAL("stateChanged(int)"), self.updateMute)

        self.timer = QTimer()
        self.timer.setInterval(500)

        self.connect(self.timer, SIGNAL("timeout()"), self.readStatus)

        self.setWindowTitle("Sonido")

        self.timer.start()

    def startTest(self):
        print "empieza el test"

    def stopTest(self):
        print "termina el test"

    def updateVolume(self):
        position = self.volumeDial.value()
        print "Volumen: %s%%" % position

    def updateMute(self):
        if self.muteCheck.isChecked():
            print "Mute on"
        else:
            print "Mute off"

    def readStatus(self):
        print "read status"
        template = "Volumen: %(volume)s%%  Estado: %(status)s"
        data = {
            'volume': '40',
            'status': 'on'
        }
        self.statusLabel.setText(template % data)

    def cleanup(self):
        print "cleanup"
        QApplication.exit()

app = QApplication(sys.argv)
form = Form(app)
form.show()
app.exec_()
