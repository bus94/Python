# 폴더명: crawling
# 파일명: crawlingEx2.py

import requests as re
from bs4 import BeautifulSoup
import time

class Naver:

    def __init__(self, title='', link1='', content=''):
        self.title = title
        self.link1 = link1
        self.content = content

    def __str__(self):
        return f"제목: {self.title}\n링크: {self.link1}\n내용: {self.content}"

class NaverBlogManager:

    def __init__(self):
        self.blogList = []

    # 추가

    # 삭제

    # 조회

    # 수정





# get 요청
# 입력하는 검색창 get 요청을 하는 창이다
resp = re.get("https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=사과")
# print(resp)
soup = BeautifulSoup(resp.text, 'html.parser')

# # 찾기
# bxList = soup.find_all('li', class_='bx')
# # print(bxList)
# for li in bxList:
#     # 양쪽 공백을 제거할 수 있도록 속성값 strip=True
#     print(li)
#     print(li.get_text(strip=True))

#     time.sleep(2)

# select()
# css 선택자를 이용해서 다양하게 데이터를 찾을 수 있다. 클래스: . , id : # , a , 태그명[속성]

# title = soup.find_all('a', class_="title_link")
title_link = soup.select('.title_link')
if len(title_link) != 0:
    for index, title in enumerate(title_link, start=1):
        print(f"{index}. 제목: {title.get_text(strip=True)}")
        print(f"{index}. 링크: {title.get('href')}")
        
# 첫 번째 링크 텍스트 가져오기
title = soup.find_all('a', class_='title_link')[0].get_text()
print(title) # 출력: 강아지 사과 먹어도 되나요,부작용과 좋은점은?

# 첫 번째 이미지 url 가져오기
imageUrl = soup.find_all('img')[2]['src']
print(imageUrl)

title = soup.select('a.title_link')[0].text
print(f"select() title : {title}")
link1 = soup.select('a.title_link')[0]['href']
print(f"select() link1 : {link1}")
img = soup.select('img')[2]['src']
print(f"select() img : {img}")

# naver 객체 생성
obj = Naver(title=title, link1=link1, content=img)
naverList = []

# 리스트에 저장
naverList.append(obj)
print(naverList[0])