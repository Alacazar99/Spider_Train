import hashlib
import json
import time
import requests
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 设置代理
# proxy = {"http":'http://119.101.118.3:9999'}
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--proxy-server = http://' + proxy)


# 上传抖音账号
share_id = "88445518961"
share_url = "https://www.douyin.com/share/user/" + share_id
# 请求头信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}
# 正则化获取参数
dytk_search = re.compile(r"dytk: '(.*?)'")
tac_search = re.compile(r"<script>tac=(.*?)</script>")

response = requests.get(url = share_url,headers = headers)
# print(response.text)

dytk = re.search(dytk_search,response.text).group(1)
tac = "var tac=" + re.search(tac_search,response.text).group(1) + ";"
print(dytk)
print(tac)

# js逆向破解
with open("html_head.txt","r") as f1:
    f1_read = f1.read()

with open("html_foot.txt","r") as f2:
    f2_read = f2.read().replace("$$$",share_id)

with open("test.html","w") as fw:
    fw.write(f1_read + '\n' +tac+"\n"+ f2_read)

# 浏览器自动化
chrome_options = Options()
chrome_options.add_argument("--headless")
douyin_driver = webdriver.Chrome(options=chrome_options)
douyin_driver.get("file://I:\Spider\Douyin_Video_get\\test.html")
signature = douyin_driver.title
# signature = input("输入：")
# print(signature)
time.sleep(2)
douyin_driver.quit()


# 视频路径
movie_url = "https://www.douyin.com/web/api/v2/aweme/post/?user_id="+ share_id+"&sec_uid=&count=21&max_cursor=0&aid=1128&_signature="+ signature+"&dytk=" +dytk

# 参数MD5加密
# def make_md5(string):
#     string = string.encode("utf-8")
#     md5 = hashlib.md5(string).hexdigest()
#     return md5

# 设置代理
proxy = {"http":'http://119.101.118.3:9999'}

while True:
    movie_response = requests.get(url=movie_url,headers=headers,proxies = proxy)
    print(movie_response.text)
    if json.loads(movie_response.text)["aweme_list"] == []:
        # 如果没有获取到信息；
        print("内容为空！")
        time.sleep(1)
        continue
    else:
        for item in json.loads(movie_response.text)["aweme_list"]:
            # 输出URL
            video_url = item["video"]['play_addr']['url_list'][0]
            video_repsonse = requests.get(url=video_url,headers = headers,proxies = proxy)
            print(video_url)

            with open("douyin.mp4","wb") as v:
                v.write(video_repsonse.content)
            break
        break


