from urllib import request
from urllib import parse
from http import cookiejar
filename = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar(filename)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

cookie2= cookiejar.MozillaCookieJar()
cookie2.load('cookie.txt', ignore_discard=True, ignore_expires=True)
req = request