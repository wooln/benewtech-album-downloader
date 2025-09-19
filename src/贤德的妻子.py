# [贤德的妻子-30/4/24 | 扎根 建基 有声书 ｜ 教会 真理](https://zhagenvoice.com/book/65600c5240e7fa9950208ed5)

import json
import os
import requests
import re

def sanitize_filename(filename):
    """清理文件名中的非法字符"""
    # 替换文件名中的非法字符为下划线
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # 去除首尾空格
    sanitized = sanitized.strip()
    return sanitized

def download_audio_files():
    # 读取JSON文件
    json_file_path = os.path.join(os.path.dirname(__file__), '贤德的妻子有声书.json')
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 获取基础URL和章节列表
    base_url = data['props']['pageProps']['book']['description']['baseUrl']
    chapters = data['props']['pageProps']['book']['chapters']
    
    # 创建目标目录
    media_dir = os.path.join(os.path.dirname(__file__), '..', 'media')
    target_dir = os.path.join(media_dir, '贤德的妻子')
    os.makedirs(target_dir, exist_ok=True)
    
    # 下载每个章节的音频文件
    for i, chapter in enumerate(chapters, 1):
        title = chapter['title']
        url = chapter['url']
        full_url = f"{base_url}/{url}"
        
        # 生成文件名并清理非法字符
        filename = f"{title}.mp3"
        filename = sanitize_filename(filename)
        file_path = os.path.join(target_dir, filename)
        
        # 如果文件已存在，跳过下载
        if os.path.exists(file_path):
            print(f"文件已存在，跳过: {filename}")
            continue
        
        try:
            # 下载文件
            print(f"正在下载 ({i}/{len(chapters)}): {title}")
            response = requests.get(full_url)
            response.raise_for_status()
            
            # 保存文件
            with open(file_path, 'wb') as f:
                f.write(response.content)
            
            print(f"下载完成: {filename}")
        except Exception as e:
            print(f"下载失败 {title}: {str(e)}")
    
    print(f"所有音频文件下载完成！保存在: {target_dir}")

if __name__ == "__main__":
    download_audio_files()