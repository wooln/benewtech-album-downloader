import requests
import os
import json

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
payload = {}

def download(album_name, album_id):
    print("1.下载专辑列表")
    url = 'https://gateway.benewtech.cn/resources-app/cloud/web/share/albums/{}/tracks?offset=0&limit=1000'.format(album_id) 
    print(url);
    response = requests.request("GET", url, headers=headers, data=payload)

    dir = 'media/{}'.format(album_name)
    if not os.path.exists(dir):
        os.mkdir(dir)
        print("不存在目录，已创建:{}".format(album_name))

    obj = json.loads(response.text)
    for album in obj['data']['datas']:
        print(album['name'])
        print(album['uid'])
        url = 'https://gateway.benewtech.cn/resources-app/cloud/web/share/tracks/{}'.format(album['uid'])
        print(url)     
        response = requests.request("GET", url, headers=headers, data=payload)
        obj = json.loads(response.text)
        url = obj['data']['link'];
        print(url)
        response = requests.request("GET", url, headers=headers, data=payload)

        media_file_path = os.path.join(dir, '{}.mp3'.format(album['name']))
        with open(media_file_path,'wb') as f:        
            f.write(response.content)

if __name__ == '__main__': 
    print('请调用(album_name, album_id)来下载专辑，将下载到 media/album_name目录')
    # download('奇妙小音符','010acbd68422fbe19f33df3572f8c317f37980660b4b10561e9a992952af6558')
    # download('玛丽琼斯和她的圣经1-16','e4f83f00d06e605ea36ae5b0dad58b2e9d6e5b74c74046c075c1dffcf06f223c')
    # download('小小天路客','ae542f529e941ec6a62f198e5080e32ea4684fbb23c8f0349389805ce9a0509f')
    # download('听妈妈讲','3749bdcef36f113953e471d281ba313f8f5009799b96f0f19abe93c9addcd133') 
