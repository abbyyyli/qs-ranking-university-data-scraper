import pandas as pd
from bs4 import BeautifulSoup

# 文件路徑
file_v1 = "QS_Employability_Rankings_API.csv"
file_v2 = "QS_Employability_Rankings_API_v2.csv"
output_file = "QS_Employability_Rankings_Corrected_Final.csv"

# 清理數據函數
def clean_data(df, is_v1=True):
    # 清理 HTML 標籤並生成 `University` 欄位
    if "title" in df.columns:
        df["University"] = df["title"].apply(
            lambda x: BeautifulSoup(x, "html.parser").get_text() if isinstance(x, str) and pd.notnull(x) else None
        )
    elif "uni" in df.columns:  # 處理 API v2 的 `uni` 欄位
        df["University"] = df["uni"].apply(
            lambda x: BeautifulSoup(x, "html.parser").get_text() if isinstance(x, str) and pd.notnull(x) else None
        )
    else:
        print("Error: Missing 'title' or 'uni' column in the dataset.")
        raise KeyError("Missing 'title' or 'uni' column.")

    # 清理數據中的 HTML 標籤，保留純數字
    html_columns = ["Overall Score", "Partnerships with Employers", "Graduate Employment Rate", 
                    "Employer-Student Connections", "Employer Reputation"]
    for column in html_columns:
        if column in df.columns:
            df[column] = df[column].apply(
                lambda x: BeautifulSoup(x, "html.parser").get_text() if isinstance(x, str) and pd.notnull(x) else x
            )

    # 重命名欄位
    if is_v1:
        df.rename(columns={
            "rank_display": "Rank",
            "score": "Overall Score",
            "country": "Country",
            "city": "City"
        }, inplace=True)
    else:
        df.rename(columns={
            "overall_rank": "Rank",  # 修正 Rank 的命名
            "ind_9": "Partnerships with Employers",
            "ind_25": "Employer-Student Connections",
            "ind_19": "Graduate Employment Rate",
            "ind_77": "Employer Reputation"
        }, inplace=True)

    # 統一 Rank 欄位為字符串類型
    if "Rank" in df.columns:
        df["Rank"] = df["Rank"].astype(str)
    return df


# 加載數據
df_v1 = pd.read_csv(file_v1)
df_v2 = pd.read_csv(file_v2)

# 清理兩個數據集
df_v1_cleaned = clean_data(df_v1, is_v1=True)
df_v2_cleaned = clean_data(df_v2, is_v1=False)

# 合併數據集
merged_df = pd.merge(
    df_v1_cleaned,
    df_v2_cleaned,
    on=["Rank", "University"],
    how="outer",
    suffixes=("_v1", "_v2")
)

# 添加 Location 欄位
merged_df["Location"] = merged_df.apply(
    lambda row: f"{row['City']}, {row['Country']}" if pd.notnull(row["City"]) and pd.notnull(row["Country"]) else "N/A",
    axis=1
)

# 選擇並格式化欄位
final_df = merged_df[[
    "Rank",
    "University",
    "Overall Score",
    "Partnerships with Employers",
    "Graduate Employment Rate",
    "Employer-Student Connections",
    "Employer Reputation",
    "Location"
]]

# 填充缺失值
final_df.fillna("N/A", inplace=True)

# 按 Rank 排序
final_df["Rank"] = final_df["Rank"].apply(
    lambda x: int(x.split("-")[0]) if "-" in x else (int(x) if x.isdigit() else float('inf'))
)
final_df.sort_values(by="Rank", inplace=True)
final_df["Rank"] = final_df["Rank"].astype(str)  # 排序後將 Rank 恢復為字串

# 保存最終數據集
final_df.to_csv(output_file, index=False, encoding="utf-8")
print(f"整合並修正後的數據已保存至 {output_file}")
print(final_df.head())
