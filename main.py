from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import ctypes
import pandas as pd

serv = Service("C:/Users/nirga/Downloads/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service=serv)

url = "https://www.yad2.co.il/realestate/forsale"

driver.get(url)

text = 'Press OK after narrowing down search results.'
title = 'Pop Up'

answer = ctypes.windll.user32.MessageBoxExW(0, text, title, 0x40000)

addresses = driver.find_elements(By.CSS_SELECTOR, "div.feeditem div.right_col div.rows .title")
type_neighborhood_town = driver.find_elements(By.CSS_SELECTOR, "div.feeditem div.right_col div.rows .subtitle") # sometimes there is no neighborhood. only type and town
rooms = driver.find_elements(By.CSS_SELECTOR, "div.feeditem div.middle_col .rooms-item .val")
floors = driver.find_elements(By.CSS_SELECTOR, "div.feeditem div.middle_col .floor-item .val")
areas = driver.find_elements(By.CSS_SELECTOR, "div.feeditem div.middle_col .SquareMeter-item .val")
prices = driver.find_elements(By.CSS_SELECTOR, "div.feeditem div.left_col .price")
merchants = driver.find_elements(By.CSS_SELECTOR, "div.feeditem div.left_col .merchant_name")
asset_types = []
neighborhoods = []
towns = []

for item in type_neighborhood_town:
    split_item = item.text.split(",")
    if len(split_item) == 1:
        asset_types.append(split_item[0])
        neighborhoods.append("NA")
        towns.append("NA")
    elif len(split_item) == 2:
        asset_types.append(split_item[0])
        neighborhoods.append("NA")
        towns.append(split_item[1])
    elif len(split_item) == 3:
        asset_types.append(split_item[0])
        neighborhoods.append(split_item[2])
        towns.append(split_item[1])


def concert_lists_of_webriver_to_text(webdriver_list):
    new_list_of_text = []
    for item in webdriver_list:
        new_list_of_text.append(item.text)
    return new_list_of_text


column_dict = {
    "address": concert_lists_of_webriver_to_text(addresses),
    "asset_type": asset_types,
    "neighborhood": neighborhoods,
    "town": towns,
    "rooms": concert_lists_of_webriver_to_text(rooms),
    "floors": concert_lists_of_webriver_to_text(floors),
    "square-meter": concert_lists_of_webriver_to_text(areas),
    "price": concert_lists_of_webriver_to_text(prices),
    "merchant": concert_lists_of_webriver_to_text(merchants)
}

df = pd.DataFrame.from_dict(column_dict, orient='index')
df = df.transpose()
df.to_csv("new_csv_file.csv", index=False, encoding='utf-8-sig')

print(df.head())

