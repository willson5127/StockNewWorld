# python system
import datetime
import pandas as pd
import numpy as np

# pyqt6 plug-in
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# import the entire necessary windows and models.
from View.ui_TechAnalyze_6 import *
from Model.m_config_6 import *


class TechAnalyze(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.ui = Ui_From_TechAnalyze()
        self.ui.setupUi(self)
        self.setWindowTitle(
            f'{ProgramInitualValue.PROGRAM_TITLE} __ {ProgramInitualValue.PROGRAM_VERSION} - 技術分析 ')
        self.show()
        self.ui.line_StockID.setText('IX0001')
        self.ui.de_ToDate.setDate(QDate.currentDate())
        self.ui.de_FromDate.setDate(QDate.currentDate().addDays(-365))
        self.initPushButtonEvent()

    def initPushButtonEvent(self):
        # Add push button's clicking event
        self.ui.pb_Query.clicked.connect(
            lambda: self.serchStockInfomation())
        self.ui.pb_Reflash.clicked.connect(
            lambda: self.reflashChart())

    def reflashChart(self):  # 重新整理圖表
        self.ui.MplWidget.plotDraw()

    def serchStockInfomation(self):
        None

    def onCheckboxStateChange(self, state, index):
        # 這個函數將在QCheckBox的狀態更改時被調用
        if state:
            self.ui.MplWidget.lines[index].set_visible(True)
        else:
            self.ui.MplWidget.lines[index].set_visible(False)
