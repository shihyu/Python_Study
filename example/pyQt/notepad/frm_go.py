# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm_Go.ui'
#
# Created: Fri Oct 22 21:08:34 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Go(object):
    def setupUi(self, Go):
        Go.setObjectName(_fromUtf8("Go"))
        Go.resize(199, 96)
        self.label = QtGui.QLabel(Go)
        self.label.setGeometry(QtCore.QRect(10, 20, 47, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.txtLineN = QtGui.QLineEdit(Go)
        self.txtLineN.setGeometry(QtCore.QRect(60, 10, 113, 20))
        self.txtLineN.setObjectName(_fromUtf8("txtLineN"))
        self.layoutWidget = QtGui.QWidget(Go)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 60, 158, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnOk = QtGui.QPushButton(self.layoutWidget)
        self.btnOk.setObjectName(_fromUtf8("btnOk"))
        self.horizontalLayout.addWidget(self.btnOk)
        self.btnCancel = QtGui.QPushButton(self.layoutWidget)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout.addWidget(self.btnCancel)

        self.retranslateUi(Go)
        QtCore.QMetaObject.connectSlotsByName(Go)

    def retranslateUi(self, Go):
        Go.setWindowTitle(QtGui.QApplication.translate("Go", "跳至...行", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Go", "第...行", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOk.setText(QtGui.QApplication.translate("Go", "確定", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("Go", "取消", None, QtGui.QApplication.UnicodeUTF8))

