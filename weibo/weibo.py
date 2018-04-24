import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import re
import time
# import proxy
from multiprocessing import Pool
def download(url):
    header={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    try:
        # proxies=proxy.retun_proxy()

        html_json=requests.get(url,
                               # proxie
                               headers=header,
                               ).json()
        return html_json
    except:
        pass

def get_weibo_id():
    for i in range(1,22):


            html_json=download("https://m.weibo.cn/api/container/getIndex?type=uid&value=1223178222&containerid=1076031223178222&page={}".format(i))


            id_list=html_json["data"]['cards']
            # print(html_json)
            for id in id_list:
                print(id["itemid"])
                id=id["itemid"][-16:]
                url="https://m.weibo.cn/api/comments/show?id={}&page=".format(id)
                get_comments(url)

def get_comments(url):
    pool=Pool(processes=4)

    for i in range(1,51):
        pool.apply_async(print_, (url,i,))
def print_(url,i):
    try:
        format_url = url + str(i)
        commit_json = download(format_url)
        commit_list = commit_json['data']['data']

        for commit in commit_list:
            screen_name = commit['user']['screen_name']
            commit = commit["text"]
            frist = re.sub("<span.*?</span>", "", commit)
            second = re.sub("<a.*?</a>", "", frist)

            print(second)
            print(screen_name)
    except:
        print(url + str(i))

if __name__ == '__main__':
    get_weibo_id()
