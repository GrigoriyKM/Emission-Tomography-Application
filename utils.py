from dataclasses import dataclass, field
from typing import List
import segyio
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from PyQt5 import QtWidgets, QtGui, QtCore
from cohsum.seismic_processing.emission_tomography import EmissionTomography


def parse_trace_headers(segyfile, n_traces):
    """
    Parse the segy file trace headers into a pandas dataframe.
    Column names are defined from segyio internal tracefield
    One row per trace
    """
    # Get all header keys
    headers = segyio.tracefield.keys
    # Initialize dataframe with trace id as index and headers as columns
    df = pd.DataFrame(index=range(1, n_traces + 1),
                      columns=headers.keys())
    # Fill dataframe with all header values
    for k, v in headers.items():
        df[k] = segyfile.attributes(v)[:]
    return df


def extract_receivers(gather_files):
    with segyio.open(gather_files, "r", ignore_geometry=True) as f:
        segy_headers = parse_trace_headers(f, f.tracecount)
    recs = np.vstack([np.zeros(f.tracecount), segy_headers['GroupY'], segy_headers['GroupX']]).T
    return recs


def create_data_for_events(tensor_moments_, tensor_indexes, t, time_in_milliseconds, sources, max_ampl_index):
    current_tensor_moment_list = tensor_moments_[tensor_indexes[int(t)]]
    data = [list(map(lambda cell: float(f'{cell:.3f}'), current_tensor_moment_list)) +
            [float(f'{time_in_milliseconds / 1000:.3f}'), float(f'{sources[max_ampl_index][0]:.2f}'),
             float(f'{sources[max_ampl_index][1]:.2f}'), float(f'{sources[max_ampl_index][2]:.2f}')]]

    df = pd.DataFrame(np.array(data),
                      columns=['M11', 'M22', 'M33', 'M23', 'M13', 'M12', 'SOU_TIME', 'SOU_Z', 'SOU_Y', 'SOU_X'])
    return df


CHECKED = 2
UNCHECKED = 0
TENSOR_MATRIX_SIZE = 6
tensor_moments = np.array([
    [1., 1., 1., 0., 0., 0.],
    [-1., 1., 0., 0., 0., 0.],
    [0., 0., 0., 0., 0., 1.],
    [-0.866, 0.866, 0., -0., -0., 0.5],
    [0., 0., 0., 1., 0., 0.],
    [-1., 0., 1., 0., 0., 0.],
    [0., 0., 0., 0., 1., 0.],
])

et = EmissionTomography()


@dataclass
class FileNamesList:
    gathers: List[str] = field(default_factory=list)
    travel_times: List[str] = field(default_factory=list)
    sources: List[str] = field(default_factory=list)


@dataclass
class TableInfo:
    table_data: np.ndarray
    check_status: np.ndarray


@dataclass
class SourcesSurface:
    sou_min_x: np.float64
    sou_max_x: np.float64
    sou_min_y: np.float64
    sou_max_y: np.float64
    sou_x_length: int
    sou_y_length: int


@dataclass
class SummationComponents:
    gather: np.ndarray
    travel_times: np.ndarray
    receivers: np.ndarray
    sources: np.ndarray
    dt: float
    current_sample: int
    time_in_milliseconds: float
    window: int
    enabled_tensor_moments: np.ndarray
    tensor_indexes: np.ndarray


@dataclass
class ChartsInfo:
    max_ampl_index: np.int64
    detect_func: np.ndarray
    n_receivers: int
    n_samples: int
    frame_by_t: np.ndarray
    df: pd.DataFrame


@dataclass
class ColorBars:
    cb1: plt.colorbar
    cb2: plt.colorbar
    color_bar_count: int = 0  # to fix bug: remove color bar after changing gather


class StyledItemDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super().createEditor(parent, option, index)
        if isinstance(editor, QtWidgets.QLineEdit):
            validator = QtGui.QRegExpValidator(
                QtCore.QRegExp(r"^-?(\d*\.)?\d+$"), editor
            )
            editor.setValidator(validator)
        return editor
