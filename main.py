import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QDialog
from PyQt5 import QtCore, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1081, 622)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.idLabel = QtWidgets.QLabel(Dialog)
        self.idLabel.setObjectName("idLabel")
        self.horizontalLayout_6.addWidget(self.idLabel)
        self.idSpinBox = QtWidgets.QSpinBox(Dialog)
        self.idSpinBox.setMaximum(1231231231)
        self.idSpinBox.setObjectName("idSpinBox")
        self.horizontalLayout_6.addWidget(self.idSpinBox)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tasteLabel = QtWidgets.QLabel(Dialog)
        self.tasteLabel.setObjectName("tasteLabel")
        self.horizontalLayout_2.addWidget(self.tasteLabel)
        self.tasteEdit = QtWidgets.QLineEdit(Dialog)
        self.tasteEdit.setObjectName("tasteEdit")
        self.horizontalLayout_2.addWidget(self.tasteEdit)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groundedLabel = QtWidgets.QLabel(Dialog)
        self.groundedLabel.setObjectName("groundedLabel")
        self.horizontalLayout_3.addWidget(self.groundedLabel)
        self.groundedSpinBox = QtWidgets.QSpinBox(Dialog)
        self.groundedSpinBox.setMaximum(1)
        self.groundedSpinBox.setObjectName("groundedSpinBox")
        self.horizontalLayout_3.addWidget(self.groundedSpinBox)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sortLabel = QtWidgets.QLabel(Dialog)
        self.sortLabel.setObjectName("sortLabel")
        self.horizontalLayout_5.addWidget(self.sortLabel)
        self.sortEdit = QtWidgets.QLineEdit(Dialog)
        self.sortEdit.setObjectName("sortEdit")
        self.horizontalLayout_5.addWidget(self.sortEdit)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.roastingLabel = QtWidgets.QLabel(Dialog)
        self.roastingLabel.setObjectName("roastingLabel")
        self.horizontalLayout_4.addWidget(self.roastingLabel)
        self.roastingEdit = QtWidgets.QLineEdit(Dialog)
        self.roastingEdit.setObjectName("roastingEdit")
        self.horizontalLayout_4.addWidget(self.roastingEdit)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.addBtn = QtWidgets.QPushButton(Dialog)
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout_7.addWidget(self.addBtn)
        self.editBtn = QtWidgets.QPushButton(Dialog)
        self.editBtn.setObjectName("editBtn")
        self.horizontalLayout_7.addWidget(self.editBtn)
        self.deleteBtn = QtWidgets.QPushButton(Dialog)
        self.deleteBtn.setObjectName("deleteBtn")
        self.horizontalLayout_7.addWidget(self.deleteBtn)
        self.gridLayout.addLayout(self.horizontalLayout_7, 10, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.volumeLabel = QtWidgets.QLabel(Dialog)
        self.volumeLabel.setObjectName("volumeLabel")
        self.horizontalLayout.addWidget(self.volumeLabel)
        self.volumeSpinBox = QtWidgets.QSpinBox(Dialog)
        self.volumeSpinBox.setMaximum(1515123512)
        self.volumeSpinBox.setObjectName("volumeSpinBox")
        self.horizontalLayout.addWidget(self.volumeSpinBox)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 9, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.costLabel = QtWidgets.QLabel(Dialog)
        self.costLabel.setObjectName("costLabel")
        self.horizontalLayout_8.addWidget(self.costLabel)
        self.costSpinBox = QtWidgets.QSpinBox(Dialog)
        self.costSpinBox.setMaximum(547456456)
        self.costSpinBox.setObjectName("costSpinBox")
        self.horizontalLayout_8.addWidget(self.costSpinBox)
        self.gridLayout.addLayout(self.horizontalLayout_8, 7, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.idLabel.setText(_translate("Dialog", "ID"))
        self.tasteLabel.setText(_translate("Dialog", "Описание вкуса"))
        self.groundedLabel.setText(_translate("Dialog", "Вид (0 - молотый, 1 - зерновой)"))
        self.sortLabel.setText(_translate("Dialog", "Название сорта"))
        self.roastingLabel.setText(_translate("Dialog", "Степень обжарки"))
        self.addBtn.setText(_translate("Dialog", "Добавить"))
        self.editBtn.setText(_translate("Dialog", "Изменить"))
        self.deleteBtn.setText(_translate("Dialog", "Удалить"))
        self.volumeLabel.setText(_translate("Dialog", "Объем упаковки"))
        self.costLabel.setText(_translate("Dialog", "Цена"))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.updateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.updateBtn.setObjectName("updateBtn")
        self.gridLayout.addWidget(self.updateBtn, 2, 0, 1, 1)
        self.editBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editBtn.setObjectName("editBtn")
        self.gridLayout.addWidget(self.editBtn, 2, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1015, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.updateBtn.setText(_translate("MainWindow", "Обновить"))
        self.editBtn.setText(_translate("MainWindow", "Редактировать"))

class EditDialog(QDialog, Ui_Dialog):
    def __init__(self, mw):
        super().__init__()
        self.setupUi(self)
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


class Coffee(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('data/coffee.sqlite.db')
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