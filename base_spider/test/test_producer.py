from  mongo_queue.Producer import Producer
from mongo_queue.Mongoqueue import MongoQueue
from mongo_queue.Cosumer import Cosumer
import time
def aaa(num):
    print(num)
    a=MongoQueue()
    i=0
    while True:
        i+= 1
        if i==1000:
            break
        time.sleep(0.2)
        # try:
        url='www.baidu.com/{}/{}'.format(i,num)
        a.push(url)
        print('push a url')
def bbb(i):
    a=MongoQueue()
    # print(i)
    while True:
        time.sleep(0.1)
        # try:
        url=a.pop()
        print(url)
if __name__ == '__main__':


    p = Producer(callback=aaa,args=(5,))
    c = Cosumer(process_num=4, callback=bbb, args=(1,))