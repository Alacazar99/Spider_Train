import pymongo
from pymongo.collection import Collection

client = pymongo.MongoClient(host='127.0.0.1:27017',port=27037)
db = client["douyin"]

def handle_init_task():
    task_id_collection = Collection(db,"task_id")
    with open("douyin_zhanghao.txt",'r') as f_share:
        for f_share_task in f_share.readlines():
            init_task = {}
            init_task['share_id'] = f_share_task.replace("\n",'')
            task_id_collection.insert(init_task)

def save_task(task):
    task_id_collection = Collection(db,'task_id')
    task_id_collection.update({'share_id':task['share_id']},task,True)

def handle_get_task():
    task_id_collection = Collection(db,'task_id')

    # print(task_id_collection)
    return task_id_collection.find_one_and_delete({})

handle_init_task()
# handle_get_task()
