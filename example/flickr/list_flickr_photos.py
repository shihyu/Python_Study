#-*- coding: UTF-8 -*-
"""
Description: 列舉 Flickr 的相簿與所屬相片

修改 FlickrAPI(http://stuvel.eu/projects/flickrapi) 的 get_token 和 get_token_part_one，加上
self.uid= rsp.auth[0].user[0].attrib['nsid']
使其驗證後取得 user id

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import flickrapi
api_key  = '9da90695b0a484e5706eceb26cafba8f'
api_secret = '989274be50e754b4'
flickr = flickrapi.FlickrAPI(api_key, api_secret)

# 取得授權
(token, frob) = flickr.get_token_part_one(perms='read')
if not token:
    raw_input("Press ENTER after you authorized this program")

flickr.get_token_part_two((token, frob))

# 相簿列表
sets = flickr.photosets_getList(user_id= flickr.uid)
for ph in sets.find('photosets').findall('photoset'):    
    print '%s: %s' % (ph.attrib['id'], ph.find('title').text)
    photos = flickr.photosets_getPhotos(photoset_id=ph.attrib['id'])
    # 相片列表
    for p in photos.find('photoset').findall('photo'):
        sl = flickr.photos_getSizes( photo_id= p.attrib['id'] )
        print sl.find('sizes').findall('size')[-1].attrib['source']            
                

