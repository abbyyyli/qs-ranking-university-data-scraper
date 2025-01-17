import pandas as pd

# 完整的60条数据
data = [
    {"Rank": 1, "City": "London", "Country": "United Kingdom", "Overall Score": 98.4, "Student View": 98.4, "Student Mix": 94, "Employer Activity": 91.8, "Desirability": 86.1, "Affordability": 21.3, "Rankings": 94.6},
    {"Rank": 2, "City": "Tokyo", "Country": "Japan", "Overall Score": 98.4, "Student View": 88.5, "Student Mix": 64.9, "Employer Activity": 100, "Desirability": 100, "Affordability": 39.5, "Rankings": 89.6},
    {"Rank": 3, "City": "Seoul", "Country": "South Korea", "Overall Score": 98.4, "Student View": 81.2, "Student Mix": 80.6, "Employer Activity": 93.2, "Desirability": 83.7, "Affordability": 36.9, "Rankings": 100},
    {"Rank": 4, "City": "Munich", "Country": "Germany", "Overall Score": 98.4, "Student View": 95.8, "Student Mix": 91.9, "Employer Activity": 88.6, "Desirability": 90, "Affordability": 49.9, "Rankings": 58.7},
    {"Rank": 5, "City": "Melbourne", "Country": "Australia", "Overall Score": 98.4, "Student View": 98.5, "Student Mix": 100, "Employer Activity": 85.4, "Desirability": 94.4, "Affordability": 22.7, "Rankings": 71.1},
    {"Rank": 6, "City": "Sydney", "Country": "Australia", "Overall Score": 98.4, "Student View": 96.2, "Student Mix": 98, "Employer Activity": 84.9, "Desirability": 96, "Affordability": 18.7, "Rankings": 70},
    {"Rank": 7, "City": "Paris", "Country": "France", "Overall Score": 98.4, "Student View": 82, "Student Mix": 79.9, "Employer Activity": 91.2, "Desirability": 86.6, "Affordability": 39.1, "Rankings": 81.3},
    {"Rank": 8, "City": "Zurich", "Country": "Switzerland", "Overall Score": 98.4, "Student View": 94.7, "Student Mix": 86.2, "Employer Activity": 84.3, "Desirability": 97, "Affordability": 34.4, "Rankings": 62.8},
    {"Rank": 9, "City": "Berlin", "Country": "Germany", "Overall Score": 98.4, "Student View": 100, "Student Mix": 77.8, "Employer Activity": 85.9, "Desirability": 89.5, "Affordability": 49.1, "Rankings": 56.9},
    {"Rank": 10, "City": "Montreal", "Country": "Canada", "Overall Score": 98.4, "Student View": 93.6, "Student Mix": 91.2, "Employer Activity": 77, "Desirability": 85.1, "Affordability": 41.6, "Rankings": 59.4},
    {"Rank": 11, "City": "Toronto", "Country": "Canada", "Overall Score": 98.4, "Student View": 94.3, "Student Mix": 92.4, "Employer Activity": 84.3, "Desirability": 92.8, "Affordability": 21.2, "Rankings": 61.8},
    {"Rank": 12, "City": "Kyoto-Osaka-Kobe", "Country": "Japan", "Overall Score": 98.4, "Student View": 87.3, "Student Mix": 56.1, "Employer Activity": 87.2, "Desirability": 85.2, "Affordability": 55.2, "Rankings": 69.4},
    {"Rank": 13, "City": "Edinburgh", "Country": "United Kingdom", "Overall Score": 98.4, "Student View": 93.2, "Student Mix": 99.1, "Employer Activity": 77.6, "Desirability": 74.6, "Affordability": 34.9, "Rankings": 60.4},
    {"Rank": 14, "City": "Vienna", "Country": "Austria", "Overall Score": 98.4, "Student View": 92.1, "Student Mix": 87.3, "Employer Activity": 75.8, "Desirability": 93, "Affordability": 45.1, "Rankings": 44.6},
    {"Rank": 15, "City": "Singapore", "Country": "Singapore", "Overall Score": 98.4, "Student View": 93.8, "Student Mix": 78, "Employer Activity": 84.3, "Desirability": 90.1, "Affordability": 21.6, "Rankings": 67.9},
    {"Rank": 16, "City": "Boston", "Country": "United States", "Overall Score": 98.4, "Student View": 96.8, "Student Mix": 86.3, "Employer Activity": 92.6, "Desirability": 76.9, "Affordability": 4.2, "Rankings": 75.9},
    {"Rank": 17, "City": "Lausanne", "Country": "Switzerland", "Overall Score": 98.4, "Student View": 76.5, "Student Mix": 91, "Employer Activity": 87.4, "Desirability": 79.9, "Affordability": 36.8, "Rankings": 55.3},
    {"Rank": 18, "City": "New York", "Country": "United States", "Overall Score": 98.4, "Student View": 96.3, "Student Mix": 86.6, "Employer Activity": 87.6, "Desirability": 72.2, "Affordability": 4.3, "Rankings": 77.8},
    {"Rank": 19, "City": "Vancouver", "Country": "Canada", "Overall Score": 98.4, "Student View": 83.8, "Student Mix": 91.5, "Employer Activity": 78.9, "Desirability": 91.1, "Affordability": 25.2, "Rankings": 53.2},
    {"Rank": 20, "City": "Amsterdam", "Country": "Netherlands", "Overall Score": 98.4, "Student View": 95, "Student Mix": 94.2, "Employer Activity": 69.6, "Desirability": 95.1, "Affordability": 15.9, "Rankings": 51.2},
    {"Rank": 21, "City": "Stockholm", "Country": "Sweden", "Overall Score": 98.4, "Student View": 95.9, "Student Mix": 84.8, "Employer Activity": 76, "Desirability": 84.8, "Affordability": 26.3, "Rankings": 53.1},
    {"Rank": 22, "City": "Hong Kong SAR", "Country": "Hong Kong SAR", "Overall Score": 98.4, "Student View": 82.7, "Student Mix": 76.1, "Employer Activity": 79, "Desirability": 75.2, "Affordability": 32.7, "Rankings": 72.5},
    {"Rank": 23, "City": "Kuala Lumpur", "Country": "Malaysia", "Overall Score": 98.4, "Student View": 73.2, "Student Mix": 68.7, "Employer Activity": 85.1, "Desirability": 52.5, "Affordability": 69.7, "Rankings": 65.8},
    {"Rank": 24, "City": "Auckland", "Country": "New Zealand", "Overall Score": 98.4, "Student View": 86.2, "Student Mix": 90.4, "Employer Activity": 68.7, "Desirability": 87.7, "Affordability": 30.9, "Rankings": 49.5},
    {"Rank": 25, "City": "Brisbane", "Country": "Australia", "Overall Score": 98.4, "Student View": 81.3, "Student Mix": 96, "Employer Activity": 69.7, "Desirability": 84.8, "Affordability": 23.8, "Rankings": 56.9},
    {"Rank": 26, "City": "Taipei", "Country": "Taiwan", "Overall Score": 98.4, "Student View": 77, "Student Mix": 59.1, "Employer Activity": 71.8, "Desirability": 66.8, "Affordability": 66.1, "Rankings": 70.3},
    {"Rank": 27, "City": "Manchester", "Country": "United Kingdom", "Overall Score": 98.4, "Student View": 81.4, "Student Mix": 88.9, "Employer Activity": 75.1, "Desirability": 69.5, "Affordability": 40.4, "Rankings": 55},
    {"Rank": 28, "City": "Adelaide", "Country": "Australia", "Overall Score": 98.4, "Student View": 90.8, "Student Mix": 92.6, "Employer Activity": 62.3, "Desirability": 82.5, "Affordability": 28.1, "Rankings": 52.6},
    {"Rank": 29, "City": "Canberra", "Country": "Australia", "Overall Score": 98.4, "Student View": 78.8, "Student Mix": 90.4, "Employer Activity": 75, "Desirability": 83.6, "Affordability": 26.1, "Rankings": 53.5},
    {"Rank": 29, "City": "San Francisco", "Country": "United States", "Overall Score": 98.4, "Student View": 86.7, "Student Mix": 84.8, "Employer Activity": 91.3, "Desirability": 71.7, "Affordability": 5.2, "Rankings": 67.8},
    {"Rank": 31, "City": "Beijing", "Country": "China (Mainland)", "Overall Score": 98.4, "Student View": 72.2, "Student Mix": 54, "Employer Activity": 89, "Desirability": 53.6, "Affordability": 49.6, "Rankings": 88.5},
    {"Rank": 32, "City": "Dublin", "Country": "Ireland", "Overall Score": 98.4, "Student View": 81.9, "Student Mix": 93, "Employer Activity": 75.8, "Desirability": 80.1, "Affordability": 14.2, "Rankings": 60.3},
    {"Rank": 33, "City": "Glasgow", "Country": "United Kingdom", "Overall Score": 98.4, "Student View": 98, "Student Mix": 91.2, "Employer Activity": 58.6, "Desirability": 68.7, "Affordability": 35.1, "Rankings": 52.7},
    {"Rank": 34, "City": "Madrid", "Country": "Spain", "Overall Score": 98.4, "Student View": 77.9, "Student Mix": 79.4, "Employer Activity": 74.6, "Desirability": 81.7, "Affordability": 27.3, "Rankings": 63.1},
    {"Rank": 35, "City": "Perth", "Country": "Australia", "Overall Score": 98.4, "Student View": 79.5, "Student Mix": 89.6, "Employer Activity": 58, "Desirability": 83.5, "Affordability": 30.2, "Rankings": 58.7},
    {"Rank": 36, "City": "Leuven", "Country": "Belgium", "Overall Score": 98.4, "Student View": 76.9, "Student Mix": 90.4, "Employer Activity": 75.1, "Desirability": 61.5, "Affordability": 40.5, "Rankings": 50.9},
    {"Rank": 37, "City": "Copenhagen", "Country": "Denmark", "Overall Score": 98.4, "Student View": 85, "Student Mix": 74.6, "Employer Activity": 72.5, "Desirability": 98.1, "Affordability": 12.4, "Rankings": 52},
    {"Rank": 37, "City": "Los Angeles", "Country": "United States", "Overall Score": 98.4, "Student View": 91.5, "Student Mix": 76.4, "Employer Activity": 87.2, "Desirability": 69.8, "Affordability": 4.3, "Rankings": 65.5},
    {"Rank": 39, "City": "Newcastle Upon Tyne", "Country": "United Kingdom", "Overall Score": 98.4, "Student View": 86.4, "Student Mix": 88.4, "Employer Activity": 62.1, "Desirability": 61.3, "Affordability": 39.9, "Rankings": 55.1},
    {"Rank": 40, "City": "Prague", "Country": "Czech Republic", "Overall Score": 98.4, "Student View": 86.7, "Student Mix": 89.2, "Employer Activity": 74.2, "Desirability": 68, "Affordability": 38.2, "Rankings": 36.4},
    {"Rank": 41, "City": "Barcelona", "Country": "Spain", "Overall Score": 98.4, "Student View": 77.4, "Student Mix": 67.9, "Employer Activity": 77.6, "Desirability": 78.5, "Affordability": 31, "Rankings": 55.9},
    {"Rank": 42, "City": "Buenos Aires", "Country": "Argentina", "Overall Score": 98.4, "Student View": 82.7, "Student Mix": 76.8, "Employer Activity": 84.1, "Desirability": 50.3, "Affordability": 22.3, "Rankings": 68.1},
    {"Rank": 43, "City": "Coventry", "Country": "United Kingdom", "Overall Score": 98.4, "Student View": 80.5, "Student Mix": 99.4, "Employer Activity": 61, "Desirability": 53.5, "Affordability": 39.3, "Rankings": 48.9},
    {"Rank": 44, "City": "Chicago", "Country": "United States", "Overall Score": 98.4, "Student View": 81.6, "Student Mix": 78.4, "Employer Activity": 79.7, "Desirability": 69.2, "Affordability": 5.2, "Rankings": 66.6},
    {"Rank": 45, "City": "Bristol", "Country": "United Kingdom", "Overall Score": 98.4, "Student View": 86.8, "Student Mix": 90.4, "Employer Activity": 53.5, "Desirability": 63, "Affordability": 37.2, "Rankings": 49.5},
    {"Rank": 46, "City": "Shanghai", "Country": "China (Mainland)", "Overall Score": 98.4, "Student View": 76.1, "Student Mix": 52.8, "Employer Activity": 76.4, "Desirability": 52.7, "Affordability": 45.7, "Rankings": 74.2},
    {"Rank": 47, "City": "Lyon", "Country": "France", "Overall Score": 98.4, "Student View": 76.1, "Student Mix": 76.8, "Employer Activity": 52.7, "Desirability": 64, "Affordability": 56.6, "Rankings": 46.9},
    {"Rank": 48, "City": "Birmingham", "Country": "United Kingdom", "Overall Score": 98.4, "Student View": 88, "Student Mix": 84, "Employer Activity": 54, "Desirability": 60.5, "Affordability": 35.1, "Rankings": 50.9},
    {"Rank": 49, "City": "Gothenburg", "Country": "Sweden", "Overall Score": 98.4, "Student View": 85.1, "Student Mix": 84.8, "Employer Activity": 53.1, "Desirability": 70.6, "Affordability": 33.2, "Rankings": 44.5},
    {"Rank": 50, "City": "Santiago", "Country": "Chile", "Overall Score": 98.4, "Student View": 65.2, "Student Mix": 53.5, "Employer Activity": 84.6, "Desirability": 47.9, "Affordability": 44, "Rankings": 74.1},
    {"Rank": 51, "City": "Nottingham", "Country": "United Kingdom", "Overall Score": 98.4, "Student View": 84.8, "Student Mix": 91.9, "Employer Activity": 48.3, "Desirability": 60, "Affordability": 41.8, "Rankings": 41},
    {"Rank": 52, "City": "Milan", "Country": "Italy", "Overall Score": 98.4, "Student View": 72.6, "Student Mix": 73.8, "Employer Activity": 82.8, "Desirability": 65, "Affordability": 19.3, "Rankings": 52.7},
    {"Rank": 53, "City": "Leeds", "Country": "United Kingdom", "Overall Score": 98.4, "Student View": 82.7, "Student Mix": 78.4, "Employer Activity": 52.2, "Desirability": 62.1, "Affordability": 41.2, "Rankings": 48.2},
    {"Rank": 54, "City": "Liverpool", "Country": "United Kingdom", "Overall Score": 98.4, "Student View": 91.8, "Student Mix": 80.8, "Employer Activity": 45.8, "Desirability": 61.4, "Affordability": 43.5, "Rankings": 39.6},
    {"Rank": 54, "City": "Rome", "Country": "Italy", "Overall Score": 98.4, "Student View": 69.2, "Student Mix": 63.3, "Employer Activity": 67, "Desirability": 69.6, "Affordability": 49.4, "Rankings": 44.3},
    {"Rank": 56, "City": "Brussels", "Country": "Belgium", "Overall Score": 98.4, "Student View": 69.4, "Student Mix": 79.9, "Employer Activity": 63.3, "Desirability": 73.7, "Affordability": 40.3, "Rankings": 34.6},
    {"Rank": 57, "City": "Ottawa", "Country": "Canada", "Overall Score": 98.4, "Student View": 81.6, "Student Mix": 90.4, "Employer Activity": 35, "Desirability": 84.5, "Affordability": 28.2, "Rankings": 39},
    {"Rank": 58, "City": "Warsaw", "Country": "Poland", "Overall Score": 98.4, "Student View": 80.2, "Student Mix": 56.9, "Employer Activity": 68.8, "Desirability": 58.1, "Affordability": 62.5, "Rankings": 31.2},
    {"Rank": 59, "City": "Bangkok", "Country": "Thailand", "Overall Score": 98.4, "Student View": 72.6, "Student Mix": 37.8, "Employer Activity": 88.4, "Desirability": 41.3, "Affordability": 57.9, "Rankings": 51.1},
    {"Rank": 60, "City": "Lisbon", "Country": "Portugal", "Overall Score": 98.4, "Student View": 55.5, "Student Mix": 84.5, "Employer Activity": 62.8, "Desirability": 70.8, "Affordability": 35.9, "Rankings": 37.2},
    {"Rank": 61, "City": "Belfast", "Country": "United Kingdom", "Overall Score": 98.4, "Student View": 80.3, "Student Mix": 90.6, "Employer Activity": 47.2, "Desirability": 58.2, "Affordability": 40.9, "Rankings": 29.1},
    {"Rank": 62, "City": "Istanbul", "Country": "Türkiye", "Overall Score": 98.4, "Student View": 68.5, "Student Mix": 52.8, "Employer Activity": 64.7, "Desirability": 43.1, "Affordability": 67.3, "Rankings": 49.1},
    {"Rank": 63, "City": "Budapest", "Country": "Hungary", "Overall Score": 98.4, "Student View": 72.1, "Student Mix": 67.1, "Employer Activity": 60.2, "Desirability": 62, "Affordability": 58.5, "Rankings": 24.1},
    {"Rank": 64, "City": "Sheffield", "Country": "United Kingdom", "Overall Score": 98.4, "Student View": 74.8, "Student Mix": 87.1, "Employer Activity": 41.8, "Desirability": 57.3, "Affordability": 40.1, "Rankings": 41.1},
    {"Rank": 65, "City": "Philadelphia", "Country": "United States", "Overall Score": 98.4, "Student View": 61.7, "Student Mix": 72.9, "Employer Activity": 73.3, "Desirability": 60, "Affordability": 10.1, "Rankings": 63.9},
    {"Rank": 66, "City": "Helsinki", "Country": "Finland", "Overall Score": 98.4, "Student View": 59.6, "Student Mix": 64, "Employer Activity": 61.9, "Desirability": 92.3, "Affordability": 15.9, "Rankings": 45.1},
    {"Rank": 67, "City": "Brno", "Country": "Czech Republic", "Overall Score": 98.4, "Student View": 87.2, "Student Mix": 88.2, "Employer Activity": 43.9, "Desirability": 54, "Affordability": 45.1, "Rankings": 20.1},
    {"Rank": 68, "City": "Turin", "Country": "Italy", "Overall Score": 98.4, "Student View": 73.8, "Student Mix": 71.5, "Employer Activity": 53.7, "Desirability": 52.4, "Affordability": 53.5, "Rankings": 32.1},
    {"Rank": 69, "City": "San Diego", "Country": "United States", "Overall Score": 98.4, "Student View": 66.8, "Student Mix": 72, "Employer Activity": 50.8, "Desirability": 64.8, "Affordability": 31.1, "Rankings": 51},
    {"Rank": 70, "City": "Washington DC", "Country": "United States", "Overall Score": 98.4, "Student View": 80.8, "Student Mix": 65.6, "Employer Activity": 64.7, "Desirability": 69.4, "Affordability": 5.9, "Rankings": 47.5},
    {"Rank": 71, "City": "Aberdeen", "Country": "United Kingdom", "Overall Score": 98.4, "Student View": 75.2, "Student Mix": 79.5, "Employer Activity": 35.7, "Desirability": 64.5, "Affordability": 41.6, "Rankings": 28.3},
    {"Rank": 72, "City": "Atlanta", "Country": "United States", "Overall Score": 98.4, "Student View": 71.9, "Student Mix": 67.7, "Employer Activity": 59.7, "Desirability": 66.6, "Affordability": 8.2, "Rankings": 48.9},
    {"Rank": 72, "City": "Dubai", "Country": "United Arab Emirates", "Overall Score": 98.4, "Student View": 98.1, "Student Mix": 43.6, "Employer Activity": 64.6, "Desirability": 75.1, "Affordability": 20.6, "Rankings": 20.8},
    {"Rank": 74, "City": "Daejeon", "Country": "South Korea", "Overall Score": 98.4, "Student View": 47.1, "Student Mix": 44.7, "Employer Activity": 77.7, "Desirability": 51.6, "Affordability": 51.1, "Rankings": 49.6},
    {"Rank": 75, "City": "Cairo", "Country": "Egypt", "Overall Score": 98.4, "Student View": 51.4, "Student Mix": 58.4, "Employer Activity": 75.8, "Desirability": 21.1, "Affordability": 67.3, "Rankings": 45.7},
    {"Rank": 76, "City": "Oslo", "Country": "Norway", "Overall Score": 98.4, "Student View": 77.3, "Student Mix": 61.5, "Employer Activity": 52.7, "Desirability": 86.4, "Affordability": 1, "Rankings": 40.6},
    {"Rank": 77, "City": "Brighton", "Country": "United Kingdom", "Overall Score": 98.4, "Student View": 81.6, "Student Mix": 78.3, "Employer Activity": 29.4, "Desirability": 63.1, "Affordability": 37.8, "Rankings": 27.9},
    {"Rank": 78, "City": "Almaty", "Country": "Kazakhstan", "Overall Score": 98.4, "Student View": 36.4, "Student Mix": 61.8, "Employer Activity": 66.5, "Desirability": 20.5, "Affordability": 74.7, "Rankings": 56},
    {"Rank": 79, "City": "Christchurch", "Country": "New Zealand", "Overall Score": 98.4, "Student View": 51.5, "Student Mix": 71.8, "Employer Activity": 40.9, "Desirability": 71.3, "Affordability": 46.6, "Rankings": 31.1},
    {"Rank": 80, "City": "Pittsburgh", "Country": "United States", "Overall Score": 98.4, "Student View": 55, "Student Mix": 72.3, "Employer Activity": 60, "Desirability": 59.2, "Affordability": 14.4, "Rankings": 51.1},
    {"Rank": 81, "City": "Cape Town", "Country": "South Africa", "Overall Score": 98.4, "Student View": 76.2, "Student Mix": 44.1, "Employer Activity": 44.5, "Desirability": 41.3, "Affordability": 65.5, "Rankings": 39.4},
    {"Rank": 82, "City": "Ankara", "Country": "Türkiye", "Overall Score": 98.4, "Student View": 63.7, "Student Mix": 44.7, "Employer Activity": 57, "Desirability": 31, "Affordability": 76.1, "Rankings": 38.4},
    {"Rank": 83, "City": "Amman", "Country": "Jordan", "Overall Score": 98.4, "Student View": 58.9, "Student Mix": 55.7, "Employer Activity": 76.2, "Desirability": 26.1, "Affordability": 56.1, "Rankings": 36},
    {"Rank": 84, "City": "Hsinchu", "Country": "Taiwan", "Overall Score": 98.4, "Student View": 51.2, "Student Mix": 48.4, "Employer Activity": 60.2, "Desirability": 41.3, "Affordability": 72.3, "Rankings": 35.1},
    {"Rank": 85, "City": "Mexico City", "Country": "Mexico", "Overall Score": 98.4, "Student View": 50, "Student Mix": 41.1, "Employer Activity": 85.5, "Desirability": 26.1, "Affordability": 34.2, "Rankings": 71.4},
    {"Rank": 86, "City": "Johannesburg", "Country": "South Africa", "Overall Score": 98.4, "Student View": 69.7, "Student Mix": 53.3, "Employer Activity": 33.7, "Desirability": 36.3, "Affordability": 80.8, "Rankings": 31},
    {"Rank": 87, "City": "Nanjing", "Country": "China (Mainland)", "Overall Score": 98.4, "Student View": 73.7, "Student Mix": 39.1, "Employer Activity": 42.5, "Desirability": 35.3, "Affordability": 60.8, "Rankings": 52},
    {"Rank": 88, "City": "Doha", "Country": "Qatar", "Overall Score": 98.4, "Student View": 59.7, "Student Mix": 56.3, "Employer Activity": 43.4, "Desirability": 50.1, "Affordability": 47.4, "Rankings": 44.8},
    {"Rank": 88, "City": "Seattle", "Country": "United States", "Overall Score": 98.4, "Student View": 56, "Student Mix": 74.3, "Employer Activity": 44, "Desirability": 70, "Affordability": 9, "Rankings": 48.5},
    {"Rank": 90, "City": "Valencia", "Country": "Spain", "Overall Score": 98.4, "Student View": 54.1, "Student Mix": 71.7, "Employer Activity": 31.8, "Desirability": 68.7, "Affordability": 57.5, "Rankings": 17.7},
    {"Rank": 91, "City": "Abu Dhabi", "Country": "United Arab Emirates", "Overall Score": 98.4, "Student View": 89.1, "Student Mix": 48, "Employer Activity": 53.9, "Desirability": 56.1, "Affordability": 22.8, "Rankings": 29.2},
    {"Rank": 91, "City": "Krakow", "Country": "Poland", "Overall Score": 98.4, "Student View": 58.9, "Student Mix": 62.5, "Employer Activity": 45.3, "Desirability": 45.9, "Affordability": 62.5, "Rankings": 24},
    {"Rank": 93, "City": "Gold Coast", "Country": "Australia", "Overall Score": 98.4, "Student View": 49.6, "Student Mix": 79.8, "Employer Activity": 31.4, "Desirability": 73.6, "Affordability": 32.5, "Rankings": 31.4},
    {"Rank": 94, "City": "Durham", "Country": "United States", "Overall Score": 98.4, "Student View": 49.8, "Student Mix": 68.4, "Employer Activity": 60.1, "Desirability": 54.3, "Affordability": 13.7, "Rankings": 49.2},
    {"Rank": 94, "City": "Leicester", "Country": "United Kingdom", "Overall Score": 98.4, "Student View": 53.6, "Student Mix": 90.8, "Employer Activity": 23.9, "Desirability": 56.9, "Affordability": 43.7, "Rankings": 26.6},
    {"Rank": 96, "City": "Graz", "Country": "Austria", "Overall Score": 98.4, "Student View": 46.7, "Student Mix": 74.5, "Employer Activity": 38.7, "Desirability": 74.3, "Affordability": 45.6, "Rankings": 13.4},
    {"Rank": 97, "City": "Riyadh", "Country": "Saudi Arabia", "Overall Score": 98.4, "Student View": 71.8, "Student Mix": 43.9, "Employer Activity": 62.3, "Desirability": 36.1, "Affordability": 31.1, "Rankings": 46.4},
    {"Rank": 97, "City": "Sao Paulo", "Country": "Brazil", "Overall Score": 98.4, "Student View": 36.7, "Student Mix": 31.6, "Employer Activity": 72.1, "Desirability": 32.1, "Affordability": 54, "Rankings": 65},
    {"Rank": 97, "City": "Tainan", "Country": "Taiwan", "Overall Score": 98.4, "Student View": 48.2, "Student Mix": 42.6, "Employer Activity": 39.1, "Desirability": 48.8, "Affordability": 84.1, "Rankings": 28.7},
    {"Rank": 97, "City": "Toulouse", "Country": "France", "Overall Score": 98.4, "Student View": 52, "Student Mix": 56.3, "Employer Activity": 45.3, "Desirability": 63.5, "Affordability": 61.3, "Rankings": 13.5},
    {"Rank": 101, "City": "Sharjah", "Country": "United Arab Emirates", "Overall Score": 98.4, "Student View": 83.7, "Student Mix": 64.9, "Employer Activity": 45.5, "Desirability": 51.7, "Affordability": 24.1, "Rankings": 21.4},
    {"Rank": 102, "City": "Stuttgart", "Country": "Germany", "Overall Score": 98.4, "Student View": 44.9, "Student Mix": 68.9, "Employer Activity": 42.5, "Desirability": 76.5, "Affordability": 36.7, "Rankings": 20.1},
    {"Rank": 103, "City": "Manila", "Country": "Philippines", "Overall Score": 98.4, "Student View": 58.8, "Student Mix": 29.1, "Employer Activity": 77, "Desirability": 20.4, "Affordability": 74.6, "Rankings": 29},
    {"Rank": 104, "City": "Wuhan", "Country": "China (Mainland)", "Overall Score": 98.4, "Student View": 62.3, "Student Mix": 37.9, "Employer Activity": 37.5, "Desirability": 35.1, "Affordability": 65.6, "Rankings": 47.7},
    {"Rank": 105, "City": "Athens", "Country": "Greece", "Overall Score": 98.4, "Student View": 57.1, "Student Mix": 61.1, "Employer Activity": 64.7, "Desirability": 46.9, "Affordability": 24.6, "Rankings": 29.8},
    {"Rank": 106, "City": "Houston", "Country": "United States", "Overall Score": 98.4, "Student View": 60.3, "Student Mix": 69, "Employer Activity": 41.4, "Desirability": 56.7, "Affordability": 13.4, "Rankings": 40.2},
    {"Rank": 107, "City": "Baltimore", "Country": "United States", "Overall Score": 98.4, "Student View": 22.7, "Student Mix": 71.3, "Employer Activity": 59.7, "Desirability": 55.3, "Affordability": 14.2, "Rankings": 52.8},
    {"Rank": 108, "City": "Nagoya", "Country": "Japan", "Overall Score": 98.4, "Student View": 10.1, "Student Mix": 42.6, "Employer Activity": 44.9, "Desirability": 68.4, "Affordability": 66.9, "Rankings": 39.8},
    {"Rank": 109, "City": "Subang Jaya", "Country": "Malaysia", "Overall Score": 98.4, "Student View": 35.8, "Student Mix": 54.1, "Employer Activity": 64.3, "Desirability": 21.5, "Affordability": 68.9, "Rankings": 27.7},
    {"Rank": 110, "City": "Bogota", "Country": "Colombia", "Overall Score": 98.4, "Student View": 44.3, "Student Mix": 28, "Employer Activity": 73.5, "Desirability": 27.9, "Affordability": 34.2, "Rankings": 62.1},
    {"Rank": 111, "City": "Delhi", "Country": "India", "Overall Score": 98.4, "Student View": 19.3, "Student Mix": 14.7, "Employer Activity": 65.9, "Desirability": 26.5, "Affordability": 92.5, "Rankings": 50},
    {"Rank": 112, "City": "Monterrey", "Country": "Mexico", "Overall Score": 98.4, "Student View": 38.3, "Student Mix": 47.1, "Employer Activity": 79.8, "Desirability": 19, "Affordability": 42.3, "Rankings": 41.8},
    {"Rank": 113, "City": "Mumbai", "Country": "India", "Overall Score": 98.4, "Student View": 50.4, "Student Mix": 5.6, "Employer Activity": 65.8, "Desirability": 29.7, "Affordability": 74.2, "Rankings": 40.7},
    {"Rank": 114, "City": "Beirut", "Country": "Lebanon", "Overall Score": 98.4, "Student View": 62, "Student Mix": 53.8, "Employer Activity": 74.6, "Desirability": 15.2, "Affordability": 21.9, "Rankings": 38.1},
    {"Rank": 115, "City": "Miami", "Country": "United States", "Overall Score": 98.4, "Student View": 75.5, "Student Mix": 52.3, "Employer Activity": 39.9, "Desirability": 69.3, "Affordability": 7.7, "Rankings": 19.7},
    {"Rank": 116, "City": "Riga", "Country": "Latvia", "Overall Score": 98.4, "Student View": 64.6, "Student Mix": 70.6, "Employer Activity": 47.3, "Desirability": 30.1, "Affordability": 39.7, "Rankings": 11.6},
    {"Rank": 117, "City": "Taichung", "Country": "Taiwan", "Overall Score": 98.4, "Student View": 32.1, "Student Mix": 47.6, "Employer Activity": 37.4, "Desirability": 42, "Affordability": 74.7, "Rankings": 23},
    {"Rank": 117, "City": "Yogyakarta", "Country": "Indonesia", "Overall Score": 98.4, "Student View": 21.3, "Student Mix": 41.6, "Employer Activity": 53.6, "Desirability": 13.3, "Affordability": 91.1, "Rankings": 35.9},
    {"Rank": 119, "City": "Pretoria", "Country": "South Africa", "Overall Score": 98.4, "Student View": 56.1, "Student Mix": 43.7, "Employer Activity": 33.7, "Desirability": 27.9, "Affordability": 75.6, "Rankings": 18.9},
    {"Rank": 120, "City": "Jakarta", "Country": "Indonesia", "Overall Score": 98.4, "Student View": 33.9, "Student Mix": 31.2, "Employer Activity": 63.3, "Desirability": 20.6, "Affordability": 68, "Rankings": 37.6},
    {"Rank": 120, "City": "Jeddah", "Country": "Saudi Arabia", "Overall Score": 98.4, "Student View": 59.4, "Student Mix": 26.7, "Employer Activity": 62.2, "Desirability": 36.3, "Affordability": 30, "Rankings": 40},
    {"Rank": 120, "City": "Wroclaw", "Country": "Poland", "Overall Score": 98.4, "Student View": 50.8, "Student Mix": 52.3, "Employer Activity": 31.7, "Desirability": 45, "Affordability": 72, "Rankings": 3.2},
    {"Rank": 123, "City": "Shah Alam", "Country": "Malaysia", "Overall Score": 98.4, "Student View": 41.4, "Student Mix": 51, "Employer Activity": 64.6, "Desirability": 23.9, "Affordability": 66.8, "Rankings": 6.6},
    {"Rank": 123, "City": "Vilnius", "Country": "Lithuania", "Overall Score": 98.4, "Student View": 53.7, "Student Mix": 62.3, "Employer Activity": 38.3, "Desirability": 34.9, "Affordability": 45.6, "Rankings": 19.5},
    {"Rank": 125, "City": "Astana", "Country": "Kazakhstan", "Overall Score": 98.4, "Student View": 10.2, "Student Mix": 46.5, "Employer Activity": 63.4, "Desirability": 25.1, "Affordability": 76.9, "Rankings": 31.6},
    {"Rank": 126, "City": "Lima", "Country": "Peru", "Overall Score": 98.4, "Student View": 39, "Student Mix": 22.6, "Employer Activity": 62.1, "Desirability": 15.3, "Affordability": 63, "Rankings": 49.9},
    {"Rank": 126, "City": "Taoyuan District", "Country": "Taiwan", "Overall Score": 98.4, "Student View": 30.3, "Student Mix": 49, "Employer Activity": 27.7, "Desirability": 43.4, "Affordability": 82, "Rankings": 19.6},
    {"Rank": 128, "City": "Quebec", "Country": "Canada", "Overall Score": 98.4, "Student View": 21.8, "Student Mix": 66.5, "Employer Activity": 27.5, "Desirability": 78.4, "Affordability": 42.6, "Rankings": 13.2},
    {"Rank": 129, "City": "Izmir", "Country": "Türkiye", "Overall Score": 98.4, "Student View": 40, "Student Mix": 48.6, "Employer Activity": 24.8, "Desirability": 23.5, "Affordability": 100, "Rankings": 9},
    {"Rank": 130, "City": "Bangalore", "Country": "India", "Overall Score": 98.4, "Student View": 56.9, "Student Mix": 5.3, "Employer Activity": 49.7, "Desirability": 22.6, "Affordability": 81.9, "Rankings": 28.8},
    {"Rank": 130, "City": "Bratislava", "Country": "Slovakia", "Overall Score": 98.4, "Student View": 39.6, "Student Mix": 62.1, "Employer Activity": 33.3, "Desirability": 46.5, "Affordability": 57.8, "Rankings": 5.6},
    {"Rank": 132, "City": "Bandung", "Country": "Indonesia", "Overall Score": 98.4, "Student View": 14.8, "Student Mix": 37, "Employer Activity": 56.5, "Desirability": 17.8, "Affordability": 81.3, "Rankings": 35.1},
    {"Rank": 133, "City": "Guangzhou", "Country": "China (Mainland)", "Overall Score": 98.4, "Student View": 45.1, "Student Mix": 54.6, "Employer Activity": 29.8, "Desirability": 34.4, "Affordability": 48.9, "Rankings": 29.4},
    {"Rank": 134, "City": "Dallas", "Country": "United States", "Overall Score": 98.4, "Student View": 70.7, "Student Mix": 68.8, "Employer Activity": 19.3, "Desirability": 63.8, "Affordability": 12.7, "Rankings": 6.4},
    {"Rank": 135, "City": "Cluj-Napoca", "Country": "Romania", "Overall Score": 98.4, "Student View": 35.5, "Student Mix": 44.6, "Employer Activity": 35.7, "Desirability": 38.4, "Affordability": 78.7, "Rankings": 4.3},
    {"Rank": 136, "City": "Busan", "Country": "South Korea", "Overall Score": 98.4, "Student View": 40.2, "Student Mix": 44.2, "Employer Activity": 26.1, "Desirability": 58.2, "Affordability": 60.5, "Rankings": 7.3},
    {"Rank": 137, "City": "Tianjin", "Country": "China (Mainland)", "Overall Score": 98.4, "Student View": 41.9, "Student Mix": 38.5, "Employer Activity": 18.9, "Desirability": 37.7, "Affordability": 67.8, "Rankings": 30.9},
    {"Rank": 138, "City": "Montpellier", "Country": "France", "Overall Score": 98.4, "Student View": 16.3, "Student Mix": 68.9, "Employer Activity": 18.2, "Desirability": 56.4, "Affordability": 62, "Rankings": 12.7},
    {"Rank": 138, "City": "Poznań", "Country": "Poland", "Overall Score": 98.4, "Student View": 22.5, "Student Mix": 57.4, "Employer Activity": 25.1, "Desirability": 40.2, "Affordability": 77.7, "Rankings": 11.4},
    {"Rank": 140, "City": "Chennai", "Country": "India", "Overall Score": 98.4, "Student View": 20.2, "Student Mix": 21.1, "Employer Activity": 52.3, "Desirability": 27.4, "Affordability": 67.6, "Rankings": 43.6},
    {"Rank": 141, "City": "Dhaka", "Country": "Bangladesh", "Overall Score": 98.4, "Student View": 31, "Student Mix": 5, "Employer Activity": 62.3, "Desirability": 9.4, "Affordability": 80.2, "Rankings": 43.8},
    {"Rank": 142, "City": "Surabaya", "Country": "Indonesia", "Overall Score": 98.4, "Student View": 13.8, "Student Mix": 36.2, "Employer Activity": 51.6, "Desirability": 10.5, "Affordability": 89.8, "Rankings": 24.1},
    {"Rank": 143, "City": "Bucharest", "Country": "Romania", "Overall Score": 98.4, "Student View": 39, "Student Mix": 32.3, "Employer Activity": 31.2, "Desirability": 42, "Affordability": 75.1, "Rankings": 3.9},
    {"Rank": 143, "City": "Macau", "Country": "Macau SAR", "Overall Score": 98.4, "Student View": 42.8, "Student Mix": 84.8, "Employer Activity": 21.9, "Desirability": 19.3, "Affordability": 25, "Rankings": 30},
    {"Rank": 143, "City": "Tallinn", "Country": "Estonia", "Overall Score": 98.4, "Student View": 46.6, "Student Mix": 49.7, "Employer Activity": 33.5, "Desirability": 40.3, "Affordability": 47.5, "Rankings": 6.2},
    {"Rank": 146, "City": "Rio de Janeiro", "Country": "Brazil", "Overall Score": 98.4, "Student View": 36.6, "Student Mix": 18.1, "Employer Activity": 56.1, "Desirability": 29.2, "Affordability": 47.3, "Rankings": 33.9},
    {"Rank": 147, "City": "Kaunas", "Country": "Lithuania", "Overall Score": 98.4, "Student View": 46, "Student Mix": 64, "Employer Activity": 28.9, "Desirability": 22.6, "Affordability": 49.8, "Rankings": 4.7},
    {"Rank": 148, "City": "Alexandria", "Country": "Egypt", "Overall Score": 98.4, "Student View": 29.1, "Student Mix": 52.5, "Employer Activity": 40.7, "Desirability": 12.4, "Affordability": 73.7, "Rankings": 3.6},
    {"Rank": 148, "City": "Harbin", "Country": "China (Mainland)", "Overall Score": 98.4, "Student View": 30.8, "Student Mix": 25.5, "Employer Activity": 32.2, "Desirability": 27, "Affordability": 68.7, "Rankings": 27.6},
    {"Rank": 150, "City": "Xi'an", "Country": "China (Mainland)", "Overall Score": 98.4, "Student View": 55.8, "Student Mix": 36.9, "Employer Activity": 26.5, "Desirability": 31.4, "Affordability": 30.6, "Rankings": 30.3}
]


    

# 保存为 CSV 和 Excel
df = pd.DataFrame(data)
df.to_csv("QS_Best_Student_Cities_2025.csv", index=False, encoding="utf-8")
df.to_excel("QS_Best_Student_Cities_2025.xlsx", index=False)
print("完整文件已生成！")