import pickle
import os

content = file('banner.p')
data=pickle.load(content)
out = file('result.txt', "w")
for item in data:
    for elem in item:
        out.write( elem[0]*int(elem[1]))
    out.write("\n")
out.close()           
os.startfile('result.txt')    
