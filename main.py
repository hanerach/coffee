import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5 import uic

class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect('coffee.sqlite.db')
        self.cur = con.cursor()
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.table)

    def table(self):
        data = self.cur.execute('SELECT * FROM coffee').fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['id', "Название сорта", "Степень обжраки", "Молотый",
                                                    "Описание вкуса", "Цена", "Объём упаковки"])
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())