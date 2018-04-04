import Spider.base_spider.spider

class dd(Spider.base_spider.spider.base_spider):

    def get(self):

        con = self.get_content('https://www.jinfuzi.com/simu/list_d2_w1_p3.html')['html']
        print(len(con))

header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
a=dd(3,header=header)
a.get()
