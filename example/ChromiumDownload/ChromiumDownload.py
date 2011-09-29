import urllib
url = "http://build.chromium.org/f/chromium/snapshots/Win_Webkit_Latest/"
build_id = urllib.urlopen(url + "LATEST").read()
urllib.urlretrieve (url +  build_id + '/chrome-win32.zip', "chrome-win32("+build_id+").zip")



