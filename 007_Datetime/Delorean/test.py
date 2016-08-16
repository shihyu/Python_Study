from delorean import parse

v1='2016-08-15T09:25:50.000 UTC'
# str to Delorean
d1 = parse(v1)
print(d1)
# timezone to 'Asia/Taipei'
taipei = d1.shift('Asia/Taipei')
print(taipei)
# unix timestamp
print(taipei.epoch)
# to datetime
print(taipei.datetime)

