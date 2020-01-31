# *-UTF-8-*
# @Time    : 2019/8/13 16:52
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : jinshan.py
# @Software: PyCharm

import requests
import json
#
# class JinShan:
#     def __init__(self,project):
#         # input("请输入您要翻译的内容：" + project)
#         self.project = project
#         self.url = 'http://fy.iciba.com/ajax.php?a=fy'
#         self.headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
#         }
#
#     def Post_data(self,project):
#         post_data = {
#             "f": "auto",
#             "t": "auto",
#             "w": project
#         }
#         return requests.post(url = self.url,headers= self.headers,data=post_data)
#
#     # def request_data(self):
#     #     response = self.Post_data(project)
#     #     return response.content.decode("utf-8")
#
#
#     def do_data(self,project):
#
#         # dict_data = self.Post_data(project)
#         translate_word = json.loads(project,encoding='utf-8')
#
        # if translate_word['status'] == 1:
        #     print(translate_word['content']['out'])
        # if translate_word['status'] == 0:
        #     print(translate_word['content']['word_mean'])
#
#     def run_Jinshan(self):
#         # project = self.request_data()
#         self.do_data(project)
#
# import sys
# if __name__ == "__main__":
#     # input("请输入您要翻译的内容：")
#     project = "pp"
#     jin = JinShan(project)
#     jin.run_Jinshan()

class JinShan(object):
    def __init__(self,word):
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537. 36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }
        self.post_data = {"f": "auto", "t": "auto", "w": word}

    def request_post(self):
        response = requests.post(url=self.url, headers=self.headers,data=self.post_data)
        # print(response.content.decode())
        return response.content.decode()

    def translates(self,data):
        dict_data = json.loads(data)
        if dict_data['status'] == 1:
            print(dict_data['content']['out'])
        if dict_data['status'] == 0:
            print(dict_data['content']['word_mean'])

    def run(self):
        data = self.request_post()
        print('【译文】：')
        self.translates(data)

if __name__ == "__main__":
    while(True):
        print('【输入您要翻译的内容】：')
        word = input()
        if word == 'exit':
            exit()
        jinshan = JinShan(word)
        jinshan.run()