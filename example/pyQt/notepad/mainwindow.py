# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Oct 22 21:41:28 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(796, 550)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_2.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 17))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menu_E = QtGui.QMenu(self.menubar)
        self.menu_E.setObjectName(_fromUtf8("menu_E"))
        self.menu_O = QtGui.QMenu(self.menubar)
        self.menu_O.setObjectName(_fromUtf8("menu_O"))
        self.menu_V = QtGui.QMenu(self.menubar)
        self.menu_V.setObjectName(_fromUtf8("menu_V"))
        self.menu_H = QtGui.QMenu(self.menubar)
        self.menu_H.setObjectName(_fromUtf8("menu_H"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuFileNew = QtGui.QAction(MainWindow)
        self.menuFileNew.setObjectName(_fromUtf8("menuFileNew"))
        self.menuFileOpen = QtGui.QAction(MainWindow)
        self.menuFileOpen.setObjectName(_fromUtf8("menuFileOpen"))
        self.mnuFileSave = QtGui.QAction(MainWindow)
        self.mnuFileSave.setObjectName(_fromUtf8("mnuFileSave"))
        self.mnuFileSaveAs = QtGui.QAction(MainWindow)
        self.mnuFileSaveAs.setObjectName(_fromUtf8("mnuFileSaveAs"))
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.mnuPrintSetting = QtGui.QAction(MainWindow)
        self.mnuPrintSetting.setObjectName(_fromUtf8("mnuPrintSetting"))
        self.mnuPrint = QtGui.QAction(MainWindow)
        self.mnuPrint.setObjectName(_fromUtf8("mnuPrint"))
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.mnuExit = QtGui.QAction(MainWindow)
        self.mnuExit.setObjectName(_fromUtf8("mnuExit"))
        self.mnuEditUndo = QtGui.QAction(MainWindow)
        self.mnuEditUndo.setObjectName(_fromUtf8("mnuEditUndo"))
        self.mnuEditCut = QtGui.QAction(MainWindow)
        self.mnuEditCut.setObjectName(_fromUtf8("mnuEditCut"))
        self.mnuEditCopy = QtGui.QAction(MainWindow)
        self.mnuEditCopy.setObjectName(_fromUtf8("mnuEditCopy"))
        self.mnuEditPaste = QtGui.QAction(MainWindow)
        self.mnuEditPaste.setObjectName(_fromUtf8("mnuEditPaste"))
        self.mnuEditDel = QtGui.QAction(MainWindow)
        self.mnuEditDel.setObjectName(_fromUtf8("mnuEditDel"))
        self.mnuFind = QtGui.QAction(MainWindow)
        self.mnuFind.setObjectName(_fromUtf8("mnuFind"))
        self.mnuFileNext = QtGui.QAction(MainWindow)
        self.mnuFileNext.setObjectName(_fromUtf8("mnuFileNext"))
        self.mnuReplace = QtGui.QAction(MainWindow)
        self.mnuReplace.setObjectName(_fromUtf8("mnuReplace"))
        self.mnuMoveNext = QtGui.QAction(MainWindow)
        self.mnuMoveNext.setObjectName(_fromUtf8("mnuMoveNext"))
        self.mnuSelectAll = QtGui.QAction(MainWindow)
        self.mnuSelectAll.setObjectName(_fromUtf8("mnuSelectAll"))
        self.mnuInsertDatetime = QtGui.QAction(MainWindow)
        self.mnuInsertDatetime.setObjectName(_fromUtf8("mnuInsertDatetime"))
        self.mnuEditWrap = QtGui.QAction(MainWindow)
        self.mnuEditWrap.setCheckable(True)
        self.mnuEditWrap.setObjectName(_fromUtf8("mnuEditWrap"))
        self.mnuViewStyle = QtGui.QAction(MainWindow)
        self.mnuViewStyle.setObjectName(_fromUtf8("mnuViewStyle"))
        self.mnuStatusBar = QtGui.QAction(MainWindow)
        self.mnuStatusBar.setObjectName(_fromUtf8("mnuStatusBar"))
        self.mnuHelp = QtGui.QAction(MainWindow)
        self.mnuHelp.setObjectName(_fromUtf8("mnuHelp"))
        self.mnuAbout = QtGui.QAction(MainWindow)
        self.mnuAbout.setObjectName(_fromUtf8("mnuAbout"))
        self.menuFile.addAction(self.menuFileNew)
        self.menuFile.addAction(self.menuFileOpen)
        self.menuFile.addAction(self.mnuFileSave)
        self.menuFile.addAction(self.mnuFileSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.mnuPrintSetting)
        self.menuFile.addAction(self.mnuPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.mnuExit)
        self.menu_E.addAction(self.mnuEditUndo)
        self.menu_E.addSeparator()
        self.menu_E.addAction(self.mnuEditCut)
        self.menu_E.addAction(self.mnuEditCopy)
        self.menu_E.addAction(self.mnuEditPaste)
        self.menu_E.addAction(self.mnuEditDel)
        self.menu_E.addSeparator()
        self.menu_E.addAction(self.mnuFind)
        self.menu_E.addAction(self.mnuFileNext)
        self.menu_E.addAction(self.mnuReplace)
        self.menu_E.addAction(self.mnuMoveNext)
        self.menu_E.addSeparator()
        self.menu_E.addAction(self.mnuSelectAll)
        self.menu_E.addAction(self.mnuInsertDatetime)
        self.menu_O.addAction(self.mnuEditWrap)
        self.menu_O.addAction(self.mnuViewStyle)
        self.menu_V.addAction(self.mnuStatusBar)
        self.menu_H.addAction(self.mnuHelp)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.mnuAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.menubar.addAction(self.menu_O.menuAction())
        self.menubar.addAction(self.menu_V.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "檔案(&F)", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_E.setTitle(QtGui.QApplication.translate("MainWindow", "編輯(&E)", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_O.setTitle(QtGui.QApplication.translate("MainWindow", "格式(&O)", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_V.setTitle(QtGui.QApplication.translate("MainWindow", "檢視(&V)", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_H.setTitle(QtGui.QApplication.translate("MainWindow", "說明(&H)", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFileNew.setText(QtGui.QApplication.translate("MainWindow", "新增(&N)", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFileNew.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFileOpen.setText(QtGui.QApplication.translate("MainWindow", "開啟舊檔(&O)...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFileOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuFileSave.setText(QtGui.QApplication.translate("MainWindow", "儲存檔案(&S)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuFileSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuFileSaveAs.setText(QtGui.QApplication.translate("MainWindow", "另存新檔(&A)...", None, QtGui.QApplication.UnicodeUTF8))
        self.action.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuPrintSetting.setText(QtGui.QApplication.translate("MainWindow", "設定列印格式(&U)...", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuPrint.setText(QtGui.QApplication.translate("MainWindow", "列印(&P)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuPrint.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.action_2.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuExit.setText(QtGui.QApplication.translate("MainWindow", "結束(&X)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuEditUndo.setText(QtGui.QApplication.translate("MainWindow", "復原(&U)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuEditUndo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuEditCut.setText(QtGui.QApplication.translate("MainWindow", "剪下(&T)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuEditCut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuEditCopy.setText(QtGui.QApplication.translate("MainWindow", "複製(&C)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuEditCopy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuEditPaste.setText(QtGui.QApplication.translate("MainWindow", "貼上(&P)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuEditPaste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuEditDel.setText(QtGui.QApplication.translate("MainWindow", "刪除(&L)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuEditDel.setShortcut(QtGui.QApplication.translate("MainWindow", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuFind.setText(QtGui.QApplication.translate("MainWindow", "尋找(&F)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuFind.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuFileNext.setText(QtGui.QApplication.translate("MainWindow", "找下ㄧ個(&N)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuFileNext.setShortcut(QtGui.QApplication.translate("MainWindow", "F3", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuReplace.setText(QtGui.QApplication.translate("MainWindow", "取代(&R)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuReplace.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+H", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuMoveNext.setText(QtGui.QApplication.translate("MainWindow", "移至(&G)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuMoveNext.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+G", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuSelectAll.setText(QtGui.QApplication.translate("MainWindow", "全選(&A)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuSelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuInsertDatetime.setText(QtGui.QApplication.translate("MainWindow", "日期/時間)&D)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuInsertDatetime.setShortcut(QtGui.QApplication.translate("MainWindow", "F5", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuEditWrap.setText(QtGui.QApplication.translate("MainWindow", "自動換行(&W)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuViewStyle.setText(QtGui.QApplication.translate("MainWindow", "格式(&F)...", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuStatusBar.setText(QtGui.QApplication.translate("MainWindow", "狀態列(&S)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuHelp.setText(QtGui.QApplication.translate("MainWindow", "說明主題(&H)", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuAbout.setText(QtGui.QApplication.translate("MainWindow", "關於筆記本(&A)", None, QtGui.QApplication.UnicodeUTF8))

