#-*- coding: utf-8 -*-
"""
Description: 備份 Facebook 相簿

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import warnings
warnings.simplefilter('ignore',DeprecationWarning)

import sqlite3
import facebook
import json
import os
import urllib
import pickle
import getopt, sys

sql_blog = """
CREATE TABLE IF NOT EXISTS blog(
    id INTEGER   PRIMARY   KEY,
    title TEXT,
    content TEXT,
    updated_time  TEXT
);
"""
sql_insert_blog = "REPLACE INTO blog(id, title, content, updated_time) VALUES(?,?,?,?)"


sql_link = """
CREATE TABLE IF NOT EXISTS link(
    id INTEGER   PRIMARY   KEY,
    summary TEXT, 
    created_time TEXT,
    title TEXT,
    url TEXT,
    owner_comment TEXT
);
"""
sql_insert_link = "REPLACE INTO link(id, summary, created_time, title, owner_comment, url) VALUES(?,?,?,?,?,?)"

fql_select_link = """
SELECT link_id,summary,created_time,title,owner_comment,url 
FROM link WHERE owner= {0}
ORDER BY created_time DESC
"""

fql_select_blog = """
SELECT title,note_id,updated_time,content
FROM note WHERE uid= {0}
ORDER BY updated_time DESC
"""


def CreateDir(fd):
    if(not os.path.exists(fd)):
        os.makedirs( fd )
        
fn_session = 'session.p'

def backup_photos(uid=None):
    api_key = '2fedd011f2c2f62bebc0971f438789e0'
    secret_key ='d4792f9c70daf4fd9b549fb4a0312744'

    fb = facebook.Facebook(api_key, secret_key)

    try:
        # 自動登入
        if os.path.exists(fn_session):
            session = pickle.load(open(fn_session, 'rb'))

            fb.session_key = session['session_key']
            fb.secret = session['secret']
            fb.uid = session['uid']            
            fb.session_key_expires = session['expires']
        else:
            raise Exception()        
    except:
        # 手動登入
        fb.session_key = None
        fb.secret = None
        fb.auth.createToken()    
        fb.login() 
        raw_input('after Login to press "ENTER"')
        session = fb.auth.getSession()
        pickle.dump(session, open(fn_session, "wb"))        

    if uid == None:
        uid = fb.uid
        
    print "user id: %s" % uid
    
    app_root = os.getcwd()

    db = sqlite3.connect("{0}.db".format(uid) )
    cur= db.cursor()
    cur.execute(sql_blog)
    cur.execute(sql_link)
    
    # 取得網誌列表
    note_list = fb.fql.query(fql_select_blog.format(str(uid)) )
    note_total = len(note_list)
    note_i = 1
    for note in note_list:
        print 'Blog: %d/%d' %(note_i, note_total)
        print note['title']
        #title,note_id,updated_time,content
        note_i += 1
        #sql_insert_blog = "REPLACE INTO blog(id, title, content, update_time) VALUES(?,?,?,?)"
        cur.execute(sql_insert_blog, (note['note_id'],note['title'],note['updated_time'],note['content'],))
    db.commit()
    
    # 取得連結列表
    link_list = fb.fql.query(fql_select_link.format(str(uid)) )
    link_total = len(link_list)
    link_i = 1
    for link in link_list:
        print 'Link: %d/%d' %(link_i, link_total)
        print link['title']
        #summary,created_time,title,owner_comment,url,image_urls 
        link_i += 1
        #sql_insert_link = "REPLACE INTO link(id, summary, created_time, title, owner_comment) VALUES(?,?,?,?,?)"
        cur.execute(sql_insert_link, (link['link_id'],link['summary'],link['created_time'],link['title'],link['owner_comment'],link['url'],))
    db.commit()
    
if __name__ == '__main__':
    if len(sys.argv)==1:
        backup_photos()
    else:
        
        try:
            opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["uid="])
        except getopt.GetoptError, err:
            sys.exit(2)
        output = None
        verbose = False
        for o, a in opts:
            if o == "-v":
                verbose = True
                print 'v0.1'
            elif o in ("-u", "--uid"):
                backup_photos(a)
            else:
                backup_photos()
        
