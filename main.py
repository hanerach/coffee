import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QDialog
from PyQt5 import uic

class EditDialog(QDialog):
    def __init__(self, mw):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.mw = mw
        self.table()
        self.initUI()

    def initUI(self):
        self.addBtn.clicked.connect(self.add)
        self.editBtn.clicked.connect(self.edit)
        self.deleteBtn.clicked.connect(self.delete)
        self.tableWidget.cellClicked.connect(self.show_data)


    def add(self):
        data = (self.sortEdit.text(), self.roastingEdit.text(),
                self.groundedSpinBox.value(), self.tasteEdit.text(), self.costSpinBox.value(),
                self.volumeSpinBox.value())
        self.mw.cur.execute('''INSERT INTO coffee (sort, roasting, ground, taste, price, volume)
        VALUES (?, ?, ?, ?, ?, ?)''', data)
        self.mw.con.commit()
        self.table()

    def edit(self):
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        if len(ids) == 1:
            data = (self.idSpinBox.value(), self.sortEdit.text(), self.roastingEdit.text(),
                    self.groundedSpinBox.value(), self.tasteEdit.text(), self.costSpinBox.value(),
                    self.volumeSpinBox.value())
            self.mw.cur.execute(f'UPDATE coffee SET'
                                        f'(id, sort, roasting, ground, taste, price, volume) = (?, ?, ?, ?, ?, ?, ?)'
                                        f'WHERE id = {int(ids[0])}',
                                        data)
            self.mw.con.commit()
            self.table()
        else:
            self.editBtn.setText('Выбрано количество строк, отличное от 1')

    def delete(self):
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        for g in ids:
            self.mw.cur.execute(f'DELETE FROM coffee WHERE id = {int(g)}')
            self.mw.con.commit()
            self.table()

    def table(self):
        data = self.mw.cur.execute('SELECT * FROM coffee').fetchall()
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

    def show_data(self):
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        if len(rows) == 1:
            data = [self.tableWidget.item(rows[0], 0).text(), self.tableWidget.item(rows[0], 1).text(),
                    self.tableWidget.item(rows[0], 2).text(), self.tableWidget.item(rows[0], 3).text(),
                    self.tableWidget.item(rows[0], 4).text(), self.tableWidget.item(rows[0], 5).text(),
                    self.tableWidget.item(rows[0], 6).text()]
            self.idSpinBox.setValue(int(data[0]))
            self.sortEdit.setText(data[1])
            self.roastingEdit.setText(data[2])
            self.groundedSpinBox.setValue(int(data[3]))
            self.tasteEdit.setText(data[4])
            self.volumeSpinBox.setValue(int(data[5]))
            self.costSpinBox.setValue(int(data[6]))


    def closeEvent(self, event):
        self.mw.table()


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.sqlite.db')
        self.cur = self.con.cursor()
        self.table()
        self.initUI()

    def initUI(self):
        self.updateBtn.clicked.connect(self.table)
        self.editBtn.clicked.connect(self.edit_dialog)

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

    def edit_dialog(self):
        dlg = EditDialog(self)
        dlg.exec()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Coffee()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())