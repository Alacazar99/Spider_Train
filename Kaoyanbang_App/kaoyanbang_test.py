import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# 请求参数；
cap = {

}

driver = webdriver.Remote("http://localhost:4723/wd/hub",cap)

# 获取尺寸
def get_size():
    x = driver.get_window_size()["width"]
    y = driver.get_window_size()["height"]
    return (x,y)
try:
    # 是否跳过；
    if WebDriverWait(driver,3).unitl(lambda x:x.find_element_by_class_name("")):
        driver.find_element_by_class_name("").click()
except:
    pass


try:
    # 输入用户名，密码；
    if WebDriverWait(driver, 3).unitl(lambda x: x.find_element_by_class_name("")):
        driver.find_element_by_class_name("").send_keys("zhanghao")
        driver.find_element_by_class_name("").send_keys("mima")
        driver.find_element_by_class_name("").click()
except:
    pass


try:
    # 判断隐私条款；
    if WebDriverWait(driver,3).unitl(lambda x:x.find_element_by_class_name("")):
        driver.find_element_by_class_name("").click()
except:
    pass
# 点击某项功能；
if WebDriverWait(driver, 3).unitl(lambda x: x.find_element_by_class_name("")):
    driver.find_element_by_class_name("").click()

    # 定位鼠标；
    L = get_size()
    x1 = int(L[0]*0.5)
    y1 = int(L[1]*0.75)
    y2 = int(L[1]*0.25)

    while True:
        driver.swipe(x1,y1,x1,y2)  # 鼠标滑动
        time.sleep(0.6)