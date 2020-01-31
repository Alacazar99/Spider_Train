# *-UTF-8-*
# @Time    : 2019/8/15 14:19
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : sele_leaning_jindong.py
# @Software: PyCharm

import time
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# 京东商城搜索
def simulate_jd_search():
    browser = webdriver.Chrome()
    browser.get("https://www.jd.com")
    # 模拟输入问题
    input = browser.find_element_by_id("key")
    input.send_keys("手机")
    time.sleep(3)
    # 模拟清空内容
    input.clear()

    input.send_keys("小猪")
    button = browser.find_element_by_css_selector("button.button")
    button.click()
    time.sleep(10)

simulate_jd_search()


# 动作链：模拟鼠标点击、拖拽、键盘按键等操作；
def simulate_drop():
    browser = webdriver.Chrome()
    browser.get("https://www.runoob.com/try/try.php?filename=jqueryui-example-droppable")
    # 切换到id是iframeResult的iframe标签中；

    browser.switch_to.frame("iframeResult")
    source = browser.find_element_by_css_selector("#draggable")
    target = browser.find_element_by_css_selector("#droppable")
    actions = ActionChains(browser)

    actions.drag_and_drop(source,target)
    actions.perform()   #执行
    time.sleep(10)
    actions.click()
    #延迟10秒

# simulate_drop()


# 执行js代码
def execute_js():
    # 执行js代码：execute_script()
    browser = webdriver.Chrome()
    browser.get("https://www.jd.com")
    while True:
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        # browser.execute_script("alert('滚动到底部')")
    # time.sleep(100)
# execute_js()

# 获取属性信息
def get_node_info():
    browser = webdriver.Chrome()
    browser.get("https://www.jd.com")
    input= browser.find_element_by_id("key")
    # 获取属性信息
    print(input.get_attribute("class"))

    # 获取属性节点的文本值，使用text属性
    a_node = browser.find_element(By.ID,"navitems-group2")
    print(a_node.text)

    # 获取id、位置、标签、大小
    print(input.id)
    print(input.location)
    print(input.tag_name)
    print(input.size)
    time.sleep(3)

get_node_info()


def switch_iframe():
    pass
    browser = webdriver.Chrome()
    # 切换到指定id的iframe中
    browser.switch_to.frame("ifame_id")
    # 切换回 iframe 所在的外部界面；
    browser.switch_to.parent_frame()


# 延时等待；
def wait_page():
    pass
    # 隐式等待：设置脚本在查找元素时的最大等待时间
    browser = webdriver.Chrome()
    browser.get("https://www.zhihu.com/explore")
    browser.implicitly_wait(10)
    elements = browser.find_elements(By.CLASS_NAME,"ExploreFollowButton")
    print(elements)


    # 显示等待：就是明确的要等待的元素在规定的时间之内都没找到,那么就抛出Exception.
    browser.get("https://www.taobao.com")
    wait = WebDriverWait(browser,10)
    input(wait.until(EC.presence_of_all_elements_located((By.ID, "q"))))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-search")))
    print(input,button)


# 等待的条件       |含义
# title_is     | 标题是某内容
# title_contains     | 标题包含某内容
# presence_of_element_located | 节点加载出来，需要传入定位元组，如：(By.ID,'q')
# visibility_of_element_located | 节点可见，传入定位元组
# visibility_of  | 传入的节点对象可见
# presence_of_all_elements_located | 所有节点可见
# text_to_be_present_in_element | 某个节点包含某文字
# element_to_be_clickable | 节点可被点击
# staleness_of | 判断一个节点是否仍在DOM中，可以判断页面是否被刷新
# alert_is_present | 判断警告框是否弹出
wait_page()


# 网页前进一步、后退一步
def control_browser():
    browser = webdriver.Chrome()
    browser.get("https://www.jd.com")
    browser.get("https://www.baidu.com")
    browser.get("https://www.tianmao.com")
    browser.get("https://www.taobao.com")

    browser.back()
    sleep(2)
    browser.forward()
    browser.forward()
    sleep(2)
    browser.close()

control_browser()


# 获取cookie
def opt_cookie():
    browser = webdriver.Chrome()
    browser.get("https://www.baidu.com")
    # 获取所有cookie
    print(browser.get_cookies())
    # 添加cookie
    browser.add_cookie({"name":"username", "value":"Zurich"})
    print(browser.get_cookies())
    # 删除 cookie
    browser.delete_all_cookies()
    print(browser.get_cookies())

opt_cookie()

# js新打开一个标签页
def opt_tag():
    browser = webdriver.Chrome()
    browser.get("https://www.tianmao.com")
    # 用js新打开一个标签页
    sleep(5)
    browser.execute_script("window.open('https://www.jd.com')")
    sleep(5)
    browser.execute_script("window.open('https://www.taobao.com')")
    # 获取所有的标签
    print(browser.window_handles)
    browser.switch_to.window(browser.window_handles[1])
    sleep(5)
    browser.switch_to.window(browser.window_handles[0])
    sleep(5)
    browser.switch_to.window(browser.window_handles[2])
    sleep(5) #直接延迟5秒

opt_tag()


# 网站首页截图
def opt_phantom_js():
    # 网站首页截图：方式 1
    from selenium.webdriver.chrome.options import Options
    chrome_options= Options()
    chrome_options.add_argument("——headless")
    broswer = webdriver.Chrome(options=chrome_options)

    # 网站首页截图：方式 2
    # broswer = webdriver.PhantomJS()

    broswer.get("http://www.tianmao.com")
    broswer.save_screenshot("tianmao.png")

opt_phantom_js()


# 图像识别库：
# pip install tesserocr