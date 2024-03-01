# python system
import sys

# pyqt6 plug-in
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# import the entire necessary windows and models.
from View.ui_Menu_6 import *
from View.ui_TechAnalyze_6 import *
from Model.m_config_6 import *
from Controller.c_TechAnalyze_6 import *
from Controller.c_BestTrade_6 import *
from Controller.c_DataList_6 import *


class MainWindow(QMainWindow):  # main program entry
    # override the init function
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_Window_Menu()
        self.ui.setupUi(self)
        self.setWindowTitle(
            f'{ProgramInitualValue.PROGRAM_TITLE} __ {ProgramInitualValue.PROGRAM_VERSION} - 功能主選單 ')
        self.initPushButtonEvent()
        self.show()

    def initPushButtonEvent(self):
        # Add link between the MainWindow and SubWindows
        self.ui.pushButton_TechAnalyze.clicked.connect(
            lambda: self.openSubWindow(TechAnalyze()))
        self.ui.pushButton_BestTrade.clicked.connect(
            lambda: self.openSubWindow(BestTrade()))
        self.ui.pushButton_DataList.clicked.connect(
            lambda: self.openSubWindow(DataList()))

    def openSubWindow(self, Window):
        # A common function for open different subWindows
        self.form = QtWidgets.QWidget()
        self.ui = Window
