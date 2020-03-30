import pkg_resources

from PyQt5 import QtWidgets
from PyQt5.uic import loadUi


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ui = pkg_resources.resource_stream("cbtexteditor", "main_window.ui")
        self.ui = loadUi(ui, self)
