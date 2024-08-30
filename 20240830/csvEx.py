# 훈련과정
# 실무 프로젝트를 위한 클라우드 서비스 기술
# 훈련과목
# 파이썬을 활용한 데이터분석 및 시각화

# csv 모듈 불러오기
import csv
import pandas as pd


# 최고기온 저장 변수
max_temp = -999
# 최고기온 날짜 저장 변수
max_date = ''

# csv파일을 open() 함수로 열어 f에 저장 (f: 파일 핸들러)
f = open('2002Seoul.csv', 'r', encoding='cp949') # cp949: Windows 한글 인코딩 방식
print("<서울의 2002년 6월 1일 ~ 30일까지의 기온 데이터>\n")

dataHeader = csv.reader(f)
# next() 함수 : 데이터의 맨 윗줄에 있는 헤더 부분을 제외한 data
header = next(dataHeader) # next() 함수
headerList = []
for row in header:
    headerList.append(row)

data = csv.reader(f, delimiter=',')
dataList = []
# print(data) # 출력: <_csv.reader object at 0x000001CF4EE3D240>
# 아래의 코드에선 for문으로 data를 가져오면 header를 제외한 data만 출력된다
for i, row in enumerate(data):
    for i, value in enumerate(row):
        if value.replace('.', '').isdigit():
            row[i] = float(row[i])
        elif value == '':
            row[i] = -999 # 빈 문자열인 경우 -999로 표시
    dataList.append(row)
# 예제
# 서울의 최고 기온이 가장 높았던 날은 언제였고, 몇 도였을까?
# 1. 데이터를 읽어온다.
# 2. 순차적으로 최고 기온을 확인한다.
# 3. 최고 기온이 가장 높았던 날짜의 데이터를 저장한다.
# 4. 최종 저장된 데이터를 출력한다.
# 주의: 기온 데이터는 숫자가 아닌 문자열 형태이므로 숫자로 타입을 변경해야한다! (소수점이 있으므로 float() 사용)
# 기온 데이터 관련해서는 인덱스 기준 1(평균기온), 2(최고기온), 4(최저기온), 6(일교차)
print(headerList)
print(dataList)

col_names = headerList
df = pd.DataFrame(dataList, columns=col_names)
print(df)
print(df.describe())
print(df[df['최고기온(℃)'] == df['최고기온(℃)'].max()][['일시', '최고기온(℃)']])


f.close()