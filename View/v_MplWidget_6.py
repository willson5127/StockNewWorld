from PyQt6 import QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt


class MplWidget(QtWidgets.QWidget):  # matplotlib專用物件
    """ 程式註解

        此為 matplotlib 專用物件，副程式功能如下
        1.__init__: 初始化
        2.plotfuc_kBar: 繪製股票期間K線圖
        3.plotset_title: 設定標題
    """

    def __init__(self, parent=None):  # 初始化
        """ 程式註解

            a.定義QT專用matplotlib元件
            b.定義QT專用matplotlib元件的工具欄
            c.新定義垂直畫面布局
            d.設定 matplotlib 圖表呈現數據
            e.設定 matplotlib 工具欄呈現
        """
        super(QtWidgets.QWidget, self).__init__(parent)

        self.canvas = MplCanvas(self)
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        self.setLayout(layout)
        self.lines = []  # 技術分析線圖層

    def plotfuc_kBar(self,  # 技術分析 - K線圖
                     arr_open,  # 開盤矩陣
                     arr_close,  # 收盤矩陣
                     arr_high,  # 最高價
                     arr_low,   # 最低價
                     Dates):  # 日期矩陣
        """ 程式註解

            a.清空圖表

            b.資料匯入(for迴圈,依照日期天數)
                1.上漲 or 下跌
                2.紅k棒 or 綠k棒
                3.k棒高度
                4.底部位置
                5.繪製k棒上下影線
                6.繪製k棒1本體

            c.設定 x 軸的刻度(日期)
            d.設定圖表 最大範圍 & 最小範圍
            e.重新繪製圖表框線
            f.呈現圖表
        """

        for date in range(len(Dates)):
            if arr_close[date] > arr_open[date]:
                color = 'red'
                height = arr_close[date] - arr_open[date]
                bottom = arr_open[date]
            else:
                color = 'limegreen'
                height = arr_open[date] - arr_close[date]
                bottom = arr_close[date]

            self.canvas.ax.vlines(date, arr_high[date], arr_low[date],
                                  linewidth=0.3, color='white')

            self.canvas.ax.bar(date, height=height, bottom=bottom, width=1,
                               linewidth=0.5, edgecolor='white', color=color)

        self.canvas.ax.set_xticks(range(len(Dates)), Dates,
                                  fontsize=8, rotation=75, ha='right')

        self.canvas.ax.set_xlim(left=-1,
                                right=len(Dates))

        self.canvas.ax.set_ylim(float(arr_low.min()) - float(arr_low.min()) * 0.05,
                                float(arr_high.max()) + float(arr_high.max()) * 0.05)

        self.canvas.ax.grid(True, linewidth=0.2)

    def plotset_title(self,  # 設定標題
                      ChName,
                      stock_id,
                      dateST,
                      dateEND):
        self.canvas.ax.set_title(str(ChName) + '(' + str(stock_id) + ')  ' +
                                 str(dateST) + ' ~ ' + str(dateEND))

    def plotClear(self):  # 清空圖表
        self.canvas.ax.clear()
        self.lines.clear()

    def plotDraw(self):  # 繪製圖表
        self.canvas.ax.legend()
        self.canvas.draw()

    def plotget_LegendTexts(self):
        return [text.get_text() for text in self.canvas.ax.legend().get_texts()]

    def plotfuc_line(self,  # 繪製折線圖
                     Data,  # 資料集
                     label,  # 項目名
                     marker,  # 資料點類型
                     markersize,  # 資料點大小
                     linestyle,  # 線段類型
                     linewidth,  # 線寬
                     color):  # 顏色

        self.lines.append(self.canvas.ax.plot(Data, label=label, marker=marker,
                                              markersize=markersize, linestyle=linestyle,
                                              linewidth=linewidth, color=color)[0])


class MplCanvas(FigureCanvas):  # PyQt6的matplotlib物件
    """ 程式註解

        此為 PyQt6的matplotlib 物件，副程式功能如下
        1.__init__: 初始化
    """

    def __init__(self, parent=None):  # 初始化
        """ 程式註解

            a.設定 matplotlib 呈現背景為黑色
            b.定義 matplotlib 圖表
            c.設定網格背景
            d.設定字體,微軟正黑體
            e.初始化 PyQt6 元件
        """
        plt.style.use('dark_background')

        fig, self.ax = plt.subplots()

        plt.grid(True, linewidth=0.2)

        font = FontProperties(fname=r"c:\windows\fonts\msjh.ttc", size=14)
        plt.rcParams["font.family"] = ["Microsoft JhengHei"]

        super().__init__(fig)
