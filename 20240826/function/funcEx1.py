# 폴더명: function
# 파일명: funcEx1.py

# 함수
#  입력값을 받아 출력값을 반환하는 코드의 묶음
# def 함수명(매개변수): 
#   실행할 문장
#   return 값

# 함수의 매개변수한테 기본값을 설정하면 값이 들어올 때 들어온 값으로 처리를 하고 값이 들어오지 않는다면 기본값으로 저장
# 주의!! 기본값을 설정할 땐 뒤의 매개변수부터 설정해야한다!! (함수가 실행될 때 입력된값이 가장 왼쪽부터 적용되기 때문에 덮어지는 문제에서 어디에 적용될지 모름)
# (뒤에서부터 기본값을 설정해야한다는 것을 기억하지 못할 땐 그냥 기본값 모두 설정하거나 아예 하지말자 또는 매개변수 이름 지정해서 값을 넘기자)
# def info(name='무명', age='영'):
#     # 문자랑 문자를 연결할 때는 +
#     print("이름:", name)
#     print("나이:", age)

# # 함수 실행
# info("이서희", 20)
# print()
# info("이서희")
# print()
# info()
# # 함수의 매개변수에 기본값을 설정하지 않는다면
# # info("이서희") → TypeError: info() missing 1 required positional argument: 'age'
# print()
# # 매개변수 이름을 지정해서 값을 넘길 수 있다. 
# # 순서에 신경 쓰지 않아도 된다.
# info(age = 25, name = "이익준")
# print()

# name = input("입력한 이름: ")
# age = input("입력한 나이: ")
# info(name = f"{name}", age = f"{age}")

# 더하기
# 파이썬이 알아서 결과값의 리턴 타입을 지정해서 넘겨준다.
# def add(a = 0, b = 0):
#     if a == 0 and b == 0:
#         return '아무것도 입력하지 않아서 계산할 수 없다.'
#     return a + b

# result = add()
# print(result)
# print(type(result)) # str
# print()
# result2 = add(10, 2)
# print(result2)
# print(type(result2)) # int

# 예제
# 나의 풀이 (끝까지x)
# def longest(a, b, c):
#     long = max(len(a), len(b), len(c))
#     return long

# def shortest(a, b, c):
#     short = max(len(a), len(b), len(c))
#     return short

# string = input("입력한 단어: ")
# stringList = []
# for i in string.split(' '):
#     stringList.append(i)

# print(longest(stringList[0], stringList[1], stringList[2]))

def longes(a, b, c):
    sizeA = len(a)
    sizeB = len(b)
    sizeC = len(c)

    if sizeA >= sizeB and sizeA >= sizeC:
        return a
    elif sizeB >= sizeA and sizeB >= sizeC:
        return b
    else:
        return c
print(longes('one', 'second', 'three'))

print()
# 아래 코드는 사전 순 기준으로 출력된다. 즉 알파벳 순서로 비교한다.
def longe(a, b, c) :
    return max(a, b, c)
print(longe('one', 'second', 'three'))

print()
# 아래 코드는 key 속성에 len을 작성해서 단어의 길이를 기준으로 가장 큰 문자를 반환한다.
def longest(a, b, c) :
    return max(a, b, c, key=len)
print("길이가 가장 긴 문자:", longest('one', 'second', 'three'))

def shortest(a, b, c) :
    return min(a, b, c, key=len)
print("길이가 가장 짧은 문자:", shortest('one', 'second', 'three'))

# 예제
# list로 여러 개의 문자를 집어넣고 위의 실행한 내용들이 정상 작동하는지 확인하기
proList = ['java', 'springboot', 'html']
# 리스트에서 가장 문자열이 긴 단어를 출력
#           가장 문자열이 짧은 단어를 출력
print(longest(proList[0], proList[1], proList[2]))
print(shortest(proList[0], proList[1], proList[2]))