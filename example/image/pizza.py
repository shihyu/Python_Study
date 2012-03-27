# «÷¹Ï
import Image
import glob
import re
names = glob.glob("c:\\temp\\*.jpg")
# here we need to sort this names to make it as the order we want
one=3
two=5
three=4
origx=0
origy=0
format = 'RGBA'
finalim = Image.new(format,(1500,1187))
#count=0
k=1
for i in range(two+1):
    for j in range(three+1):
        name = str(one)+"-"+str(i)+"-"+str(j)+".jpg"
        im = Image.open("c:\\temp\\"+name)
        x,y = im.size
        if k%(three+1) == 0:
            #print name, origx, origy, origx+x, origy+y
            finalim.paste(im, (origx, origy, origx+x, origy+y))
            origx = origx + x
            origy = 0
            #print "next column"
        else:
            #print name, origx, origy, origx+x, origy+y
            finalim.paste(im, (origx, origy, origx+x, origy+y))
            origy = origy + y
        k += 1
finalim.save("c:\\temp\\mypic.jpg")
        #count+=1
#print count
'''
for name in names:
    base, ext = os.path.splitext(os.path.basename(name))
    one, two, three = base.split("-")
    filename=one+"-"+two+"-"+three
    print filename


num = len(names)
print num

i=1
origx=0
origy=0
format = 'RGBA'
finalim = Image.new(format,(3516,2647))
for name in names:
    base, ext = os.path.splitext(os.path.basename(name))
    one, two, three = base.split("-")
    print one,"-",two,"-",three
    im = Image.open(name)
    x,y = im.size
    if i%11 == 0:
        print name, origx, origy, origx+x, origy+y
        #finalim.paste(im, (origx, origy, origx+x, origy+y))
        origx = origx + x
        origy = 0
        print "next column"
    else:
        print name, origx, origy, origx+x, origy+y
        #finalim.paste(im, (origx, origy, origx+x, origy+y))
        origy = origy + y
    i += 1
'''
finalim.show()