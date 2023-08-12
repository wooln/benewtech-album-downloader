# 牛听听专辑下载

步骤:
1. 通过分享的专辑id进入网页，微信登录
https://cloud.benewtech.cn/fh5/album/010acbd68422fbe19f33df3572f8c317f37980660b4b10561e9a992952af6558

2. 查找分页获取track的信息，默认30个每一页，改为较大数值，如1000
https://gateway.benewtech.cn/resources-app/cloud/web/share/albums/010acbd68422fbe19f33df3572f8c317f37980660b4b10561e9a992952af6558/tracks?offset=0&limit=30

https://gateway.benewtech.cn/resources-app/cloud/web/share/albums/010acbd68422fbe19f33df3572f8c317f37980660b4b10561e9a992952af6558/tracks?offset=0&limit=1000

3. 下载的json中获取track id列表

4. 通过track id请求track详情，里面的data.link是音频地址
https://gateway.benewtech.cn/resources-app/cloud/web/share/tracks/64645916

5. 下载音频即可