#-*- coding: UTF-8 -*-
__author__ = "Chui-Wen Chiu"
__author_email__ = "cwchiu@hotmail.com"

import tempfile

class Logger():
    def __init__(self):
        self.fn = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
    def close(self):
        self.fn.close()
    def append(self, msg):
        self.fn.writelines('%s\r\n' % msg)
    def __getattr__(self, name):
        if(name=='name'):
            return self.fn.name

class RepeatableTimer(object):
    """
    example: 
    def doIt():
      print 1
    tmr = RepeatableTimer(1, doIt)
    tmr.start()
    """
    def __init__(self, interval, function, args=[], kwargs={}):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def start(self):
        self.stop()
        import threading
        self._timer = threading.Timer(self.interval, self._run)
        self._timer.setDaemon(True)
        self._timer.start()

    def restart(self):
        self.start()

    def stop(self):
        if self.__dict__.has_key("_timer"):
            self._timer.cancel()
            del self._timer

    def _run(self):
        try:
            self.function(*self.args, **self.kwargs)
        except:
            pass
        self.restart()