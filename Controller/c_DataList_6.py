# python system
import sys

# pyqt6 plug-in
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# import the entire necessary windows and models.
from View.ui_DataList_6 import *
from Model.m_config_6 import *


class DataList(QWidget):
    _private_result = None  # 結果
    _private_stock_list = None  # 結果

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.ui = Ui_Form_DataList()
        self.ui.setupUi(self)
        self.setWindowTitle(
            f'{ProgramInitualValue.PROGRAM_TITLE} __ {ProgramInitualValue.PROGRAM_VERSION} - 查詢股票詳細數據 ')
        self.show()
        self.ui.de_ToDate.setDate(QDate.currentDate())
        self.ui.de_FromDate.setDate(QDate.currentDate().addDays(-3))
        self.initEvent()

    def initEvent(self):  # 各事件初始化
        self.ui.pb_SearchData.clicked.connect(
            lambda: self.event_DataCalculate())

    def event_DataCalculate(self):  # 計算股票數據
        None
