# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1090, 782)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_13 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(890, 170, 181, 41))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_14 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(890, 250, 181, 41))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_15 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(890, 330, 181, 41))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.pushButton_16 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(890, 410, 181, 41))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.pushButton_17 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(890, 490, 181, 41))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 110, 181, 151))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 110, 181, 151))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 110, 181, 151))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(660, 110, 181, 151))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 280, 181, 151))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(260, 280, 181, 151))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(460, 280, 181, 151))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(660, 280, 181, 151))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(60, 450, 181, 151))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(260, 450, 181, 151))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_11 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(460, 450, 181, 151))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_12 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(660, 450, 181, 151))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_13.setText(_translate("MainWindow", "Portfolio 1", None))
        self.pushButton_14.setText(_translate("MainWindow", "Portfolio 2", None))
        self.pushButton_15.setText(_translate("MainWindow", "Portfolio 3", None))
        self.pushButton_16.setText(_translate("MainWindow", "Portfolio 4", None))
        self.pushButton_17.setText(_translate("MainWindow", "Portfolio 5", None))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2", None))

