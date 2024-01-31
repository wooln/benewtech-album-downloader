import requests
import os
import json

headers = {
        'authority': 'gateway.benewtech.cn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': 'connect.sid=s%3A4jjJKxcZkRmK5bC8xX6kxOM1mZhcKwAN.Kz3GlArmol0MuUkM1ePUqm47FRyi%2FI1Lelvr8T6eLT0',
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
        media_file_path = os.path.join(dir, '{}.mp3'.format(album['name']))
        if os.path.exists(media_file_path): # 已经保存过的跳过
            continue
        url = 'https://gateway.benewtech.cn/resources-app/cloud/web/share/tracks/{}'.format(album['uid'])
        print(url)     
        response = requests.request("GET", url, headers=headers, data=payload)
        obj = json.loads(response.text)
        url = obj['data']['link'];
        print(url)
        response = requests.request("GET", url, headers=headers, data=payload)
        with open(media_file_path,'wb') as f:        
            f.write(response.content)

if __name__ == '__main__': 
    print('请调用(album_name, album_id)来下载专辑，将下载到 media/album_name目录')
    # download('奇妙小音符','010acbd68422fbe19f33df3572f8c317f37980660b4b10561e9a992952af6558')
    # download('玛丽琼斯和她的圣经1-16','e4f83f00d06e605ea36ae5b0dad58b2e9d6e5b74c74046c075c1dffcf06f223c')
    # download('小小天路客','ae542f529e941ec6a62f198e5080e32ea4684fbb23c8f0349389805ce9a0509f')
    # download('听妈妈讲','3749bdcef36f113953e471d281ba313f8f5009799b96f0f19abe93c9addcd133') 
    # download('语感启蒙系统课儿歌40首','781a2a01d5529c2cd2594bf38926246db7f4be807c859b6f84c2869cf9008fa8') 
    # download('亲子趣英文','0a3ffadbd308f1d8e0ac03ddd15cac7acbb25eea87f222623ca4bb62cd9b43e7')
    # download('好诗咏相传 第一册','b57f2d9de5e89843e439471ad7ea6f1863c61c185611d9e9ed78ac05634b5fd0')
    # download('小听学成语 一年级','6873506e133e52a5ef3133b5e4022ce801c736e0b08001514eaf52f40a128b03')
    # download('动物园开音乐会','487375f1d4771eab4991b8dc3b390b2572455de7c5ecdb18a9c15adb04548abe')
    # download('STEAM探索馆','00effcbb4cf9486c02bfff401294b4d91807e32b95a4c45c07c2a72e7fa4f8f0')
    # download('官方推荐专辑之凯迪克大奖绘本','b7d047916a5cddbfd3c241102cd084a83122bebfaf188b5f6cc2be1910c34cc5')
    # download('官方推荐专辑之宝宝睡前古典乐','56305e23855bbc9ff4fb08d57e2177501792c0fc370d3b5b80457e285390f2e2')
    # download('官方推荐专辑之磨耳朵系列','90c98844e30404158ba0f0eaa2460b986734eead8e3edc31b0fdb81477718b70')