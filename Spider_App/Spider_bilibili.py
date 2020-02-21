
"""
爬取内容： 微信美团小程序
爬取目的：获取相关店铺数据并存入数据库中
"""

import  ssl
import urllib.request
import urllib.parse
import json

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
}

# 获取数据
store_page_url = "https://api.bilibili.com/pgc/web/timeline?types=1"
# "https://wx.waimai.meituan.com/weapp/v2/poi/homepage?ui=1807785726&region_id=1000130300&region_version=1580907712941"

for i in range(0,5):
    for bili_data in json.loads(urllib.request.urlopen(urllib.request.Request(url=store_page_url,headers=headers)).read().decode("utf-8"))["result"]:
        print(bili_data["episodes"][i]["title"])
        print(bili_data["episodes"][i]["cover"])
        print(bili_data["episodes"][i]["square_cover"])

