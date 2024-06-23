import requests
import json

url = "https://www.ipalfish.com/pfapi/picturebookunionapi/base/picturebookunion/book/compound/get"

payload = json.dumps({
  "official_account_appid": "wxdcec8d9b3f0b1c7c",
  "h_m": 3274447480,
  "h_src": 24,
  "h_lc": "zh_CN",
  "h_model": "microsoft",
  "cate": 1,
  "h_ts": 1719145822099,
  "token": "CPi0sJkMEPCJ1rMGGAEiCEhuc01OWktJ.75f3fda5a15ed998",
  "ticket": "1195761a19588cc5b33a6f2fadccc3936cd00265a30bb7748b3ddf808b555633b2cc31372478ffd2f2f7889ccd9ac0ddeaa5467d02791c067b192d1e09d8ed9d2a26f2faa9fb696f9342f8092c5c4109b883c4e4b36707a644db302ef2c48c71c3fd3e1cb03be4edad6a6245593f61cd",
  "zone": -480,
  "h_et": 5,
  "atype": 22,
  "book_id": 180003,
  "limit": 10,
  "offset": 0
})
headers = {
  'Host': 'www.ipalfish.com',
  'Connection': 'keep-alive',
  'xweb_xhr': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/9129',
  'Content-Type': 'application/json',
  'Accept': '*/*',
  'Sec-Fetch-Site': 'cross-site',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://servicewechat.com/wx39446263a9b936f2/42/page-frame.html',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': 'ipalfish_device_id=6b79a616e7baad6feabf68bf1628b03e'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
