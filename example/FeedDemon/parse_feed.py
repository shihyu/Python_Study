# -*- coding: utf-8 -*-
import sys, win32console, codecs
reload(sys)
sys.setdefaultencoding('utf-8')
win32console.SetConsoleCP(65001)
win32console.SetConsoleOutputCP(65001)
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)
    
import OPML
opml = OPML.parse(r'H:\FeedDemon-data\v1\Subscriptions.opml')
for o in opml.outlines:

	print '[',o['text'], ']'
	for o2 in o.children:
		if 'title' in o2:
			print '\t',o2['title'], '(', o2['fd:feedId'], ')'
		else:
			print '\t[',o2['text'], ']'
			for o3 in o2.children:
				print '\t\t',o3['title'], '(', o3['fd:feedId'], ')'
