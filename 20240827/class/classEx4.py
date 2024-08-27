# classEx4.py

# class Person:
#     def __init__(self, name=None, age=None):
#         self.name = name
#         self.age = age
#         print(f"부모: {self.name}")
    
#     # 학생 정보를 출력
#     def info(self):
#         print("이름:", self.name)
#         print("나이:", self.age)

# class Student(Person):
#     def __init__(self, name="", age=0, hakbun=0):
#         super().__init__(name, age)
#         self.hakbun = hakbun
#         print("자식 클래스")

#     def info(self):
#         print("학번:", self.hakbun)
#         super().info()

# # 파이썬에서는 오버라이딩은 지원(사용)
# # 부모클래스에서 작성한 메서드를 재정의해서 사용할 수 있다. 별다른 키워드 없이!

# # 객체 생성 시
# # 자식 클래스에서 객체 생성시 부모클래스 객체를 생성하는데 매개변수 받는 생성자
# stu = Student()
# stu2 = Student("이서희",20,1004)
# print(stu2.name)
# print(stu2.age)

# print()
# stu.info()
# stu2.info()

# 파이썬은 다중 상속이 가능하다.
class A:
    def action(self):
        print("A action()")
    
class B:
    def action(self):
        print("B action()")

# 똑같은 메서드가 있는 경우 먼저 상속받은 A클래스의 action이 우선적으로 호출된다.
# 그러나 자신이 같은 메서드를 가지고 있다면 자신의 메서드가 우선적으로 호출된다.
class C(A, B):
    pass

class D(A, B):
    def action(self):
        print("D action()")

# 객체 생성
c1 = C()
c1.action()

d1 = D()
d1.action()

# 클래스 상속 구조
# Object 클래스는 모든 클래스가 자동으로 상속
# 다형성의 개수
print(C.__mro__) # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(C.mro()) # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

class A:
    def __init__(self):
        print("A클래스")
    
class B(A):
    def __init__(self):
        super().__init__()
        print("B클래스")

class C(A):
    def __init__(self):
        super().__init__()
        print("C클래스")

class D(B,C):
    def __init__(self):
        super().__init__()
        print("D클래스")
        
# B,C 각각클래스 인데 부모는 A
# B의 부모가 C클래스 X
a = A()
print()
b = B()
print()
c = C()
print()
d = D()
print(D.mro())
# d의 출력 
# A클래스
# C클래스
# B클래스
# D클래스
# D클래스가 생성될 때 부모인 B, C를 생성한다. 두 번째로 생성된 C가 부모인 A를 호출하고 C가 출력, 그리고 B, D 순서로 출력되는 것이다. (B와 C가 같은 부모를 가지는 경우)
# 만약 B와 C가 다른 부모를 가지면 B의 부모까지 호출되면 C가 호출되지 않고 B가 호출된다.