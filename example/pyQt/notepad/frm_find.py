# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm_find.ui'
#
# Created: Fri Oct 22 21:08:06 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Find(object):
    def setupUi(self, Find):
        Find.setObjectName(_fromUtf8("Find"))
        Find.resize(374, 95)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Find.sizePolicy().hasHeightForWidth())
        Find.setSizePolicy(sizePolicy)
        self.label = QtGui.QLabel(Find)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.txtName = QtGui.QLineEdit(Find)
        self.txtName.setGeometry(QtCore.QRect(70, 10, 201, 20))
        self.txtName.setObjectName(_fromUtf8("txtName"))
        self.btnFindNext = QtGui.QPushButton(Find)
        self.btnFindNext.setGeometry(QtCore.QRect(280, 10, 75, 23))
        self.btnFindNext.setObjectName(_fromUtf8("btnFindNext"))
        self.btnCancel = QtGui.QPushButton(Find)
        self.btnCancel.setGeometry(QtCore.QRect(280, 40, 75, 23))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.groupBox = QtGui.QGroupBox(Find)
        self.groupBox.setGeometry(QtCore.QRect(150, 30, 121, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 102, 19))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.rdoUp = QtGui.QRadioButton(self.layoutWidget)
        self.rdoUp.setObjectName(_fromUtf8("rdoUp"))
        self.horizontalLayout.addWidget(self.rdoUp)
        self.rdoDown = QtGui.QRadioButton(self.layoutWidget)
        self.rdoDown.setObjectName(_fromUtf8("rdoDown"))
        self.horizontalLayout.addWidget(self.rdoDown)
        self.chkIgoneCase = QtGui.QCheckBox(Find)
        self.chkIgoneCase.setGeometry(QtCore.QRect(30, 60, 111, 17))
        self.chkIgoneCase.setObjectName(_fromUtf8("chkIgoneCase"))

        self.retranslateUi(Find)
        QtCore.QMetaObject.connectSlotsByName(Find)

    def retranslateUi(self, Find):
        Find.setWindowTitle(QtGui.QApplication.translate("Find", "尋找", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Find", "尋找目標:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFindNext.setText(QtGui.QApplication.translate("Find", "找下一個", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("Find", "取消", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Find", "搜尋方向", None, QtGui.QApplication.UnicodeUTF8))
        self.rdoUp.setText(QtGui.QApplication.translate("Find", "向上", None, QtGui.QApplication.UnicodeUTF8))
        self.rdoDown.setText(QtGui.QApplication.translate("Find", "向下", None, QtGui.QApplication.UnicodeUTF8))
        self.chkIgoneCase.setText(QtGui.QApplication.translate("Find", "大小寫視為相異", None, QtGui.QApplication.UnicodeUTF8))

