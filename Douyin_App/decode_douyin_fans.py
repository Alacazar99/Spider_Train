import json

try:
    from Douyin_App.douyin_db import save_task
except:
    from douyin_db import save_task

def response(flow):
    # 通过抓包软件获取请求的接口；
    if "aweme/v1/user/follower/list" in flow.request.url:
    #     with open("user.txt",'W') as f:
    #         f.write(flow.response.text)
        # 数据的解析
        for user in json.loads(flow.response.text)["follwers"]:
            douyin_info = {}
            douyin_info["share_id"] = user['id']
            douyin_info['douyin_id'] = user['short_id']
            douyin_info['nickname'] = user['nickname']
            save_task(douyin_info)