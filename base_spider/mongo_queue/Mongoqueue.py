from pymongo import MongoClient,errors
from datetime import datetime ,timedelta

class MongoQueue:

    OUTSTANDING,PROCESSING,COMPLETE=range(3)

    def __init__(self,timeout=300):
        self.client=MongoClient('localhost',27017)
        self.db=self.client.urls
        self.timeout=timeout

    def __nonzoro__(self):
        record=self.db.crawl_queue.find_one(
            {'status':{'$ne':self.COMPLETE}}
        )
        return True if record else False

    def push(self,url):
        try:
            self.db.crawl_queue.insert({'_id':url,'status':self.OUTSTANDING})
        except errors.DuplicateKeyError as e:
            #已经在队列中了
            pass

    def pop(self):
        record=self.db.crawl_queue.find_and_modify(query={'status':self.OUTSTANDING},
                                                   update={'$set':{'status':self.PROCESSING,'timestamp':datetime.now()}})
        if record:
            return record['_id']
        else:
            raise KeyError

    def complete(self,url):
        self.db.crawl_queue.update(
            {'_id':url},{'$set':{'status':self.COMPLETE}}
        )

    def repair(self):

        record=self.db.crawl_queue.find_and_modify(
            query={
                'timestamp':{'$lt':datetime.now()-timedelta(seconds=self.timeout),
                'status':{'$ne':self.COMPLETE}}
            },
            update={'$set':{'status':self.OUTSTANDING}}
        )
        if record:
            print('Released:',record)

a=MongoQueue()
for i in range(1000):
    a.push('wwww.baidu.com/{}'.format(i))