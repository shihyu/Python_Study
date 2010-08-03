import urllib
url = "http://build.chromium.org/buildbot/snapshots/chromium-rel-xp/"
build_id = urllib.urlopen(url + "LATEST").read()
urllib.urlretrieve (url +  build_id + '/chrome-win32.zip', "chrome-win32("+build_id+").zip")
