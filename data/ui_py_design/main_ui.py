# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data/ui_design/main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_map = QtWidgets.QLabel(self.centralwidget)
        self.label_map.setGeometry(QtCore.QRect(140, 0, 500, 500))
        self.label_map.setObjectName("label_map")
        self.type_map = QtWidgets.QComboBox(self.centralwidget)
        self.type_map.setGeometry(QtCore.QRect(10, 20, 69, 22))
        self.type_map.setFocusPolicy(QtCore.Qt.NoFocus)
        self.type_map.setObjectName("type_map")
        self.type_map.addItem("")
        self.type_map.addItem("")
        self.type_map.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 561, 401, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 565, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setGeometry(QtCore.QRect(640, 565, 81, 31))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.label_place = QtWidgets.QLabel(self.centralwidget)
        self.label_place.setGeometry(QtCore.QRect(140, 540, 581, 16))
        self.label_place.setObjectName("label_place")
        self.label_index = QtWidgets.QLabel(self.centralwidget)
        self.label_index.setGeometry(QtCore.QRect(140, 520, 401, 16))
        self.label_index.setObjectName("label_index")
        self.radioButton_index = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_index.setGeometry(QtCore.QRect(550, 520, 171, 21))
        self.radioButton_index.setObjectName("radioButton_index")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_map.setText(_translate("MainWindow", "TextLabel"))
        self.type_map.setItemText(0, _translate("MainWindow", "Схема"))
        self.type_map.setItemText(1, _translate("MainWindow", "Спутник"))
        self.type_map.setItemText(2, _translate("MainWindow", "Гибрид"))
        self.pushButton.setText(_translate("MainWindow", "Искать"))
        self.pushButton_reset.setText(_translate("MainWindow", "Сбросить"))
        self.label_place.setText(_translate("MainWindow", "Адрес:"))
        self.label_index.setText(_translate("MainWindow", "Почтовый индекс:"))
        self.radioButton_index.setText(_translate("MainWindow", "Показать индекс"))
