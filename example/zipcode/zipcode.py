# -*- coding: cp950 -*-
#-*- coding: utf-8 -*-
"""
Description: �ƥ� Facebook ��ï

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


    city=[u"�x�_��", u"�򶩥�", u"�x�_��", u"�y����", u"�s�˥�",
          u"�s�˿�", u"��鿤", u"�]�߿�", u"�x����", u"�x����",
          u"���ƿ�", u"�n�뿤", u"�Ÿq��", u"�Ÿq��", u"���L��",
          u"�x�n��", u"�x�n��", u"������", u"������", u"���",
          u"�̪F��", u"�x�F��", u"�Ὤ��", u"������", u"�s����",
          u"�n���Ѯq", u"�����x�C��"]

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
