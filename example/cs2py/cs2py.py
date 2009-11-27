import re
content = file('d:\\cs.data').read()
content = content.replace("//", "#")\
            .replace("this.", "self.")\
            .replace("new System.Drawing.", "")\
            .replace("false", "False")\
            .replace("true", "True")\                        
            .replace("System.Drawing.", "")

content = re.sub('(.*) new System\.EventHandler\((.*)\);', "\\1 \\2", content)
print content            
