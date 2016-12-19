# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConversorTemCaF.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
#!/bin/bash

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QLabel, QPushButton, QGridLayout


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(390, 275)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 370, 250))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.CaF = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CaF.setEnabled(True)
        self.CaF.setMaximumSize(QtCore.QSize(100, 50))
        self.CaF.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.CaF.setObjectName("CaF")
        self.gridLayout.addWidget(self.CaF, 2, 0, 1, 1)
        self.temp = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.temp.setMinimumSize(QtCore.QSize(10, 10))
        self.temp.setMaximumSize(QtCore.QSize(260, 30))
        self.temp.setObjectName("temp")
        self.gridLayout.addWidget(self.temp, 0, 1, 1, 1)
        self.temp.setAlignment(QtCore.Qt.AlignRight)
        self.resultado = QtWidgets.QLabel(self.gridLayoutWidget)
        self.resultado.setEnabled(True)
        self.resultado.setMinimumSize(QtCore.QSize(10, 10))
        self.resultado.setMaximumSize(QtCore.QSize(260, 50))
        self.resultado.setIndent(-1)
        self.resultado.setObjectName("resultado")
        self.gridLayout.addWidget(self.resultado, 1, 1, 1, 1)
        self.FaC = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.FaC.setMaximumSize(QtCore.QSize(100, 50))
        self.FaC.setObjectName("FaC")
        self.gridLayout.addWidget(self.FaC, 1, 0, 1, 1)

        self.CaF.clicked.connect(self.BCaF)
        self.FaC.clicked.connect(self.BFaC)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def BCaF(self):
        temp = float(self.temp.text())
        conver = temp * 9 / 5 + 32
        self.resultado.setText(str(temp) + " ºC es igual a " + str(conver) + " ºF")

    def BFaC(self):
        temp = float(self.temp.text())
        conver = (temp - 32) / 1.8
        self.resultado.setText(str(temp) + " ºF es igual a " + str(conver) + " ºC")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Conversor de Temperatura"))
        self.CaF.setText(_translate("Form", "ºC a ºF"))
        self.resultado.setText(_translate("Form", ""))
        self.FaC.setText(_translate("Form", "ºF a ºC"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

