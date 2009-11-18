# -*- coding: cp950 -*-
#-*- coding: utf-8 -*-
"""
Description: 備份 Facebook 相簿

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import sqlite3

DB_NAME = "city-tw.db"

def create_db():
    sql_city = """
    CREATE TABLE IF NOT EXISTS city(
        id INTEGER   PRIMARY   KEY,
        name TEXT
    );
    """
    sql_area = """
    CREATE TABLE IF NOT EXISTS area(
        id INTEGER   PRIMARY   KEY,
        name TEXT,
        city_id INTEGER
    );
    """

    sql_insert_city = """
    REPLACE INTO city(id, name) VALUES(?,?)
    """

    sql_insert_area = """
    REPLACE INTO area(id, name, city_id) VALUES(?,?,?)
    """

    db = sqlite3.connect(DB_NAME)
    cur= db.cursor()
    cur.execute(sql_city)
    cur.execute(sql_area)


    city=[u"台北市", u"基隆市", u"台北縣", u"宜蘭縣", u"新竹市",
          u"新竹縣", u"桃園縣", u"苗栗縣", u"台中市", u"台中縣",
          u"彰化縣", u"南投縣", u"嘉義市", u"嘉義縣", u"雲林縣",
          u"台南市", u"台南縣", u"高雄市", u"高雄縣", u"澎湖縣",
          u"屏東縣", u"台東縣", u"花蓮縣", u"金門縣", u"連江縣",
          u"南海諸島", u"釣魚台列嶼"]

    for i,c in enumerate(city):
        cur.execute(sql_insert_city, ( str(i+1), c,))
    db.commit()


    area = {}
    #cur = None
    key = None

    for line in open('zipdata.txt'):
        data= line.strip()
        if '#' in data:
            key = int(data.replace('#', ''))        
            #cur = area[key] = []
            print key
            continue
        else:

            data  = filter( lambda x: len(x)>0, data.split(' '))
            #print data
            #print data[0], data[1]        
            #cur.append( {"id": data[1], "name": data[0]})
            cur.execute(sql_insert_area, (int(data[1]), str.decode(data[0], 'big5'), key,))

    db.commit()
    db.close()

def test():
    db = sqlite3.connect(DB_NAME)
    cur= db.cursor()
    cur.execute('select count(*) from area where city_id = 25')
    print cur.fetchone()
    db.close()
