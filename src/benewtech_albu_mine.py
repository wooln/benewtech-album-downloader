import requests
import os
import json

headers = {
        'authority': 'gateway.benewtech.cn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': 'connect.sid=s:Ic8qBYOrqwgei6HJCSUhYy7ZoSCmmcJZ.hqWuJoPKfVkA9Aj2cmY8Zzt0laZTtigi5apValMobKo',
        'origin': 'https://pan.benewtech.cn',
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
    url = 'https://gateway.benewtech.cn/resources-app/cloud/web/albums/{}/tracks?offset=0&limit=500&order=&familyId=3245226'.format(album_id) 
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
        media_file_path = os.path.join(dir, '{}.mp3'.format(album['name']))
        if os.path.exists(media_file_path): # 已经保存过的跳过
            continue
        url = album['trackUrl']
        print(url)        
        response = requests.request("GET", url, headers=headers, data=payload)
        with open(media_file_path,'wb') as f:        
            f.write(response.content)

if __name__ == '__main__': 
    # print('请调用(album_name, album_id)来下载专辑，将下载到 media/album_name目录')
    download('糖溪帮第1季1_老树洞的藏宝图', '1627759404')