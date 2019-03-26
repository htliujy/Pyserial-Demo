import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui  import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog

class File_Deal(object):

    def fileSelect(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
        return fname



