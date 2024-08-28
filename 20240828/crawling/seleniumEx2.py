#seleniumEx2.py

# 'http://ncov.kdca.go.kr'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

# 웹 사이트 고정 창
options = webdriver.ChromeOptions()
# 너비랑 높이를 고정으로 설정
options.add_argument("window-size=1500,800")

driver = webdriver.Chrome(options=options)
driver.get('https://ncov.kdca.go.kr/pot/index.do')

# 반응형 때문에 경로 이슈가 생긴다.
# data = driver.find_element(By.XPATH,'/html/body/div[2]/section[2]/div/div/ul/li[1]/ul/li/div/div/div/div[1]')
# css를 이용해서 데이터 가져오기
# 창 크기를 고정
# data = driver.find_element(By.CSS_SELECTOR, 'div.con')
# print(f"데이터: {data.text}")

# list1 = driver.find_elements(By.CSS_SELECTOR, 'a.notice_box')

# for ele in list1:
#     print(f"텍스트: {ele.text}")
#     print(f"링크: {ele.get_attribute('href')}")

# 사이트 전체 이미지 가져오기
# list2 = driver.find_elements(By.CSS_SELECTOR, 'img')

# for ele in list2:
#     print(f"이미지 url: {ele.get_attribute('src')}")

# 내가 원하는 이미지 가져오기
# a, img 선택자 없을 경우
# div 클래스를 이용해서 찾아보기
list3 = driver.find_element(By.CSS_SELECTOR, 'div.item img') # 단일 이미지
img_src = list3.get_attribute('src')
print(img_src)

list4 = driver.find_elements(By.CSS_SELECTOR, 'div.item img')
for ele in list4:
    print(f"이미지: {ele.get_attribute('src')}")

time.sleep(20)