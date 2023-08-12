import requests
url = "https://gateway.benewtech.cn/resources-app/cloud/web/share/albums/010acbd68422fbe19f33df3572f8c317f37980660b4b10561e9a992952af6558/tracks?offset=0&limit=300"

payload = {}
headers = {
  'authority': 'gateway.benewtech.cn',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'cookie': 'connect.sid=s%3ABnPYwLViKnJHOnZEOjVavpjWMfO9ij2b.sy7r526MmUJ%2BlUgv1WZwHwPEBH5NZT0i7bV3kz7U2LQ',
  'origin': 'https://cloud.benewtech.cn',
  'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Linux"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
