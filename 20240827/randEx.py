# 파일명: randEx.py

# 파이썬에서 랜덤 파일을 가지고 와서 랜덤값을 출력

import random

# 정수값 출력
# randint(시작, 끝)
rand = random.randint(1, 3)
print(rand)

# 리스트에서 랜덤으로 
items = ['python', 'java', 'spring', 'html']

# choice(리스트) 리스트 안에 데이터 중에서 하나를 뽑는다.
rend_item = random.choice(items)
print(rend_item)

# 위에 하나의 데이터만 출력
# 중복적으로 2개 이상 출력
rend_item2 = random.choices(items, k=3)
print(rend_item2)
print()

# 리스트 섞기
print("섞기 전:",items)
random.shuffle(items)
print("섞기 후:",items)

