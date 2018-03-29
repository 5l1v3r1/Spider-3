url='https://zhaoqing.anjuke.com/sale/?from=navigation'
import requests
import copyheaders
headers=b'''accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding:gzip, deflate, br
accept-language:zh-CN,zh;q=0.9
upgrade-insecure-requests:1
user-agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'''

print(requests.get(url,copyheaders.headers_raw_to_dict(headers)).text)

