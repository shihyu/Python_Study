# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm_font.ui'
#
# Created: Fri Oct 22 21:08:04 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Font(object):
    def setupUi(self, Font):
        Font.setObjectName(_fromUtf8("Font"))
        Font.resize(469, 311)
        self.label = QtGui.QLabel(Font)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Font)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Font)
        self.label_3.setGeometry(QtCore.QRect(240, 10, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Font)
        self.label_4.setGeometry(QtCore.QRect(120, 260, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(Font)
        self.lineEdit.setGeometry(QtCore.QRect(0, 40, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Font)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 40, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Font)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 40, 113, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.btnCancel = QtGui.QPushButton(Font)
        self.btnCancel.setGeometry(QtCore.QRect(390, 50, 75, 23))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.btnFindNext_3 = QtGui.QPushButton(Font)
        self.btnFindNext_3.setGeometry(QtCore.QRect(390, 20, 75, 23))
        self.btnFindNext_3.setObjectName(_fromUtf8("btnFindNext_3"))
        self.groupBox = QtGui.QGroupBox(Font)
        self.groupBox.setGeometry(QtCore.QRect(119, 180, 231, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.textEdit = QtGui.QTextEdit(self.groupBox)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setItalic(True)
        font.setUnderline(True)
        font.setStrikeOut(True)
        font.setBold(True)
        self.textEdit.setFont(font)
        self.textEdit.setAcceptDrops(False)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.listWidget = QtGui.QListWidget(Font)
        self.listWidget.setGeometry(QtCore.QRect(0, 70, 111, 101))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget_2 = QtGui.QListWidget(Font)
        self.listWidget_2.setGeometry(QtCore.QRect(120, 70, 111, 101))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.listWidget_3 = QtGui.QListWidget(Font)
        self.listWidget_3.setGeometry(QtCore.QRect(240, 70, 111, 101))
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
        self.comboBox = QtGui.QComboBox(Font)
        self.comboBox.setGeometry(QtCore.QRect(120, 280, 231, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))

        self.retranslateUi(Font)
        QtCore.QMetaObject.connectSlotsByName(Font)

    def retranslateUi(self, Font):
        Font.setWindowTitle(QtGui.QApplication.translate("Font", "字型", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Font", "字型:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Font", "字型樣式:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Font", "大小:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Font", "字集:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("Font", "取消", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFindNext_3.setText(QtGui.QApplication.translate("Font", "確定", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Font", "範例", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("Font", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'新細明體\'; font-size:12pt; font-weight:600; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">中文字型範例</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

