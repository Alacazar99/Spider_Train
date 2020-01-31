# *-UTF-8-*
# @Time    : 2019/8/13 16:24
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : baidu_tieba.py
# @Software: PyCharm

import requests
import sys

class BaiduTieBa:
    # 构建请求地址
    def __init__(self,name,pn):
        self.name = name
        self.url = "http://tieba.baidu.com/f?kw={}&ie=utf-8&tab=main".format(name)
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }

        self.url_list = [self.url + str(n*50) for n in range(pn)]
        print(self.url_list)

    def get_data(self,url):
        """
        请求数据
        :param url:
        :return:
        """
        r = requests.get(url, headers = self.headers)
        return r.content

    def save_data(self,data,num):
        # 保存数据
        file_name = self.name + "_" + str(num) + ".html"

        with open(file_name,'wb') as f:
            f.write(data)

    def run(self):
        for url in self.url_list:
            data = self.get_data(url)
            num = self.url_list.index(url)
            self.save_data(data,num)

if __name__ == "__main__":
    name = sys.argv[1]
    pn = int(sys.argv[2])
    baidu = BaiduTieBa(name,pn)
    baidu.run()
