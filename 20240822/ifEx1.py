# 파일명: ifEx1.py

'''
# 참과 거짓을 저장하는 타입 bool (자바에서 boolean)
result = True
result2 = False
print(result)
print(type(result))

# 들여쓰기 기준 4칸 (띄어쓰기 4번으로 작성은 하지 않기)
if result :
    if result2 :
        print("result가 참이면서 result2가 참일 때 실행")
    print("result가 거짓이면서 result2가 거짓일 때 실행")
print("result가 거짓일 때 실행")

print()

# 백화점에서 여러 물품 구매
# 구매한 물품이 총합 10만원 이상이면 상품권 수령 가능
# 30000, 50000, 15000, 25000
total = 30000 + 50000 + 15000 + 25000

# if문으로만 작성
# 10만원 이상이면 실행
if total >= 100000 :
    print('상품권 수령 가능')

# 10만원 미만이면 실행
if total < 100000 :
    print('상품권 수령 불가')

# 나이를 입력 받아서 버스 요금을 출력
#  20세 이상이면 요금 2800원
#       미만이면 무료, 65세 이상 무료
age = 25

# if, else 문으로 작성
if age >= 20 :
    print('요금 2800원')
else :
    print('요금 무료')

# 65세 이상도 무료라는 조건 추가하기
# or(또는) : 둘 중 하나만 참이면 실행
if age < 20 or age >= 65 :
    print("요금 무료")
else :
    print("요금 2800원")

# 90 ~ 100 사이 범위 안에 들어오는 숫자는 A
num = 95
if num >= 90 and num <= 100 :
    print("A")
else :
    print("F")

# 파이썬은 수학과 같이 90 <= x <= 100 의 표현이 가능하다
if 90 <= num <= 100 :
    print("A")
else :
    print("F")


num = int(input('점수: '))
if 90 <= num <= 100 :
    result = 'A'
elif 80 <= num < 90 :
    result = 'B'
elif 70 <= num < 80 :
    result = 'C'
elif 60 <= num < 70 :
    result = 'D'
else :
    result = 'F'

print("결과:", result)
'''
# Q1
a_gender = 'female'
a_grade = 2

b_gender = 'female'
b_grade = 1

price = 10000

# 할인 여부
isDiscountA = (a_gender == 'female') and a_grade == 1
isDiscountB = (b_gender == 'female') and b_grade == 1
if isDiscountA :
    print("20% 할인된 A의 가격:", price - (price * 20 // 100))
else :
    print("할인되지 않은 A의 가격:", price)
if isDiscountB :
    print("20% 할인된 B의 가격:", price - (price * 20 // 100))
else :
    print("할인되지 않은 B의 가격:", price)

# Q2
toeicScore = 900
engGrade = 'B'

# 입사지원 여부
isApply = (toeicScore >= 800) or (engGrade == 'A')
if isApply :
    print("회사 지원 가능!")
else :
    print("회사 지원 불가!")
