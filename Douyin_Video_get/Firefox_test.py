from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# douyin_driver = webdriver.Chrome()
# douyin_driver.get("http://www.baidu.com")
# douyin_driver.get("file://‪I:\Spder\Douyin_Video_get\\test.html")

chrome_options = Options()
chrome_options.add_argument("--headless")
douyin_driver = webdriver.Chrome(options=chrome_options)
douyin_driver.get("file://I:\Spider\Douyin_Video_get\\test.html")

# douyin_driver.get("http://www.baidu.com")
signature = douyin_driver.title
# signature = input("输入：")
print(signature)
douyin_driver.quit()