# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmissionTomographyApp.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1278, 916)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/feather-version-1-1/png-48/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_12.addWidget(self.label_15)
        self.window_size_spinBox = QtWidgets.QSpinBox(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.window_size_spinBox.setFont(font)
        self.window_size_spinBox.setToolTip("")
        self.window_size_spinBox.setStyleSheet("border-radius: 2px;\n"
"border-width: 1px;\n"
"border: 1px solid #999999;\n"
"")
        self.window_size_spinBox.setWrapping(False)
        self.window_size_spinBox.setMaximum(500)
        self.window_size_spinBox.setProperty("value", 1)
        self.window_size_spinBox.setObjectName("window_size_spinBox")
        self.horizontalLayout_12.addWidget(self.window_size_spinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, 7)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_22.addWidget(self.label_22)
        self.dt_spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.dt_spinBox.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dt_spinBox.setFont(font)
        self.dt_spinBox.setMouseTracking(False)
        self.dt_spinBox.setStyleSheet("border-radius: 2px;\n"
"border-width: 1px;\n"
"border: 1px solid #999999;")
        self.dt_spinBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dt_spinBox.setAccelerated(False)
        self.dt_spinBox.setPrefix("")
        self.dt_spinBox.setProperty("value", 1)
        self.dt_spinBox.setObjectName("dt_spinBox")
        self.horizontalLayout_22.addWidget(self.dt_spinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_22)
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.gather_load = QtWidgets.QPushButton(self.tab_2)
        self.gather_load.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/feather-version-1-1/svg/inbox-434350.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gather_load.setIcon(icon1)
        self.gather_load.setDefault(False)
        self.gather_load.setObjectName("gather_load")
        self.horizontalLayout_11.addWidget(self.gather_load, 0, QtCore.Qt.AlignRight)
        self.gather_del = QtWidgets.QPushButton(self.tab_2)
        self.gather_del.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gather_del.sizePolicy().hasHeightForWidth())
        self.gather_del.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gather_del.setFont(font)
        self.gather_del.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.gather_del.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/feather-version-1-1/png-48/trash-48x48-434411.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gather_del.setIcon(icon2)
        self.gather_del.setDefault(False)
        self.gather_del.setObjectName("gather_del")
        self.horizontalLayout_11.addWidget(self.gather_del, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.gather_listWidget = QtWidgets.QListWidget(self.tab_2)
        self.gather_listWidget.setStyleSheet("QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListView::item:alternate {\n"
"    background: #EEEEEE;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border: 1px solid #6a6ea9;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
"}")
        self.gather_listWidget.setObjectName("gather_listWidget")
        self.verticalLayout_4.addWidget(self.gather_listWidget)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_14.setSpacing(7)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_14.addWidget(self.label_16)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.travel_times_load = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.travel_times_load.sizePolicy().hasHeightForWidth())
        self.travel_times_load.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.travel_times_load.setFont(font)
        self.travel_times_load.setText("")
        self.travel_times_load.setIcon(icon1)
        self.travel_times_load.setDefault(False)
        self.travel_times_load.setObjectName("travel_times_load")
        self.horizontalLayout_14.addWidget(self.travel_times_load, 0, QtCore.Qt.AlignRight)
        self.travel_times_del = QtWidgets.QPushButton(self.tab_2)
        self.travel_times_del.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.travel_times_del.sizePolicy().hasHeightForWidth())
        self.travel_times_del.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.travel_times_del.setFont(font)
        self.travel_times_del.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/feather-version-1-1/svg/trash-434411.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.travel_times_del.setIcon(icon3)
        self.travel_times_del.setObjectName("travel_times_del")
        self.horizontalLayout_14.addWidget(self.travel_times_del, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.travel_times_listWidget = QtWidgets.QListWidget(self.tab_2)
        self.travel_times_listWidget.setStyleSheet("QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListView::item:alternate {\n"
"    background: #EEEEEE;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border: 1px solid #6a6ea9;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
"}")
        self.travel_times_listWidget.setObjectName("travel_times_listWidget")
        self.verticalLayout_4.addWidget(self.travel_times_listWidget)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_15.setSpacing(7)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_15.addWidget(self.label_17)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.source_coords_load = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_coords_load.sizePolicy().hasHeightForWidth())
        self.source_coords_load.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.source_coords_load.setFont(font)
        self.source_coords_load.setText("")
        self.source_coords_load.setIcon(icon1)
        self.source_coords_load.setObjectName("source_coords_load")
        self.horizontalLayout_15.addWidget(self.source_coords_load, 0, QtCore.Qt.AlignRight)
        self.source_coords_del = QtWidgets.QPushButton(self.tab_2)
        self.source_coords_del.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_coords_del.sizePolicy().hasHeightForWidth())
        self.source_coords_del.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.source_coords_del.setFont(font)
        self.source_coords_del.setText("")
        self.source_coords_del.setIcon(icon3)
        self.source_coords_del.setObjectName("source_coords_del")
        self.horizontalLayout_15.addWidget(self.source_coords_del, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.sources_coords_listWidget = QtWidgets.QListWidget(self.tab_2)
        self.sources_coords_listWidget.setStyleSheet("QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListView::item:alternate {\n"
"    background: #EEEEEE;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border: 1px solid #6a6ea9;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
"}")
        self.sources_coords_listWidget.setObjectName("sources_coords_listWidget")
        self.verticalLayout_4.addWidget(self.sources_coords_listWidget)
        self.plot_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.plot_pushButton.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.plot_pushButton.setFont(font)
        self.plot_pushButton.setStyleSheet("")
        self.plot_pushButton.setObjectName("plot_pushButton")
        self.verticalLayout_4.addWidget(self.plot_pushButton)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.line_6 = QtWidgets.QFrame(self.tab_2)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_10.addWidget(self.line_6)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, -1, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.coherent_semblance_widget = MPLWidget(self.tab_2)
        self.coherent_semblance_widget.setObjectName("coherent_semblance_widget")
        self.gridLayout.addWidget(self.coherent_semblance_widget, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.detect_function_widget = MPLWidget(self.tab_2)
        self.detect_function_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.detect_function_widget.setObjectName("detect_function_widget")
        self.verticalLayout_5.addWidget(self.detect_function_widget)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalSlider = QtWidgets.QSlider(self.tab_2)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_13.addWidget(self.horizontalSlider)
        self.detect_function_spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.detect_function_spinBox.setEnabled(False)
        self.detect_function_spinBox.setStyleSheet("border-radius: 2px;\n"
"border-width: 1px;\n"
"border: 1px solid #999999;")
        self.detect_function_spinBox.setObjectName("detect_function_spinBox")
        self.horizontalLayout_13.addWidget(self.detect_function_spinBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.gridLayout.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        self.gather_widget = MPLWidget(self.tab_2)
        self.gather_widget.setObjectName("gather_widget")
        self.gridLayout.addWidget(self.gather_widget, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.HLine)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(85)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(49)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 1, 1, 1, 1)
        self.horizontalLayout_10.addLayout(self.gridLayout)
        self.horizontalLayout_10.setStretch(2, 3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.frame = QtWidgets.QFrame(self.tab_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tensor_moments_tableWidget = QtWidgets.QTableWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tensor_moments_tableWidget.sizePolicy().hasHeightForWidth())
        self.tensor_moments_tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tensor_moments_tableWidget.setFont(font)
        self.tensor_moments_tableWidget.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tensor_moments_tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tensor_moments_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tensor_moments_tableWidget.setAutoScrollMargin(6)
        self.tensor_moments_tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tensor_moments_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tensor_moments_tableWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tensor_moments_tableWidget.setCornerButtonEnabled(False)
        self.tensor_moments_tableWidget.setColumnCount(0)
        self.tensor_moments_tableWidget.setObjectName("tensor_moments_tableWidget")
        self.tensor_moments_tableWidget.setRowCount(0)
        self.tensor_moments_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tensor_moments_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tensor_moments_tableWidget.verticalHeader().setMinimumSectionSize(31)
        self.tensor_moments_tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tensor_moments_tableWidget.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_7.addWidget(self.tensor_moments_tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.select_alltoolButton = QtWidgets.QToolButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_alltoolButton.sizePolicy().hasHeightForWidth())
        self.select_alltoolButton.setSizePolicy(sizePolicy)
        self.select_alltoolButton.setStyleSheet("")
        self.select_alltoolButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/feather-version-1-1/svg/square-434399.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_alltoolButton.setIcon(icon4)
        self.select_alltoolButton.setObjectName("select_alltoolButton")
        self.horizontalLayout.addWidget(self.select_alltoolButton, 0, QtCore.Qt.AlignBottom)
        self.unselect_alltoolButton = QtWidgets.QToolButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unselect_alltoolButton.sizePolicy().hasHeightForWidth())
        self.unselect_alltoolButton.setSizePolicy(sizePolicy)
        self.unselect_alltoolButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/feather-version-1-1/svg/stop-434405.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unselect_alltoolButton.setIcon(icon5)
        self.unselect_alltoolButton.setObjectName("unselect_alltoolButton")
        self.horizontalLayout.addWidget(self.unselect_alltoolButton, 0, QtCore.Qt.AlignLeft)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_16.addWidget(self.frame)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.update_tensor_moments_pushButton = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_tensor_moments_pushButton.sizePolicy().hasHeightForWidth())
        self.update_tensor_moments_pushButton.setSizePolicy(sizePolicy)
        self.update_tensor_moments_pushButton.setToolTip("")
        self.update_tensor_moments_pushButton.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/feather-version-1-1/svg/repeat-434386.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_tensor_moments_pushButton.setIcon(icon6)
        self.update_tensor_moments_pushButton.setDefault(False)
        self.update_tensor_moments_pushButton.setObjectName("update_tensor_moments_pushButton")
        self.verticalLayout_8.addWidget(self.update_tensor_moments_pushButton, 0, QtCore.Qt.AlignTop)
        self.add_row_pushButton = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_row_pushButton.sizePolicy().hasHeightForWidth())
        self.add_row_pushButton.setSizePolicy(sizePolicy)
        self.add_row_pushButton.setStyleSheet("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/feather-version-1-1/svg/marquee-434366.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_row_pushButton.setIcon(icon7)
        self.add_row_pushButton.setDefault(False)
        self.add_row_pushButton.setObjectName("add_row_pushButton")
        self.verticalLayout_8.addWidget(self.add_row_pushButton, 0, QtCore.Qt.AlignTop)
        self.delete_row_pushButton = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_row_pushButton.sizePolicy().hasHeightForWidth())
        self.delete_row_pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.delete_row_pushButton.setFont(font)
        self.delete_row_pushButton.setStyleSheet("")
        self.delete_row_pushButton.setIcon(icon3)
        self.delete_row_pushButton.setDefault(False)
        self.delete_row_pushButton.setObjectName("delete_row_pushButton")
        self.verticalLayout_8.addWidget(self.delete_row_pushButton, 0, QtCore.Qt.AlignTop)
        self.upload_pushButton = QtWidgets.QPushButton(self.tab_3)
        self.upload_pushButton.setStyleSheet("")
        self.upload_pushButton.setIcon(icon1)
        self.upload_pushButton.setObjectName("upload_pushButton")
        self.verticalLayout_8.addWidget(self.upload_pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.horizontalLayout_16.addLayout(self.verticalLayout_8)
        self.horizontalLayout_16.setStretch(0, 10)
        self.horizontalLayout_16.setStretch(1, 4)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_16)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_9.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.horizontalSlider.valueChanged['int'].connect(self.detect_function_spinBox.setValue)
        self.detect_function_spinBox.valueChanged['int'].connect(self.horizontalSlider.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Emission Tomography"))
        MainWindow.setStatusTip(_translate("MainWindow", "Version 0.1"))
        self.label_15.setText(_translate("MainWindow", "Window size"))
        self.window_size_spinBox.setSuffix(_translate("MainWindow", "ms"))
        self.label_22.setText(_translate("MainWindow", "dt"))
        self.dt_spinBox.setSuffix(_translate("MainWindow", "ms"))
        self.label_14.setText(_translate("MainWindow", "Gathers"))
        self.label_16.setText(_translate("MainWindow", "Travel times"))
        self.label_17.setText(_translate("MainWindow", "Sources coords"))
        self.plot_pushButton.setText(_translate("MainWindow", "plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Processing"))
        self.select_alltoolButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Select All Items</span></p></body></html>"))
        self.unselect_alltoolButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Unselect All Items</span></p></body></html>"))
        self.update_tensor_moments_pushButton.setText(_translate("MainWindow", "save & update"))
        self.add_row_pushButton.setText(_translate("MainWindow", "add"))
        self.delete_row_pushButton.setText(_translate("MainWindow", "delete"))
        self.upload_pushButton.setText(_translate("MainWindow", "upload"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tensor moments"))


from mplwidget import MPLWidget
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
