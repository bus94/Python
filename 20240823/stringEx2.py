# 파일명: stringEx2.py

# f문자열 포맷팅
# f 문자는 대소문자 상관없음
# 문자열 시작 앞에 붙인다.
name = "이서희"
age = 20
text = f"이름: {name}, 나이: {age}"
print(text)

# 변수만 들어가는 것이 아니라 계산식을 작성할 수 있다.
hours = 6
minutes = hours * 60
text2 = f"{hours}시간 = {minutes}분"
print(text2)

text3 = f"{hours}시간 = {hours * 60}분"
print(text3)

# 정렬
name2 = "이익준"
left = f"{name2:<10}"
right = f"{name2:>10}"
center = f"{name2:^10}"
# 나머지 공백을 별로 채우기
center2 = f"{name2:*^10}"
print(left)
print(right)
print(center)
print(center2)

# 소수점 출력
num = 10.1234
text4 = f"{num:.2f}" # 만약 .5f 이런식이면 없는 소수점 뒤의 자리 수는 0으로 채워져서 출력된다 → 10.12340
print(text4)

