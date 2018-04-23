import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import re
import time


def sina():
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 ' \
                          '(Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 ' \
                          '(KHTML, like Gecko) Version/5.1 Safari/534.50'


    ii = 0
    while ii <10000:
        ii = ii + 1
        url = 'https://m.weibo.cn/api/comments/show?id=4171979403983768&page='+str(ii)
        html = requests.get(url, headers=headers)
        # html = requests.get(url,headers=headers,proxies=proxies)

        try:
            for jj in range(0,len(html.json()['data']['data'])):
                # print(html.json()['data']['data'][jj]['text'])
                data = html.json()['data']['data'][jj]['text']
                print( ''.join(re.findall('[\u4300-\u9fa5]',data)))
                # with open('E:\\Graduation design\\gd\\sina_data\\weibo5.txt','a',encoding='utf-8') as ff:
                #     hanzi = ''.join(re.findall('[\u4300-\u9fa5]',data))
                #     # print(str(hanzi))
                #     ff.write(str(hanzi)+'\n')
        except ReadTimeout:
            print('time out')

        except HTTPError:
            print('htt perror')

        except RequestException:
            print('request error')

        time.sleep(2)

sina()