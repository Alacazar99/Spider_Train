import requests
import re
import time
from lxml import etree

from Douyin_App.douyin_db import handle_get_task

def handle_decode(input_data):
    search_douyin_str = re.compile("抖音ID：")

    # 抖音web页面数字解析列表
    regex_list = [
        {'name': ['&#xe603; ', '&#xe60d;' , '&#xe616; '], 'value': 0},
        {'name': ['&#xe602; ', '&#xe60e; ', '&#xe618; '], 'value': 1},
        {'name': ['&#xe605; ', '&#xe610; ', '&#xe617; '], 'value': 2},
        {'name': ['&#xe604; ', '&#xe611; ', '&#xe61a; '], 'value': 3},
        {'name': ['&#xe606; ', '&#xe60c; ', '&#xe619; '], 'value': 4},
        {'name': ['&#xe607; ', '&#xe60f; ', '&#xe61b; '], 'value': 5},
        {'name': ['&#xe608; ', '&#xe612; ', '&#xe61f; '], 'value': 6},
        {'name': ['&#xe60a; ', '&#xe613; ', '&#xe61c; '], 'value': 7},
        {'name': ['&#xe60b; ', '&#xe614; ', '&#xe61d; '], 'value': 8},
        {'name': ['&#xe609; ', '&#xe615; ', '&#xe61e; '], 'value': 9},
    ]
    for i1 in regex_list:
        for i2 in i1["name"]:
            input_data = re.sub(i2,str(i1['value']),input_data)

    # 构造html结构；
    share_web_html = etree.HTML(input_data)
    user_info = {}
    user_info['nickname'] = share_web_html.xpath("//p[@class='nickname']/text()")[0]
    douyin_id1 = share_web_html.xpath("//p[@class='shortid']/text()")[0].replace(" ", "")
    douyin_id2 = ''.join(share_web_html.xpath("//p[@class='shortid']/i/text()")).replace(" ", "")

    user_info['douyin_id'] = re.sub(search_douyin_str, "", douyin_id1 + douyin_id2)
    # user_info["job"] = share_web_html.xpath("//span[@class='info']/text()")[0].replace(" ", "")
    user_info["signature"] = share_web_html.xpath("//p[@class='signature']/text()")[0].replace(" ", "")
    user_info['关注'] = "".join(share_web_html.xpath("//p[@class='follow-info']/span[1]//i/text()")).replace(" ", '')

    fans = "".join(share_web_html.xpath("//p[@class='follow-info']/span[2]//i/text()")).replace(" ", '')
    fans_danwei = share_web_html.xpath("//p[@class='follow-info']/span[2]/span[@class='num']/text()")[-1]
    # print(fans_danwei)
    if fans_danwei.strip() == "w":
        user_info["粉丝"] = str(int(fans) / 10) + " W"

    like = "".join(share_web_html.xpath("//p[@class='follow-info']/span[3]//i/text()")).replace(" ", '')
    like_danwei = share_web_html.xpath("//p[@class='follow-info']/span[3]/span[@class='num']/text()")[-1]
    # print(like_danwei)
    if like_danwei.strip() == "w":
        user_info["点赞量"] = str(int(like) / 10) + " W"

    print(user_info)

def handle_douyin_web_share(task):
    # share_web_url = "https://www.douyin.com/share/user/61002725169"
    share_web_url = "https://www.douyin.com/share/user/{a}" .format(a = task["share_id"])
    print(share_web_url)
    share_web_headers = {
        "user-agent":"Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/79.0.3945.130Safari/537.36"
    }

    share_web_response = requests.post(url=share_web_url,headers= share_web_headers)

    handle_decode(share_web_response.text)

    # print(share_web_response.text)

while True:
    task = handle_get_task()
    handle_douyin_web_share(task)
    time.sleep(1)