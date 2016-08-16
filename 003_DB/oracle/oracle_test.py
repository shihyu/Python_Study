#!/usr/bin/env python
#
#
import cx_Oracle;
import sys;
import time,datetime;
import random;
 
TT_ALARM_RAISETIME = datetime.datetime(2008, 8, 2, 12, 30, 25)
IncidentNum = 60000000001;
SERVICEID = '987654321';
counter = 0;


   
while(True):
    IncidentID='SOS'+str(IncidentNum);
    TTNONCOMPELLINGDURATION=1
    TTCOMPELLINGDURATION = random.randint(0,5);
    SERVICEID=random.randint(1,100);
    ranNum=random.randint(1,100);
    TT_ALARM_RAISETIME = TT_ALARM_RAISETIME+ datetime.timedelta(seconds=60)
    if ranNum>10:
        OPENCODE='closed';
    else:
        OPENCODE='open - idle';
        
        
    try:
        my_conn = cx_Oracle.connect("DEMO6","DEMO6","BEAVER.JAVAEYE.COM")
        my_cursor = my_conn.cursor();
        nowTime = datetime.datetime.now()
        #SYSTEMMODTIME = time.strftime('%Y-%m-%d %H:%M:%S', nowTime)
        #SYSTEMMODTIME=datetime.strptime(nowTime, "%Y-%m-%d %H:%M:%S")
        SYSTEMMODTIME= str(nowTime)[0:19]
       
        #print("SYSTEMMODTIME==", SYSTEMMODTIME)
      
        sql="""insert into INCIDENTSM1(INCIDENT_ID, TT_ALARM_RAISETIME,TT_COMPELLING_DURATION, TT_NON_COMPELLING_DURATION, RESOLUTION_CODE, OPEN, SERVICE_ID, SYSMODTIME) values('%s',to_date('%s', 'YYYY-MM-DD HH24:MI:SS'), %s, %s,'3.SAHIS HASARLARI', 'closed', '%s', to_date('%s', 'YYYY-MM-DD HH24:MI:SS')) """ % (IncidentID,TT_ALARM_RAISETIME, TTCOMPELLINGDURATION, TTNONCOMPELLINGDURATION, SERVICEID, SYSTEMMODTIME)
        print("sql==", sql)
        my_cursor.execute(sql)
        my_conn.commit()
      
    except:
        sys.stderr.write("execute sql error\n")
    finally:
        my_cursor.close();
        my_conn.close();
    IncidentNum+=1