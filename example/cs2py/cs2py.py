import re
def convertFile():
    content = file('d:\\cs.data').read()
    content = content.replace("//", "#")\
                .replace("this.", "self.")\
                .replace("new ", "")\
                .replace("System.Drawing.", "")\
                .replace("System.Windows.Forms.", "")\
                .replace("System.ComponentModel.", "")\
                .replace("System.IO.", "")\
                .replace("System.Timers.", "")\
                .replace("null", "None")\
                .replace("string.Empty", "''")\
                .replace(";", "")\
                .replace("&&", "and")\
                .replace("||", "or")\
                .replace("false", "False")\
                .replace("true", "True")\
                .replace("System.Drawing.", "")\
                .replace("else if", "elif:")\
                .replace("else", "else:")\
                .replace("catch", "except:")\
                .replace("Control[]", "Array[Control]")

    content = re.sub('(.*) System\.EventHandler\((.*)\)', "\\1 \\2", content)
    content = re.sub('(.*) System\.Timers\.ElapsedEventHandler\((.*)\)', "\\1 \\2", content)    
    #.replace("if", "if:")\
    #.replace("try", "try:")\
    print content            

def createProp(name):
    print """
    @property 
    def {0}(self): 
        return self._{0} 

    @{0}.setter 
    def {0}(self, value): 
        self._{0} = value 
""".format(name)
    
def createEvent(name):
    print """
def %s(self, sender, e):
    pass
""" %name

def createMethod(name):
    print """
def %s(self):
    pass
""" %name

def batchMethod():
    names = [
        'buttonOk_Click',
        'lbFormatsInputListbox_SelectedIndexChanged'

    ]
    for n in names:
        createEvent(n)    

def batchEvent():
    names = [
        'checkboxRecord_CheckedChanged',
        'buttonSoundfile_Click',
        'MainForm_Closing'

    ]
    for n in names:
        createEvent(n)    

#createProp('Effect')
#batchEvent()        
#batchMethod()
convertFile()

#createProp('InputFormat')
