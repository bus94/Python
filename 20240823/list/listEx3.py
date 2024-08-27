#파일명: listEx3.py

# /*
#    * # 숫자이동[1단계]
#    * 1. 숫자2는 캐릭터이다.
#    * 2. 숫자1을 입력하면, 캐릭터가 왼쪽으로
#    *      숫자2를 입력하면, 캐릭터가 오른쪽으로 이동한다.
#    * 3. 단, 좌우 끝에 도달했을 때, 예외처리를 해야한다.
#    * 4. {0, 0, 2, 0, 0, 0, 0};  ==> 왼쪽 ==> {0, 2, 0, 0, 0, 0, 0};
#    * 
#    */
'''
gameList = [0, 0, 0, 2, 0, 0, 0]

print(gameList)
while True :
    p = gameList.index(2)
    direcNum = int(input("좌(1) 우(2): "))
    
    if direcNum == 1 and p > 0 :
        gameList[p - 1], gameList[p] = gameList[p], gameList[p - 1]
    elif direcNum == 2 and p < len(gameList) - 1:
        gameList[p], gameList[p + 1] = gameList[p + 1], gameList[p]

    print(gameList)
'''

'''
gameList = [0, 0, 0, 2, 0, 0, 0]

print(gameList)
newP = 0
while True :
    p = gameList.index(2)
    direcNum = int(input("좌(1) 우(2): "))
    
    if direcNum == 1 and p > 0 :
        newP = p - 1
    elif direcNum == 2 and p < len(gameList) - 1:
        newP = p + 1
    gameList[newP], gameList[p] = gameList[p], gameList[newP]

    print(gameList)
'''

# 관리비

apt = [
    [101, 102, 103],
    [201, 202, 203],
    [301, 302, 303]
]

pay = [
    [1000, 2100, 1300],
    [4100, 2000, 1000],
    [3000, 1600, 800]
]


# 문제 1) 각층별 관리비 합 출력
# 정답 1) 4400, 7100, 5400
'''
stairPay = []
i = 0
while i < len(pay) :
    stairPay.append(sum(pay[i]))
    i += 1
print(stairPay)
'''

# 문제 2) 호를 입력하면 관리비 출력
# 예    2) 입력 : 202  관리비 출력 : 2000
'''
inputApt = int(input("입력 : "))
i = 0
while i < len(apt) :
    findApt = inputApt in apt[i]
    if findApt :
        payIndex = apt[i].index(inputApt)
        print(inputApt, "호 관리비 출력 : ", pay[i][payIndex], sep='')
    i += 1
'''
    

# 문제 3) 관리비가 가장 많이 나온 집, 적게 나온 집 출력
# 정답 3) 가장 많이 나온 집(201), 가장 적게 나온 집(303)
'''
maxPayIndex = {"i": -1, "j": -1}
minPayIndex = {"i": -1, "j": -1}
print("pay:", pay)
payList = sum(pay, [])
for i, eachPay in enumerate(pay) :
    for j, valuePay in enumerate(eachPay):
        if max(payList) == valuePay:
            maxPayIndex["i"] = i
            maxPayIndex["j"] = j
        if min(payList) == valuePay:
            minPayIndex["i"] = i
            minPayIndex["j"] = j
print("가장 많이 나온 집:", apt[maxPayIndex["i"]][maxPayIndex["j"]])
print("가장 적게 나온 집:", apt[minPayIndex["i"]][minPayIndex["j"]])
'''

# 문제 4) 호 2개를 입력하면 관리비 교체
'''
originPayIndex = {"i": -1, "j": -1}
replacePayIndex = {"i": -1, "j": -1}
print("101~103,201~203,301~303 중 변경할 호수 2개를 입력해주세요")
input1 = int(input("변경할 호수 입력1: "))
input2 = int(input("변경할 호수 입력2: "))
for i, eachApt in enumerate(apt):
    for j, valueApt in enumerate(eachApt):
        if valueApt == input1:
            originPayIndex["i"] = i
            originPayIndex["j"] = j
        if valueApt == input2:
            replacePayIndex["i"] = i
            replacePayIndex["j"] = j
pay[originPayIndex["i"]][originPayIndex["j"]], pay[replacePayIndex["i"]][replacePayIndex["j"]] = pay[replacePayIndex["i"]][replacePayIndex["j"]], pay[originPayIndex["i"]][originPayIndex["j"]]
print("바뀐 pay1:", pay[originPayIndex["i"]][originPayIndex["j"]])
print("바뀐 pay2:", pay[replacePayIndex["i"]][replacePayIndex["j"]])
'''

# 쇼핑몰[장바구니]
#  1. 로그인 후 쇼핑 메뉴를 선택하면, 다음과 같이 상품목록을 보여준다.
#  1) 사과
#  2) 바나나
#  3) 딸기
#
#  2. 번호를 선택해 상품을 장바구니에 담을 수 있다.
#  3. 로그인 회원의 인덱스 번호는 각 행의 첫번째 열에 저장한다.
#  4. 해당 회원이 구매한 상품의 인덱스 번호는 각 행의 두번째 열에 저장한다.
#  예)
#  [
#       [0, 1],             qwer회원          > 사과구매
#       [1, 2],             javaking회원      > 바나나구매
#       [2, 1],             abcd회원          > 사과구매
#       [0, 3],             qwer회원          > 딸기구매
#       ...
#  ]

ids = ["qwer", "pythonking", "abcd"]
pws = ["1111", "2222", "3333"]

items = ["사과", "바나나", "딸기"]

jang = [[0] * 2 for i in range(100)]

count = 0

log = -1

while True:
    print("[MEGA MART]")
    print("[1]로 그 인")
    print("[2]로그아웃")
    print("[3]쇼    핑")
    print("[4]장바구니")
    print("[0]종    료")

    sel = input("메뉴 선택 : ")

    if sel.isdigit() :
        int(sel)
    else :
        print("다시 입력해주세요.")
        continue

    if sel == 1:
        while True:
            if log == 0:
                print("로그인 되어있습니다. 메인으로 돌아갑니다.")
                break
            print("=" * 5, "로그인 진행 중", "=" * 5)
            print(("[0]뒤로가기"))
            print(("[1]입력하기"))
            back = int(input("메뉴 선택 : "))
            if back == 0:
                break

            logId = (input("아이디: "))
            logPw = (input("비밀번호: "))
            
            for i in range(len(ids)):
                if logId == ids[i] and logPw == pws[i]:
                    log = 0
                    print("로그인 되었습니다.")
                    break
            if log == 0:
                print("로그인 확인!")
                break
            print("i:", i)
            print("log:", log)
            print("아이디와 비밀번호를 다시 입력해주세요.")
            continue

    elif sel == 2:
        if log == 0:
            logout = input("정말 로그아웃을 하시겠습니까?[y/n]\n")
            if logout.lower() == "y":
                log = -1
                print("log:", log)
                print("로그아웃 되었습니다.")
                continue
            elif logout.lower() == "n" :
                print("메인으로 돌아갑니다.")
            else :
                print("다시 입력해주세요.")
                
        else :
            print("로그인을 먼저 해주세요.")
            pass

    elif sel == 3:
        if log == 0:

            pass
        else :
            print("로그인을 먼저 해주세요.")
            break
        pass

    elif sel == 4:
        pass

    elif sel == 0:
        print("프로그램 종료")
        break

    else :
        print("다시 입력해주세요.")
        continue
