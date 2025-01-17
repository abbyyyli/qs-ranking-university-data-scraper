import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
import time

# QS 學科排名的 URL 模板
BASE_URL = "https://www.topuniversities.com/university-subject-rankings/{}"

# 學科列表（54 個學科標識符）
SUBJECTS = [
    "engineering-technology", "medicine", "computer-science-information-systems",
    "business-management", "economics-econometrics", "arts-humanities",
    "natural-sciences", "social-sciences-management", "life-sciences-medicine",
    "engineering-mechanical-aeronautical-manufacturing",
    "engineering-civil-structural", "law-legal-studies", "education",
    "environmental-studies", "architecture", "philosophy",
    # 添加完整 54 個學科標識符
]

# 創建目標資料夾
OUTPUT_DIR = "qs_subject_rankings"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_qs_subject_rankings(subject):
    """
    抓取特定學科的 QS 排名數據並返回 DataFrame。
    """
    url = BASE_URL.format(subject)
    print(f"Fetching subject: {subject} ({url})")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch data for subject: {subject}")
        return pd.DataFrame()

    soup = BeautifulSoup(response.content, 'html.parser')

    # 找到排名數據表
    rankings = []
    rows = soup.find_all('div', class_='main ranking-row-js-')
    for row in rows:
        try:
            rank = row.find('div', class_='rank').text.strip()
            university = row.find('div', class_='uni').text.strip()
            location = row.find('div', class_='location').text.strip()
            rankings.append({'Rank': rank, 'University': university, 'Location': location})
        except Exception as e:
            print(f"Error parsing row: {e}")

    # 轉為 DataFrame
    df = pd.DataFrame(rankings)
    return df

def main():
    """
    抓取所有學科的 QS 排名數據並保存為獨立的 CSV 文件。
    """
    for subject in SUBJECTS:
        # 抓取數據
        df = fetch_qs_subject_rankings(subject)
        if not df.empty:
            # 保存為 CSV
            output_file = os.path.join(OUTPUT_DIR, f"{subject.replace('/', '_')}.csv")
            df.to_csv(output_file, index=False, encoding="utf-8")
            print(f"Saved rankings for {subject} to {output_file}")
        else:
            print(f"No data found for subject: {subject}")
        time.sleep(2)  # 延遲避免觸發反爬機制

if __name__ == "__main__":
    main()
