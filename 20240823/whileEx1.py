# 파일명: whileEx1.py

# num = 1
# while num != 6 :
#     print(num)
#     num += 1

# num = 1
# while num != 11 :
#     print("나무를 ", num, "번 찍었다.")
#     num += 1
# print("나무가 넘어갔다.")

# 별 1~5 계단 형식 출력
# start = 1
# while start <= 5 :
#     print("*" * start)
#     start += 1

# 구구단
# number = 2
# sta = 1
# while number != 10 :
#     print(number, "단: ", sep='', end='')
#     while sta != 10 :
#         print(number * sta, end=' ')
#         sta += 1
#     number += 1
#     sta = 1
#     print()

# 별 1~9 계단 2개씩 증가 형식 출력
# start = 1
# while start <= 9 :
#     print("*" * start)
#     start += 2

# 1부터 n까지의 홀수 합 구하기
# num = int(input("자연수 입력:"))
# startNum = 1
# sum = 0
# while startNum <= num :
#     sum += startNum
#     startNum += 2
# print('1부터 ', num, '까지 홀수의 총합: ', sum, sep='')

# 시험을 치른 후, 맞은 개수를 알려주기 (사용자의 이름과 문제의 개수 입력, 맞혔는지 아닌지 입력)
# input() 함수는 입력을 받으면 모두 문자로 반환 된다
# name = input('이름:')
# count = int(input('문제 개수:'))

# totalCount = 0
# start = 1
# print('****************************')
# while start <= count :
#     save = input(f'{start}번 문제를 해결했니?\n')

#     # 사용자 입장에서 y, Y (풀었다면 yes의 대답)
#     save = save.lower()

#     if save == 'y' :
#         totalCount += 1

#     # 이렇게 함수를 종료해도 된다
#     # if totalCount == count :
#     #     break

#     start += 1
# print('****************************')
# print(name, "학생, 총", totalCount, "문제 정답!")

# 원래의 높이의 1/2만큼 튀어오르는 공. 높이가 0.00001m 보다 낮으면 튀어오르지 않는다
height = int(input("높이를 입력하세요(m): "))
count = 0
while height >= 0.00001 :
    count += 1
    height = height / 2
    print(height, count)
print("공이 튀긴 횟수는", count, "회 입니다.")

