import  multiprocessing

def Producer(callback=None,args=()):
    p=multiprocessing.Process(target=callback, args=args)
    p.start()