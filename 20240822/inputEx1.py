# 파일명: inputEx1.py

'''
# input()
# 입력한 모든 내용은 모두 str 타입으로 저장
str1 = input('정수: ')
print(type(str1))

# 문자를 숫자로 저장
str1 = int(str1)

print(type(str1))
print(str1 + 10)

# 정수
age = int(input('나이 > ')) # 문자 타입으로 입력 받은 값을 정수 타입으로 바로 바꿔주기
# 실수
hei = float(input('키 > ')) # 200.20을 입력하면 hei = float('200.20') 이 되고, 키보드로 입력받은 '200.20'은 실수 타입으로 저장됨

# 문자
string = input('아무 문자나 입력 > ')

# 더하기
# 문자 + 문자 = 연결
# 문자 + 숫자 = 에러


# 곱하기
# 문자열 복사
print("hello" * 5)
# ***** 출력하는 경우
print("*" * 5)

print(' ' * 5)
print(' ' * 4 + '*' * 1)
print(' ' * 3 + '*' * 2)
print(' ' * 2 + '*' * 3)
print(' ' * 1 + '*' * 4)
print('*' * 5)

# map(변환할 타입, input().split())
# 여러 개를 한 번에 입력받고 싶을 때
# (+ 일반적으로 파이썬은 한 줄에 명령문을 전부 작성하는게 맞지만, 코드가 너무 길어지는 경우 등 줄을 개행해서 작성하고 싶다면 "\"을 작성하면 된다.)
list1 = input('여러 개의 문자를 입력: ') \
        .split(' ')
print(list1)
print(type(list1)) # <class 'list'>

# 파이썬에서 여러 개의 변수를 저장
a = 10; b = 20
c = 100; d = 20; e = 30 # 잘 사용하진 않는다.
print(a, b)
'''
'''
# 값 교체
일반적인 값 교체
temp = a
a = b
b = temp

a, b = b, a
'''

'''
# 파이썬만 사용하는 변수 선언
a1, b1, c1 = 1000, 2000, 3000
print(a, b)
print(a1, b1, c1)

# 형변환
# int(), float(), str()

# 산술연산자
# 나눗셈 몫
print("나눗셈 몫: ", 100 / 10) # 결과 실수
print("나눗셈 몫: ", 100 // 10) # 결과 정수


# 증감 연산자 못씀
# 복합 연산자 가능
a += 1

str3 = "hello"
print("변경 전 문자: ", str3)
print("모두 대문자로: ", str3.upper()) # 모두 대문자 - 함수를 사용한다고 저장이 바로 되지 않는 것들도 있다
print("변경 후 문자: ", str3)
print()
print("변경 전 문자: ", str3)
str3 = str3.upper()
print("변경 후 문자: ", str3)
'''

# 문자열의 길이, 배열의 길이
size = len('python java springboot') # 6 + 1(공백) + 4 + 1(공백) + 10 = 22
print("문자열의 길이: ", size)

list2 = ['python', 'java', 'springboot'] # 문자의 개수가 3개이므로 배열의 길이 = 3
print("배열의 길이: ", len(list2))


