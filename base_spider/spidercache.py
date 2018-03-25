import hashlib
import os
from functools import wraps
import codecs
import time


def cache(func):
    @wraps(func)
    def wrapper(*args):
        result = None
        son_obj = args[0]
        url = args[1]
        if son_obj.cache:
            try:
                print(url, 'read cache')
                result = son_obj.cache[url]
            except KeyError as e:
                print(e)
            else:
                if 500 < result['code'] < 600:
                    result = None
                    print(url,'server error re download')

        if result is None:
            son_obj.throttle.wait(url)
            print('get content from internet')
            result = son_obj.get_content.__wrapped__(son_obj, url)

            if son_obj.cache:
                son_obj.cache[url] = result
        return result['html']
        # url = url
        # hash = hashlib.md5()
        # hash.update(url.encode('utf8'))
        # md5 = hash.hexdigest()
        # cachedir = os.path.join('.cache',md5[0:2],md5[2:4])
        # cachepath = os.path.join('.cache',md5[0:2],md5[2:4],md5)
        # try:
        #     mtime = os.path.getmtime(cachepath)
        #     if time.time() - mtime > cachetime:
        #         raise Exception('cache time expired')
        #     else:
        #         print(url,'read cache')
        #         with codecs.open(cachepath,'r','utf8') as f:
        #             data = f.read()
        #             return data
        # except Exception as e:
        #     self.throttle.wait(url)
        #     print(url,'get content from internet',e)
        #     if not os.path.exists(cachedir):
        #         os.makedirs(cachedir)
        #     data = func(self,url)
        #
        #     with codecs.open(cachepath,'w+','utf-8') as f:
        #         f.write(data)
        #     return data

    return wrapper




