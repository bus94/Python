# 폴더명: list 
# 파일명: listEx1.py

# 리스트(list)
#  배열: 하나의 타입으로 여러 개를 저장
#  클래스: 다른 타입으로 타입 만들고 여러 개 저장

# 리스트 생성시 []
# 여러개 저장 
# 인덱스 사용 가능 (0부터)
# 순서가 있는 자료구조 (순차적인 자료구조)

# list1 = [1, 2, 3, 4]
# list2 = [1.1, 2.2, 3.3]
# list3 = ["a", "b", "c"]
# print(list1)
# print(list2)
# print(list3)

# list4 = [1, "python", 10.12345]
# print(list4)

# # 데이터 접근
# print(list4[0])
# print(list4[1])
# print(list4[2])

# # 파이썬 만의 리스트 접근 방법
# # 오른쪽부터 인덱스를 이용해서 접근 가능하다
# # 오른쪽에서는 음수값을 이용해서 인덱스를 지정
# print(list4[-1])
# print(list4[-2])
# print(list4[-3])

# 빈 리스트
# list5 = []
# print(list5)

# 비어 있는 리스트는 저장할 공간이 없다
# ex) list5[0] = 10 → 이렇게 하면 인덱스 범위에 맞지 않다는 에러가 난다

# 따라서 만들어서 저장해야한다
# append(값) : 하나의 값만 맨 마지막에 추가
# list5.append(10)
# print(list5)
# list5.append(20)
# print(list5)
# list5.append(30)
# print(list5)
# list5.append("수업 중")
# print(list5)

# 여러 개를 추가
# list5.append([40, 50, 60])
# print(list5) # 출력: [[40, 50, 60]]
# print(list5[0]) # 출력: [40, 50, 60]
# print(list5[0][1]) # 출력: 50

# # 리스트 안에 리스트를 저장
# list6 = [
#     [1,2,3], [1.1, 2.2, 3.3], ["python", "java", "spring"]
# ]
# print(list6)

# # [1,2,3] 중에서 2를 출력
# print(list6[0][1])
# # print(list6[-3][-2])

# # [1.1, 2.2, 3.3] 중에서 3.3 출력
# print(list6[1][2])
# # print(list6[-2][-1])

# # ["python", "java", "spring"] python 출력
# print(list6[2][0])
# # print(list6[-1][-3])

# # 2차원 배열과 비슷하다.
# numberList = [1,2,3,4,5]

# # insert(인덱스,값)
# numberList.insert(2,6) # 2번 index에 '6'을 넣기
# print(numberList)

# numberList.insert(0, "hello")
# print(numberList)

# # 여러 개를 각각 저장할 때
# nameList = ["이익준"]
# print(nameList)
# # [] 괄호를 하는 이유는 여러 개의 데이터를 어떤 타입으로 저장
# nameList.extend(["김준완, 양석형"])
# print(nameList)

# # 예제 요구사항 만족하는 프로그램 만들기
# winner = ['박민아', '정민호', '김철수', '이영희', '손수정']
# print(len(winner))
# # winner의 list는 어떤 공모전의 수상자 명단이다.

# # # 1) 정수지가 수상했는지 확인하라
# # # 2) 김철수가 수상하지 못했는지 확인하라
# # # 3) 박민아가 수상했는지 확인하라
# # # 4) 전은진이 수상하지 못했는지 확인하라

# # in, not in
# # 결과값이 True, False
# # 리스트 안에 검색하는 값이 있어? in 연산자
# print('정수지' in winner) # False
# # 리스트 안에 검색하는 값이 없어? not in 연산자
# print('정수지' not in winner) # True

# # 검색할 명단
# checkName = ['정수지', '김철수', '박민아', '전은진']

# # 반복문하고 index 번호를 이용해서 체크하는 명단을 수상자 명단에서 확인하기
# i = 0
# while i < len(checkName) :
#     if checkName[i] in winner :
#         print(f'{checkName[i]} 은/는 수상했다.')
#     else :
#         print(f'{checkName[i]} 은/는 수상하지 못했다.')
#     i += 1

# 예제
# 판매 실적 점수와 고객 평가 점수를 통해 우수 제품을 선발하고자 한다. 판매 실적 점수가 4 이상, 고객 평가 점수가 4 이상이면 우수 제품, 모두 4 미만 제품은 판매 중지 제품
itemList = [
    ["비누", 3, 2],
    ["칫솔", 5, 4],
    ["샴푸", 2, 1],
    ["치약", 4, 4],
    ["로션", 5, 3],
]

i = 0
bestItemList = []
worstItemList = []
while i < len(itemList) :
    a = itemList[i][1]
    b = itemList[i][2]
    if a >= 4 and b >= 4 :
        bestItemList.extend([itemList[i][0]])
    if a < 4 and b < 4 :
        worstItemList.extend([itemList[i][0]])
    i += 1
print("우수제품 목록: ", bestItemList)
print("판매중지 목록: ", worstItemList)