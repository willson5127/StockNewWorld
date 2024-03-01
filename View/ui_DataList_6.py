# Form implementation generated from reading ui file 'DataList.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_DataList(object):
    def setupUi(self, Form_DataList):
        Form_DataList.setObjectName("Form_DataList")
        Form_DataList.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        Form_DataList.resize(671, 446)
        Form_DataList.setAutoFillBackground(False)
        Form_DataList.setWindowFilePath("")
        self.gridLayout = QtWidgets.QGridLayout(Form_DataList)
        self.gridLayout.setObjectName("gridLayout")
        self.lw_ListOfStock = QtWidgets.QListWidget(parent=Form_DataList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lw_ListOfStock.sizePolicy().hasHeightForWidth())
        self.lw_ListOfStock.setSizePolicy(sizePolicy)
        self.lw_ListOfStock.setObjectName("lw_ListOfStock")
        self.gridLayout.addWidget(self.lw_ListOfStock, 2, 0, 1, 1)
        self.tv_DataView = QtWidgets.QTableView(parent=Form_DataList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tv_DataView.sizePolicy().hasHeightForWidth())
        self.tv_DataView.setSizePolicy(sizePolicy)
        self.tv_DataView.setObjectName("tv_DataView")
        self.gridLayout.addWidget(self.tv_DataView, 2, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.de_FromDate = QtWidgets.QDateEdit(parent=Form_DataList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.de_FromDate.sizePolicy().hasHeightForWidth())
        self.de_FromDate.setSizePolicy(sizePolicy)
        self.de_FromDate.setObjectName("de_FromDate")
        self.gridLayout_2.addWidget(self.de_FromDate, 2, 1, 1, 1)
        self.lab_StartDate = QtWidgets.QLabel(parent=Form_DataList)
        self.lab_StartDate.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lab_StartDate.setObjectName("lab_StartDate")
        self.gridLayout_2.addWidget(self.lab_StartDate, 2, 0, 1, 1)
        self.pb_ExportExcel = QtWidgets.QPushButton(parent=Form_DataList)
        self.pb_ExportExcel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_ExportExcel.sizePolicy().hasHeightForWidth())
        self.pb_ExportExcel.setSizePolicy(sizePolicy)
        self.pb_ExportExcel.setMinimumSize(QtCore.QSize(100, 0))
        self.pb_ExportExcel.setObjectName("pb_ExportExcel")
        self.gridLayout_2.addWidget(self.pb_ExportExcel, 2, 3, 1, 1)
        self.pb_SearchData = QtWidgets.QPushButton(parent=Form_DataList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_SearchData.sizePolicy().hasHeightForWidth())
        self.pb_SearchData.setSizePolicy(sizePolicy)
        self.pb_SearchData.setMinimumSize(QtCore.QSize(100, 50))
        self.pb_SearchData.setObjectName("pb_SearchData")
        self.gridLayout_2.addWidget(self.pb_SearchData, 0, 3, 1, 1)
        self.lab_ToDate = QtWidgets.QLabel(parent=Form_DataList)
        self.lab_ToDate.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.lab_ToDate.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lab_ToDate.setObjectName("lab_ToDate")
        self.gridLayout_2.addWidget(self.lab_ToDate, 0, 0, 1, 1)
        self.de_ToDate = QtWidgets.QDateEdit(parent=Form_DataList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.de_ToDate.sizePolicy().hasHeightForWidth())
        self.de_ToDate.setSizePolicy(sizePolicy)
        self.de_ToDate.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.de_ToDate.setObjectName("de_ToDate")
        self.gridLayout_2.addWidget(self.de_ToDate, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 2)

        self.retranslateUi(Form_DataList)
        QtCore.QMetaObject.connectSlotsByName(Form_DataList)

    def retranslateUi(self, Form_DataList):
        _translate = QtCore.QCoreApplication.translate
        Form_DataList.setWindowTitle(_translate("Form_DataList", "Form"))
        self.lab_StartDate.setText(_translate("Form_DataList", "查詢起始日:"))
        self.pb_ExportExcel.setText(_translate("Form_DataList", "匯出Excel"))
        self.pb_SearchData.setText(_translate("Form_DataList", "查詢"))
        self.lab_ToDate.setText(_translate("Form_DataList", "查詢截止日:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_DataList = QtWidgets.QWidget()
    ui = Ui_Form_DataList()
    ui.setupUi(Form_DataList)
    Form_DataList.show()
    sys.exit(app.exec())