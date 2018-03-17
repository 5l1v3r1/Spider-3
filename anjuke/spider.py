import requests
import copyheaders
from  lxml import etree
import time
import re

headers=b'''accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding:gzip, deflate, br
accept-language:zh,en-US;q=0.9,en;q=0.8
cache-control:max-age=0
upgrade-insecure-requests:1
user-agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'''


class anjuke(object):

    def get_list(self,city):#获取该城市的所有地区的url
        area_all_url=[]
        url='https://{}.anjuke.com/sale/?from=navigation'.format(city)
        content=self.download(url)
        selector=etree.HTML(content)
        area_list=selector.xpath('//*[@id="content"]/div[3]/div[1]/span[2]/a/@href')
        for area_url in area_list:
            next_content=self.download(area_url)
            sel=etree.HTML(next_content)
            area_list_url=sel.xpath('//*[@id="content"]/div[3]/div[1]/span[2]/div/a/@href')
            for url in  area_list_url:
                area_all_url.append(url)
        print("---------获取所有的url成功-----------")
        return area_all_url

    def download(self,url):
        time.sleep(1)
        content = requests.get(url,headers=copyheaders.headers_raw_to_dict(headers)).text
        return content

    def ever_page(self,urls):
        for url in  urls:#遍历每个城市的地区
            for i in range(1,50):
                complete_url=url+'p{}/'.format(i)
                city=''.join(re.findall('//(.*?).an',complete_url))
                area=''.join(re.findall('/sale/(.*?)/',complete_url))
                print('爬去'+city+'的'+area+'的第'+str(i)+'页成功')
                content_page=self.download(complete_url)
                selector=etree.HTML(content_page)
                ever_hotels=selector.xpath('//ul/li/div[2]/div[1]/a/@href')
                if len(ever_hotels)<10: #如果小于10跳出循环 跳到下个地区
                    print('----------不到50页跳出循环-----------')
                    break
                self.scraped_ever_hotel(ever_hotels)

    def scraped_ever_hotel(self,hotel_page):
        for item_url in hotel_page:#每个url遍历
            content=self.download(item_url)
            selector=etree.HTML(content)
            Subordinate_District=selector.xpath('//div[@class="houseInfo-wrap"]/div/div/dl/dd/a/text()')
            local=selector.xpath('//p[@class="loc-text"]/a/text()')
            bulid_time=selector.xpath('//div[@class="houseInfo-wrap"]/div/div[1]/dl[3]/dd/text()')
            type = selector.xpath('//div[@class="houseInfo-wrap"]/div/div/dl[4]/dd/text()')
            #//*[@id="content"]/div[3]/div[1]/div[3]/div/div[1]/div/div[2]/dl[1]/dd
            hotel_type=selector.xpath('//div[1]/div/div[2]/dl[1]/dd/text()')
            area = selector.xpath('//div[@class="houseInfo-wrap"]/div/div[2]/dl[2]/dd/text()')
            first_pay= selector.xpath('//div[@class="houseInfo-wrap"]/div/div[3]/dl[3]/dd/text()')
            month_pay = selector.xpath('//*[@id="reference_monthpay"]/text()')
            all_pay=selector.xpath('//div[@class="wrapper"]/div/div/span/em/text()')
            hotel_type=''.join(hotel_type).replace('\n', '').replace(' ', '')
            print(''.join(all_pay))
            print(''.join(local))
            print(''.join(Subordinate_District))
            print(''.join(bulid_time))
            print(''.join(type))
            print(hotel_type)
            print(''.join(area))
            print(''.join(first_pay).replace('\n','').replace(' ',''))
            print(''.join(month_pay))
if __name__ == '__main__':
    S=anjuke()
    area_all_url=S.get_list('shenzhen')
    S.ever_page(area_all_url)