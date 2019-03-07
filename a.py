from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from UI.untitled import Ui_MainWindow
from UI.dialog import Ui_Dialog
import sys

data = ['id', 'name_mysql', 'age']


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ('field_name', 'field_type'))
        self.row = 0
        for item in data:
            cellinfo = QTableWidgetItem(item)
            combo = QtWidgets.QComboBox()
            combo.addItem('int')
            combo.addItem('string')
            self.ui.tableWidget.setItem(self.row, 0, cellinfo)
            self.ui.tableWidget.setCellWidget(self.row, 1, combo)
            self.row += 1
        self.ui.pushButton.clicked.connect(self.add_row)
        self.ui.pushButton_2.clicked.connect(self.remove_row)
        self.ui.pushButton_3.clicked.connect(self.new_window)
        self.ui.pushButton_4.clicked.connect(self.open_dialog)

    def new_window(self):
        self.window = MyWindow()
        self.window.show()

    def add_row(self):
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        cellinfo = QTableWidgetItem('hello')
        combo = QtWidgets.QComboBox()
        combo.addItem('int')
        combo.addItem('string')
        self.ui.tableWidget.setItem(row, 0, cellinfo)
        self.ui.tableWidget.setCellWidget(row, 1, combo)


    def remove_row(self):
        self.ui.tableWidget.removeRow(self.ui.tableWidget.rowCount() - 1)

    def open_dialog(self):
        self.dialog = MyDialog
        self.dialog.show()

class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.pushButton.connect(self.show_message)

    def show_message(self):
        print(self.ui.lineEdit.text())



app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
sys.exit(app.exec_())