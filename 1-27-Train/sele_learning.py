# *-UTF-8-*
# @Time    : 2019/8/15 10:55
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : sele_learning.py
# @Software: PyCharm


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Firefox()
try:
    browser.get("https://www.baidu.com")
    input = browser.find_element_by_id('kw')
    input.send_keys('简书')
    input.send_keys(Keys.ENTER)
    # 等待对象反应
    wait = WebDriverWait(browser,100)
    locator = (By.ID,"content")
    wait.until(EC.presence_of_element_located((locator)))
    print(browser.current_url)
    print(browser.get_cookies())
    # print(browser.page_source)
    ele = browser.find_element_by_id("content_left")
    print(ele)


    # 查找节点；
    # 查找单节点
    # 通过id查找：

    # 原生语法
    browser.find_element_by_id("kw")
    # css语法
    browser.find_element_by_css_selector("#kw")
    # xpath语法：
    browser.find_element_by_xpath("//*[@id='kw']")
    # 【总结】：这三种方法获取的元素类型都是WebElement类型；

    # browser.find_element_by_id("kw")
    # # 另一种形式：
    # browser.find_element((By.id,"kw"))


    ##多个节点和查找单个节点相同，只是将element + s.例如：
    # browser.find_elements_by_css_selector()
    # browser.find_elements_by_id()
    # browser.find_elements_by_name()
    # browser.find_elements_by_link_text()
    # browser.find_element_by_partial_link_text()

finally:
    browser.close()
    # pass

