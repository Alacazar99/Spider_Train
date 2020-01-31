import requests
from concurrent import futures
import threading


def down_file(url,type='content'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
    r = requests.get(url, headers=headers)
    if type == 'text':
        return r.text

    return r.content

class MultiTask:
    def __init__(self):
        self.task_executor = futures.ThreadPoolExecutor(3)
        self.index = 0
        self.save_dir = "./xiaohua/"
        self.lock = threading.Lock()

    def download_img(self,url):
        content = down_file(url)
        # 截取图片名称
        index = url.rfind('/')
        file_name = url[index + 1:]
        save_file = self.save_dir + file_name
        with open(save_file, 'wb+') as f:
            f.write(content)
            with self.lock:
                self.index += 1
            print(save_file + "下载成功,下载图片总数：" + str(self.index))

    def add_download_task(self,imgs):
        if isinstance(imgs,list):
            todo = []
            for url in imgs:
                # 提交任务
                print(url)
                future = self.task_executor.submit(self.download_img,url)
                future.result()
                # todo.append(future)