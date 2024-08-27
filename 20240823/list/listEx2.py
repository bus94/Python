# 파일명: listEx2.py

# # 여러 개의 리스트 값을 꺼낼 때
# list1 = [1,2,3,4,5,6]

# # 2 3 4 출력
# # 리스트명[시작 인덱스:끝 인덱스]
# # 시작은 값을 포함한다
# # 끝 값을 포함하지 않는다
# print(list1[1 : 4])

# # 1~4까지 슬라이싱
# print(list1[0 : 4])
# print(list1[: 4])

# # 4부터 마지막 슬라이싱
# print(list1[4 : 6])
# print(list1[4 :])

# # [1, 2, 3, 4, 5, 6]
# # 오른쪽에서 슬라이싱
# # 4 5 6 출력
# print(list1[-3 :]) # 4 5 6
# print(list1[-4 : -1]) # 3 4 5

# # 리스트 +
# a = [1,2,3]
# b = [6,4,5]

# # 결과창 지우기 cls
# # a 리스트에 b를 연결한다.
# print(a + b)
# # b 리스트에 a를 연결한다.
# print(b + a)

# print(a)

# # 문자랑 똑같은 리스트 복사
# print(a * 3)

# # [1, 2, 3] 2번 삭제
# # 파이썬 변수, 리스트 삭제 del
# num = 10
# print(num)
# del num

# del a[1]
# print(a)

# 리스트에 하나의 값을 맨 마지막에 추가 append()
# 여러 개를 각각 추가 extend()
# 중간에 값을 추가 insert()

# c = [10, 3, 90, 25, 33]
# # 가장 큰 값
# # 가장 작은 값
# print(max(c))
# print(min(c))

# # c 리스트 합계
# print(sum(c))

# # 정렬 기본적으로 오름차순
# print('정렬 전:', c)
# c.sort(); print()
# print('정렬 후:', c)
# print()
# # 내림차순
# c.sort(reverse=True)
# print('내림차순 정렬:', c)
# c.reverse(); print()
# print('역 정렬:', c)

# # 문자 가능
# nameList = ["z", "h", "f", "b", "l"]

# # 내림차순, 오름차순
# nameList.sort()
# print("오름차순:",nameList)
# nameList.sort(reverse=True)
# print("내림차순:",nameList)

# # sorted() 메서드
# nameList2 = ['하나', '둘', '셋', '넷']
# nameList3 = ['ㅎ', 'ㅌ', 'ㄲ', 'ㄴ']

# # 비어있는 리스트 생성
# # 학생들 의 점수를 6개 저장
# # 1번 학생의 점수: **
# # 2번 학생의 점수: ** 6번까지 입력받기
# scoreList = []

# start = 1
# while start <= 6 :
#     num = int(input(f'{start}번 점수: '))
#     scoreList.append(num)
#     start += 1
# print("입력받은 리스트:",scoreList)

# 입력 받은 점수 중에 85점이 있어?
# index = 1   
# find = 85
# result = find in scoreList
# if result :
#     # 만약 점수가 있다면 몇 번째 인덱스에 있는지 출력
#     # 출력 index(값) 함수
#     index = scoreList.index(find)
#     print(index, "번 째에 있습니다!", sep='')
# else :
#     # 만약 점수가 없다면 85점은 없습니다
#     # index() 함수는 값이 없으면 ValueError 발생
#     #  ValueError: 85 is not in list
#     #  > try ~ catch 예외처리
#     print(scoreList.index(find))
#     print(find, "점 점수는 없습니다.", sep='')

# scoreList = [85, 100, 90, 75, 85]

# # index(value, start, end)
# # value 값 (필수)
# # start 검색 시작할 인덱스 (선택 사항) - 중복 확인 가능
# # end 검색 종료할 인덱스 (선택 사항)
# print("처음 검색:", scoreList.index(85))
# print("두 번째 검색:", scoreList.index(85, 1))

proList = ["python","spring","html", "Java", "css", "springboot", "Java"]

# 대소문자 구별함 "java" → 에러
# print(proList.index("Java"))

# 리스트 삭제 
# remove() 리스트에서 원하는 값을 삭제할 때
#          사용하는 함수
#          특정값이 처음 나오는 위치의 값을
#          삭제 
# proList.remove("Java")
# print(proList)

# pop() 함수
# 특정 인덱스에 해당하는 값을 제거하고 그 값을 반환하는 기능을 가진다.
# 삭제를 하게 되면 뒤에 있는 데이터가 자동으로 앞쪽으로 온다.
# pop()로 작성하면 맨 뒤의 데이터가 없어진다.
# print(proList.pop(3))
# print(proList)

# print(proList.pop())
# print(proList)

#TypeError: 'str' object cannot be
#         interpreted as an integer
# print(proList.pop()) 특정 인덱스가 없다면 에러

# # 리스트 안에 데이터만 전부 삭제
# proList.clear()
# print(proList)

# del proList

# # NameError: name 'proList' is not defined
# print(proList)

print(proList)
print()
proList.reverse()
print("뒤집기:", proList)