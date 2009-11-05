# -*- coding: cp950 -*-
"""
Description: 顯示執行結果

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

from Tkinter import Tk, Canvas, Scrollbar, Menu
from xml.dom.minidom import parseString
from idlelib.TreeWidget import TreeItem, TreeNode, ScrolledCanvas
import os
gMenu = None
gNode = None
gFile = None
def popup(event):
    global gMenu
    gMenu.post(event.x_root, event.y_root)
        
class MyTreeNode(TreeNode):
    def drawtext(self):
        TreeNode.drawtext(self)
        self.label.bind("<Button-3>", self.test)
        
    #def drawicon(self):
    #    TreeNode.drawicon(self)
    #    self.canvas.bind("<Button-3>", self.test)

    def dump(self):
        for c in self.children[:]:
            print dir(c) 
        
    def test(self, event=None):
        fn = event.widget['text']
        if '\\' in fn:
            global gFile
            gFile = fn
            popup(event)
        #print 'test'
        
class DomTreeItem(TreeItem):
    def __init__(self, node):
        self.node = node
        
    def GetText(self):
        node = self.node
        attr = node.attributes

        if node.nodeType == node.ELEMENT_NODE and attr.has_key("id"):
            return attr["id"].value
        
        elif node.nodeType == node.TEXT_NODE:
            return node.nodeValue
            
    def IsExpandable(self):
        node = self.node
        return node.hasChildNodes()
    
    def GetSubList(self):
        parent = self.node
        children = parent.childNodes
        prelist = [DomTreeItem(node) for node in children]
        itemlist = [item for item in prelist if item.GetText().strip()]
        return itemlist

    #def OnDoubleClick(self):
    #    if len(self.GetSubList()) == 0:
    #        #print self.GetText()
    #        os.startfile(self.GetText())
    #    #print 'dbclick'


def del_file():
    global gFile, gNode    
    
    if gFile:
        try:            
            os.remove(gFile)        
        except:
            pass

        # remove node
        for c in gNode.children:            
            #<name>
            for d in c.item.GetSubList():
                #<item>
                #print d.GetText()
                if gFile ==  d.GetText():
                    c.item.node.removeChild(d.node)
                    c.children = []
                    c.update()
                    c.expand()

        print "%s => deleted" % gFile
        
def view_file():
    global gFile
    if gFile:
        os.startfile(gFile)
        
    #print "view"    
    #pass
   
def view_result(data):
    root = Tk()
    root.title("View Result")
    menu = Menu(root, tearoff=0)
    menu.add_command(label=u"檢視", command=view_file)
    menu.add_command(label=u"刪除", command=del_file)

    global gMenu, gNode
    gMenu = menu
        
    sbar = Scrollbar(root)
    canvas = Canvas(root)

    canvas.config(bg='white', scrollregion=(0,0,300, 1000))
    sbar.config(command=canvas.yview)
    sbar.pack(side='right', fill="y")   
    canvas.config(yscrollcommand=sbar.set) 
    canvas.pack(side="left", expand=1, fill="both")

    dom = parseString(data)
    
    item = DomTreeItem(dom.documentElement)
    node = MyTreeNode(canvas, None, item)

    node.update()
    node.expand()
    gNode = node
    #node.dump()
    
    root.mainloop()

if __name__ == '__main__':    
    data = u'''
    <list id="中文Result">
     <name id="a.pdf">
         <item id="c:\\a.pdf" />
         <item id="2" />     
     </name>
    </list>
    '''

    view_result(data.encode('utf-8'))

