from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas,  NavigationToolbar2QT as \
    NavigationToolbar
from matplotlib.figure import Figure


class MPLWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure(tight_layout=True))
        self.canvas.setParent(self)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        toolbar = NavigationToolbar(self.canvas, self)
        vertical_layout.addWidget(toolbar)
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
