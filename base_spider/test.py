from spider import  base_spider

class dd(base_spider):
    def get(self):
        con = self.get_content('https://blog.twitter.com/official/en_us/topics/company/2018/growingtogetherattwitter.html')

        print(con)

a=dd(3)
a.get()
