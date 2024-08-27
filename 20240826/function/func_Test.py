# 파일명: func_Test.py

# 1번 예제
'''
list_fruit = ['apple', 'banana', 'tomato']
list_animal = ['bear', 'elephant', 'monkey']
list_instrument = ['guitar', 'piano', 'harmonica']

def len_word(wordlist):
    lenWord = 0
    for word in wordlist:
        lenWord += len(word)
    return lenWord

print(len_word(list_fruit))
print(len_word(list_animal))
print(len_word(list_instrument))
'''

# 2번 예제
'''
scoreList = [30, 40, 50, 60, 70]
def calavg(numlist):
    sum = 0
    for num in numlist:
        sum += num
    avg = sum // len(numlist)
    if avg >= 60:
        return "Pass"
    else :
        return "Fail"
print(calavg(scoreList))
'''

# 3번 예제
'''
time = int(input("time 초를 입력: "))

def cal_time(time):
    if time < 24 * 60 * 60:
        hour = time // (60 * 60)
        time = time - hour * 60 * 60
        minute = time // 60
        time = time - minute * 60
        second = time
        return f"{hour}시 {minute}분 {second}초"
    else :
        return '입력 시간이 하루를 초과합니다.'
print(cal_time(time))
'''

# 4번 예제
'''
password = input("password 입력: ")

def checkPW(passwd):
    if len(passwd) >= 9:
        return 'Good'
    elif len(passwd) >= 5:
        return 'Normal'
    else :
        return 'Bad'

print("Your Password:", checkPW(password))
'''

'''
# 201 예제
def print_coin():
    return "비트코인"
# 202 예제
print(print_coin())
# 203 예제
for i in range(1, 101):
    print(f"{i}: {print_coin()}")
# 204 예제
def print_coins():
    for i in range(1, 101):
        print(f"{i}: 비트코인")

print_coins()
print_coins()
'''

def solution(array, commands):
    print("함수 시작")
    answer = []
    for i in range(len(commands)): 
        print("반복문 시작")
        print(f"commands[{i}][0]: {commands[i][0]}")
        print(f"commands[{i}][1]: {commands[i][1]}")
        print(f"commands[{i}][2]: {commands[i][2]}")
        print("array: ", array[commands[i][0]-1:commands[i][1]])
        a = array[commands[i][0]-1:commands[i][1]]
        a.sort()
        print("a: ", a)
        answer.append(a[commands[i][2] + 1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
