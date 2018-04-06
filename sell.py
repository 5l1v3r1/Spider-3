from requests import session
from copyheaders import headers_raw_to_dict
import re
import time
import requests_html
# url=input("请输入url \n")
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
driver=webdriver.PhantomJS(r'C:\Users\战神皮皮迪\Downloads\phantomjs-2.1.1-windows\bin\phantomjs.exe')

    
def get_content(i):
    driver.get('https://shopsearch.taobao.com/search?app=shopsearch&q=%E6%B5%B4&imgfile=&commend=all&ssid=s5-e&search_type=shop&sourceId=tb.index&spm=a21bo.1000386.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc&isb=0&shop_type=&ratesum=&qq-pf-to=pcqq.c2c&s={}'.format(i*20))
    content=driver.page_source
    if len(driver.page_source)<500:
        get_content(i)
    else:
        nick=re.findall('"nick":"(.*?)","provcity',content)
        print(nick)
for i in range(1,100):
    get_content(i)
