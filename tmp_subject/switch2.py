import pandas as pd
import os

# Step 1: 讀取 Excel 文件
excel_path = "/Users/shiaupi/Downloads/mine/data_processing_project/qs-ranking-university-2024-data-scraper/QS DATA from web/2024 QS WUR by Subject.xlsx"  # 替換為您的檔案路徑
sheets = pd.read_excel(excel_path, sheet_name=None)  # 讀取所有工作表

# Step 2: 定義清理函數
def clean_sheet(sheet_name, data):
    # 移除空行
    data = data.dropna(how="all")
    
    # 找到數據的起始行（包含 "2024" 的行）
    start_row = data[data.iloc[:, 0].astype(str).str.contains("2024", na=False)].index
    if len(start_row) == 0:
        print(f"跳過工作表 {sheet_name}，未找到 '2024'")
        return None
    start_row = start_row[0]
    
    # 提取數據行
    data = data.iloc[start_row + 1:].copy()
    
    # 定義所有標準欄位名稱
    standard_columns = [
        "2024", "2023", "Institution", "Location", "Academic Reputation",
        "Employer Reputation", "Citations per Paper", "H-index Citations", "International", "Score"
    ]
    
    # 確認欄位數與標準對應
    actual_columns = data.shape[1]
    if actual_columns < len(standard_columns):
        # 補充缺失的欄位數據（使用空值）
        for i in range(len(standard_columns) - actual_columns):
            data[f"Extra Column {i + 1}"] = None
    
    # 設置標準欄位名稱，超出的欄位將被移除
    data.columns = standard_columns[:data.shape[1]]
    
    # 確保 "International" 和 "Score" 欄位存在並正確填充
    if "International" not in data.columns:
        data["International"] = None
    if "Score" not in data.columns:
        data["Score"] = None

    # 重置欄位順序，確保標準欄位名稱的一致性
    data = data.reindex(columns=standard_columns, fill_value=None)
    
    # 修正錯位問題：檢查欄位是否有數據偏移
    for idx, row in data.iterrows():
        # 如果 `International` 和 `Score` 都為空，可能是欄位錯位
        if pd.isnull(row["Score"]) and pd.notnull(row["International"]):
            # 將 `International` 欄位數據移至 `Score`
            data.at[idx, "Score"] = row["International"]
            data.at[idx, "International"] = None

    # 移除空行並重置索引
    data = data.dropna(how="all").reset_index(drop=True)
    return data

# Step 3: 清理每個工作表並保存為 CSV
output_dir = "./QS_Subject_Data/"  # 輸出目錄，確保已存在該目錄 
os.makedirs(output_dir, exist_ok=True)  # 如果目錄不存在則創建

for sheet_name, df in sheets.items():
    cleaned_data = clean_sheet(sheet_name, df)
    if cleaned_data is not None:
        # 確保前三名數據完整
        if cleaned_data.shape[0] < 3:
            print(f"警告：工作表 {sheet_name} 前三名數據可能缺失，請檢查輸出！")
        
        # 儲存為 CSV
        output_path = os.path.join(output_dir, f"{sheet_name}.csv")
        cleaned_data.to_csv(output_path, index=False, encoding='utf-8')
        print(f"工作表 {sheet_name} 已儲存為 {output_path}")
    else:
        print(f"工作表 {sheet_name} 未被處理")

print("所有工作表的處理完成！")
