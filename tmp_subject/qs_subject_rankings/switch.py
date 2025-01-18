import pandas as pd

# 讀取多工作表
xlsx_file = "/Users/shiaupi/Downloads/mine/QS DATA/2024 QS WUR by Subject.xlsx"
sheets = pd.read_excel(xlsx_file, sheet_name=None)  # None 表示讀取所有工作表

# 將每個工作表存為單獨的 .csv
for sheet_name, df in sheets.items():
    output_csv = f"{sheet_name}.csv"
    df.to_csv(output_csv, index=False, encoding='utf-8')
    print(f"工作表 {sheet_name} 已儲存為 {output_csv}")
