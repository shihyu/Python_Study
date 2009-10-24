import sqlite3
db = sqlite3.connect("d:\\t.db")
cur= db.cursor()
db.text_factory=lambda x: unicode(x, "utf-8", "ignore")
sql_bible = """
CREATE TABLE IF NOT EXISTS bible(
    id INTEGER   PRIMARY   KEY   AUTOINCREMENT,
    name TEXT,
    sname TEXT,
    memo TEXT,
    catelogy INTEGER
);
"""
cur.execute(sql_bible)

sql_section = """
CREATE TABLE IF NOT EXISTS section(
    id INTEGER   PRIMARY   KEY   AUTOINCREMENT,
    n INTEGER,
    m INTEGER,
    content TEXT,
    bible_id INTEGER
);
"""


cur.execute(sql_section)
f=file("d:\\bible.txt")
table = {}
i=1
for n,ln in enumerate(f):
    a,b,c,d= ln.split('-')
    table[a]={"id":i, "name":b}
    cur.execute('REPLACE INTO bible(name, sname,catelogy) VALUES(?,?,?)',(b,c,d,))
    ++i
db.commit()

#print table
#print table["Gen"]

import re
f=file("d:\\cniv.dat")
regex = re.compile('(.*)[ ][a-z]*(\d+):(\d+)\t(.*)')

for i,ln in enumerate(f):
    ret = regex.search(ln)
    if ret == None:
        print ln
        continue
    
    a,n,m,c = ret.groups()
    #print table[a]['name'], n,m,c
    cur.execute('REPLACE INTO section(n, m,content,bible_id) VALUES(?,?,?,?)',(int(n), int(m), c, table[a]['id'],))
db.commit()
