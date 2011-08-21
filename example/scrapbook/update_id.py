import codecs, glob,os,time
from datetime import datetime

def update_id(index_dat):
    fn = codecs.open(index_dat, 'r', 'utf-8');
    c=fn.read()
    fn.close()
    lines = c.split('\n')
    line_id = lines[0].split('\t')
    line_id[1] = datetime.now().strftime("%Y%m%d%H%M%S")
    lines[0] = '\t'.join(line_id)
    
    codecs.open(index_dat, 'w', 'utf-8').write('\n'.join(lines))
    print 'ok'
for fn in glob.glob('c:\\b\\*'):
          
    update_id(os.path.join(fn, 'index.dat'))
    time.sleep(1)	