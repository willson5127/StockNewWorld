# python system
import winsound
import pandas as pd

# pyqt6 plug-in
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# import the entire necessary windows and models.
from View.ui_BestTrade_6 import *
from View.v_QtableModel_6 import QpdTableModel
from Model.m_config_6 import *


class BestTrade(QWidget):
    _private_methods = {}   # 公式名稱對照表
    _private_result = None  # 結果

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.ui = Ui_Form_BestTrade()
        self.ui.setupUi(self)
        self.setWindowTitle(
            f'{ProgramInitualValue.PROGRAM_TITLE} __ {ProgramInitualValue.PROGRAM_VERSION} - 最佳交易點 ')
        self.show()
        self.ui.de_ToDate.setDate(QDate.currentDate())
        self.ui.de_FromDate.setDate(QDate.currentDate().addDays(-365))

        self.initEvent()

    def initEvent(self):  # 各事件初始化
        self.ui.pb_SearchStart.clicked.connect(
            lambda: self.event_SearchingBestDeal())
        self.ui.cb_HistorySearching.stateChanged.connect(
            lambda state: self.event_EnableHistorySearch(state=state))
        self.ui.cb_ResultCategory.currentIndexChanged.connect(
            lambda: self.event_ChangedResultCategory())

    def event_EnableHistorySearch(self, state):  # 歷史計算勾選事件
        if state:
            self.ui.de_FromDate.setEnabled(True)
        else:
            self.ui.de_FromDate.setEnabled(False)

    def event_ChangedResultCategory(self):  # 算法下拉選單替換事件
        if self._private_result is not None:
            methodname = self.ui.cb_ResultCategory.currentData()
            if methodname in self._private_result:
                self.ui.model = QpdTableModel(
                    self._private_result[methodname])
                self.ui.tv_ResultBoard.setModel(self.ui.model)
            # else:
            #    blank = pd.DataFrame()
            #    self.ui.model = QpdTableModel(blank)
            #    self.ui.tv_ResultBoard.setModel(self.ui.model)
        else:
            print('Anser is empty!!')

    def event_SearchingBestDeal(self):  # 計算開始按鈕
        frequency = 1000  # 频率（Hz）
        duration = 300  # 持续时间（毫秒）

        print('Analyze Done')
        winsound.Beep(frequency, duration)

        for key, value in self._private_methods.items():
            self.ui.cb_ResultCategory.addItem(value, userData=key)
        self.event_ChangedResultCategory()
