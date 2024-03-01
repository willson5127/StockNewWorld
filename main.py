import sys

from PyQt6 import QtWidgets

# loading main controller
from Controller.c_MainWindow_6 import MainWindow


def main():  # activate this program
    """
    主程式，使用於啟動程式
    :return: None
    """
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
