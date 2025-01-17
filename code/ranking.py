import requests
import pandas as pd
import os
import numpy as np

def rnkg(url, path, rank):
    """
    Fetch and process QS ranking data, including extracting city and country,
    and save the data to a CSV file.
    
    Args:
        url (str): QS ranking API URL.
        path (str): Directory to save the output CSV file.
        rank (str): Ranking category name (e.g., "Econ").
    
    Returns:
        None
    """
    # 設置 User-Agent 模擬正常瀏覽器請求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    # 發送請求獲取 JSON 數據
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 確保請求成功
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return

    # 解析 JSON 數據
    try:
        res = response.json()
        df = pd.json_normalize(res, record_path=['data'])
    except Exception as e:
        print(f"Error parsing JSON data: {e}")
        return

    # 數據清理
    df = df.replace(r'^\s*$', np.nan, regex=True)  # 替換空字符串為 NaN
    df = df.fillna(0)  # 填充 NaN
    if 'score' in df.columns:
        df['score'] = df['score'].astype(float)  # 確保分數為浮點數

    # 提取學校名稱和城市/國家
    if 'title' in df.columns:
        left = 'k">'
        right = '</a'
        df['University'] = df['title'].str.extract(r'k">(.*?)</a')
    
    if 'location' in df.columns:
        df[['City', 'Country']] = df['location'].str.split(',', expand=True)
        df['City'] = df['City'].str.strip()  # 清理空格
        df['Country'] = df['Country'].str.strip()  # 清理空格

    # 保存數據為 CSV 文件
    output_file = os.path.abspath(os.path.join(path, f'Ranking_{rank}.csv'))
    try:
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"Ranking data for {rank} saved to {output_file}")
    except Exception as e:
        print(f"Error saving CSV file: {e}")

# 主程式：調用 rnkg 函數抓取並保存多個排名數據
if __name__ == "__main__":
   
    # 獲取用戶目錄
    path = os.path.join(os.environ['HOME'], 'Desktop', 'QS_Rankings')  # 儲存目錄
    os.makedirs(path, exist_ok=True)  # 如果目錄不存在則創建


    # 替換為從 QS 網站獲取的 URL
    subjects = {
        'Econ': "https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3517143.txt",
        'Engineering': "https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3517112.txt",
        'Medicine': "https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3517165.txt"
    }

    # 遍歷每個學科並抓取數據
    for rank, url in subjects.items():
        rnkg(url, path, rank)
