# -*- coding:utf-8 -*-
import os
import sys
import subprocess
import os.path

from PyQt4 import QtGui
from PyQt4 import QtCore

class MyWin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)
        self.setWindowTitle("My Window")
        # self.setWindowIcon(QtGui.QIcon('log.png'))

        app_icon = QtGui.QIcon()
        app_icon.addFile('log.png', QtCore.QSize(16,16))
        app_icon.addFile('log.png', QtCore.QSize(24,24))
        app_icon.addFile('log.png', QtCore.QSize(32,32))
        app_icon.addFile('log.png', QtCore.QSize(48,48))
        app_icon.addFile('log.png', QtCore.QSize(256,256))
        self.setWindowIcon(app_icon)

        self.show()

def main(args):
    app = QtGui.QApplication([])

    ww= MyWin()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main(sys.argv[1:])