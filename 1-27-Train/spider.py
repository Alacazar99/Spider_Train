# *-UTF-8-*
# @Time    : 2019/8/13 15:17
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : spider.py
# @Software: PyCharm

import requests
def demo1():
    response = requests.get("https://www.baidu.com/")
    print(type(response))

    print(response.status_code)
    print(type(response.text))
    print(response.text)
    print(response.cookies)

def demo2():
    """
    参数传递
    :return:
    """
    # r = requests.get('http://httpbin.org/get?name = zhangsan&age=22')
    # print(r.text)
    #
    data = {
        'name':"zhangsan",
        "age":30
    }

    headers = {
        "User-Agent":"Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 75.0.3770.142Safari / 537.36"
    }
    # r = requests.get('http://httpbin.org/get',headers=headers)
    r = requests.post('http://192.168.14.74:5000/', headers=headers)
    print(r.text)
    print(r.json()[1].get)

# demo2()

def demo3():
       t = requests.get("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1565692318831&di=895ba487930c92c1ea4ab1ab64a512e1&imgtype=0&src=http%3A%2F%2Fguangdong.sinaimg.cn%2Fdy%2Fslidenews%2F5_img%2F2014_09%2F30939_947679_563317.jpg_U11307P693DT20140708171932.jpg")
       r = requests.get("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1565694218744&di=04f575c41c39ea4a2541454a9045a45f&imgtype=0&src=http%3A%2F%2Fs2.sinaimg.cn%2Fmiddle%2F60d27f6dtbc305fefd3f1%26690")
       print(r.text)
       print(r.content)

       with open("123.jpg","wb") as f:
           f.write(r.content)
demo3()

def demo4():
    files = {"file":open("请老师务必看看.jpg",'rb')}
    r = requests.post("http://192.168.14.74:5000/",files = files)
    print(r.text)
demo4()