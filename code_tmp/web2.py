import json
from bs4 import BeautifulSoup

# 載入提供的 HTML 檔案
with open("a.txt", "r", encoding="utf-8") as file:
    html_content = file.read()

# 解析 HTML
soup = BeautifulSoup(html_content, "html.parser")

# 儲存學校數據的列表
school_data = []

# 找到所有排名項目
ranking_rows = soup.find_all("div", class_="main ranking-row-js-")

for row in ranking_rows:
    try:
        # 提取排名
        rank = row.find("div", class_="rank-no").get_text(strip=True)

        # 提取學校名稱
        university_name = row.find("a", class_="uni-link").get_text(strip=True)

        # 提取學校位置
        location = row.find("div", class_="location").get_text(strip=True)

        # 儲存數據
        school_data.append({
            "Rank": rank,
            "University": university_name,
            "Location": location
        })
    except AttributeError:
        continue  # 如果某個元素不存在，跳過該項目

# 將結果保存為 JSON 文件
with open("school_data.json", "w", encoding="utf-8") as json_file:
    json.dump(school_data, json_file, ensure_ascii=False, indent=4)

print("數據提取完成並儲存至 school_data.json")
