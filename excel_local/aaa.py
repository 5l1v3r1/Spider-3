import requests
import copyheaders
header=b''':authority: maps.googleapis.com
:method: GET
:path: /maps/api/js/AuthenticationService.Authenticate?1shttps%3A%2F%2Fwww.unitedstateszipcodes.org%2F&4sAIzaSyA11LGixNdjBOJIKIgJM51_8JL11Ow7NXw&callback=_xdc_._uxz8ey&token=126211
:scheme: https
accept: */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
referer: https://www.unitedstateszipcodes.org/
user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
x-client-data: CKS1yQEIlLbJAQiktskBCMG2yQEIqZ3KAQioo8oB'''
print(requests.get('https://www.unitedstateszipcodes.org/',headers=copyheaders.headers_raw_to_dict(header)).content)
