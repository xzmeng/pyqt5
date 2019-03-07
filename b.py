import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from UI.MainWindowDemo2 import Ui_MainWindow
from UI.ChildrenForm2 import Ui_Form


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.child = ChildrenForm()
        self.fileCloseAction.triggered.connect(self.close)
        self.fileOpenAction.triggered.connect(self.openMsg)
        self.addWinAction.triggered.connect(self.childShow)

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(
            self, "打开", "C:/", "All Files (*);;TextFiles (*.txt)"
        )
        self.statusbar.showMessage(file)

    def childShow(self):
        self.MainGridLayout.addWidget(self.child)
        self.child.show()


class ChildrenForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())