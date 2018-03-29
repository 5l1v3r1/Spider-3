from spider import  base_spider

class dd(base_spider):

    def get(self):

        con = self.get_content('https://www.sec.gov/cgi-bin/browse-edgar?company=Care+Investment+Trust+Inc&owner=exclude&action=getcompany')
        print(con)

header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
a=dd(3,header)
a.get()
