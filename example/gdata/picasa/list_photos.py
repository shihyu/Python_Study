#-*- coding: UTF-8 -*-
"""
Description: �C�|��ï�P���ݪ��ۤ��C��

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import gdata.photos.service
import gdata.media
import gdata.geo

gd_client = gdata.photos.service.PhotosService()

# �n�J
gd_client.email = email
gd_client.password = password
gd_client.source = 'exampleCo-exampleApp-1'
gd_client.ProgrammaticLogin()

# ��ï�C��
albums = gd_client.GetUserFeed(user=username)
for album in albums.entry:
  print 'title: %s, number of photos: %s, id: %s' % (album.title.text,
      album.numphotos.text, album.gphoto_id.text)

# �ۤ��C��
photos = gd_client.GetFeed(
    '/data/feed/api/user/%s/albumid/%s?kind=photo' % (
        username, album.gphoto_id.text))
for photo in photos.entry:
  # �ۤ����D�M URL  
  print 'title: %s, %s' %( photo.title.text, photo.content.src) 
