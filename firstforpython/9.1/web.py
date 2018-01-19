import urllib.request as ur
import http

url = 'http://quotesondesign.com/wp-json/posts'
conn = ur.urlopen(url)

for key, value in conn.getheaders():
    print(key, value)



