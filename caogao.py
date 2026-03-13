import requests
from bs4 import BeautifulSoup
import os

def scrape_douban_img():

    folder_name='豆瓣电影封面合集'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f'文件夹{folder_name}创建成功')

    #定位进攻坐标
    url = 'https://movie.douban.com/top250'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
    }
    print('锁定目标'+'-'*30)

    #突击步兵进攻
    response = requests.get(url,headers=headers)
    if response.status_code != 200:
        print(f'服务器错误，您的状态码是{response.status_code}')
        return

    #使用BeauitfullSoup翻译战利品
    soup = BeautifulSoup(response.text,'html.parser')
    #从翻译完的战利品里提取我需要的几个类别
    movie_items = soup.find_all('div',class_='item')

    print('开始下载电影封面')

    for item in movie_items:
        title = item.find('span',class_='title').text
        img_tag = item.find('img')
        img_url = img_tag['src']

        # 1. 升级你的装备包（Header）
        img_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
            'Referer': 'https://movie.douban.com/top250'  # 👈 关键！这就是那封“介绍信”
        }

        # 2. 发起带“介绍信”的二次冲锋
        # 注意：这里传的是 img_headers 而不是通用的 headers
        img_response = requests.get(img_url, headers=img_headers)

        file_path = os.path.join(folder_name,f'{title}.jpg')
        with open(file_path,'wb') as f:
            f.write(img_response.content)
        print(f'{title}封面已下载成功')



if __name__=='__main__':
    scrape_douban_img()
