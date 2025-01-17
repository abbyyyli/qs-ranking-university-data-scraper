import pandas as pd
from bs4 import BeautifulSoup

# 文件路徑
input_file = "QS_Employability_Rankings_Corrected_Final.csv"
output_file = "QS_Employability_Rankings_Cleaned.csv"

# 清理 HTML 標籤函數
def clean_html(value):
    if pd.notnull(value) and isinstance(value, str):
        return BeautifulSoup(value, "html.parser").get_text()
    return value

# 加載數據
df = pd.read_csv(input_file)

# 清理 HTML 標籤
for col in df.columns:
    df[col] = df[col].apply(clean_html)

# 排序數據
if "Rank" in df.columns:
    # 確保 Rank 是數字型以進行排序
    df["Rank"] = pd.to_numeric(df["Rank"], errors="coerce")
    df = df.sort_values(by="Rank")

# 保存清理後的數據
df.to_csv(output_file, index=False, encoding="utf-8")
print(f"清理完成，結果已保存至 {output_file}")
