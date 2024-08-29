import chardet
import csv # csv 파일들을 다루는 라이브러리

from tkinter import *

# csv
# 쉼표로 나눠진 값을 데이터로 표현
# 엑셀에서도 csv를 생성
# 국어, 영어, 수학
# 90, 80, 100

# 파일 읽기하는 함수 그 안에서 encoding 설정
# 리스트에 저장

def det(filepath):
  result = ''
  # csv처럼 이진 파일들을 읽어올 때 사용하는 모드 rb
  with open(filepath, 'rb') as f:
    # detect() 인코딩 감지하는 역할
    # 딕셔너리 형태로 반환
    # {'encoding': 'EUC-KR', 'confidence': 0.99, 'language': 'Korean'}
    result = chardet.detect(f.read())
    print(result)
  return result['encoding']

def read_csv_file_open(filepath):
    encoding = det(filepath)
    print(f"인코딩 타입: {encoding}")
    reader = ''
    with open(filepath, 'r', encoding=encoding) as f:
        # csv 파일을 읽을 때 사용
        # reader() 파일을 행 단위로 읽어서 리스트 형태로 반환한다.
        reader = csv.reader(f)
        # print(type(reader))
        # for line in reader:
        #     print(line)
        return list(reader)

list1 = read_csv_file_open('singer1.csv')
print(list1)
print(type(list1))

# print()
# read_csv_file_open('newex.csv')

root = Tk()
root.geometry("800x500")

# 리스트의 값을 가져와서 라벨 출력
for row in list1:
   # join: 리스트나 튜플과 같은 반복 가능한 객체의 모든 값들을 하나의 문자열로 연결할 수 있다.
   labelText = " | ".join(row)
   print(labelText)
   label = Label(root, text=labelText)
   label.pack()

root.mainloop()

# 여자이면서 키가 160보다 큰 사람을 조회
# $ and연산자
# 1. 성별 시리즈 , 키 시리즈
# 2. 두 조건을 모두 만족하는 데이터 가져오기
