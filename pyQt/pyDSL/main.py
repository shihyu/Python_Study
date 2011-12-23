#-*- coding: utf8 -*-
import os, sys, time
from qt import * 
# Generally advertised as safe

class Logger(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)
        self.setCaption(u"簡易網絡連接控制器 - PyDSL")
        self.layout = QGridLayout(self, 3, 2, 5, 10)
        self.tsdisp = QTextEdit(self)
        self.tsdisp.setMinimumSize(300, 100)
        self.tsdisp.setTextFormat(Qt.PlainText)
        self.author = QLabel(u"作者: 錢燕翔 n使用PyQT開發 n版本：1.0", self)
        self.author.setFont(QFont("Monospace", 10))
        self.tsdisp.setFont(QFont("Monospace", 10))
        self.conn = QPushButton(u"連接", self)
        self.disconn = QPushButton(u"斷線", self)
        self.layout.addMultiCellWidget(self.tsdisp, 0, 2, 0, 0)
        self.layout.addWidget(self.author, 0, 1)
        self.layout.addWidget(self.conn, 1, 1)
        self.layout.addWidget(self.disconn, 2, 1)
        self.connect(self.conn, SIGNAL("clicked()"),
        self.connectLog)
        self.connect(self.disconn, SIGNAL("clicked()"), self.disConnectLog)
        
    def connectLog(self):
        os.system("lian")
        stamp = [u'連接於:',time.ctime()]
        self.tsdisp.append(' '.join(stamp))
        
    def disConnectLog(self):
        os.system("duan")
        stamp = [u'斷線於:',time.ctime()]
        self.tsdisp.append(' '.join(stamp))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.connect(app, SIGNAL('lastWindowClosed()'), app, SLOT('quit()'))
    logger = Logger()
    logger.show()
    app.setMainWidget(logger)
    app.exec_loop()