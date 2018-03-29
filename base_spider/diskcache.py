import os
import re
from urllib import parse
import sys
import pickle
import json
import hashlib
class DiskCache:
    def __init__(self,cache_dir='cache'):
        self.cache_dir=cache_dir

    def url_to_path(self,url):
        hash=hashlib.md5()
        hash.update(url.encode('utf-8'))
        md5=hash.hexdigest()
        cachedir = os.path.join('.cache', md5[0:2], md5[2:4])
        cachepath = os.path.join('.cache', md5[0:2], md5[2:4], md5)+'.json'
        return cachepath
    def __getitem__(self, url):
        path=self.url_to_path(url)
        if os.path.exists(path):
            with open(path,'rb') as f:
                return pickle.loads(f.read())
        else:
            raise KeyError(url +'dose not exist')

    def __setitem__(self, url, result):
        path=self.url_to_path(url)
        folder=os.path.dirname(path)
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(path,'wb') as f:
            f.write(pickle.dumps(result))
