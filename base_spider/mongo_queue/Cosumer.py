from  multiprocessing import Process
import multiprocessing

import time
def Cosumer(process_num=4,callback=None,args=()):
    processes=[]
    for i in range(process_num):
        p=multiprocessing.Process(target=callback,args=args)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()


