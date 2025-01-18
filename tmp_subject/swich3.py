import pandas as pd
import os

def clean_sheet(sheet_name, data):
    # Step 1: 移除空行並重置索引
    data = data.dropna(how="all").reset_index(drop=True)

    # Step 2: 找到包含年份（例如 "2024"）的標題行
    potential_header_rows = data[data.apply(lambda x: x.astype(str).str.contains("2024", na=False).any(), axis=1)].index
    if len(potential_header_rows) == 0:
        print(f"跳過工作表 {sheet_name}，未找到包含 '2024' 的欄位標題行")
        return None

    # 假設第一個符合條件的行為標題行
    header_row = potential_header_rows[0]

    # Step 3: 設置標題行為列名
    data.columns = data.iloc[header_row].fillna("").astype(str).str.strip()

    # Step 4: 提取標題行之後的所有數據
    data = data.iloc[header_row + 1:].copy()

    # Step 5: 定義標準欄位名稱
    standard_columns = [
        "2024", "2023", "Institution", "Location", "Academic Reputation",
        "Employer Reputation", "Citations per Paper", "H-index Citations", "International", "Score"
    ]

    # Step 6: 檢查並補全缺失的欄位
    for col in standard_columns:
        if col not in data.columns:
            data[col] = None  # 補全缺失的欄位

    # 僅保留標準欄位並按順序排列
    data = data[standard_columns]

    # Step 7: 修正欄位錯位問題
    for idx, row in data.iterrows():
        if pd.isnull(row["Score"]) and pd.notnull(row["International"]):
            # 將 `International` 欄位數據移至 `Score`
            data.at[idx, "Score"] = row["International"]
            data.at[idx, "International"] = None

    # Step 8: 確保前三行數據完整（如數據行少於3行，則補空行）
    while data.shape[0] < 3:
        empty_row = {col: None for col in standard_columns}
        data = pd.concat([pd.DataFrame([empty_row]), data], ignore_index=True)

    # Step 9: 清除多餘的空行並重置索引
    data = data.dropna(how="all").reset_index(drop=True)

    return data


def process_excel_file(excel_path, output_dir):
    # Step 1: 讀取 Excel 文件中的所有工作表
    sheets = pd.read_excel(excel_path, sheet_name=None)  # 讀取所有工作表

    # Step 2: 確保輸出目錄存在
    os.makedirs(output_dir, exist_ok=True)

    # Step 3: 處理每個工作表
    for sheet_name, df in sheets.items():
        print(f"正在處理工作表: {sheet_name}")
        cleaned_data = clean_sheet(sheet_name, df)
        if cleaned_data is not None:
            # Step 4: 保存清理後的數據為 CSV
            output_path = os.path.join(output_dir, f"{sheet_name}.csv")
            cleaned_data.to_csv(output_path, index=False, encoding="utf-8")
            print(f"工作表 {sheet_name} 已儲存為 {output_path}")
        else:
            print(f"跳過工作表 {sheet_name}")

    print("所有工作表的處理完成！")


# 主程序
if __name__ == "__main__":
    excel_path = "/Users/shiaupi/Downloads/mine/data_processing_project/qs-ranking-university-2024-data-scraper/QS DATA from web/2024 QS WUR by Subject.xlsx"  # 替換為您的檔案路徑
    output_dir = "./QS_Subject_Data2/"  # 替換為您的輸出目錄路徑
    process_excel_file(excel_path, output_dir)
