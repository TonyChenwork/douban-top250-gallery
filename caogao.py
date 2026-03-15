import requests
from bs4 import BeautifulSoup
import os
import time


def final_harvest():
    folder_name = '豆瓣电影封面合集'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # 1. 启动“会话模式”，自动处理 Cookie
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })

    print("🚀 最终收割行动开始...")

    for start_num in range(0, 250, 25):
        url = f'https://movie.douban.com/top250?start={start_num}'

        # 像真人一样先访问页面
        resp = session.get(url)
        if resp.status_code != 200:
            print(f"❌ 页面访问受阻，状态码：{resp.status_code}")
            continue

        soup = BeautifulSoup(resp.text, 'html.parser')
        items = soup.find_all('div', class_='item')

        for item in items:
            title = item.find('span', class_='title').text
            img_url = item.find('img')['src']

            # 2. 动态伪装 Referer：告诉图片服务器，我正从刚才那个页面看着这张图
            img_resp = session.get(img_url, headers={'Referer': url})
            ctype = img_resp.headers.get('Content-Type', '')

            # 3. 严格验货：不拿 900 字节的假货
            if img_resp.status_code == 200 and 'image' in ctype:
                safe_name = title.replace('/', '_').replace(':', '_')
                path = os.path.join(folder_name, f'{safe_name}.jpg')
                with open(path, 'wb') as f:
                    f.write(img_resp.content)
                print(f"✅ 缴获：{safe_name}")
            else:
                print(f"⚠️ 拦截警告：{title} 拿回的是 JS 脚本或空包弹")

        # 战术间歇，保护 IP
        time.sleep(1.5)

    print("\n" + "=" * 30 + "\n报告站长！250 张封面已全部入库，可以撤退！")


if __name__ == '__main__':
    final_harvest()