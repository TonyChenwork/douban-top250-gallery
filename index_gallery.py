import pandas as pd
import os

# 1. 设置路径（这部分你已经写对了）
img_folder = '豆瓣电影封面合集'
csv_file = '电影信息简报.csv'

# 2. 读取数据
df = pd.read_csv(csv_file)

# 3. 准备网页开头（这是你之前写到的地方）
html_content = f"""
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
"""

# 4. 🟢 核心逻辑：循环生成每一张电影卡片（你之前漏掉的部分！）
for i, row in df.iterrows():
    title = row['电影名']
    rating = row['评分']
    img_path = f"{img_folder}/{title}.jpg"
    
    # 检查图片是否存在
    if not os.path.exists(img_path) or os.path.getsize(img_path) == 0:
        img_tag = f'<div style="width:100%; height:300px; background:#333; display:flex; align-items:center; justify-content:center;">Image Missing</div>'
    else:
        img_tag = f'<img src="{img_path}">'

    # 把卡片追加到网页内容里
    html_content += f"""
        <div class="movie-card">
            {img_tag}
            <div class="info">
                <h3>{title}</h3>
                <p>Rating: ★ {rating}</p>
            </div>
        </div>
    """

# 5. 封底
html_content += """
    </div>
</body>
</html>
"""

# 6. 🟢 真正把内容写入硬盘（快门动作！）
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# 7. 打印提示，让你知道它成功了
print("✅ 网页生成成功！快去左侧看 index.html")