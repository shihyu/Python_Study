"""
讀取網卡號碼
"""
import pcap  
import dpkt  
  
aaa='a'  
bbb='b'  
pc=pcap.pcap()    #注，參數可為網卡名，如eth0  
pc.setfilter('tcp port 80')    #設置監聽過濾器  
  
for ptime,pdata in pc:    #ptime為收到時間，pdata為收到數據  
    p=dpkt.ethernet.Ethernet(pdata)  
    if p.data.__class__.__name__=='IP':  
        ip='%d.%d.%d.%d'%tuple(map(ord,list(p.data.dst)))  
        if p.data.data.__class__.__name__=='TCP':  
            if p.data.data.dport==80:  
               #print p.data.data.data  
               sStr1 = p.data.data.data  
               sStr2 = 'Host: '  
               sStr3 = 'Connection'  
               sStr4 = 'GET /'  
               sStr5 = ' HTTP/1.1'  
               nPos = sStr1.find(sStr3)  
               nPosa = sStr1.find(sStr5)                 
               for n in range(sStr1.find(sStr2)+6,nPos-1):  
                   aaa=sStr1[sStr1.find(sStr2)+6:n]                 
               for n in range(sStr1.find(sStr4)+4,nPosa+1):                 
                   bbb=sStr1[sStr1.find(sStr4)+4:n]  
               ccc=aaa+bbb  
               print ccc   