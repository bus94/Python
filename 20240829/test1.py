# GUI 데이터 입력

import pymysql
from tkinter import *
# from ttkthemes import ThemedTk
# pip install ttkthemes

def insert():
    pass

def select():
    pass

# mysql 연결
conn = pymysql.connect(host='localhost', user='root', password='1234', db='guitest', charset='utf8')
print(conn)
cur = conn.cursor()
# guitest 테이블 생성
# cur.execute(
#  '''
#      create table guitest(
#          id varchar(10),
#          name varchar(10),
#          email varchar(50),
#          birthYear int
#      )
#  '''
# )

window = Tk()
# 창 크기
window.geometry("780x500")
# 창 제목
window.title("GUI 데이터 입력")
# 창 크기 조절 x
# window.resizable(False, False) 

# 프레임
frameTop = Frame(window)
frameMain = Frame(window)
frameId = Frame(frameMain, relief="solid", bd=1, height=200)
frameName = Frame(frameMain, relief="solid", bd=1, height=200)
frameEmail = Frame(frameMain, relief="solid", bd=1, height=200)
frameBirthYear = Frame(frameMain, relief="solid", bd=1, height=200)


# 입력 받는 컴포넌트
idEntry = Entry(frameTop, width=20)
nameEntry = Entry(frameTop, width=20)
emailEntry = Entry(frameTop, width=20)
birthYearEntry = Entry(frameTop, width=20)

insertBtn = Button(frameTop, text="입력", command=insert)
selectBtn = Button(frameTop, text="조회", command=select)

showId = Label(frameId, text="사용자ID")
showName = Label(frameName, text="사용자이름")
showEmail = Label(frameEmail, text="이메일")
showBirthYear = Label(frameBirthYear, text="출생연도")


# 컴포넌트 추가
idEntry.grid(row=0, column=0, padx=10, pady=5)
nameEntry.grid(row=0, column=1, padx=10, pady=5)
emailEntry.grid(row=0, column=2, padx=10, pady=5)
birthYearEntry.grid(row=0, column=3, padx=10, pady=5)
insertBtn.grid(row=0, column=4, padx=10, pady=5)
selectBtn.grid(row=0, column=5, padx=10, pady=5)
showId.grid(row=0, column=0)
showName.grid(row=0, column=0)
showEmail.grid(row=0, column=0)
showBirthYear.grid(row=0, column=0)

frameTop.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
frameMain.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
frameMain.columnconfigure(0, weight=1)
frameMain.columnconfigure(1, weight=1)
frameMain.columnconfigure(2, weight=1)
frameMain.columnconfigure(3, weight=1)

frameId.grid(row=0, column=0, padx=1, pady=5, sticky="ew")
frameName.grid(row=0, column=1, padx=1, pady=5, sticky="ew")
frameEmail.grid(row=0, column=2, padx=1, pady=5, sticky="ew")
frameBirthYear.grid(row=0, column=3, padx=1, pady=5, sticky="ew")


window.mainloop()
conn.commit()
conn.close()
