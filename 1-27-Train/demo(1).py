# *-UTF-8-*
# @Time    : 2019/8/15 12:44
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : demo(1).py
# @Software: PyCharm

from selenium import webdriver
import time


# QQ空间登录
def qq_recive():
    url = 'https://qzone.qq.com/'
    # 构建浏览器对象
    dr = webdriver.Firefox()
    # 访问url
    dr.get(url)
    # 首先必须要进入内部框架iframe!!!! #
    # 进入框架的两种方式
    # 通过id #
    dr.switch_to.frame('login_frame')
    # 通过元素定位
    el_1 = dr.find_element_by_xpath('//*[@id="login_frame"]')
    dr.switch_to.frame(el_1)
    # 尝试点击账号密码登录按钮
    el = dr.find_element_by_id('switcher_plogin')
    el.click()
    # 输入账号密码
    el_user = dr.find_element_by_id('u')
    el_user.send_keys('1178824808')
    el_pwd = dr.find_element_by_id('p')
    el_pwd.send_keys('hsx199888024')
    time.sleep(2)
    # 点击登录
    el_sub = dr.find_element_by_id('login_button')
    el_sub.click()
    dr.close()
    dr.quit()

qq_recive()



from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.alert import Alert


def run():
    browser = webdriver.Firefox()
    url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
    try:
        browser.get(url)
        # 切换到目标元素所在的frame
        browser.switch_to.frame("iframeResult")
        # 确定拖拽目标的起点
        source = browser.find_element_by_id("draggable")
        # 确定拖拽目标的终点
        target = browser.find_element_by_id("droppable")
        # 形成动作链接
        actions = ActionChains(browser)
        actions.drag_and_drop(source, target)

        # 执行
        actions.perform()
        sleep(5)
        '''
        1.先用switch_to_alert()方法切换到alert弹出框上
        2.用text方法获取弹出的文本框的文本信息
        3.accpet()方法点击确认按钮
        4.dimiss()相当于点击右上角的取消按钮，取消弹出框
        '''
        t = browser.switch_to_alert()
        print(t.text)
        t.accept()
        # t.dismiss()
        sleep(10)
    except BaseException as msg:
        print(msg)
    finally:
        browser.close()
run()

# from selenium import webdriver
#
# browser = webdriver.Firefox()
# browser.get('http://www.baidu.com/')


