import re
import urllib
#s='and the next nothing is 92512'
def extract_n(s):
    print s
    n, = re.search('the next nothing is (\d+)',s, re.M).groups()
    return n

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
#n = '12345'
n='46059'
#result = [12345]
for i in range(400):
    s = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + n).read()
    n = extract_n(s)
#    result.append(n)
#print ''.join(result)    
