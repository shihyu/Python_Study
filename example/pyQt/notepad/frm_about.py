# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm_about.ui'
#
# Created: Fri Oct 22 23:18:46 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(400, 300)
        self.pushButton = QtGui.QPushButton(About)
        self.pushButton.setGeometry(QtCore.QRect(100, 80, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(QtGui.QApplication.translate("About", "關於", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("About", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

