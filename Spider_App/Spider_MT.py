import requests
from bs4 import BeautifulSoup
import re
import json
import time

'''
    @Author: 黄世祥
'''

class MeiTuanSpider:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
            "Cookie": "_lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=167ffca928ec8-0e654d87ed4011-4d045769-100200-167ffca928ec8; __mta=210679722.1546184730073.1546184730073.1546184730073.1; _lxsdk=167ffca928ec8-0e654d87ed4011-4d045769-100200-167ffca928ec8; _ga=GA1.2.268215992.1546188830; _gid=GA1.2.2085490335.1546188830; mtcdn=K; lsu=; token2=k5KFzZOmjNtI4RXwSn-MBwHYS_QFAAAAqgcAAM17q21drlYFsEkrWY8nBciWgigr_vFCL5FDakc3B15Z318X6W3X_Dkc15OrK0yCPQ; u=646978641; n=XwR964951585; lt=k5KFzZOmjNtI4RXwSn-MBwHYS_QFAAAAqgcAAM17q21drlYFsEkrWY8nBciWgigr_vFCL5FDakc3B15Z318X6W3X_Dkc15OrK0yCPQ; ci=146; rvct=146%2C224%2C527%2C1114%2C1268%2C758%2C835%2C811%2C729%2C113%2C402; unc=XwR964951585; uuid=d927d5e7a70f4031900e.1546184723.2.0.0; client-id=03aeb51b-56e7-4809-b3a0-1fd44f5b4ea4; lat=40.74812; lng=107.400892; _lxsdk_s=16803187a83-b3c-b35-5ba%7C%7C171",
            "Referer": "https://servicewechat.com/wx2c348cf579062e56/237/page-frame.html",
            "Upgrade-Insecure-Requests": "1"
        }
        self.start_url = "https://wx.waimai.meituan.com/weapp/v2/poi/homepage?ui=1807785726&region_id=1000130300&region_version=1580907712941"

    def getHTML(self, url):
        '''
        get方式请求url
        :param url: 请求url
        :return: str
        '''
        resp = requests.get(url, headers=self.headers)
        return resp.content.decode(resp.apparent_encoding)

if __name__ == "__main__":
    meituan = MeiTuanSpider()
    meituan.getHTML("https://wx.waimai.meituan.com/weapp/v2/poi/homepage?ui=1807785726&region_id=1000130300&region_version=1580907712941")

    def getCityList(self, html):
        '''
        获取全国城市的美团主页地址列表
        :param html: 城市选择页面html
        :return: list
        '''
        soup = BeautifulSoup(html, 'html.parser')
        spans = soup.findAll("span", attrs={"class": "cities"})
        citys = []
        for i in range(len(spans)):
            a = spans[i].findAll("a", attrs={"class": re.compile("link.*?city.*?")})
            for j in range(len(a)):
                url = "https:" + a[j]['href']
                city_name = a[j].text
                citys.append({"city_name": city_name, "url": url})
        return citys

    def getMoreList(self, html):
        '''
        获取城市主页的分类信息地址
        :param html: 主页html
        :return: list
        '''
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.findAll("a", attrs={"class": re.compile("link.*?detail-more.*?")})
        moreList = []
        for i in range(len(a)):
            url = a[i]['href']
            type_name = re.findall(r'"title":"(.*?)"', str(a[i]))[0]
            moreList.append({"type_name": type_name, "url": url})
        return moreList

    def meiShiParser(self, html):
        '''
        解析美食类目下所有店铺的店铺信息以及店铺类目下的所有商品信息，店铺评价信息等等
        :param html: 店铺页面html
        :return: None
        '''
        req = re.compile(r'{"itemId":"(.*?)"', re.S)
        itemsIds = re.findall(req, html)
        preURL = "https://www.meituan.com/meishi/"
        for i in range(len(itemsIds)):
            url = preURL + itemsIds[i] + "/"
            detailHTML = self.getHTML(url)
            shopDirtyInfo = re.findall(r'detailInfo":(.*?),"crumbNav', detailHTML)[0]
            # 店铺信息
            shopId, shopName = re.findall(r'"poiId":(.*?),"name":"(.*?)"', shopDirtyInfo)[0]
            avgScore = re.findall(r'"avgScore": (.*?)', shopDirtyInfo)
            address = re.findall(r'"address":"(.*?)"', shopDirtyInfo)
            phone = re.findall(r'"phone":"(.*?)"', shopDirtyInfo)
            # 店铺提供设施服务
            extraInfos = re.findall(r'"text":"(.*?)"', shopDirtyInfo)
            req_good = re.compile(r'recommended":(.*?)]', re.S)
            # 商品列表
            goods = re.findall(req_good, shopDirtyInfo)[0]
            req_goodList = re.compile(r'{"id":"(.*?)","name":"(.*?)","price":(.*?),"frontImgUrl":"(.*?)"}', re.S)
            goodsList = re.findall(req_goodList, goods)
            # 用户评价
            evaluateURL = "http://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=d927d5e7a70f4031900e.1546184723.2.0.0&platform=1&partner=126&originUrl=" + url + "&riskLevel=1&optimusCode=1&id=" + str(itemsIds[i]) + "&userId=646978641&offset=0&pageSize=10&sortType=1"
            totalPages = int(json.loads(self.getHTML(evaluateURL))['data']['total'])
            evaluateList = []
            for k in range(totalPages):
                offset = k * 10
                evaluateURL = "http://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=d927d5e7a70f4031900e.1546184723.2.0.0&platform=1&partner=126&originUrl=" + url + "&riskLevel=1&optimusCode=1&id=" + str(itemsIds[i]) + "&userId=646978641&offset=" + str(offset) + "&pageSize=10&sortType=1"
                evaluateList.extend(json.loads(self.getHTML(evaluateURL))['data']['comments'])
                # 数据量太大，此处做测试打印
                print(evaluateList)
                time.sleep(5)
            for j in range(len(goodsList)):
                good_id = goodsList[j][0]
                good_name = goodsList[j][1]
                good_price = goodsList[j][2]
                good_img = goodsList[j][3]
                print("shopId: %s,shopName: %s, avgScore: %s, address: %s, phone: %s, extraInfos: %s, good_id: %s, good_name: %s, good_price: %s, good_img: %s" %
                      (shopId, shopName, avgScore, address, phone, extraInfos, good_id, good_name, good_price, good_img)
                )
            print(evaluateList)
            time.sleep(10)

    def spider(self):
        pass
        '''
        数据分析
        :return: None
        '''
        html = self.getHTML(self.start_url)
        # cityList = self.getCityList(html)
        type_detail = []
        # 每一个城市为单位
        # for i in range(len(cityList)):
        #     cityIndexHtml = self.getHTML(cityList[i]['url'])
        #     moreList = self.getMoreList(cityIndexHtml)
        #     # 每一个城市下每一个类目为单位
        #     for j in range(len(moreList)):
        #         moreType = moreList[j]['type_name']
        #         moreURL = moreList[j]['url']
                #############################
                # 爬取数据量较大，此处做测试步骤#
                #############测试块开始############
                # print(moreURL)
                # aimHTML = self.getHTML(moreURL)
                # self.meiShiParser(aimHTML)
                # exit(0)
                #############测试块结束############
                # type_detail.append({"city_name": cityList[i]['city_name'], "type_name": moreType, "type_url": moreURL})
        #     time.sleep(5)
        # for k in range(len(type_detail)):
        #     city_name = type_detail[k]['city_name']
        #     type_name = type_detail[k]['type_name']
        #     type_url = type_detail[k]['type_url']
        #     aimHTML = self.getHTML(type_url)
        #     if type_name == '美食':
        #         self.meiShiParser(aimHTML)
        #     elif type_name == '外卖':
        #         pass
        #     elif type_name == '酒店星级':
        #         pass
        #     elif type_name == '热门城市':
        #         pass
        #     elif type_name == '火车票':
        #         pass
        #     elif type_name == '休闲娱乐':
        #         pass
        #     elif type_name == '生活服务':
        #         pass
        #     elif type_name == '丽人':
        #         pass
        #     elif type_name == '结婚':
        #         pass
        #     elif type_name == '儿童乐园':
        #         pass
        #     elif type_name == '幼儿教育':
        #         pass
        #     elif type_name == '亲子摄影':
        #         pass
        #     elif type_name == '孕产护理':
        #         pass
        #     elif type_name == '运动健身':
        #         pass
        #     elif type_name == '装修设计':
        #         pass
        #     elif type_name == '装修建材':
        #         pass
        #     elif type_name == '家具家居':
        #         pass
        #     elif type_name == '家装卖场':
        #         pass
        #     elif type_name == '音乐培训':
        #         pass
        #     elif type_name == '职业技术':
        #         pass
        #     elif type_name == '外语培训':
        #         pass
        #     elif type_name == '美术培训':
        #         pass
        #     elif type_name == '医疗健康':
        #         pass
        #     elif type_name == '爱车':
        #         pass
        #     elif type_name == '宠物':
        #         pass
        #     elif type_name == '玩乐':
        #         pass


# if __name__ == '__main__':
#     mt = MeiTuanSpider()
#     mt.spider()
