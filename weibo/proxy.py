# import requests
# import random
#
# content = requests.get(
#     "https://proxyapi.mimvp.com/api/fetchopen.php?orderid=868070421812120409&num=20&result_fields=1,2").text
# proxy_list = content.split("\n")
# # print(proxy_list)
# httplist = []
# httpslist = []
# for i in proxy_list:
#     if 'HTTPS' in i:
#         httpslist.append(i.replace(",HTTP/HTTPS\r", "").replace(",HTTPS\r", ""))
# for i in proxy_list:
#
#     if 'HTTP\r' in i:
#         httplist.append(i.replace(",HTTP\r", "").replace(",HTTPS\r", ""))
# for i in range(10):
#     proxies = {
#         "http": "http://" + random.choice(httplist),
#         "https": "http://" + random.choice(httpslist),
#     }
#     try:
#         print(requests.get("http://httpbin.org/ip", proxies=proxies,timeout=2).text)
#         print(requests.get("https://httpbin.org/ip", proxies=proxies,timeout=2).text)
#     except:
#         print("error")
import requests

def return_():
    # 要访问的目标页面
    targetUrl = "http://test.abuyun.com/proxy.php"
    # targetUrl = "http://proxy.abuyun.com/switch-ip"
    # targetUrl = "http://proxy.abuyun.com/current-ip"

    # 代理服务器

    proxyHost = "http-pro.abuyun.com"
    proxyPort = "9010"

    # 代理隧道验证信息
    proxyUser = "HD2V7LPM57I930UP"
    proxyPass = "D729689756557530"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta,
    }
    return proxies
# resp = requests.get(targetUrl, proxies=proxies)
#
# print(resp.status_code)
# print(resp.text  )
