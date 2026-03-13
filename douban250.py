import requests
from bs4 import BeautifulSoup
import csv

def scrape_douban():
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
    #讲这几个类别的战利品的具体的零件提出来分析并输出

    with open('电影信息简报.csv','w',encoding='utf-8-sig',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['电影名','评分','评语'])

        for item in movie_items:
            title = item.find('span',class_='title').text
            rating = item.find('span',class_='rating_num').text
            quote_try = item.find('p',class_='quote')
            if quote_try:
                quote = quote_try.text.strip()
            else:
                quote='这个电影很高冷，没有评论'

            writer.writerow([title, rating, quote])
            print(f'{title}已存入库')
            print(title)
            print(rating)
            print(quote)
            print('-'*30)

        writer.writerow([title,rating,quote])
        print(f'{title}已存入库')

if __name__=='__main__':
    scrape_douban()






