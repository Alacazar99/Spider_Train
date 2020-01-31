import re
headers_str = """
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: keep-alive
Content-Length: 237
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: OUTFOX_SEARCH_USER_ID_NCOO=1675753892.689935; OUTFOX_SEARCH_USER_ID="1891886365@10.108.160.17"; JSESSIONID=aaaaF06z6d7pJeYtEE6-w; ___rl__test__cookies=1580458772491
Host: fanyi.youdao.com
Origin: http://fanyi.youdao.com
Referer: http://fanyi.youdao.com/
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
X-Requested-With: XMLHttpRequest
"""

pattern = "^(.*?): (.*)$"

for line in headers_str.splitlines():
    print(re.sub(pattern, '\'\\1\':\'\\2\',',line))