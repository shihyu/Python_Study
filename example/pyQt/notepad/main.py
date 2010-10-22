# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from mainwindow import Ui_MainWindow
from frm_replace import Ui_Replace
from frm_go import Ui_Go
from frm_font import Ui_Font
from frm_find import Ui_Find
from frm_about import Ui_About
import codecs, os
'''
TODO: 空白字元路徑
'''

class GoDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Go()
        self.ui.setupUi(self)

class FontDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Font()
        self.ui.setupUi(self)

class FindDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Find()
        self.ui.setupUi(self)

class ReplaceDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Replace()
        self.ui.setupUi(self)


class AboutDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_About()
        self.ui.setupUi(self)

class Notepad(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.__filename = None;
        self.__saved = True

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    	self.__init_event()

    def __init_event(self):
        QtCore.QObject.connect(self.ui.menuFileNew, QtCore.SIGNAL("triggered()"), self.menuFileNew_onClick)
        QtCore.QObject.connect(self.ui.menuFileOpen, QtCore.SIGNAL("triggered()"), self.menuFileOpen_onClick)
        QtCore.QObject.connect(self.ui.mnuFileSave, QtCore.SIGNAL("triggered()"), self.mnuFileSave_onClick)
        QtCore.QObject.connect(self.ui.mnuFileSaveAs, QtCore.SIGNAL("triggered()"), self.mnuFileSaveAs_onClick)
        QtCore.QObject.connect(self.ui.mnuPrintSetting, QtCore.SIGNAL("triggered()"), self.file_dialog)
        QtCore.QObject.connect(self.ui.mnuPrint, QtCore.SIGNAL("triggered()"), self.file_dialog)
        QtCore.QObject.connect(self.ui.mnuExit, QtCore.SIGNAL("triggered()"), self.mnuExit_onClick)

        QtCore.QObject.connect(self.ui.mnuEditUndo, QtCore.SIGNAL("triggered()"), self.mnuEditUndo_onClick)
        QtCore.QObject.connect(self.ui.mnuEditCut, QtCore.SIGNAL("triggered()"), self.mnuEditCut_onClick)
        QtCore.QObject.connect(self.ui.mnuEditCopy, QtCore.SIGNAL("triggered()"), self.mnuEditCopy_onClick)
        QtCore.QObject.connect(self.ui.mnuEditPaste, QtCore.SIGNAL("triggered()"), self.mnuEditPaste_onClick)
        QtCore.QObject.connect(self.ui.mnuEditDel, QtCore.SIGNAL("triggered()"), self.mnuEditDel_onClick)
        QtCore.QObject.connect(self.ui.mnuSelectAll, QtCore.SIGNAL("triggered()"), self.mnuSelectAll_onClick)

        QtCore.QObject.connect(self.ui.mnuFind, QtCore.SIGNAL("triggered()"), self.mnuFind_onClick)
        QtCore.QObject.connect(self.ui.mnuFileNext, QtCore.SIGNAL("triggered()"), self.file_dialog)
        QtCore.QObject.connect(self.ui.mnuReplace, QtCore.SIGNAL("triggered()"), self.mnuReplace_onClick)
        QtCore.QObject.connect(self.ui.mnuMoveNext, QtCore.SIGNAL("triggered()"), self.mnuMoveNext_onClick)
        QtCore.QObject.connect(self.ui.mnuInsertDatetime, QtCore.SIGNAL("triggered()"), self.file_dialog)

        QtCore.QObject.connect(self.ui.mnuEditWrap, QtCore.SIGNAL("triggered()"), self.mnuEditWrap_onClick)
        QtCore.QObject.connect(self.ui.mnuViewStyle, QtCore.SIGNAL("triggered()"), self.mnuViewStyle_onClick)

        QtCore.QObject.connect(self.ui.mnuStatusBar, QtCore.SIGNAL("triggered()"), self.mnuStatusBar_onClick)

        QtCore.QObject.connect(self.ui.mnuHelp, QtCore.SIGNAL("triggered()"), self.mnuHelp_onClick)
        QtCore.QObject.connect(self.ui.mnuAbout, QtCore.SIGNAL("triggered()"), self.mnuAbout_onClick)

        QtCore.QObject.connect(self.ui.textEdit,QtCore.SIGNAL("textChanged()"), self.textEdit_onChange)

    def mnuMoveNext_onClick(self):
        # http://www.cnblogs.com/hicjiajia/archive/2010/08/27/1809920.html
        self.dlg = GoDialog()
        self.dlg.setModal(True)
        self.dlg.show()

    def mnuFind_onClick(self):
        self.dlg = FindDialog()
        self.dlg.setModal(True)
        self.dlg.show()

    def mnuReplace_onClick(self):
        self.dlg = ReplaceDialog()
        self.dlg.setModal(True)
        self.dlg.show()


    def textEdit_onChange(self):
        self.__saved = False

    def mnuEditUndo_onClick(self):
        self.ui.textEdit.undo()
        #self.ui.textEdit.redo()

    def mnuEditCut_onClick(self):
        self.ui.textEdit.cut()

    def mnuEditCopy_onClick(self):
        self.ui.textEdit.copy()

    def mnuEditPaste_onClick(self):
        self.ui.textEdit.paste()

    def mnuEditDel_onClick(self):
        self.mnuEditCut_onClick()        

    def mnuSelectAll_onClick(self):
        self.ui.textEdit.selectAll()

    def mnuEditWrap_onClick(self):
        if self.ui.mnuEditWrap.isChecked() == True:
            self.ui.textEdit.LineWrapMode(QtGui.QTextEdit.WidgetWidth)
        else:
            self.ui.textEdit.LineWrapMode(QtGui.QTextEdit.NoWrap)
        

    def mnuViewStyle_onClick(self):
        self.dlg = FontDialog()
        self.dlg.setModal(True)
        self.dlg.show()

    def mnuStatusBar_onClick(self):
        self.ui.mnuEditWrap.setChecked(True)

    def mnuAbout_onClick(self):
        self.dlg = AboutDialog()
        self.dlg.setModal(True)
        self.dlg.show()

    def mnuExit_onClick(self):
        self.close()

    def mnuHelp_onClick(self):
        print 'help'


    def menuFileOpen_onClick(self):
        fd = QtGui.QFileDialog(self)
        tmp = fd.getOpenFileName()
        s = codecs.open(tmp,'r','utf-8').read()
        self.ui.textEdit.setPlainText(s)
        self.__filename = tmp
        self.__saved = True

    def menuFileNew_onClick(self):
        if self.__saved == False:
            SAVE = 'Save'
            DISCARD = 'Discard'
            CANCEL = 'Cancel'

            message = QtGui.QMessageBox(self)
            message.setText('What to do about unsaved changes ?')
            message.setIcon(QtGui.QMessageBox.Question)
            message.setWindowTitle('Notepad')
            message.addButton(SAVE, QtGui.QMessageBox.AcceptRole)
            message.addButton(DISCARD, QtGui.QMessageBox.DestructiveRole)
            message.addButton(CANCEL, QtGui.QMessageBox.RejectRole)
            #message.setDetailedText('Unsaved changes in file: ' + str(self.__filename))
            message.exec_()
            response = message.clickedButton().text()
            if response == SAVE:
                self.mnuFileSave_onClick()
            elif response == DISCARD:
                pass
            elif response == CANCEL:
                return

        self.ui.textEdit.clear()
        self.__filename = None
        self.__saved = True
        

    def mnuFileSaveAs_onClick(self):
        tmp = self.__filename
        self.__filename = None
        try:
            self.mnuFileSave_onClick()
        except:
            self.__filename = tmp

    def mnuFileSave_onClick(self):
        if self.__filename == None:
            fd = QtGui.QFileDialog(self)
            newfile = fd.getSaveFileName()
            if newfile:
                self.__filename = newfile
            else:
                return
        s = codecs.open(self.__filename,'w','utf-8')
        s.write(unicode(self.ui.textEdit.toPlainText()))
        s.close()
        self.__saved = True

    def file_dialog(self):
	    print 'x'
	

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Notepad()
    myapp.show()
    sys.exit(app.exec_())
