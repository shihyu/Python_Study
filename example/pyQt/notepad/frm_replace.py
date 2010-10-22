# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm_replace.ui'
#
# Created: Fri Oct 22 21:07:59 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Replace(object):
    def setupUi(self, Replace):
        Replace.setObjectName(_fromUtf8("Replace"))
        Replace.resize(368, 130)
        self.txtName = QtGui.QLineEdit(Replace)
        self.txtName.setGeometry(QtCore.QRect(70, 20, 201, 20))
        self.txtName.setObjectName(_fromUtf8("txtName"))
        self.label = QtGui.QLabel(Replace)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.btnFindNext = QtGui.QPushButton(Replace)
        self.btnFindNext.setGeometry(QtCore.QRect(280, 10, 75, 23))
        self.btnFindNext.setObjectName(_fromUtf8("btnFindNext"))
        self.btnCancel = QtGui.QPushButton(Replace)
        self.btnCancel.setGeometry(QtCore.QRect(280, 100, 75, 23))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.chkIgoneCase = QtGui.QCheckBox(Replace)
        self.chkIgoneCase.setGeometry(QtCore.QRect(10, 100, 111, 17))
        self.chkIgoneCase.setObjectName(_fromUtf8("chkIgoneCase"))
        self.txtName_2 = QtGui.QLineEdit(Replace)
        self.txtName_2.setGeometry(QtCore.QRect(70, 50, 201, 20))
        self.txtName_2.setObjectName(_fromUtf8("txtName_2"))
        self.label_2 = QtGui.QLabel(Replace)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btnFindNext_2 = QtGui.QPushButton(Replace)
        self.btnFindNext_2.setGeometry(QtCore.QRect(280, 40, 75, 23))
        self.btnFindNext_2.setObjectName(_fromUtf8("btnFindNext_2"))
        self.btnFindNext_3 = QtGui.QPushButton(Replace)
        self.btnFindNext_3.setGeometry(QtCore.QRect(280, 70, 75, 23))
        self.btnFindNext_3.setObjectName(_fromUtf8("btnFindNext_3"))

        self.retranslateUi(Replace)
        QtCore.QMetaObject.connectSlotsByName(Replace)

    def retranslateUi(self, Replace):
        Replace.setWindowTitle(QtGui.QApplication.translate("Replace", "取代", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Replace", "尋找目標:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFindNext.setText(QtGui.QApplication.translate("Replace", "找下一個", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("Replace", "取消", None, QtGui.QApplication.UnicodeUTF8))
        self.chkIgoneCase.setText(QtGui.QApplication.translate("Replace", "大小寫視為相異", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Replace", "尋找目標:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFindNext_2.setText(QtGui.QApplication.translate("Replace", "取代", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFindNext_3.setText(QtGui.QApplication.translate("Replace", "全部取代", None, QtGui.QApplication.UnicodeUTF8))

