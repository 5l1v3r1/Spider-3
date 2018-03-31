import time
import requests
import json


# 目标url
url = "http://mp.weixin.qq.com/mp/getappmsgext/mp/getappmsgext"

# 添加Cookie避免登陆操作，这里的"User-Agent"最好为手机浏览器的标识
headers = {
    "Cookie": 'wap_sid2=CPXWyvsJElxzX24yUWdYM2JSR3Q2c20zOUplNndHVlNOa0dQMEJJT0hfY0RzRkJ6eWtxZkxhQkpmbF9RWXJ3UEstNnlKSUMxTlpjdi00RjFlSUNjTWFRN0JsSU9DTE1EQUFBfjDD6o3VBTgNQAE=',
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.27.400 QQBrowser/9.0.2524.400"
}
# 添加data，`req_id`、`pass_ticket`分别对应文章的信息，从fiddler复制即可。不过貌似影响不大
data = {
    "is_only_read": "1",
}
# with open('cookie.txt','r',encoding='utf-8') as f:
#     cookie=f.read()
# cookies = json.loads(cookie)
"""
添加请求参数
__biz对应公众号的信息，唯一
mid、sn、idx分别对应每篇文章的url的信息，需要从url中进行提取
key、appmsg_token从fiddler上复制即可
pass_ticket对应的文章的信息，貌似影响不大，也可以直接从fiddler复制
"""
params = {
    "__biz": 'MjM5Njc5MzA4MQ==',
    "mid": '2897761218',
    "sn": 'a375d3476faeb3e036bd45430657f73e',
    "idx": '1',

    "appmsg_token": '947_V9G1wTvl3yV%2FOIdfhPyDZjAUrDEiH1pxsT8wxi792TdPRy8rpO-uTe_DYx_sBadT47TN-agRwKdOv4rh', #只要随便找一个就行
}
# 使用post方法进行提交
content = requests.post(url, headers=headers, data=data, params=params,).json()

# 提取其中的阅读数和点赞数
print(content)