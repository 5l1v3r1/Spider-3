### 安装环境
`cd tmail`
`pip install -r pip_list.txt`

### 使用说明
根据`Chrome`的版本安装相应版本的`webdriver`并且添加到环境变量
[地址](http://npm.taobao.org/mirrors/chromedriver/)
先执行`LinkTmailSpider`的main函数
可以修改
#### link爬取
```python
stat_url = [
            "https://pages.tmall.com/wow/yao/17473/baojianzibu",
            "https://pages.tmall.com/wow/yao/act/711jf",
            "https://pages.tmall.com/wow/yao/act/999",
            "https://pages.tmall.com/wow/yao/act/aljkdyf-fuke",
            "https://miao.tmall.com/"
        ]
    ts = LinkTmailSpider(stat_url)
    ts.all_url_list()
```
中的startr_url来修改爬取的站点
然后爬取的link存储在`json/url_list.json`中

#### 详细页面爬取

需要自己配置数据库地址
在`__init__`中
```python
self.driver = webdriver.Chrome()
self.load_url_list(json_path)
self.conn = pymysql.connect("url",
                                    "root", "123456", "product")
self.cursor = self.conn.cursor()
self.driver.set_page_load_timeout(15)
```
运行main函数就可以爬取+入库

#### 图片爬虫

从数据库中的`test_xquark_sku_img`中获取图片地址
然后下载
运行main函数就可以爬去


#### resize脚本

调整图片大小

#### TODO

* api调用
* 数据库配置优化

