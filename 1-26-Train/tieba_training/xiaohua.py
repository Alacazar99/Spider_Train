import requests
from lxml import etree

from download import DownLoadExecutor, down_file

class XiaoHua:
    def __init__(self,init_url):
        self.init_url = init_url
        self.download_executor = DownLoadExecutor()

    def start(self):
        self.download_executor.start()
        self.download(self.init_url)


    def download(self,url):
        html_text = down_file(url,type='text')
        html = etree.HTML(html_text)
        img_urls = html.xpath("//a[contains(@class,'thumbnail')]/img/@bpic")
        self.download_executor.put_task(img_urls)

        # 获取下一页的连接
        next_page = html.xpath("//div[@id='frs_list_pager']/a[contains(@class,'next')]/@href")
        next_page = "http:" + next_page[0]
        self.download(next_page)


if __name__ == '__main__':
    x = XiaoHua("http://tieba.baidu.com/f?kw=校花&ie=utf-8")
    x.start()
#