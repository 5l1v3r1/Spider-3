import Spider.base_spider.spider

class dd(Spider.base_spider.spider.base_spider):

    def get(self):

        con = self.get_content('https://list.tmall.com/chaoshi_data.htm?p=1&user_id=725677994&cat=51454011&sort=td&from=chaoshi')['html']
        print(len(con))

header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
a=dd(3,header=header)
a.get()
