import sys

from PyQt5.QtWidgets import QDialog, QApplication

from UI.interest_calculator import Ui_Dialog


class Calculator(QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.doubleSpinBox.setPrefix('RMB ')
        self.doubleSpinBox_2.setSuffix(' %')
        print('b')
        self.comboBox.addItems(
            ["{} years".format(x) for x in range(1, 11)]
        )
        print('c')

        self.updateUi()


    def updateUi(self):
        principal = self.doubleSpinBox.value()
        rate = self.doubleSpinBox_2.value()
        years = self.comboBox.currentIndex() + 1
        print(years)
        amount = principal * (1 + rate / 100) ** years
        self.label_amount.setText(
            "RMB {0:.2f}".format(amount)
        )


if __name__ == '__main__':
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())