from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

def fetch_best_student_cities():
    # 初始化 Selenium WebDriver
    driver = webdriver.Chrome()  # 确保已安装 ChromeDriver
    url = "https://www.topuniversities.com/city-rankings?tab=indicators&sort_by=rank&order_by=asc"
    driver.get(url)

    # 等待页面加载完成
    time.sleep(5)

    # 获取动态加载后的 HTML
    html = driver.page_source
    driver.quit()

    # 解析 HTML
    soup = BeautifulSoup(html, "html.parser")

    # 定位数据容器
    city_rows = soup.find_all("div", class_="ranking-row")  # 假设每行数据在 class="ranking-row"

    if not city_rows:
        print("No ranking rows found. Check the webpage structure.")
        return None

    # 提取数据
    rankings = []
    for row in city_rows:
        try:
            rank = row.find("div", class_="rank").text.strip()
            city = row.find("div", class_="city").text.strip()
            country = row.find("div", class_="country").text.strip()
            overall_score = row.find("div", class_="overall-score").text.strip()
            student_view = row.find("div", class_="student-view").text.strip()
            student_mix = row.find("div", class_="student-mix").text.strip()
            employer_activity = row.find("div", class_="employer-activity").text.strip()
            desirability = row.find("div", class_="desirability").text.strip()
            affordability = row.find("div", class_="affordability").text.strip()
            rankings.append({
                "Rank": rank,
                "City": city,
                "Country": country,
                "Overall Score": overall_score,
                "Student View": student_view,
                "Student Mix": student_mix,
                "Employer Activity": employer_activity,
                "Desirability": desirability,
                "Affordability": affordability
            })
        except AttributeError:
            continue

    return pd.DataFrame(rankings)

if __name__ == "__main__":
    df = fetch_best_student_cities()
    if df is not None:
        df.to_csv("QS_Best_Student_Cities_2025_2.csv", index=False, encoding="utf-8")
        print("Data saved to QS_Best_Student_Cities_2025_2.csv")
    else:
        print("No data extracted.")
