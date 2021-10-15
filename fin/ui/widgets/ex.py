#!/usr/bin/env python
#-*- coding:utf-8 -*-
#https://www.semicolonworld.com/question/55795/pyqt-populating-qtablewidget-with-csv-data
import csv

from PyQt5 import QtCore, QtGui, QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self, fileName, parent=None):
        super(MyWindow, self).__init__(parent)
        self.fileName = fileName
        self.resize(1200, 500)
        self.model = QtGui.QStandardItemModel(self)

        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        # self.pushButtonLoad = QtWidgets.QPushButton(self)
        # self.pushButtonLoad.setText("Load Csv File!")
        # self.pushButtonLoad.clicked.connect(self.on_pushButtonLoad_clicked)

        # self.pushButtonWrite = QtWidgets.QPushButton(self)
        # self.pushButtonWrite.setText("Write Csv File!")
        # self.pushButtonWrite.clicked.connect(self.on_pushButtonWrite_clicked)

        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.tableView)
        # self.layoutVertical.addWidget(self.pushButtonLoad)
        # self.layoutVertical.addWidget(self.pushButtonWrite)
        self.loadCsv(self.fileName)
    def loadCsv(self, fileName):
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

    def writeCsv(self, fileName):
        with open(fileName, "w") as fileOutput:
            writer = csv.writer(fileOutput)
            for rowNumber in range(self.model.rowCount()):
                fields = [
                    self.model.data(
                        self.model.index(rowNumber, columnNumber),
                        QtCore.Qt.DisplayRole
                    )
                    for columnNumber in range(self.model.columnCount())
                ]
                writer.writerow(fields)

    @QtCore.pyqtSlot()
    def on_pushButtonWrite_clicked(self):
        self.writeCsv(self.fileName)

    @QtCore.pyqtSlot()
    def on_pushButtonLoad_clicked(self):
        self.loadCsv(self.fileName)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('INSIDER TRADING')

    main = MyWindow("/home/tyler/Documents/openanal/fin/ui/var/openinsider.csv")
    main.show()

    sys.exit(app.exec_())