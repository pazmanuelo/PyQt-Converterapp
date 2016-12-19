import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QLabel, QPushButton, QGridLayout
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("ConversorTemCaF.ui", self)
        self.setWindowTitle("Conversor de Temperatura")


        self.CaF.clicked.connect(self.BCaF)
        self.FaC.clicked.connect(self.BFaC)

    def BCaF(self):
        temp = float(self.temp.text())
        conver = temp * 9 / 5 + 32
        self.resultado.setText(str(temp) + " ºC es igual a " + str(conver) + " ºF")

    def BFaC(self):
        temp = float(self.temp.text())
        conver = (temp - 32) / 1.8
        self.resultado.setText(str(temp) + " ºF es igual a " + str(conver) + " ºC")


app = QApplication(sys.argv)
_ventana = Ventana()
_ventana.show()
app.exec_()
