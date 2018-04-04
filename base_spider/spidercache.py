import hashlib
import os
from functools import wraps
from  Spider.base_spider import log
import Spider.base_spider.spider
import time

def cache(cachetime):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            result = None
            # print(args)
            son_obj = args[0]
            url = args[1]
            # header=son_obj.header
            if son_obj.cache:
                try:
                    log.mylogging().info(url+' read cache')
                    result = son_obj.cache[url]

                except KeyError as e:
                    log.mylogging().info(e)

            if result is None:
                son_obj.throttle.wait(url)
                log.mylogging().info('get content from internet')
                BS=Spider.base_spider.spider.base_spider()
                BS.throttle.wait(url)
                result = son_obj.get_content.__wrapped__(son_obj, url)
                if son_obj.cache:
                    son_obj.cache[url] = result
            return result

        return wrapper
    return decorator




