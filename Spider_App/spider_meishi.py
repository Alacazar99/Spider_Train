import requests
import  ssl
import urllib.request
import requests
import urllib.parse
import execjs
import json
import  base64
import time
import  zlib
import datetime
import random

def get_visit_id():
    js = execjs.compile('''
    var x = function() {
    var x = Date.now();
    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g,
    function(r) {
        var t = (x + 16 * Math.random()) % 16 | 0;
        return x = Math.floor(x / 16),
        ("x" === r ? t: 3 & t | 8).toString(16);
    });
};

    var r = 0,
    t = "";

    getVisitID = function() {
        var e = Date.now();
        return (!t || r < e - 18e5) && (r = e, t = x()),
            t;
        };
    ''')
    result = js.call('getVisitID')
    return result

def handel_request(url,data):
    headers = {
        'Host':'wx.waimai.meituan.com',
        'Connection':'keep-alive',
        'Content-Length':'1847',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'content-type':'application/x-www-form-urlencoded',
        'r2x-referer':'https://servicewechat.com/wx2c348cf579062e56/0/page-frame.html',
        'uuid':'1167636692753145881',
        'wm-ctype':'wxapp',
        'Referer':'https://servicewechat.com/wx2c348cf579062e56/237/page-frame.html',
        'Accept-Encoding':'gzip, deflate, br',
    }
    response = requests.post(url = url,headers = headers,data = data)
    return response

# 获取_token参数
def get_list_token(open_id,page_index,page_size,req_time,sort_type,user_token,user_id,uuid,lat,lon,platform,dtype,visitid):
	sign = "category_type=0&lch=1089&load_type=1&navigate_type=0&open_id={}&optimusCode=20&page_index={}&page_size={}&partner=4&platform=13&rc_app=4&rc_platform=13&req_time={}&riskLevel=71&second_category_type=0&sort_type={}&userToken={}&user_id={}&userid={}&uuid={}&waimai_sign=/&wm_actual_latitude={}&wm_actual_longitude={}&wm_appversion=5.0.0&wm_ctype=wxapp&wm_dplatform={}&wm_dtype={}&wm_dversion=7.0.8&wm_latitude={}&wm_logintoken={}&wm_longitude={}&wm_uuid={}&wm_visitid={}".format(open_id,page_index,page_size,req_time,sort_type,user_token,user_id,user_id,uuid,lat,lon,platform,dtype,lat,user_token,lon,uuid,visitid)
	bz_sign = base64.b64encode(zlib.compress(sign.encode(encoding="utf-8"))).decode()
	t = int(time.mktime(
		(datetime.datetime.now() - datetime.timedelta(minutes=random.randint(5, 20))).timetuple()) * 1000)
	cs = int(round(time.time() * 1000))
	token = {
		"rId":100016,"ts":t,"cts":cs,"brVD":[414,624],"brR":[[1242,1872],[1242,1872],24,24],
		"bI":["pages/index/index",""],
		"mT":["244,577","247,550","255,499","270,446","287,410","301,387","200,403","203,398","212,293","223,250","231,220","233,205","9,124","38,143","71,169","101,208","121,247","132,272","2,104","9,118","24,134","41,151","52,164","61,176","61,179","61,178","83,200","113,260","129,312","135,351"],
		"kT":[],
		"aT":["145,1226,view","317,1467,view","36,1330,view","50,1229,view","100,2278,view","78,2222,view","76,2218,view","66,2233,view","137,1234,view","173,1320,view","59,1232,view","56,134,view","50,454,view","268,547,view","63,131,view","143,129,view","113,13,view","110,12,view","216,96,view","238,108,view","139,89,view","53,132,view","118,1339,view","76,1243,view","151,14,view","73,16,view"],
		"tT":["244,577,1","247,550,1","255,499,1","270,446,1","287,410,1","301,387,1","200,403,1","203,398,1","212,293,1","223,250,1","231,220,1","233,205,1","9,124,1","38,143,1","71,169,1","101,208,1","121,247,1","132,272,1","2,104,1","9,118,1","24,134,1","41,151,1","52,164,1","61,176,1","61,179,1","61,178,1","83,200,1","113,260,1","129,312,1","135,351,1"],
		"sign":bz_sign
	}
	# str.encode(json.dumps(token).replace(" ",""))
	bz_token = base64.b64encode(zlib.compress(json.dumps(token).replace(" ","").encode(encoding="utf-8"))).decode()
	return bz_token

def handle_index():
    url ="https://wx.waimai.meituan.com/weapp/v2/poi/homepage?ui=1807785726&region_id=1000130300&region_version=1580907712941"
    open_id = 'oOpUI0V0ofGrOeWmbZp1PrENesaA'
    page_index = '0'
    page_size = '20'
    req_time = '1581395721513'
    sort_type = '0'
    user_token = 'Z_SWQMrvu-s86wtXOiYsKZsUxXMAAAAA-wkAANw7QPJxa1l8Hi-hgCZyzGu4voDqFuAcjQ4DjBm8d_AAodF7hUtDPK4dY0QzBrYksw'
    user_id = '1807785726'
    uuid = '1167636692753145881'
    lat = '29561864'
    lon = '106554449'
    platform = '13'
    dtype = '0'
    visitid = get_visit_id()
    _token = get_list_token(open_id, page_index, page_size, req_time, sort_type, user_token, user_id, uuid, lat, lon,platform, dtype, visitid)

    data = {
        'ui': '1807785726',
        'region_id': '1000130300',
        'region_version': '1580907712941',
        'wm_uuid': uuid,
        'wm_longitude': lon,
        'wm_latitude': lat,
        'wm_visitid': visitid,
        'wm_appversion': '5.1.2',
        'wm_logintoken': user_token,
        'userToken': user_token,
        'req_time': req_time,
        'waimai_sign': '/',
        # 'wm_actual_longitude': '106554449',
        # 'wm_actual_latitude': '29561864',
        'userid': '1807785726',
        'user_id': '1807785726',
        'lch': '1007',
        'optimusCode': '20',
        'riskLevel': '71',
        'partner': '4',
        'platform': '13',
        'uuid': uuid,
        'open_id':open_id,
        'rc_app': '4',
        'rc_platform': platform,
        'sort_type': '0',
        'second_category_type': '0',
        'category_type': '0',
        'navigate_type': '0',
        'load_type': '1',
        'page_size': page_size,
        'page_index': page_index,
        '_token':_token,
        'rank_list_id': '1343b13af587024af82ab11676366927',
        'wm_ctype': 'wxapp',
    }

    response = handel_request(url=url,data = data)
    print(response)

handle_index()