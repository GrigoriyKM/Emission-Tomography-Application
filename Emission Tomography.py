import sys
import os
from ui_interface import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox, QHeaderView
from cohsum.reader.seism.tomography.segy_tomography_seism_reader import SegyTomographySeismReader
from utils import *
import obspy.imaging.mopad_wrapper


class MyAPP(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, flags=QtCore.Qt.Window)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # to load table saved data if exist
        FileNamesList.gathers = []
        FileNamesList.travel_times = []
        FileNamesList.sources = []
        try:
            TableInfo.table_data = np.load('current_tensor_moments.npy')
            TableInfo.check_status = np.load('rows_check_states.npy')
            # to set data to table
            self.set_table_data(TableInfo.table_data, TableInfo.check_status)
            self.save_table_and_update_tensor_moments()
        except FileNotFoundError:
            SummationComponents.enabled_tensor_moments = tensor_moments
            TableInfo.check_status = np.empty(0)
            self.set_table_data(SummationComponents.enabled_tensor_moments, TableInfo.check_status)
        # to upload files to list widgets
        self.ui.gather_load.clicked.connect(self.upload_sgy)
        self.ui.source_coords_load.clicked.connect(self.upload_sc)
        self.ui.travel_times_load.clicked.connect(self.upload_tt)
        # to show and update charts
        self.ui.plot_pushButton.clicked.connect(self.show_charts)
        self.ui.horizontalSlider.valueChanged.connect(self.update_charts_by_t)
        # to enable plotting
        self.ui.gather_listWidget.itemSelectionChanged.connect(self.plot_enable_status_changed)
        self.ui.travel_times_listWidget.itemSelectionChanged.connect(self.plot_enable_status_changed)
        self.ui.sources_coords_listWidget.itemSelectionChanged.connect(self.plot_enable_status_changed)
        # to enable deleting from listWidget
        self.ui.gather_listWidget.itemSelectionChanged.connect(
            lambda: self.del_button_enable_status_changed(self.ui.gather_listWidget, self.ui.gather_del))
        self.ui.travel_times_listWidget.itemSelectionChanged.connect(
            lambda: self.del_button_enable_status_changed(self.ui.travel_times_listWidget, self.ui.travel_times_del))
        self.ui.sources_coords_listWidget.itemSelectionChanged.connect(
            lambda: self.del_button_enable_status_changed(self.ui.sources_coords_listWidget, self.ui.source_coords_del))
        # to delete from listWidget
        self.ui.gather_del.clicked.connect(
            lambda: self.delete_files_from_list_widget(self.ui.gather_listWidget, FileNamesList.gathers))
        self.ui.travel_times_del.clicked.connect(
            lambda: self.delete_files_from_list_widget(self.ui.travel_times_listWidget, FileNamesList.travel_times))
        self.ui.source_coords_del.clicked.connect(
            lambda: self.delete_files_from_list_widget(self.ui.sources_coords_listWidget, FileNamesList.sources))
        # table operations
        self.ui.upload_pushButton.clicked.connect(self.upload_tensor_moments)
        self.ui.add_row_pushButton.clicked.connect(self.add_row)
        self.ui.update_tensor_moments_pushButton.clicked.connect(self.save_table_and_update_tensor_moments)
        self.ui.delete_row_pushButton.clicked.connect(self.delete_row)
        self.ui.select_alltoolButton.clicked.connect(self.set_all_items_checked)
        self.ui.unselect_alltoolButton.clicked.connect(self.set_all_items_unchecked)

    # graphics methods
    def show_charts(self):
        SummationComponents.gather = SegyTomographySeismReader(FileNamesList.gathers).read(
            self.ui.gather_listWidget.row(self.ui.gather_listWidget.currentItem())
        )
        SummationComponents.travel_times = np.load(
            FileNamesList.travel_times[
                self.ui.travel_times_listWidget.row(self.ui.travel_times_listWidget.currentItem())
            ]
        )
        SummationComponents.sources = np.load(
            FileNamesList.sources[
                self.ui.sources_coords_listWidget.row(self.ui.sources_coords_listWidget.currentItem())
            ]
        )
        SummationComponents.receivers = extract_receivers(
            FileNamesList.gathers[self.ui.gather_listWidget.row(self.ui.gather_listWidget.currentItem())]
        )
        SummationComponents.dt = self.ui.dt_spinBox.value() / 1000
        SummationComponents.current_sample = 0
        self.ui.horizontalSlider.setValue(SummationComponents.current_sample)
        SummationComponents.window = self.ui.window_size_spinBox.value()
        SummationComponents.time_in_milliseconds = SummationComponents.current_sample * (SummationComponents.dt * 1000)
        print(SummationComponents.enabled_tensor_moments)
        ChartsInfo.detect_func, SummationComponents.tensor_indexes = et.compute_detect_func_with_focal_mechanisms(
            SummationComponents.gather, SummationComponents.travel_times,
            SummationComponents.sources, SummationComponents.receivers,
            SummationComponents.enabled_tensor_moments, SummationComponents.dt,
            verbose=False, frame_len=SummationComponents.window)
        ChartsInfo.frame_by_t = et.compute_frame(
            SummationComponents.gather, SummationComponents.travel_times,
            SummationComponents.receivers, SummationComponents.sources,
            np.array(SummationComponents.enabled_tensor_moments[
                         SummationComponents.tensor_indexes[SummationComponents.current_sample]]),
            SummationComponents.dt, SummationComponents.time_in_milliseconds, verbose=False,
            frame_len=SummationComponents.window) / SummationComponents.window

        SourcesSurface.sou_x_length = int(
            (np.max(SummationComponents.sources[:, 1]) - np.min(SummationComponents.sources[:, 1])) /
            np.diff(np.unique(SummationComponents.sources[:, 1]))[0]) + 1
        SourcesSurface.sou_y_length = int(
            (np.max(SummationComponents.sources[:, 2]) - np.min(SummationComponents.sources[:, 2])) /
            np.diff(np.unique(SummationComponents.sources[:, 2]))[0]) + 1
        ChartsInfo.n_receivers = SummationComponents.gather.shape[0]
        ChartsInfo.n_samples = SummationComponents.gather.shape[1]
        ChartsInfo.max_ampl_index = np.argmax(ChartsInfo.frame_by_t)
        SourcesSurface.sou_min_x = SummationComponents.sources[:, 2].min()
        SourcesSurface.sou_max_x = SummationComponents.sources[:, 2].max()
        SourcesSurface.sou_min_y = SummationComponents.sources[:, 1].min()
        SourcesSurface.sou_max_y = SummationComponents.sources[:, 1].max()

        ChartsInfo.df = create_data_for_events(SummationComponents.enabled_tensor_moments,
                                               SummationComponents.tensor_indexes, SummationComponents.current_sample,
                                               SummationComponents.time_in_milliseconds, SummationComponents.sources,
                                               ChartsInfo.max_ampl_index)
        if ColorBars.color_bar_count > 0:
            ColorBars.cb1.remove()
            ColorBars.cb2.remove()
        self.ui.horizontalSlider.setMaximum(len(ChartsInfo.detect_func) - 1)
        self.ui.detect_function_spinBox.setMaximum(len(ChartsInfo.detect_func) - 1)
        self.update_gather_chart()
        self.update_detect_function_chart()
        self.update_semblance_chart()
        self.update_tensor_moment_chart()
        self.update_tensor_moments_table_by_t()
        self.ui.horizontalSlider.setEnabled(True)
        self.ui.detect_function_spinBox.setEnabled(True)

    def update_charts_by_t(self):
        SummationComponents.current_sample = self.ui.horizontalSlider.value()
        SummationComponents.time_in_milliseconds = SummationComponents.current_sample * (SummationComponents.dt * 1000)
        ChartsInfo.frame_by_t = et.compute_frame(
            SummationComponents.gather, SummationComponents.travel_times,
            SummationComponents.receivers, SummationComponents.sources,
            np.array(SummationComponents.enabled_tensor_moments[
                         SummationComponents.tensor_indexes[SummationComponents.current_sample]]),
            SummationComponents.dt, SummationComponents.time_in_milliseconds, verbose=False,
            frame_len=SummationComponents.window) / SummationComponents.window
        ChartsInfo.max_ampl_index = np.argmax(ChartsInfo.frame_by_t)
        ChartsInfo.df = create_data_for_events(
            SummationComponents.enabled_tensor_moments, SummationComponents.tensor_indexes,
            SummationComponents.current_sample, SummationComponents.time_in_milliseconds,
            SummationComponents.sources, ChartsInfo.max_ampl_index)
        ColorBars.cb1.remove()
        ColorBars.cb2.remove()
        self.update_gather_chart()
        self.update_detect_function_chart()
        self.update_semblance_chart()
        self.update_tensor_moment_chart()
        self.update_tensor_moments_table_by_t()

    def update_gather_chart(self):
        self.ui.gather_widget.canvas.axes.clear()
        self.ui.gather_widget.canvas.figure.supxlabel('samples')
        self.ui.gather_widget.canvas.figure.supylabel('receivers')
        im = self.ui.gather_widget.canvas.axes.imshow(SummationComponents.gather, cmap='seismic',
                                                      aspect="auto",
                                                      extent=(0, ChartsInfo.n_samples, ChartsInfo.n_receivers, 0))
        ColorBars.cb1 = self.ui.gather_widget.canvas.figure.colorbar(im, location='right')
        # to plot travel_times on gather chart
        self.ui.gather_widget.canvas.axes.plot(
            (SummationComponents.travel_times[ChartsInfo.max_ampl_index] // SummationComponents.dt) -
            np.min(SummationComponents.travel_times[ChartsInfo.max_ampl_index] // SummationComponents.dt) +
            SummationComponents.current_sample, np.arange(0, ChartsInfo.n_receivers, 1)
        )
        ColorBars.color_bar_count += 1
        self.ui.gather_widget.canvas.draw()

    def update_detect_function_chart(self):
        self.ui.detect_function_widget.canvas.axes.clear()
        self.ui.detect_function_widget.canvas.figure.supxlabel('samples')
        self.ui.detect_function_widget.canvas.figure.supylabel('amplitude')
        self.ui.detect_function_widget.canvas.axes.plot(range(len(ChartsInfo.detect_func)),
                                                        ChartsInfo.detect_func / SummationComponents.window)
        self.ui.detect_function_widget.canvas.axes.axvline(SummationComponents.current_sample, ymax=0.99,
                                                           color='red')
        self.ui.detect_function_widget.canvas.axes.set_title(f'Sample = {SummationComponents.current_sample}')
        self.ui.detect_function_widget.canvas.draw()

    def update_semblance_chart(self):
        self.ui.coherent_semblance_widget.canvas.axes.clear()
        im = self.ui.coherent_semblance_widget.canvas.axes.imshow(
            ChartsInfo.frame_by_t.reshape(SourcesSurface.sou_x_length, SourcesSurface.sou_y_length),
            aspect='auto',
            cmap='seismic',
            origin='lower',
            extent=(SourcesSurface.sou_min_x, SourcesSurface.sou_max_x,
                    SourcesSurface.sou_min_y, SourcesSurface.sou_max_y)
        )
        ColorBars.cb2 = self.ui.coherent_semblance_widget.canvas.figure.colorbar(im, location='right')
        self.ui.coherent_semblance_widget.canvas.axes.set_title(f'window = {SummationComponents.window}ms')
        self.ui.coherent_semblance_widget.canvas.axes.plot(
            SummationComponents.sources[ChartsInfo.max_ampl_index][2],
            SummationComponents.sources[ChartsInfo.max_ampl_index][1], 'pg')
        self.ui.coherent_semblance_widget.canvas.draw()

    def update_tensor_moment_chart(self):
        tensor_moment = SummationComponents.enabled_tensor_moments[
            SummationComponents.tensor_indexes[SummationComponents.current_sample]].copy()
        tensor_moment[[3, 5]] = SummationComponents.enabled_tensor_moments[
            SummationComponents.tensor_indexes[SummationComponents.current_sample]][[5, 3]]
        self.ui.tensor_moment_widget.canvas.axes.clear()
        self.ui.tensor_moment_widget.canvas.axes.autoscale()
        self.ui.tensor_moment_widget.canvas.axes.set_axis_off()
        self.ui.tensor_moment_widget.canvas.axes.add_collection(
            obspy.imaging.mopad_wrapper.beach(
                tensor_moment, facecolor='red', axes=self.ui.tensor_moment_widget.canvas.axes))
        self.ui.tensor_moment_widget.canvas.draw()

    def update_tensor_moments_table_by_t(self):
        self.ui.tableWidget.setRowCount(ChartsInfo.df.shape[0])
        self.ui.tableWidget.setColumnCount(ChartsInfo.df.shape[1])
        self.ui.tableWidget.setHorizontalHeaderLabels(ChartsInfo.df.columns)
        for row_index, values in ChartsInfo.df.iterrows():
            for column_index, value in enumerate(values):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row_index, column_index, item)

    # to upload files to list widgets
    def upload_sgy(self):
        cur_dir = os.curdir
        file_filter = 'Data File(s) (*.sgy)'
        current_gathers = QFileDialog.getOpenFileNames(self, 'Load gathers', cur_dir, filter=file_filter,
                                                       options=QFileDialog.Options())[0]
        FileNamesList.gathers.extend(current_gathers)
        for current_gather in current_gathers:
            self.ui.gather_listWidget.addItem(current_gather.split(sep='/')[-1])

    def upload_tt(self):
        cur_dir = os.curdir
        file_filter = 'Data File(s) (*.npy)'
        file_names = QFileDialog.getOpenFileNames(self, 'Load travel times', cur_dir, filter=file_filter,
                                                  options=QFileDialog.Options())[0]
        FileNamesList.travel_times.extend(file_names)
        for file_name in file_names:
            self.ui.travel_times_listWidget.addItem(file_name.split(sep='/')[-1])

    def upload_sc(self):
        cur_dir = os.curdir
        file_filter = 'Data File(s) (*.npy)'
        file_names = QFileDialog.getOpenFileNames(self, 'Load sources coordinates', cur_dir, filter=file_filter,
                                                  options=QFileDialog.Options())[0]
        FileNamesList.sources.extend(file_names)
        for file_name in file_names:
            self.ui.sources_coords_listWidget.addItem(file_name.split(sep='/')[-1])

    # enable status of changed functions
    def plot_enable_status_changed(self):
        if not np.all((
                self.ui.gather_listWidget.count(),
                self.ui.travel_times_listWidget.count(),
                self.ui.sources_coords_listWidget.count()
        )):
            self.ui.plot_pushButton.setDisabled(True)
            self.ui.horizontalSlider.setDisabled(True)
            self.ui.detect_function_spinBox.setDisabled(True)
            return
        if self.ui.update_tensor_moments_pushButton.isEnabled() and np.all((
                np.size(self.ui.gather_listWidget.selectedItems()),
                np.size(self.ui.travel_times_listWidget.selectedItems()),
                np.size(self.ui.sources_coords_listWidget.selectedItems())
        )):
            self.ui.plot_pushButton.setEnabled(True)

    def del_button_enable_status_changed(self, list_widget, del_button):
        if list_widget.count() and len(list_widget.selectedItems()):
            del_button.setEnabled(True)
        else:
            del_button.setDisabled(True)
            self.ui.plot_pushButton.setDisabled(True)

    # to delete files from list widget
    @staticmethod
    def delete_files_from_list_widget(list_widget, file_names_list):
        current_row = list_widget.row(list_widget.currentItem())
        del file_names_list[current_row]
        list_widget.takeItem(current_row)

    def set_table_data(self, tensor_moments_data, first_column_item_check_states):
        row_header = self.ui.tensor_moments_tableWidget.verticalHeader()
        column_header = self.ui.tensor_moments_tableWidget.horizontalHeader()
        row_count = tensor_moments_data.shape[0]
        column_count = tensor_moments_data.shape[1]
        self.ui.tensor_moments_tableWidget.setRowCount(row_count)
        self.ui.tensor_moments_tableWidget.setColumnCount(column_count)
        self.ui.tensor_moments_tableWidget.setHorizontalHeaderLabels(['M11', 'M22', 'M33', 'M23', 'M13', 'M12'])
        # allowing user only digit inputs
        delegate = StyledItemDelegate(self.ui.tensor_moments_tableWidget)
        for column_index in range(column_count):
            column_header.setSectionResizeMode(column_index, QHeaderView.Stretch)
            self.ui.tensor_moments_tableWidget.setItemDelegateForColumn(column_index, delegate)
        # ===========================================
        data_frame = pd.DataFrame(tensor_moments_data, columns=['M11', 'M22', 'M33', 'M23', 'M13', 'M12'])
        for row_index, values in data_frame.iterrows():
            row_header.setSectionResizeMode(row_index, QHeaderView.Stretch)
            if len(first_column_item_check_states) == 0 or first_column_item_check_states[row_index] == 2:
                item = QTableWidgetItem(str(values[0]))
                item.setCheckState(QtCore.Qt.Checked)
                self.ui.tensor_moments_tableWidget.setItem(row_index, 0, item)
            else:
                item = QTableWidgetItem(str(values[0]))
                item.setCheckState(QtCore.Qt.Unchecked)
                self.ui.tensor_moments_tableWidget.setItem(row_index, 0, item)
            for column_index, value in enumerate(values[1::], 1):
                item = QTableWidgetItem(str(value))
                self.ui.tensor_moments_tableWidget.setItem(row_index, column_index, item)

    def add_row(self):
        row_index = self.ui.tensor_moments_tableWidget.rowCount()
        self.ui.tensor_moments_tableWidget.insertRow(row_index)
        for column_index in range(self.ui.tensor_moments_tableWidget.columnCount()):
            item = QTableWidgetItem(None)
            if column_index:
                continue
            item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tensor_moments_tableWidget.setItem(row_index, column_index, item)
        if self.ui.update_tensor_moments_pushButton.isEnabled():
            return
        self.ui.update_tensor_moments_pushButton.setEnabled(True)
        self.ui.delete_row_pushButton.setEnabled(True)

    def delete_row(self):
        row_index = self.ui.tensor_moments_tableWidget.currentRow()
        self.ui.tensor_moments_tableWidget.removeRow(row_index)
        if self.ui.tensor_moments_tableWidget.rowCount():
            return
        self.ui.update_tensor_moments_pushButton.setDisabled(True)
        self.ui.delete_row_pushButton.setDisabled(True)
        if np.any(np.array((self.ui.gather_listWidget.count(),
                            self.ui.travel_times_listWidget.count(),
                            self.ui.sources_coords_listWidget.count()))):
            self.ui.plot_pushButton.setDisabled(True)
            self.ui.horizontalSlider.setDisabled(True)
            self.ui.detect_function_spinBox.setDisabled(True)
        self.save_table_and_update_tensor_moments()

    def save_table_and_update_tensor_moments(self):
        entrance_count = 0
        first_column_index = 0
        current_tensor_moments = []
        rows_check_states = []
        for row_index in range(self.ui.tensor_moments_tableWidget.rowCount()):
            row_data = []
            for column_index in range(self.ui.tensor_moments_tableWidget.columnCount()):
                item = self.ui.tensor_moments_tableWidget.item(row_index, column_index)
                if len(self.ui.tensor_moments_tableWidget.item(row_index, first_column_index).text()) == 0:
                    continue
                if item is None:
                    break
                row_data.append(float(item.text()))
            if len(row_data) == TENSOR_MATRIX_SIZE:
                current_tensor_moments.append(row_data)
                rows_check_states.append(self.ui.tensor_moments_tableWidget.item(row_index, 0).checkState())
            elif rows_check_states[row_index] == CHECKED and entrance_count < 1:
                entrance_count += 1
                msg_box = QMessageBox()
                msg_box.setText('Fill in the blanks!')
                msg_box.setWindowTitle('Emission Tomography')
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setStandardButtons(msg_box.Ok)
                msg_box.exec()
        TableInfo.check_status = np.array(rows_check_states)
        TableInfo.table_data = np.array(current_tensor_moments)
        np.save('current_tensor_moments', TableInfo.table_data)
        np.save('rows_check_states', TableInfo.check_status)
        SummationComponents.enabled_tensor_moments = TableInfo.table_data[TableInfo.check_status == CHECKED]
        self.ui.horizontalSlider.setDisabled(True)
        self.ui.detect_function_spinBox.setDisabled(True)
        if not self.ui.plot_pushButton.isEnabled() and \
                SummationComponents.enabled_tensor_moments.shape[0] and \
                np.all((
                        self.ui.gather_listWidget.count(),
                        self.ui.travel_times_listWidget.count(),
                        self.ui.sources_coords_listWidget.count()
                )):
            self.ui.plot_pushButton.setEnabled(True)

    def upload_tensor_moments(self):
        cur_dir = os.curdir
        file_filter = 'Data File (*.npy)'
        file_name = QFileDialog.getOpenFileName(self, 'Upload tensor moments', cur_dir, filter=file_filter,
                                                options=QFileDialog.Options())[0]
        try:
            uploaded_tensor_moments = np.load(file_name)
            row_count = self.ui.tensor_moments_tableWidget.rowCount()
            self.ui.tensor_moments_tableWidget.setRowCount(row_count + uploaded_tensor_moments.shape[0])
            new_row_count = self.ui.tensor_moments_tableWidget.rowCount()
            for idx, row_index in enumerate(range(row_count, new_row_count)):
                for column_index in range(self.ui.tensor_moments_tableWidget.columnCount()):
                    item = QTableWidgetItem(str(uploaded_tensor_moments[idx][column_index]))
                    if column_index == 0:
                        item.setCheckState(QtCore.Qt.Unchecked)
                    self.ui.tensor_moments_tableWidget.setItem(row_index, column_index, item)
        except FileNotFoundError:
            pass

    def set_all_items_checked(self):
        row_count = self.ui.tensor_moments_tableWidget.rowCount()
        if row_count == 0:
            return
        for row_index in range(row_count):
            if self.ui.tensor_moments_tableWidget.item(row_index, 0).checkState():
                continue
            self.ui.tensor_moments_tableWidget.item(row_index, 0).setCheckState(QtCore.Qt.Checked)

    def set_all_items_unchecked(self):
        row_count = self.ui.tensor_moments_tableWidget.rowCount()
        if row_count == 0:
            return
        for row_index in range(row_count):
            if self.ui.tensor_moments_tableWidget.item(row_index, 0).checkState() == 2:
                self.ui.tensor_moments_tableWidget.item(row_index, 0).setCheckState(QtCore.Qt.Unchecked)


def main():
    app = QApplication(sys.argv)
    with open("Combinear.qss", 'r') as style_sheet_file:
        app.setStyleSheet(style_sheet_file.read())
    window = MyAPP()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
