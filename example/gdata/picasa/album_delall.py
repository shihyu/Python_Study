#-*- coding: UTF-8 -*-
"""
Description: 刪除所有的 Picasa 相簿

Author: Chui-Wen Chiu <sisimi.pchome@gmail.com>
License: PYTHON SOFTWARE FOUNDATION LICENSE
"""

__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import getopt, sys
import gdata.photos, gdata.photos.service
def delete_all_albums(id, pwd):
	pws = gdata.photos.service.PhotosService()
	pws.ClientLogin(id,pwd)
	albums = pws.GetUserFeed().entry
	for album in albums:
	  pws.Delete(album)	

if __name__ == '__main__':

  try:
    opts, args = getopt.getopt(sys.argv[1:], '',
                               ['name=', 'pwd='])
  except getopt.error, msg:
    printHelp()


  name = None
  pwd = None
  for option, arg in opts:
    if option == '--name':
      name = arg
    elif option == '--pwd':
      pwd = arg
  if(name is None):
    name = raw_input('username: ')

  if(pwd is None):
    pwd = raw_input('password: ')

  delete_all_albums(name, pwd)