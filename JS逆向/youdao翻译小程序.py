import requests
import time
import random
import hashlib
import tkinter as tk

# word = input("请输入您要翻译的内容：")
# 视频教学： https://www.bilibili.com/video/av78359263?from=search&seid=11162552017551929747
def make_md5(string):
    string = string.encode("utf-8")
    md5 = hashlib.md5(string).hexdigest()
    return md5
# print(make_md5("234234"))

def  translation():
    """四个js逆向参数"""
    ts = str(int(time.time()*1000))
    print(ts)
    salt = ts + str(random.randint(0,9))
    # print(salt)
    sign = make_md5("fanyideskweb" + t1.get(0.0,"end")+ salt + "n%A-rKaT5fb[Gy?;N5@Tj")
    print(sign)
    bv = make_md5("5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")
    print(bv)

    data = {
        'i':t1.get(0.0,"end"),
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':salt,
        'sign':sign,
        'ts':ts,
        'bv':bv,
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTlME',
    }
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '237',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1675753892.689935; OUTFOX_SEARCH_USER_ID="1891886365@10.108.160.17"; JSESSIONID=aaaaF06z6d7pJeYtEE6-w; ___rl__test__cookies=1580458772491',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    test = requests.post("http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule",data=data,headers=headers).json()

    # print(test["translateResult"])
    # print(test["translateResult"][0])
    # t1.delete(0.0,'end')

    text = test["translateResult"][0][0]["tgt"]
    print(text)
    t2.insert(0.0,text)

    # t2.insert(0.0, "当前还没有要翻译的内容哦~")
    # return test["translateResult"][0][0]["tgt"]

root = tk.Tk()
root.geometry("600x400")
root.title("黄世祥-在线翻译")
L1 = tk.Label(root, text="在 线 翻 译",height=3)
L1.pack()
t1 = tk.Text(root,height=10)
t1.pack()
t1_button = tk.Button(root,text="翻   译",width=20,command=translation)
t1_button.pack()
t2 = tk.Text(root,height=10)
t2.pack()
root.mainloop()