# 예제 1
'''
o = input("춘천(운임:5000원) 부산(운임:30000원) 대구(운임:20000원) 수원(운임 10000원) 중 목적지를 한 곳 입력하세요: ")
t = input("KTX(10000원 추가) / 새마을호(5000원 추가) / 무궁화호(3000원 추가) 중 하나를 입력하세요: ")
s = input("좌석 / 입석(2000원 할인) 중 하나를 입력하세요: ")

def objection(o):
    if o == '춘천':
        return 5000
    elif o == '부산':
        return 30000
    elif o == '대구':
        return 20000
    elif o == '수원':
        return 10000
    
def train(t):
    if t == 'KTX':
        return 10000
    elif t == '새마을호':
        return 5000
    elif t == '무궁화호':
        return 3000

def ud(s):
    if s == '좌석':
        return 0
    elif s == '입석':
        return 2000
    
def cal_payment(a, b, c):
    return a + b + c

print(cal_payment(objection(o), train(t), ud(s)), "원" , sep='')
'''

'''
# 예제 85
ice = {
    '메로나' : 1000,
    '폴라포' : 1200,
    '빵빠레' : 1800
}
print(ice)

# 예제 86
ice1 = {
    '죠스바' : 1200,
    '월드콘' : 1500
}

ice.update(ice1)
print(ice)

# 예제 87
name = input("가격이 궁금한 상품: ")
for list in ice:
    if list == name:
        print(ice[name])

# 예제 88
ice["메로나"] = 1300
print(ice)

# 예제 89
ice.pop('메로나')
print(ice)
'''

'''
# 예제 91
inventory = {
    "메로나" : [300, 20],
    "비비빅" : [400, 3],
    "죠스바" : [250, 100]
}
print(inventory)

# 예제 92
print(inventory["메로나"][0], "원")

# 예제 93
print(inventory["메로나"][1], "개")

# 예제 94
inventory.update({"월드콘" : [500, 7]})
print(inventory)

# 예제 95
icecream = {'탱크보이':1200, '폴라포':1200, '빵빠레':1800, '월드콘':1500, '메로나':1000}
keyList = [key for key in icecream]
print(keyList)
# 또는 keys() 메서드 이용
keys = list(icecream.keys())
print(keys)
'''

'''
# 예제 221
# 리스트로 저장해서 역순 저장한 후 다시 문자열로 출력
def print_reverse(string):
    strList = list(string)
    strList.reverse()
    rev_str = ''.join(strList)
    print(rev_str)
print_reverse("python")
# 또는
def print_reverseA(string):
    print(string[::-1]) # 전체 문자를 거꾸로 이동
    # 문자[start:stop:step]
    # :step 생략 시 기본적으로 1
print_reverseA("python")

# 예제 222
def print_score(scores):
    avg = sum(scores) / len(scores)
    print(avg)
print_score([1, 2, 3])
'''

'''
# 예제 96
icecream = {'탱크보이':1200, '폴라포':1200, '빵빠레':1800, '월드콘':1500, '메로나':1000}
valueList = [value for value in icecream.values()]
print(valueList)

# 예제 97
print(sum(valueList))
# 또는 values() 메서드를 이용하여 바로 sum 하기
print(sum(icecream.values()), "원", sep='')

# 예제 98
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)
'''

