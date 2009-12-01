import pickle
import os

content = file('d:\\banner.p')
data=pickle.load(content)
out = file('d:\\result.txt', "w")
for item in data:
    for elem in item:
        out.write( elem[0]*int(elem[1]))
    out.write("\n")
out.close()           
os.startfile('d:\\result.txt')    
