# -*- coding: utf-8 -*-
"""
Description: 取出指定標籤的所有連結

"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"


import apsw
import os
from datetime import datetime


def query(FeedDemonPath, tag):
    FeedDemonPath = os.path.join(FeedDemonPath, 'v1')
    db = apsw.Connection( os.path.join(FeedDemonPath, 'tags.fdb'))
    cur = db.cursor()
    cur.execute("select fd_postid from tbl_tags where tag_name = '"+tag+"'")
    # 列出所有 tag
    # cur.execute("select tag_name from tbl_tags group by tag_name")
    ids = cur.fetchall()
    db.close()

    sql = "select link from tbl_posts where fd_postid in ('" + "','".join([row[0] for row in ids]) + "')"
    db = apsw.Connection( os.path.join(FeedDemonPath, 'feeds.fdb'))
    cur = db.cursor()
    cur.execute(sql)

    fn = open("%s_%s" % (tag, datetime.now().strftime("%Y%m%d%H%M%S")), 'w')
    for row in cur:
        fn.write( row[0] )
        fn.write( '\n')
        
    fn.close()    
    db.close()

FeedDemonPath = r'H:\FeedDemon-data'

tag = u'php'
query(FeedDemonPath, tag)
                          
