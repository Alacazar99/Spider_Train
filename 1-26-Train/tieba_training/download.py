from queue import Queue
import threading
import requests

def down_file(url,type='content'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
    r = requests.get(url, headers=headers)
    if type == 'text':
        return r.text

    return r.content


class DownLoadExecutor(threading.Thread):
    def __init__(self):
        super().__init__()
        self.q = Queue(maxsize=50)
        # 图片保存目录
        self.save_dir = './xiaohua/'
        # 图片计数
        self.index = 0

    def put_task(self,urls):
        if isinstance(urls,list):
            for url in urls:
                self.q.put(url)
        else:
            self.q.put(urls)

    def run(self):
        while True:
            url = self.q.get()
            content = down_file(url)

            # 截取图片名称
            index = url.rfind('/')
            file_name = url[index+1:]
            save_file = self.save_dir + file_name
            with open(save_file, 'wb+') as f:
                f.write(content)
                self.index += 1
                print(save_file + "下载成功,下载图片总数：" + str(self.index))