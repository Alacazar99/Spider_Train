import requests
import re
import json
import time
import random
from requests.exceptions import RequestException

def get_ono_page(url):
    """
    获取一个页面数据,并下载数据
    """
    headers = {
        "User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"
    }

    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
    except RequestException:
        return None #报错

#{“poiId”:1782324,“frontImg”:“https://img.meituan.net/600.600/msmerchant/15063dce5c3491d6383b015df333524186600.jpg",“title”:“原石牛扒（石岩店）”,“avgScore”:5,“allCommentNum”:3241,“address”:“宝安区宝石东路377号2楼（石岩影剧院东侧）”,"avgPrice”:59,

def deal_one_page(html):
    # print(type(html))
    # 正则表达式匹配
    pattern = re.compile('"frontImg":"[\s\S]?",“title”:"[\s\S]?",“avgScore”:[\s\S]?,“allCommentNum”:\d?,“address”:"[\s\S]?",“avgPrice”:\d?,')
    results = re.findall(pattern, html)
    print(results) ##匹配出来数据是字符串格式
    # 新建列表
    resultsL = []
    #遍历字符串
    for item in results:
        # 对字符串进行切割,先以逗号—索引下标，再以冒号切割—索引下标
        resultsL.append({
            'frontImg':item.split(",")[0].split(":",1),
            'title':item.split(",")[1].split(":",1),
            'avgScore':item.split(",")[2].split(":",1),
            'allCommentNum':item.split(",")[3].split(":",1),
            'address':item.split(",")[4].split(":",1),
            'avgPrice':item.split(",")[5].split(":",1),
        })
    print(resultsL)
    return resultsL

def write2File(item):
    """
    将抓取到数据一条条写入meituanmeishi.txt
    """
    #json数据格式
    with open("meituanmeishi.txt", "a", encoding='utf-8') as f:
        #转化为json字符串写入,方便数据分析
        f.write(json.dumps(item, ensure_ascii=False+"\n"))

def crawlPage(i):
    # 得到真正的URL
    #http://sz.meituan.com/meishi/b32/pn1/
    url = "http://sz.meituan.com/meishi/b32/pn"+str(i)+"/"
    # 下载页面
    html = get_ono_page(url)
    # 提取信息,写入到本地文件系统
    for item in deal_one_page(html):
        #将数据写到本地的文件系统中
        write2File(item)

if __name__ == "__main__":
    # 循环爬取次数,根据数据数量而定
    for i in range(3):
        #页面序号:1\2\3\4\5\6…
        # crawlPage(i)
        time.sleep(random.randint(1,3)) #每抓取一个页面随机休息1到3秒钟
        print("爬取完成")
