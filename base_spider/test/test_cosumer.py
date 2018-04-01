from mongo_queue.Mongoqueue import MongoQueue
import time
from mongo_queue.Cosumer import Cosumer
#被传入的参数
def aaa(num):
    a=MongoQueue()
    while True:
        time.sleep(0.1)
        # try:
        url=a.pop()
        print(url)
if __name__ == '__main__':
    c=Cosumer(process_num=4,callback=aaa,args=(1,))