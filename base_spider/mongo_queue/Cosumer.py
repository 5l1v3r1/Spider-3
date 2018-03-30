from  multiprocessing import Process
import multiprocessing
from  Mongoqueue import MongoQueue
import time
def Cosumer(process_num=4,callback=None,args=()):
    processes=[]
    for i in range(process_num):
        p=multiprocessing.Process(target=callback,args=args)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()


def aaa(num):
    a=MongoQueue()

    while True:
        time.sleep(0.1)
        # try:
        url=a.pop()
        print(url)
        # except KeyError as e:

        # else:
        #     a.complete(url)
if __name__ == '__main__':

    c=Cosumer(process_num=4,callback=aaa,args=(1,))