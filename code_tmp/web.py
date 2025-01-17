import os
import json
import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 初始化 WebDriver
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 啟用無頭模式
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 隨機延遲
def random_delay(min_delay=2, max_delay=5):
    delay = random.uniform(min_delay, max_delay)
    print(f"隨機延遲 {delay:.2f} 秒")
    time.sleep(delay)

# 爬取學校數據
def scrape_school_data(driver, url, output_file="school_data.json"):
    print(f"訪問 URL: {url}")
    driver.get(url)
    random_delay(5, 8)

    school_data = []

    while True:
        try:
            # 找到排名表格
            table = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'qs-rankings')]"))
            )
            rows = table.find_elements(By.XPATH, ".//tr")[1:]  # 跳過表頭

            for row in rows:
                columns = row.find_elements(By.TAG_NAME, "td")
                if len(columns) >= 3:
                    rank = columns[0].text.strip()
                    name = columns[1].text.strip()
                    location = columns[2].text.strip()
                    school_data.append({
                        "Rank": rank,
                        "Name": name,
                        "Location": location
                    })

            # 嘗試點擊下一頁按鈕
            next_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")
            if next_button:
                next_button.click()
                random_delay()
            else:
                break
        except Exception as e:
            print(f"分頁爬取失敗或沒有更多數據: {e}")
            break

    # 保存數據為 JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(school_data, f, ensure_ascii=False, indent=4)
    print(f"數據已保存至 {output_file}")

# 數據清理
def clean_school_data(input_file, output_file):
    df = pd.read_json(input_file)
    df.dropna(inplace=True)  # 刪除空值
    df.drop_duplicates(inplace=True)  # 刪除重複數據
    df.to_json(output_file, orient="records", indent=4, force_ascii=False)
    print(f"清理後的數據已保存至 {output_file}")

if __name__ == "__main__":
    # 目標 URL
    target_urls = [
        "https://www.topuniversities.com/university-rankings/world-university-rankings/2024"
    ]

    # 初始化 WebDriver
    driver = init_driver()

    try:
        for url in target_urls:
            file_name = f"school_data_{url.split('/')[-1]}.json"
            scrape_school_data(driver, url, output_file=file_name)
            clean_file_name = f"cleaned_{file_name}"
            clean_school_data(file_name, clean_file_name)
    finally:
        driver.quit()
        print("爬取結束")
