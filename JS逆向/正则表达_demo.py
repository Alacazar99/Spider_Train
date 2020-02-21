import re
"""
Host: wx.waimai.meituan.com
Connection: keep-alive
Content-Length: 1847
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat
content-type: application/x-www-form-urlencoded
r2x-referer: https://servicewechat.com/wx2c348cf579062e56/0/page-frame.html
uuid: 1167636692753145881
wm-ctype: wxapp
Referer: https://servicewechat.com/wx2c348cf579062e56/237/page-frame.html
Accept-Encoding: gzip, deflate, br
"""
headers_str = """
ui:1807785726
region_id:1000130300
region_version:1580907712941
"""

pattern = "^(.*?):(.*)$"

for line in headers_str.splitlines():
    print(re.sub(pattern, '\'\\1\':\'\\2\',',line))