#파일명: test3.py

'''
# 252
class Human:
    pass

# 253
areum = Human()
print(areum)

# 254
class Human2:
    def __init__(self):
        print("응애응애")
h1 = Human2()

# 255
class Human3:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"이름: {self.name}, 나이: {self.age}, 성별: {self.gender}"

    def who(self):
        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.gender))

    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("정상적으로 수정되었습니다.")


areum1 = Human3("아름", 25, "여자")
areum2 = Human3("조아름", 25, "여자")

# 256
print(areum2.__str__())

# 257
areum2.who()

# 258
areum3 = Human3("모름", 0, "모름")
print(areum3)
areum3.setInfo("아름", 25, "여자")
print(areum3)
'''
# 271
import random as r
class Account:
    # 클래스 변수
    acc_count = 0

    def __init__(self, name, accNum=0):
        self.name = name
        self.accNum = accNum

        num1 = r.randint(0,999)
        num2 = r.randint(0,99)
        num3 = r.randint(0,999999)

        # zfill(width)
        # - 문자열의 길이를 지정하고 데이터를 채운다 만약 부족한 길이는 0으로 채운다.
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.accNum = num1 + '-' + num2 + '-' + num3
        print("계좌번호:", self.accNum)

        # 클래스변수 증가
        Account.acc_count += 1

acc = Account("카카오은행")
print("현재 계좌 개수:" , Account.acc_count,'개')

# 261 ~ 264
class Stock:
    pass

class Stock2:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    # toString() 메서드랑 똑같다
    # return 타입으로 str 타입으로 넘어가야하는데 print() 실행하고 문자열로 넘겨주는 리턴 타입이 맞지 않아서 에러
    def __str__(self):
        return f"{self.name},{self.code}"

    def set_name(self,name):
        self.name = name

    # 코드 수정하는 메서드
    def set_code(self, code):
        pass

st = Stock2("삼성전자", "005930")
print(st)

st.set_name("현대")
print(st)

# 객체지향 언어 접근제한자 
# public ,private 작성하지 않는다. 지원X
class MyClass:
    def __init__(self):
        # 비공개!
        self.__name = "private"

    def getName(self):
        return self.__name
    
my = MyClass()

# print(my.name)
# AttributeError: 'MyClass' object has no attribute 'name'
# 예외 발생

print(my.getName())

# Protected 
# 자신클래스와  상속한 자식클래스만 접근이 가능하도록! 
# _변수명
