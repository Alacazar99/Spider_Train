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

wm_dtype: microsoft
wm_dversion: 7.0.4
wm_dplatform: windows
wm_uuid: 1167636692753145881
wm_longitude: 106554449
wm_latitude: 29561864
wm_visitid: c957b7e5-db08-4684-ad81-f7b9fc35ca03
wm_appversion: 5.1.2
wm_logintoken: Z_SWQMrvu-s86wtXOiYsKZsUxXMAAAAA-wkAANw7QPJxa1l8Hi-hgCZyzGu4voDqFuAcjQ4DjBm8d_AAodF7hUtDPK4dY0QzBrYksw
userToken: Z_SWQMrvu-s86wtXOiYsKZsUxXMAAAAA-wkAANw7QPJxa1l8Hi-hgCZyzGu4voDqFuAcjQ4DjBm8d_AAodF7hUtDPK4dY0QzBrYksw
req_time: 1581393022486
waimai_sign: /
wm_actual_longitude: 106554449
wm_actual_latitude: 29561864
userid: 1807785726
user_id: 1807785726
lch: 1007
optimusCode: 20
riskLevel: 71
partner: 4
platform: 13
uuid: 1167636692753145881
open_id: oOpUI0V0ofGrOeWmbZp1PrENesaA
rc_app: 4
rc_platform: 13
sort_type: 0
second_category_type: 0
category_type: 0
navigate_type: 0
load_type: 1
page_size: 20
page_index: 0
_token: eJxVkkuPolAQhf8LW0zgXl7eTnrBWxBQoQGh0wsEQUAQectk/vvQmU4mk1TqO3XOWdYvrNUS7A2QJAnYDdZ3q2a2gEIUCSGNViv+32MA2GCX1pOwt0+apjcsYL6+DXu9PxmG2XAs+tr8U5Be57uhrQWsibJrR+R1cp3/bmyDYWtafazpyvKH0Q/7H3Z5VmNv2FV/oTIGr2rh3VuyvYtURMvlTTOU/DTI9cUyZNSGY6CSgW/eAzOXM/EiISRoJXdxLon37LmROtbEbU5iNVQe6Wnutomqm3yLO6zAC+LoiTNxS8TWd2LDo7LBfcCHyZR11AfdSOvpSQUjkqetp/eAx1N2y5GTsfMU7x71g7dnHN7IrGg6VdG8xG5xlXPreKGfsE94fds8HRhRjnfSpQ/iYFoBlIwxN3I8Na1z2AanVjrwtpCpRRn5NaRIt349bH6Z8oEtZi5lehs2XAGyArk4UOrotewm3DggCManYl9mVMeVNwAYMldjNm54SuGLg7jtPScGig/kinB26Hzew2PDdH7it2xqwYpQK6Ep8bMSw8VSzoyVlD13tvGc0DxfnwbkNyNe7zJaqMpMEPeOLVqsAJrbPKs6/yz2PK1J+U68y/sx5PScvN99YJZ1y25fc0UZr24KNUhyB2EpREvTiKhqhjrztCCb7KxQHuhB1omgPotWkJdMF7pw5xFPiaQDkoCA5ijGRH4kByR5H7xQvVyhtjwobS2rpE0MLtuIYAyJqiAPRCqx6dLHYbj+dPEMZ+bW5aaAj9nOtWdFOXZdg4yklCFicqmU6Ng1vFfsi9P7O/b7Dz0M9RQ=
rank_list_id: 1343b13af587024af82ab11676366927
wm_ctype: wxapp

"""

pattern = "^(.*?): (.*)$"

for line in headers_str.splitlines():
    print(re.sub(pattern, '\'\\1\':\'\\2\',',line))