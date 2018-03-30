import hashlib
import os
from functools import wraps
import log
import time

def cache(cachetime):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            result = None
            son_obj = args[0]
            url = args[1]
            header=son_obj.header

            if son_obj.cache:
                try:
                    log.mylogging().info(url+' read cache')
                    result = son_obj.cache[url]

                except KeyError as e:
                    log.mylogging().info(e)

            if result is None:
                son_obj.throttle.wait(url)
                log.mylogging().info('get content from internet')
                result = son_obj.get_content.__wrapped__(son_obj, url,header)
                if son_obj.cache:
                    son_obj.cache[url] = result

            return result['html']

        return wrapper
    return decorator




