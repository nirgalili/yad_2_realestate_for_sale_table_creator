from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import ctypes
from selenium.webdriver.support import expected_conditions as EC


serv = Service("C:/Users/nirga/Downloads/chromedriver_win32/chromedriver.exe")


driver = webdriver.Chrome(service=serv)

url = "https://www.yad2.co.il/realestate/forsale"

driver.get(url)

text = 'Press OK after narrowing down search results.'
title = 'Pop Up'

answer = ctypes.windll.user32.MessageBoxExW(0, text, title, 0x40000)

addresses = driver.find_elements(By.CSS_SELECTOR, "div.feeditem div.right_col div.rows .title")
# print(addresses[0].text)
type_neighborhood_town = driver.find_elements(By.CSS_SELECTOR, "div.feeditem div.right_col div.rows .subtitle") # sometimes there is no neighborhood. only type and town
rooms = driver.find_elements(By.CSS_SELECTOR, "div.feeditem div.middle_col .rooms-item .val")
floors = driver.find_elements(By.CSS_SELECTOR, "div.feeditem div.middle_col .floor-item .val")
areas = driver.find_elements(By.CSS_SELECTOR, "div.feeditem div.middle_col .SquareMeter-item .val")
prices = driver.find_elements(By.CSS_SELECTOR, "div.feeditem div.left_col .price")
merchants = driver.find_elements(By.CSS_SELECTOR, "div.feeditem div.left_col .merchant_name")
print(addresses[30].text)
# print(type_neighborhood_town[39].text)
# print(rooms[39].text)
# print(floors[39].text)
# print(areas[39].text)
# print(prices[39].text)
# print(merchants[39].text)
