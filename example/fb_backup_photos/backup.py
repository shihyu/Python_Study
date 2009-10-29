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

import facebook
import json
import os
import urllib
import pickle
import getopt, sys

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

    # 取得相簿列表
    album_list = fb.fql.query('SELECT aid,name FROM album WHERE owner= '+ str(uid) )
    album_total = len(album_list)
    album_i = 1
    for album in album_list:
        print "Album %d/%d: %s" % (album_i, album_total, album['name'])
        
        # 建立相簿目錄
        CreateDir( album['name'] )
        folder = os.path.join(app_root, album['name'])
        aid = album['aid']
        
        # 取得相片列表
        photo_list = fb.fql.query('SELECT src_big FROM photo WHERE aid=' + aid)
        photo_total = len( photo_list)
        photo_i = 1
        for photo in photo_list:
            photo_name = photo['src_big'].split('/')[-1]
            print "\tPhoto %d/%d: %s" % (photo_i, photo_total, photo_name)            
            # 下載相片
            inf =urllib.urlopen(photo['src_big'])
            fn = os.path.join(folder, photo_name)
            open(fn, "wb").write(inf.read())
            photo_i += 1
            
        album_i += 1         

def usage():
    print 'help'
    
if __name__ == '__main__':
    if len(sys.argv)==1:
        backup_photos()
    else:
        
        try:
            opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["uid="])
        except getopt.GetoptError, err:
            # print help information and exit:
            print 'def'
            usage()
            sys.exit(2)
        output = None
        verbose = False
        for o, a in opts:
            if o == "-v":
                verbose = True
            elif o in ("-u", "--uid"):
                backup_photos(a)
            else:
                backup_photos()
        
