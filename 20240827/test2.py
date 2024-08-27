import pymysql

# conn = pymysql.connect(host='localhost', user='root', password='1234', db='pythonTest', charset='utf8')
# cur = conn.cursor()
# cur.execute('''
#  create table farm(
#     kind varchar(10),
#     name varchar(10)
#  )
#  '''
#  )

class Farm:
    def __init__(self, kind):
        self.kind = kind

    def __str__(self):
        return f"(kind: {self.kind})"
    
class Fruit(Farm):
    def __init__(self, kind, name):
        super().__init__(kind)
        self.name = name

    def __str__(self):
        return f"(kind: {self.kind}, name: {self.name})"
    
class Vegetable(Farm):
    def __init__(self, kind, name):
        super().__init__(kind)
        self.name = name

    def __str__(self):
        return f"(kind: {self.kind}, name: {self.name})"
    
class Nut(Farm):
    def __init__(self, kind, name):
        super().__init__(kind)
        self.name = name

    def __str__(self):
        return f"(kind: {self.kind}, name: {self.name})"

farmList = []
fruitList = []
vegetableList = []
nutList = []
dictFruit = {}
dictVeget = {}
dictNut = {}

# 농작물 추가 메서드
def addNewKind():
    print("1. 과일 / 2. 채소 / 3. 견과")
    sel = int(input("추가할 종류 번호: "))
    name = input("이름 : ")
    amount = int(input("수량 : "))

    if sel == 1:
        fruit = Fruit("과일", name)
        dictFruit = {"종류": fruit.kind, "이름": fruit.name, "수량": amount}
        print(dictFruit["종류"], dictFruit["이름"], dictFruit["수량"])
    elif sel == 2:
        vegetable = Vegetable("채소", name)
        dictVeget = {"종류": vegetable.kind, "이름": vegetable.name, "수량": amount}
        print(dictVeget["종류"], dictVeget["이름"], dictVeget["수량"])
    elif sel == 3:
        nut = Nut("견과", name)
        dictNut = {"종류": nut.kind, "이름": nut.name, "수량": amount}
        print(dictNut["종류"], dictNut["이름"], dictNut["수량"])
    
    if dictFruit != None:
        farmList.append(dictFruit)
        dictFruit = None
    elif dictVeget != None:
        farmList.append(dictVeget)
        dictVeget = None

    elif dictNut != None:
        farmList.append(dictNut)
        dictNut = None

# 농작물 조회 메서드
def printFarm():
    for farm in farmList:
        print(f'{farm["종류"]: farm["이름"](farm["수량"]개)}')

while True:
    print("=" * 10, " 쌍용 마트 ", "=" * 10)
    print("*" * 7, " 메인 메뉴 ", "*" * 7)
    print("1. 직원 메뉴")
    print("2. 손님 메뉴")
    print("9. 종료")
    selNum = input("메뉴 번호 선택: ")

    if selNum.isdigit() :
        selNum = int(selNum)
    else :
        print("숫자로 다시 입력해주세요.")
        continue

    if selNum == 1:
        while True:
            print("*" * 7, " 직원 메뉴 ", "*" * 7)
            print("1. 새 농산물 추가")
            print("2. 종류 삭제")
            print("3. 수량 수정")
            print("4. 농산물 목록")
            print("9. 메인으로 돌아가기")
            selNum1 = input("메뉴 번호 선택: ")

            if selNum1.isdigit() :
                selNum1 = int(selNum1)
            else :
                print("숫자로 다시 입력해주세요.")
                continue
            
            if selNum1 == 1:
                addNewKind()
                print("새 농작물이 추가되었습니다.")
                continue
            elif selNum1 == 2:
                
                continue
            elif selNum1 == 3:
                
                continue
            elif selNum1 == 4:
                print(farmList)
                continue
            elif selNum1 == 9:
                break
            else :
                print("잘못 입력하였습니다. 다시 입력해주세요.")
                continue

    elif selNum == 2:
        while True:
            print("*" * 7, " 고객 메뉴 ", "*" * 7)
            print("1. 농산물 사기")
            print("2. 농산물 빼기")
            print("3. 구입한 농산물 보기")
            print("9. 메인으로 돌아가기")
            selNum2 = input("메뉴 번호 선택: ")

            if selNum2.isdigit() :
                selNum2 = int(selNum2)
            else :
                print("숫자로 다시 입력해주세요.")
                continue
            
            if selNum2 == 1:
                
                break
            elif selNum2 == 2:
                
                break
            elif selNum2 == 9:
                break
            else :
                print("잘못 입력하였습니다. 다시 입력해주세요.")
                break
            
    elif selNum == 9:
        print("종료합니다.")
        break
    else :
        print("잘못 입력하였습니다. 다시 입력해주세요.")
        break

# conn.commit()
# conn.close()