class Farm:
    def __init__(self, kind):
        self.kind = kind

    def __str__(self):
        return f"(kind: {self.kind})"
    
class Fruit:
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def __str__(self):
        return f"(name: {self.name})"
    
class Vegetable:
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def __str__(self):
        return f"(name: {self.name})"
    
class Nut:
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def __str__(self):
        return f"(name: {self.name})"

farmList = []
fruitList = []
vegetableList = []
nutList = []
dictFruit = {}
dictVeget = {}
dictNut = {}

def addNewKind():
    print("1. 과일 / 2. 채소 / 3. 견과")
    sel = int(input("추가할 종류 번호: "))
    name = input("이름 : ")
    amount = int(input("수량 : "))

    if sel == 1:
        fruit = Fruit("과일", name)
        dictFruit = {"이름": fruit.name, "수량": amount}
    elif sel == 2:
        vegetable = Vegetable("채소", name)
        dictVeget = {"이름": vegetable.name, "수량": amount}
    elif sel == 3:
        nut = Nut("견과", name)
        dictNut = {"이름": nut.name, "수량": amount}

    

while True:
    print("=" * 10, " 쌍용 마트 ", "=" * 10)
    print("*" * 7, " 메인 메뉴 ", "*" * 7)
    print("1. 직원 메뉴")
    print("2. 손님 메뉴")
    print("9. 종료")
    selNum = int(input("메뉴 번호 선택: "))

    if selNum.isdigit() :
        int(selNum)
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
            selNum1 = int(input("메뉴 번호 선택: "))
            
            if selNum1 == 1:
                
                break
            elif selNum1 == 2:
                
                break
            elif selNum1 == 9:
                break
            else :
                print("잘못 입력하였습니다. 다시 입력해주세요.")
                break

    elif selNum == 2:
        while True:
            print("*" * 7, " 고객 메뉴 ", "*" * 7)
            print("1. 농산물 사기")
            print("2. 농산물 빼기")
            print("3. 구입한 농산물 보기")
            print("9. 메인으로 돌아가기")
            selNum2 = int(input("메뉴 번호 선택: "))
            
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