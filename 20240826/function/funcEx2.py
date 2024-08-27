# 파일명: funcEx2.py

# 함수 리턴
# 파이썬은 여러 개의 데이터를 리턴
# 튜플(tuple)
# - 리스트랑 똑같은 자료형
# - 한 번 값을 저장하면 변경 못한다.
# - 위치 정보
# - 여러 개의 리턴 값을 하나의 타입으로 넘길 때


# 상수
# - 값을 한 번 정하면 변경할 수 없는 것
# def a():
#     return 1
# def b():
#     return 1, 2

# print(a())
# print(b())

# tuple1 = ()
# print(type(tuple1))

# # 1
# # 고정 된 값으로 튜플 형태로 저장 - 콤마를 붙인다.
# num = (1)
# print(type(num)) # tuple
# tuple2 = (1,)
# print(type(tuple2)) # int
# tuple3 = ('1', 1.1, 1)
# tuple4 = 1, 2, 3, 4, 5, 6, 7
# print(tuple3[0])
# print(tuple4[1:3])

# # 접근 리스트와 똑같다!
# # 리스트명[인덱스]

# # 튜플 데이터 변경
# #tuple4[1] = 100 # 에러

# # 튜플 → 리스트 변경
# #   튜플 → 리스트로 변경해서 리스트의 값을 수정 후 수정된 리스트를 튜플의 형태로 해당 튜플에 저장
# temp = list(tuple4)
# print(temp)

# temp[1] = 100
# tuple4 = tuple(temp)
# print(tuple4)

# def greet(name="Guest"):
#     print(f"Hello, {name}")

# greet()
# greet("익준")

# def calcPrice(price, discount=0.1): # 기본 10% 할인
#     return price * (1 - discount)

# print(calcPrice(100))
# print(calcPrice(100, 0.2))

# # 여러 숫자의 합을 계산
# # 가변인자 튜플 형태
# def addNumbers(*num):
#     print(num)
#     # num 여러 개를 저장하는 튜플의 합
#     return sum(num)

# print(addNumbers(1, 2, 3))
# addNumbers(1, 2, 3, 4, 5, 6, 7, 8, 9)
# addNumbers(1)

# # 여러 개의 메시지를 출력
# def print_msg(*msg):
#     for i, m in enumerate(msg, 1):
#         print(f"{i}. {m}")

# print_msg("hello", "python", "welcome")

# # 가변인자 두 개 같이 사용 못한다
# # 가변 인자는 맨 마지막에 한 번만 작성 가능하다.
# def info2(c, *d):
#     print(c)
#     print(d)

# info2(1, 2, 3, 4, 5, 6)
# # def info(*a, *b):
# #     print(a, b)

