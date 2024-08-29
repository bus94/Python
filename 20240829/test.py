# 코로나 발생현황 데이터 수집

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1500,800")

driver = webdriver.Chrome(options=options)
driver.get('https://dportal.kdca.go.kr/pot/cv/trend/dmstc/selectMntrgSttus.do')

titleList = driver.find_elements(By.CSS_SELECTOR, 'h3.title1')
for title in titleList:
    print(f"분류: {title.get_text(strip=True)}")

subtitleList = driver.find_elements(By.CSS_SELECTOR, 'div.sub-title')
for subtitle in subtitleList:
    print(f"현황: {title.get_text(strip=True)}")

textList = driver.find_elements(By.CSS_SELECTOR, 'p.text-center')
for text in textList:
    print(f": {text.get_text(strip=True)}")

imgList = driver.find_elements(By.CSS_SELECTOR, 'div.image-box')
for img in imgList:
    print(f"이미지: {img.get_attribute('src')}")



time.sleep(20)