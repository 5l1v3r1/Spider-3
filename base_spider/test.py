from spider import  base_spider

class dd(base_spider):
    def get(self):
        con=self.get_content('https://blog.csdn.net/dreamcoding/article/details/8611578')
        print(con)
        # print(con.encode('utf-8'))
a=dd(3)
a.get()