import pandas as pd
import os

img_folder = '豆瓣电影封面合集'
csv_file = '电影信息简报.csv'

#得到‘电影信息简报.csv’和‘豆瓣电影封面合集’数据-----循环赋值给新变量

#找出html文件需要的滤镜代码（不含末尾）
html_content = f'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Alfred's Cinema Archive</title>
    <style>
        body {{ background-color: #0a0a0a; color: #e0e0e0; font-family: sans-serif; padding: 40px; }}
        .gallery {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 30px; }}
        .movie-card {{ background: #161616; border-radius: 8px; overflow: hidden; transition: transform 0.3s; border: 1px solid #222; }}
        .movie-card:hover {{ transform: translateY(-10px); border-color: #444; }}
        .movie-card img {{ width: 100%; height: 300px; object-fit: cover; }}
        .info {{ padding: 15px; }}
        h3 {{ margin: 0; font-size: 16px; color: #fff; }}
        p {{ color: #888; font-size: 14px; margin-top: 5px; }}
    </style>
</head>
<body>
    <h1 style="text-align: center; margin-bottom: 50px; letter-spacing: 5px;">TOP 250 MOVIE ARCHIVE</h1>
    <div class="gallery">
'''


#得到‘电影信息简报.csv’和‘豆瓣电影封面合集’数据-----循环赋值给新变量
df = pd.read_csv('电影信息简报.csv')

for i,row in df.iterrows():
    img_title = row['电影名']
    img_rating = row['评分']
    img_quote = row['评语']
    img_path = f'{img_folder}/{img_title}.jpg'

#写出html文件放一个电影的框架然后写循环放入全部
    html_content += f'''
    <div class='movie-card'>
        <img src='{img_path}'>
        <div class='info'>
            <h3>{img_title}</h3>
            <p>评分⭐{img_rating}</p>
            <p>评语：{img_quote}</p>
        </div>
    </div>
    '''

#补全html收尾的代码
html_content += f'''
    </div>
</body>
</html>
'''
#使用with open（）as f；创建.html文件并写入代码
with open('IW_index.html','w',encoding='UTF-8-sig') as f:
    f.write(html_content)

print('html文件以自动生成！')

    