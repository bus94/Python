# # 폴더명: class
# # 파일명: classEx1.py

# class Dog:
#     def info(self):
#         print("멍멍")

# # 파이썬에서는 메서드 첫 번째 매개변수는 자기 자신의 주소값을 받아야 된다. (self)
# # 클래스명()
# dog = Dog()
# dog.info()

# # 변수
# # 클래스 변수 (static)
# # 인스턴스 변수 (객체 생성시 각각 생성)

# class Cat:
#     # 생성자 (기본 생성자)
#     def __init__(self):
#         pass

# class Cat2:
#     # 클래스 변수
#     # 여러 클래스들끼리 공유해서 데이터를 사용

#     # 매개 변수 받는 생성자
#     def __init__(self, name):
#         self.name = name
#         print("Cat2 생성한 이름:", name)

# class Cat3:
#     # 생성자 초기화 함수
#     # 클래스 오버로딩 지원 x
#     # 기본값 설정, 가변인자 *변수명
#     def __init__(address, age):
#         # 객체 안에 각각 저장
#         address.age = age
#         print("Cat3 생성한 나이:", age)

# cat1 = Cat()
# # 객체를 생성할 때 self 변수에 자동으로 객체의 주소값이 들어가기 때문에 매개변수는 self 다음부터 들어가면 된다.
# cat2 = Cat2("나비")
# cat3 = Cat3(10)

class User:
    # 생성자
    # 이메일, 비밀번호(필수), 이름, 핸드폰(선택)
    def __init__(self, email, passwd, name=None, phone=None):
        self.email = email
        self.passwd = passwd
        # None 파이썬에서 아무 값도 없다
        self.name = name
        self.phone = phone

    # toString과 비슷한 함수
    def __str__(self):
        return f"User(email={self.email}, passwd={self.passwd}, name={self.name}, phone={self.phone})"
        
# __**__
# 파이썬 클래스에서 특별하게 동작하는 메서드
# 연산자 오버로딩

# __init__ : 생성자 객체가 생성될 때 자동으로 호출되고 인스턴스 변수를 초기화

# __str__ : 객체 안에 있는 멤버들을 문자열 반환
user1 = User("ex@g.c","1234","seohee")
user2 = User("ex@g.c","1234","seohee","01012341234")

# __str__() 함수를 생성하면 문자열을 리턴받아서 출력한다.
# 만약 __str__() 하지 않으면 <__main__.User object at 0x00000210C6DA2270> 라는 객체의 주소값을 출력한다.
print(user1)
print(user2)

