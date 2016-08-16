#-*- coding: UTF-8 -*-
"""
Description: 列舉相簿與所屬的相片列表

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import gdata.photos.service
import gdata.media
import gdata.geo

gd_client = gdata.photos.service.PhotosService()

# 登入
gd_client.email = email
gd_client.password = password
gd_client.source = 'exampleCo-exampleApp-1'
gd_client.ProgrammaticLogin()

# 相簿列表
albums = gd_client.GetUserFeed(user=username)
for album in albums.entry:
  print 'title: %s, number of photos: %s, id: %s' % (album.title.text,
      album.numphotos.text, album.gphoto_id.text)

# 相片列表
photos = gd_client.GetFeed(
    '/data/feed/api/user/%s/albumid/%s?kind=photo' % (
        username, album.gphoto_id.text))
for photo in photos.entry:
  # 相片標題和 URL  
  print 'title: %s, %s' %( photo.title.text, photo.content.src) 
