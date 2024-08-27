# 파일명: classEx3.py
# 클래스 변수
class Student:
    # 클래스 변수: 모든 학생들의 학번을 관리
    next_id = 1

    def __init__(self, name):
        self.name = name
        self.student_id = Student.next_id
        Student.next_id += 1 # 다음 학생 학번 증가

    def __str__(self):
        return f"({self.student_id}번 이름:{self.name})"
class StudentManager:
    def __init__(self):
        self.stuList = []

    def add_student(self, name):
        stu = Student(name)
        self.stuList.append(stu)
        print(f"학생 추가됨: {stu}")

    def remove_student(self, student_id):
        for student in self.stuList:
            if student.student_id == student_id:
                self.stuList.remove(student)
                print(f"학생 삭제됨: {student}")

    def find_student(self, student_id):
        for student in self.stuList:
            if student.student_id == student_id:
                print(f"학생 찾음: {student}")
            else :
                print("찾는 학생 없음!")
    
    def list_student(self):
        # 학생 목록을 출력
        for student in self.stuList:
            print(student)

# 학생들 관리하는 클래스 객체 생성
ma = StudentManager()

# 학생들 추가하는 내용
ma.add_student("seohee")
ma.add_student("hee")
ma.add_student("Bob")

# 학생 찾기 seohee 있니?
ma.find_student(1)
ma.find_student(2)

# 학생 삭제 Bob 삭제!
ma.remove_student(3)

# 학생 목록
ma.list_student()


