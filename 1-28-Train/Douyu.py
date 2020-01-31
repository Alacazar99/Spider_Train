# *-UTF-8-*
# @Time    : 2019/8/16 8:22
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : Douyu.py
# @Software: PyCharm

import time
import json
from time import sleep
from selenium import webdriver

class Douyu(object):
    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        # 实例化浏览器对象
        self.driver = webdriver.Chrome()
        # 创建文件
        self.file = open('douyu.json','w')


    # 解析数据
    def parse_data(self):

        node_list = self.driver.find_elements_by_css_selector("ul.layout-Cover-list")

        print(len(node_list))

        data_list = []

        for node in node_list:
            temp = {}
            # 提取房间的标题/房间类型/房间主人/关注人数/封面
            # title = node.find_elements_by_css_selector('h3.DyListCover-intro')
            temp['category'] = node.find_element_by_xpath('./div/a/div[2]/div[1]/span').text
            temp['owner'] = node.find_element_by_xpath('./div/a[1]/div[2]/div[2]/h2').text
            temp['num'] = node.find_element_by_xpath('./div/a/div[2]/div[2]/span').text
            # print(title)
            temp['cover'] = node.find_element_by_xpath('./span/img').get_attribute('data-original')
            temp['link'] = node.get_attribute('href')
            data_list.append(temp)
            print(temp)
            # 返回数据
        return data_list

    # 保存数据
    def save_data(self,data_list):
        # 遍历列表数据
        for data in data_list:
            str_data = json.dumps(data, ensure_ascii=False) + ',\n'
            self.file.write(str_data)


    def __del__(self):
        # 关闭浏览器对象
        self.driver.close()
        self.file.close()

    def run(self):
        # 构造url #
        # 构造webdriver浏览器对象   发送请求
        self.driver.get(self.url)
        while True:
            # 解析数据,返回数据列表
            data_list = self.parse_data()
            self.save_data(data_list)
            # 提取下一页链接,模拟点击
            try:
                ele_next_url = self.driver.find_element_by_xpath('//*[@class="dy-Pagina tion-next"]/span/text()')
                ele_next_url.click()
                time.sleep(7)
            except:
                break
# 保存数据
if __name__ == '__main__':
    douyu = Douyu()
    douyu.run()