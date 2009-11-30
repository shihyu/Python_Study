import re
content=file('d:\\lv3.data').read()
print ''.join(re.findall('[a-z]{1}[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]{1}', content))


             
