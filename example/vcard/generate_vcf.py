# -*- coding: utf-8 -*-
import sys, random, codecs, os.path, base64

'''
輸出 vCard

Chui-Wen Chiu

@ref
http://stronglyemergent.com/blog/2011/generating-vcards-in-python/
http://softwareas.com/vcard-for-developers
'''
def fill_card(data):
    new_card = ["BEGIN:VCARD", "VERSION:2.1",]
    new_card.append("REV:%d" % random.randrange(100,500))
    if "Last Name" in data or "First Name" in data:
        namefield = "N:"
        namefield += unicode(data['Last Name']) if "Last Name" in data else ""
        namefield +=";"
        namefield += unicode(data['First Name']) if "First Name" in data else ""
        new_card.append(namefield)

        fnamefield = "FN:"
        fnamefield += unicode(data['First Name']) if "First Name" in data else ""
        fnamefield += " "
        fnamefield += unicode(data['Last Name']) if "Last Name" in data else ""
        new_card.append(fnamefield)
    
    if "Email" in data:
        emailfield = "EMAIL;PREF;INTERNET:"
        emailfield += str.lower(data['Email'])
        new_card.append(emailfield)
        
    # 需要的自己加
    # http://en.wikipedia.org/wiki/VCard
    map = {
      'TEL HOME': 'TEL;HOME:',
      'TEL WORK': 'TEL;WORK:',
      'Title': 'TITLE:',
      'Address HOME': 'ADR;HOME:;;',
      'Address WORK': 'ADR;WORK:;;',
      'Organization' : 'ORG:'
    }
    
    for v in map:
        if v in data:
            field = map[v]
            field += unicode(data[v])
            new_card.append(field)
        
        
    if 'Photo' in data and os.path.exists(data['Photo']):        
        field = 'PHOTO;ENCODING=BASE64;JPEG:'
        with open(data['Photo'], 'rb') as photo_f:
            field += base64.b64encode(photo_f.read())            
        new_card.append(field)
        new_card.append('')
    
    new_card.append("END:VCARD")
    return new_card
    
def gen_vcf(vcf_file, datas):
    with codecs.open(vcf_file, 'w', 'utf-8') as vcf_out:
        for data in datas:
            card = fill_card(data)
            for card_line in card:
                vcf_out.write(card_line)
                vcf_out.write("\n")
                
if __name__ == '__main__':
    datas = [{
            'First Name' : u'01代書',
            'Last Name' : u'無名氏',
            'TEL HOME' : '0933124567',
            'TEL WORD' : '021234567',
            'Photo' : r'c:\1188243673.jpg',
            'Title' : u'代書',
            'Address HOME' : u'台北市中正一路3號',
            'Address WORK' : u'台北市中正一路4號',
            'Organization' : u'xx工會',
        }]
    vcf_file = r'C:\test.vcf'
    gen_vcf(vcf_file, datas)
        
