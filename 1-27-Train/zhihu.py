# *-UTF-8-*
# @Time    : 2019/8/15 10:17
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : zhihu.py
# @Software: PyCharm

# 搜索jquery官网学习

# pyquery解析库
# 用法类似于jQuery

import requests
from pyquery import PyQuery as py

url = "https://www.zhihu.com"
headers = {
    "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 75.0.3770.142Safari / 537.36"
}
html = requests.get(url=url,headers=headers).text

# print(html)
doc = py(html)
topics = doc("._blank").text()
print(topics)
# topics_list = doc(".")
