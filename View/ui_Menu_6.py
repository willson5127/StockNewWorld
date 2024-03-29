# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Window_Menu(object):
    def setupUi(self, Window_Menu):
        Window_Menu.setObjectName("Window_Menu")
        Window_Menu.resize(600, 200)
        self.centralwidget = QtWidgets.QWidget(parent=Window_Menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalWidget = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setMinimumSize(QtCore.QSize(350, 40))
        self.horizontalWidget.setAutoFillBackground(False)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_TechAnalyze = QtWidgets.QPushButton(parent=self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_TechAnalyze.sizePolicy().hasHeightForWidth())
        self.pushButton_TechAnalyze.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.pushButton_TechAnalyze.setFont(font)
        self.pushButton_TechAnalyze.setObjectName("pushButton_TechAnalyze")
        self.horizontalLayout.addWidget(self.pushButton_TechAnalyze)
        self.pushButton_BestTrade = QtWidgets.QPushButton(parent=self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_BestTrade.sizePolicy().hasHeightForWidth())
        self.pushButton_BestTrade.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.pushButton_BestTrade.setFont(font)
        self.pushButton_BestTrade.setObjectName("pushButton_BestTrade")
        self.horizontalLayout.addWidget(self.pushButton_BestTrade)
        self.pushButton_DataList = QtWidgets.QPushButton(parent=self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_DataList.sizePolicy().hasHeightForWidth())
        self.pushButton_DataList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.pushButton_DataList.setFont(font)
        self.pushButton_DataList.setObjectName("pushButton_DataList")
        self.horizontalLayout.addWidget(self.pushButton_DataList)
        self.gridLayout.addWidget(self.horizontalWidget, 0, 0, 1, 1)
        Window_Menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window_Menu)
        QtCore.QMetaObject.connectSlotsByName(Window_Menu)

    def retranslateUi(self, Window_Menu):
        _translate = QtCore.QCoreApplication.translate
        Window_Menu.setWindowTitle(_translate("Window_Menu", "MainWindow"))
        self.pushButton_TechAnalyze.setText(_translate("Window_Menu", "技術分析"))
        self.pushButton_BestTrade.setText(_translate("Window_Menu", "最佳交易點清單"))
        self.pushButton_DataList.setText(_translate("Window_Menu", "產品資料分析清單"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window_Menu = QtWidgets.QMainWindow()
    ui = Ui_Window_Menu()
    ui.setupUi(Window_Menu)
    Window_Menu.show()
    sys.exit(app.exec())
