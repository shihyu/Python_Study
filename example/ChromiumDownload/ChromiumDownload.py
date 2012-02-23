import urllib
#url = "http://build.chromium.org/f/chromium/snapshots/Win_Webkit_Latest/"
url = 'http://commondatastorage.googleapis.com/chromium-browser-snapshots/Win/'
build_id = urllib.urlopen(url + "LAST_CHANGE").read()
urllib.urlretrieve (url +  build_id + '/chrome-win32.zip', "chrome-win32("+build_id+").zip")
#urllib.urlretrieve ('http://download-chromium.appspot.com/dl/Win', "chrome-win32.zip")

