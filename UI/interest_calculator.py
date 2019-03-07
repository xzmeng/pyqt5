# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\interest_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(344, 240)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(70, 50, 201, 110))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox.setMaximum(1000000.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 0, 1, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 1, 1, 1, 1)
        self.label_amount = QtWidgets.QLabel(self.widget)
        self.label_amount.setObjectName("label_amount")
        self.gridLayout.addWidget(self.label_amount, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.doubleSpinBox.valueChanged['double'].connect(Dialog.updateUi)
        self.doubleSpinBox_2.valueChanged['double'].connect(Dialog.updateUi)
        self.comboBox.currentIndexChanged['int'].connect(Dialog.updateUi)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Rate:"))
        self.label.setText(_translate("Dialog", "Principal:"))
        self.label_3.setText(_translate("Dialog", "Years"))
        self.label_4.setText(_translate("Dialog", "Amount"))
        self.label_amount.setText(_translate("Dialog", "TextLabel"))

