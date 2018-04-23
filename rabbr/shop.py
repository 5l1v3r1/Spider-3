import requests
import re
import pymysql
from lxml import etree
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    # 'Cookie': 's_ViewType=10; _lxsdk_cuid=162d7c8a08ec8-06574899d6d2f2-3a614f0b-1fa400-162d7c8a08ec8; _lxsdk=162d7c8a08ec8-06574899d6d2f2-3a614f0b-1fa400-162d7c8a08ec8; _hc.v=0d0a6c6c-835b-e634-730c-4861e6dd7e9c.1524038673; cy=258; cye=guiyang; __utmz=1.1524041034.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); thirdtoken=8C4ED196C7CE8D362A03346FED4A2A04; JSESSIONID=3591B15133B62DB142A213FA0386C5F4; _thirdu.c=62528643ab77e5f146542a0d511817c4; dper=e5b5aa8cba5ad90edcbd56145582c4ee5aa79b399a8e623e94f8630af3d27c49; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_1222058167; ctu=12a017cea659512d0c8b94961d2e13e43d190551dc80235b2ac37b11158f15f6; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=162dbadbd74-35d-80a-568%7C%7C499'
}#浏览器头
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='dazhong', charset='utf8')
# cursor = conn.cursor()
# cursor.execute('USE dazhong')#链接数据库


# def connect_to_my_sql():。


def get_content():
    list=['g105','g110','g132','g111']#遍历四个标签
    for j in  list:
        for i in range(1, 51):#遍历每一页
            content = requests.get('http://www.dianping.com/guiyang/ch10/{}p{}'.format(j,i), headers=header).text
            parse_content(content)


def parse_content(content):
    selector=etree.HTML(content)#树状HTML
    sel=selector.xpath('//*[@id="shop-all-list"]/ul/li')
    for item in sel:
        # time.sleep(1)
        url=''.join(item.xpath('./div[@class="txt"]/div[@class="tit"]/a[1]/@href'))
        name=''.join(item.xpath('./div[2]/div[1]/a/h4/text()'))
        amount=''.join(item.xpath('./div[2]/div[2]/a[1]/b/text()'))
        if amount=='':
            amount=0
        adress=''.join(item.xpath('./div[2]/div[3]/span/text()'))
        per=''.join(item.xpath('./div[2]/div[2]/a[2]/b/text()'))
        # print(name)
        sql="INSERT INTO shop VALUES ('{url}', '{name}', {amount}, '{adress}', '{per}')".format(
                                            url=url,name=name,
                                            amount=amount,adress=adress,per=per
        )#sql语句
        # instert_to_bd(sql)
        ID=''.join(re.findall("(\d+)",url))
        commit_content(ID)#插入


def commit_content(ID): #获取评论的函数
    url = 'http://www.dianping.com/shop/{}'.format(ID)
    content = requests.get(url, headers=header).text
    # print(content)
    selector = etree.HTML(content)
    sel=selector.xpath('//div[@id="comment"]/ul/li')
    # print(len(sel))
    for item in sel:#先定位标签为列表
        #解析标签中所有需要的元素
        id=''.join(item.xpath('./a/@data-user-id'))
        time=''.join(item.xpath('./div[@class="content"]/div[@class="misc-info"]/span[@class="time"]/text()'))
        #//*[@id="rev_411659869"]/div/div[1]/p#//*[@id="rev_410272490"]/div/div[1]/p/text()[1]
        # commit=item.xpath('./div/div[1]/p/text()')
        data=''.join(item.xpath('./div')[0].xpath('string(.)'))
        # print(data)
        taste=''.join(re.findall("口味：(.*?) 环境",data))
        enviroment = ''.join(re.findall("环境：(.*?) 服务", data))
        service=''.join(re.findall("服务：(.*?) ",data))

        overall_rating =(''.join(re.findall('\d+', ''.join(item.xpath('./div/p[1]/span[1]/@class')))).replace('0',''))
        try:
            coment =re.sub('：(.*?)  ','',re.findall("服务(.*?) 赞",data)[0])
        except:
            coment=''

        sql = "INSERT INTO comment VALUES ('{ID}', '{time}', '{coment}', '{service}', '{enviroment}','{taste}','{overall_rating}')".format(
            ID=id, time=time,
            coment=coment, service=service, enviroment=enviroment,
            taste=taste,overall_rating=overall_rating
        )#sql语句
        # instert_to_bd(sql)#插入数据库
        print(sql)



def instert_to_bd(sql): #插入数据库
        try:
            cursor.execute(sql)
            conn.commit()
        except pymysql.err.IntegrityError as e:
            pass
        except pymysql.err.ProgrammingError as  ex:
            pass
        else:
            print("写入成功")



get_content()
conn.close()
