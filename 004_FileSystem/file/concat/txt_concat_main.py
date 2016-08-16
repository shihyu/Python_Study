# -*- coding: utf-8 -*-
'''

'''

import sys,os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from txt_concat_ui import *
            
class MainForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        '''
        '''
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.connect(self.ui.btnConcat,QtCore.SIGNAL("clicked()"), self.onbtnConcatClick)
        self.connect(self.ui.btnClear,QtCore.SIGNAL("clicked()"), self.onbtnClearClick)
        self.connect(self.ui.btnRemove,QtCore.SIGNAL("clicked()"), self.onbtnRemoveClick)
        self.enableDrop(self.ui.listWidget, self.ondrop)
        
    def DragEnterEvent(self, event):
        '''
        
        '''
        #if event.mimeData().hasUrls:
        
        event.accept()
        #else:
        #    event.ignore()    
    
    def ondrop(self, event):  
        '''
        '''
        for item in event.mimeData().urls():
            url = item.path()[1:]                        
            if len(self.ui.listWidget.findItems(url, Qt.MatchFlags()))>0:
                return
            self.ui.listWidget.addItem(url)
            
    def enableDrop(self, ui, handler):
        '''
        '''        
        ui.dragEnterEvent = self.DragEnterEvent
        ui.dragMoveEvent = self.DragEnterEvent
        ui.dropEvent = handler
        ui.setAcceptDrops(True)        
        
    def onbtnClearClick(self):
        self.ui.listWidget.clear()
        
    def onbtnRemoveClick(self):
        pass
        
    def onbtnConcatClick(self):
        #print str(self.ui.lineEdit.text())
        out=open(str(self.ui.lineEdit.text()), 'w')
        #print 'input'
        for v in xrange(0, self.ui.listWidget.count()):                
            inf = open(str(self.ui.listWidget.item(v).text()))
            out.write(inf.read())
            inf.close()
        out.close()
        
        for v in xrange(0, self.ui.listWidget.count()):                
            try:
                os.remove(str(self.ui.listWidget.item(v).text()))
            except:
                pass
        QMessageBox.information(self, 'Info', 'OK')        


app = QApplication(sys.argv)
form = MainForm()
form.show()

app.connect(app, SIGNAL("lastWindowClosed()"),
            app, SLOT("quit()"))
sys.exit(app.exec_())
