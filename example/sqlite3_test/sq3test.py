#-*- coding: UTF-8 -*-
"""
Description: SQLite3 CRUD 測試

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import sqlite3
db = sqlite3.connect("d:/data.db")
cur= db.cursor()

# Create Table
create_songbook_sql = """
CREATE TABLE IF NOT EXISTS songbook(
    id INTEGER   PRIMARY   KEY   AUTOINCREMENT,
    serial TEXT,
    name TEXT
);
"""
create_lyrics_sql = """
CREATE TABLE IF NOT EXISTS lyrics (
    id INTEGER   PRIMARY   KEY,
    songbook_id INTEGER,   
    name TEXT
);
"""
cur.execute(create_songbook_sql)
cur.execute(create_lyrics_sql)


#select
count_sql='SELECT COUNT(*) FROM songbook WHERE serial=?'
cur.execute(count_sql, ('0001',))
count= cur.fetchone()[0]
print count

if count > 0:
    # update
    cur.execute('UPDATE songbook SET name=? WHERE serial=?', ('xxxx', '0001',) )

    # read
    cur.execute('SELECT id,serial,name FROM songbook WHERE serial=?', ('0001',) )
    id, serial, name = cur.fetchone()
    print id, serial, name
    
    #delete
    delete_sql = 'DELETE FROM songbook WHERE serial=?'
    cur.execute(delete_sql, ('0001', ));
    db.commit()
    
#insert
insert_songbook_sql = 'INSERT INTO songbook(serial, name) VALUES(?,?)';
cur.execute(insert_songbook_sql, ('0001', u'新靈糧詩選',));
db.commit()

db.close()
