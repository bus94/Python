
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"(x: {self.x}, y: {self.y})"

class Circle(Point):
    pi = 3.141592

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f"(x: {self.x}, y: {self.y}, radius: {self.radius})"
    
    # 원의 면적 
    def calcAreaCircle(self):
        area = Circle.pi * self.radius **2
        return area
    
    # 원의 둘레
    def calcCircum(self):
        circum = Circle.pi * self.radius * 2
        return circum
    
class Rectangle(Point):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def __str__(self):
        return f"(x: {self.x}, y: {self.y}, height: {self.height}, width: {self.width})"
    
    # 사각형의 면적
    def calcAreaRectangle(self):
        area = self.height * self.width
        return area
    
    # 사각형의 둘레
    def calcPerimeter(self):
        circum = 2 * (self.width + self.height)
        return circum

while True:
    print("=" * 5, " 메뉴 ", "=" * 5)
    print("1. 원")
    print("2. 사각형")
    print("9. 끝내기")
    selNum = input("메뉴 번호: ")

    if selNum.isdigit() :
        int(selNum)
    else :
        print("숫자로 다시 입력해주세요.")
        continue

    if selNum == 1:
        while True:
            print("=" * 5, " 원 메뉴 ", "=" * 5)
            print("1. 원 둘레")
            print("2. 원 넓이")
            print("9. 메인으로")
            selNumCir = int(input("메뉴 번호 : "))
            
            if selNumCir == 1:
                x = int(input("x 좌표 : "))
                y = int(input("y 좌표 : "))
                radius = int(input("반지름 : "))
                c1 = Circle(x, y, radius)
                print(f"둘레 : {x}, {y}, {radius} / {c1.calcCircum()}")
                break
            elif selNumCir == 2:
                x = int(input("x 좌표 : "))
                y = int(input("y 좌표 : "))
                radius = int(input("반지름 : "))
                c2 = Circle(x, y, radius)
                print(f"면적 : {x}, {y}, {radius} / {c2.calcAreaCircle()}")
                break
            elif selNumCir == 9:
                break
            else :
                print("번호를 다시 입력해주세요.")
                pass

    elif selNum == 2:
        while True:
            print("=" * 5, " 메뉴 ", "=" * 5)
            print("1. 사각형 둘레")
            print("2. 사각형 넓이")
            print("9. 메인으로")
            selNumRec = int(input("메뉴 번호 : "))
            
            if selNumRec == 1:
                x = int(input("x 좌표 : "))
                y = int(input("y 좌표 : "))
                height = int(input("높이 : "))
                width = int(input("너비 : "))
                t1 = Rectangle(x, y, height, width)
                print(f"둘레 : {x}, {y}, {height}, {width} / {t1.calcPerimeter()}")
                break
            elif selNumRec == 2:
                x = int(input("x 좌표 : "))
                y = int(input("y 좌표 : "))
                height = int(input("높이 : "))
                width = int(input("너비 : "))
                t2 = Rectangle(x, y, height, width)
                print(f"면적 : {x}, {y}, {height}, {width} / {t2.calcAreaRectangle()}")
                break
            elif selNumRec == 9:
                break
            else :
                print("번호를 다시 입력해주세요.")
                pass
            
    elif selNum == 9:
        print("종료합니다.")
        break
    else :
        print("1, 2, 9번 중에 입력해주세요.")
        continue