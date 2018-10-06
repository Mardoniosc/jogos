# coding: utf-8
import sys
from segundo import Segundo
from terceiro import Terceiro
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi


class Janelas(QMainWindow):
    def __init__(self):
        super(Janelas, self).__init__()
        loadUi('principal.ui', self)
        self.setWindowTitle('Principal')

        self.buttonSegundo.clicked.connect(self.segundo)
        self.buttonTerceiro.clicked.connect(self.terceiro)
        self.menuSair.triggered.connect(self.sair_sistema)
        self.actionSegundo.triggered.connect(self.segundo)
        self.actionTerceiro.triggered.connect(self.terceiro)

    def segundo(self):
        self.frmsegundo = QMainWindow()
        self.widget = Segundo()
        self.widget.show()


    def terceiro(self):
        self.frmterceiro = QMainWindow()
        self.widget = Terceiro()
        self.widget.show()

    def sair_sistema(self):
        exit()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    widget=Janelas()
    widget.show()
    sys.exit(app.exec())
