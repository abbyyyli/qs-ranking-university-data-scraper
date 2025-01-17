import requests
import pandas as pd
import time

# QS Rankings API Endpoint
RANKING_API_URL = "https://www.topuniversities.com/rankings/endpoint"

# 爬取學科數據
def fetch_subject_rankings(subject, full_view=False, **kwargs):
    all_rankings = []
    page = 1
    items_per_page = 100  # 每頁 100 條記錄

    while True:
        print(f"Fetching subject '{subject}' - Page {page}...")
        query_params = {
            "subject": subject,
            "page": page,
            "items_per_page": items_per_page,
            "sort_by": "overallscore",
            "order_by": "asc",
            "tab": "indicators" if full_view else "",
            **kwargs,  # 額外參數（如地區、國家等）
        }

        response = requests.get(RANKING_API_URL, params=query_params)
        if response.status_code != 200:
            print(f"Error fetching page {page}: {response.status_code}")
            break

        data = response.json().get("score_nodes", [])
        if not data:
            print(f"No more data for subject '{subject}'.")
            break

        all_rankings.extend(data)
        page += 1
        time.sleep(2)  # 延遲以防止過快爬取

    return pd.DataFrame(all_rankings)

# 按學科爬取並保存數據
def scrape_and_save_by_subject(subjects, full_view=False, output_dir="rankings"):
    for subject in subjects:
        print(f"開始爬取學科: {subject}")
        rankings = fetch_subject_rankings(subject, full_view=full_view)

        # 清理數據（可選）
        rankings.drop(columns=["nid", "score_nid", "logo", "path", "dagger"], errors="ignore", inplace=True)

        # 展開指標數據（可選）
        if "scores" in rankings.columns:
            indicators_data = rankings["scores"].apply(parse_indicators)
            indicators_df = pd.DataFrame(indicators_data.tolist())
            rankings = pd.concat([rankings, indicators_df], axis=1)
            rankings.drop(columns=["scores"], inplace=True)

        # 保存為 CSV 文件
        file_name = f"{output_dir}/QS_{subject.replace('/', '_')}_Rankings.csv"
        rankings.to_csv(file_name, index=False, encoding="utf-8")
        print(f"學科 {subject} 的數據已保存至 {file_name}")

# 解析指標數據
def parse_indicators(indicators):
    parsed_data = {}
    for indicator in indicators:
        parsed_data[f"{indicator['indicator_name']} Score"] = indicator.get("score", "N/A")
    return parsed_data

if __name__ == "__main__":
    # 學科列表
    subjects = [
        "engineering-technology",
        "data-science-artificial-intelligence",
        "computer-science-information-systems",
        "medicine",
        "business-management"
    ]

    # 執行爬取並保存
    scrape_and_save_by_subject(subjects, full_view=True)
