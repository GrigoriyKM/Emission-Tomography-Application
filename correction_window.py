import os
from PyQt5 import QtWidgets, QtGui, QtCore
from utils import StyledItemDelegate, FileNamesList
import numpy as np
import atexit


class CorrectionWindow(QtWidgets.QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        left, top, height, width = 100, 100, 600, 350
        self.setGeometry(left, top, width, height)
        self.setWindowTitle("Set correction for travel times")
        layout_v = QtWidgets.QVBoxLayout()
        layout_h = QtWidgets.QHBoxLayout()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.add_tool_button = QtWidgets.QToolButton()
        self.add_tool_button.setSizePolicy(sizePolicy)
        add_icon = QtGui.QIcon()
        add_icon.addPixmap(QtGui.QPixmap(":/icons/icons/feather-version-1-1/svg/marquee-434366.svg"),
                           QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
        self.add_tool_button.setIcon(add_icon)
        self.delete_tool_button = QtWidgets.QToolButton()
        self.delete_tool_button.setSizePolicy(sizePolicy)
        delete_icon = QtGui.QIcon()
        delete_icon.addPixmap(QtGui.QPixmap(":/icons/icons/feather-version-1-1/svg/trash-434411.svg"),
                              QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
        self.delete_tool_button.setIcon(delete_icon)
        self.upload_tool_button = QtWidgets.QToolButton()
        self.upload_tool_button.setSizePolicy(sizePolicy)
        upload_icon = QtGui.QIcon()
        upload_icon.addPixmap(QtGui.QPixmap(":/icons/icons/feather-version-1-1/svg/inbox-434350.svg"),
                              QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
        self.upload_tool_button.setIcon(upload_icon)
        self.save_tool_button = QtWidgets.QToolButton()
        self.save_tool_button.setSizePolicy(sizePolicy)
        save_icon = QtGui.QIcon()
        save_icon.addPixmap(QtGui.QPixmap(":/icons/icons/feather-version-1-1/svg/paper-434376.svg"),
                            QtGui.QIcon.Normal,
                            QtGui.QIcon.Off)
        self.save_tool_button.setIcon(save_icon)

        self.set_correction_tool_button = QtWidgets.QToolButton()
        self.set_correction_tool_button.setSizePolicy(sizePolicy)
        set_correction_icon = QtGui.QIcon()
        set_correction_icon.addPixmap(QtGui.QPixmap(":/icons/icons/feather-version-1-1/svg/icons8-done.svg"),
                            QtGui.QIcon.Normal,
                            QtGui.QIcon.Off)
        self.set_correction_tool_button.setIcon(set_correction_icon)

        layout_h.addWidget(self.set_correction_tool_button, 0, QtCore.Qt.AlignLeft)
        layout_h.addWidget(self.save_tool_button, 0, QtCore.Qt.AlignLeft)
        layout_h.addWidget(self.upload_tool_button, 0, QtCore.Qt.AlignLeft)
        layout_h.addWidget(self.add_tool_button, 0, QtCore.Qt.AlignLeft)
        layout_h.addWidget(self.delete_tool_button, 0, QtCore.Qt.AlignLeft)
        spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        layout_h.addSpacerItem(spacer)
        layout_v.addLayout(layout_h)
        self.correction_table = QtWidgets.QTableWidget()
        column_count = 2
        column_header = self.correction_table.horizontalHeader()
        self.delegate = StyledItemDelegate(self.correction_table)
        row_count = 0
        self.correction_table.setColumnCount(column_count)
        self.correction_table.setRowCount(row_count)
        for column_index in range(column_count):
            column_header.setSectionResizeMode(column_index, QtWidgets.QHeaderView.Stretch)
            self.correction_table.setItemDelegateForColumn(column_index, self.delegate)

        self.correction_table.setHorizontalHeaderLabels(['# RECS', 'CORRECTION, ms'])
        layout_v.addWidget(self.correction_table)
        self.setLayout(layout_v)
        self.save_tool_button.setDisabled(True)
        self.delete_tool_button.setDisabled(True)
        self.set_correction_tool_button.setDisabled(True)

    def add_row(self):
        row_index = self.correction_table.rowCount()
        self.correction_table.insertRow(row_index)
        for column_index in range(self.correction_table.columnCount()):
            item = QtWidgets.QTableWidgetItem(None)
            if column_index:
                continue
            self.correction_table.setItem(row_index, column_index, item)
        if self.save_tool_button.isEnabled():
            return
        self.save_tool_button.setEnabled(True)
        self.delete_tool_button.setEnabled(True)
        self.set_correction_tool_button.setEnabled(True)

    def delete_row(self):
        index_list = []
        for model_index in self.correction_table.selectionModel().selectedRows():
            index = QtCore.QPersistentModelIndex(model_index)
            index_list.append(index)
        for index in index_list:
            self.correction_table.removeRow(index.row())
        if self.correction_table.rowCount():
            return
        self.save_tool_button.setDisabled(True)
        self.set_correction_tool_button.setDisabled(True)
        self.delete_tool_button.setDisabled(True)

    def upload_table(self):
        outer_dir = os.path.dirname(os.getcwd())
        file_filter = 'Data File (*.txt)'
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Upload table', outer_dir, filter=file_filter,
                                                          options=QtWidgets.QFileDialog.Options())[0]

        try:
            data = []
            with open(file_name) as f:
                for line in f:
                    (key, val) = line.split()
                    data.append((key, val))
            row_count = self.correction_table.rowCount()
            self.correction_table.setRowCount(row_count + len(data))
            new_row_count = self.correction_table.rowCount()
            for idx, row_index in enumerate(range(row_count, new_row_count)):
                for column_index in range(self.correction_table.columnCount()):
                    item = QtWidgets.QTableWidgetItem(str(data[idx][column_index]))
                    self.correction_table.setItem(row_index, column_index, item)
        except FileNotFoundError:
            pass

        if not self.save_tool_button.isEnabled():
            self.save_tool_button.setEnabled(True)
            self.delete_tool_button.setEnabled(True)
            self.set_correction_tool_button.setEnabled(True)

    def save_table(self):
        outer_dir = os.path.dirname(os.getcwd())
        file_filter = 'Data File (*.txt)'
        file_name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save table', outer_dir, filter=file_filter,
                                                          options=QtWidgets.QFileDialog.Options())[0]
        try:
            with open(file_name, 'w') as f:
                for row_index in range(self.correction_table.rowCount()):
                    for column_index in range(self.correction_table.columnCount()):
                        item = self.correction_table.item(row_index, column_index)
                        f.write(f"{item.text()} ")
                    f.write("\n")
        except FileNotFoundError:
            pass

    def set_correction(self, list_widget):
        data = []

        for row_index in range(self.correction_table.rowCount()):
            try:
                key, val = np.float64(self.correction_table.item(row_index, 0).text()), \
                        np.float64(self.correction_table.item(row_index, 1).text())
            except ValueError:
                continue
            data.append([key, val])
        data = np.array(data)
        if not data.shape[0]:
            return
        corr_travel_times = np.load(FileNamesList.travel_times[list_widget.row(list_widget.currentItem())])
        recs_number = data[:, 0].astype(np.int32)
        for i in range(len(corr_travel_times)):
            corr_travel_times[i][recs_number] = corr_travel_times[i][recs_number] + (data[:, 1] / 1000)

        outer_dir = os.path.dirname(os.getcwd())
        file_filter = 'Data File (*.npy)'
        corr_travel_times_name = \
            QtWidgets.QFileDialog.getSaveFileName(self, 'Save travel times after correction', outer_dir,
                                                  filter=file_filter,
                                                  options=QtWidgets.QFileDialog.Options())[0]
        if len(corr_travel_times_name):
            np.save(corr_travel_times_name, corr_travel_times)
            FileNamesList.travel_times.extend(corr_travel_times_name)
            list_widget.addItem(corr_travel_times_name.split(sep='/')[-1])

    @atexit.register
    def close_window(self):
        self.close()
