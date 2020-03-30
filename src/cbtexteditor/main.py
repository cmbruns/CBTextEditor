import sys

from PyQt5 import QtWidgets

from cbtexteditor.main_window import MainWindow


def run_cb_text_editor():
    print("Hello")
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run_cb_text_editor()
