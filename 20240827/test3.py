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
class Account:
    def __init__(self, name, accNum):
        self.name = name
        self.accNum = accNum

    

