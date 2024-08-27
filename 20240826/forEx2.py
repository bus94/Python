# 파일명: forEx2.py

# # 파이썬에서만 사용할 수 있는 for문
# # list() 형 변환
# # range(개수) 0 부터 끝-1
# list1 = list(range(10)) 
# print(list1)

# # 리스트 생성할 때 반복문을 이용해서 리스트를 생성할 수 있다. 한줄로!
# list2 = [i for i in range(1, 6)]
# # 실행 순서
# # 1. range(1, 6) 1부터 5까지의 숫자를 생성
# # 2. 생성된 숫자를 순서대로 꺼내와서 i에 저장
# # 3. 저장된 값을 이용해서 list 생성
# print(list2)

# '''
# 리스트 컴프리헨션
# - 파이썬에서 리스트를 간단하게 한 줄로 선언
# - 리스트 생성 시 코드의 가독성을 높여준다.
# [data for item in iterable]
# data : 값이 들어온다.
# item : 현재 반복되어있는 값
# iterable : 리스트, 숫자범위(range), 문자열 ...
# '''

# list3 = ['a','b','c']
# upperList = [str.upper() for str in list3]
# print(upperList)

# # 짝수만 리스트에 포함
# # 1부터 10까지 숫자 중에서 짝수만
# numbers = [i for i in range(1, 11) if i % 2 == 0]
# # 1. range() 범위값 반환
# # 2. 범위값에서 하나씩 꺼내서 i에 저장
# # 3. 조건검사 이때 True이면 리스트에 포함한다.
# print(numbers)

# # -6 부터 10까지 반복을 하는데 홀수만 리스트에 저장하기
# # 문자열로 저장
# list4 = [i for i in range(-6, 11) if i % 2 != 0]
# print("정수형:",list4)
# list5 = [str(i) for i in range(-6, 11) if i % 2 == 1]
# print("문자형:",list5)
# # 숫자 → 문자로 변경해서 저장 str()
# # 문자 → 숫자 (정수) int()

# list5 = []

# for i in range(-6,11):
#     if i % 2 == 1:
#         list5.append(str(i))

'''
구구단을 for문을 이용해서 range로 2 ~ 9단까지 출력
'''
for i in range(2, 10):
    print(f"{i}단: ", end=" ")
    for j in range(1, 10):
        print(i * j, end=" ")
    print() # 줄바꿈

print("=" * 20)

# 한 줄로 작성할 때
gugudan = [[i * j for j in range(1, 10)] for i in range(2, 10)]
for i, dan in enumerate(gugudan):
    print(f"{i + 2}단: {dan}")

# start 속성을 이용해서 index값을 지정할 수 있다. 기본적으로 0으로 되어있다.
# join()
# map(문자타입, value)
#   여러 개의 문자를 각각의 타입으로 변환 x
for i, dan in enumerate(gugudan, start=2):
    print(f"{i}단: {dan}")


# input으로 입력 받을 때 정수형인지 문자형인지 구분하는 방법 2가지

# 여러 개의 데이터를 입력 받아서 각각의 데이터로 리스트에 저장
user = input('여러 개의 데이터: ')
# 결과를 저장할 리스트 생성
values = []

# 1. 입력 문자를 공백으로 분리해서 각각의 값을 처리
for i in user.split(' '):
    if i.isdigit():
        # isdigit() 정수로 변환 가능하니?
        values.append(int(i))
    elif '.' in i and i.replace('.', '', 1).isdigit():
        values.append(float(i))
    else :
        values.append(i)
        print()

# 2. 예외 처리를 이용해서 여러 데이터를 입력받는다.
def value(val):
    try:
        print("정수형")
        # 실행할 문장 정수형으로 형변환이 되면 정수형으로 리턴
        return int(val)
    except ValueError:
        pass

    try:
        print("실수형")
        # 실수 형태로 형변환이 되면 실수형으로 변경 후 리턴
        return float(val)
    except ValueError:
        pass

    # 정수, 실수형으로 변경이 안되면 문자형 자체로 리턴
    print("문자형")
    return val
values = list(map(value, user.split()))

print(values)