import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException
import re
import time
import proxy
from multiprocessing import Pool
def download(url,retry=0):
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }

        # proxies=proxy.retun_proxy()
    try:
        html_json = requests.get(url,
                                 proxies=proxy.return_(),
                                 headers=header, timeout=2
                                 ).json()
        return html_json
    except:
        retry+=1
        time.sleep(1)
        download(url,retry)
        if retry==10:
            return None



def get_weibo_id():
    for i in range(1, 22):

        html_json = download(
            "https://m.weibo.cn/api/container/getIndex?type=uid&value=1223178222&containerid=1076031223178222&page={}".format(
                i))
        if html_json == None:
            print("--------------------worn")
            continue

        id_list = html_json["data"]['cards']
        # print(html_json)
        for id in id_list:
            # print(id["itemid"])
            id = id["itemid"][-16:]
            url = "https://m.weibo.cn/api/comments/show?id={}&page=".format(id)
            get_comments(url)


def get_comments(url):
    pool = Pool(processes=4)

    for i in range(1, 51):
        pool.apply_async(print_, (url, i,))


def print_(url, i):

        format_url = url + str(i)
        commit_json = download(format_url)
        if commit_json == None:

            pass
        else:
            commit_list = commit_json['data']['data']

            for commit in commit_list:
                screen_name = commit['user']['screen_name']
                commit = commit["text"]
                frist = re.sub("<span.*?</span>", "", commit)
                second = re.sub("<a.*?</a>", "", frist)

                print(second)
                print(screen_name)



if __name__ == '__main__':
    get_weibo_id()
