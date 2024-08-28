# tkinEx3.py

# 버튼을 클릭하면 간단한 메시지 창이 나오는 프로그램

from tkinter import *
# import tkinter.messagebox as box # 팝업창
from tkinter.messagebox import showinfo

# 함수를 정의할 때 클래스 안에 선언하는 것이 아니므로 매개변수가 없어도 된다.
def myFunc():
    # tkinter.messagebox.showinfo('버튼 클릭', '버튼을 클릭했다')
    # box.showinfo('버튼 클릭', '버튼을 클릭했다')
    showinfo('버튼 클릭', '버튼을 클릭했다')

def myFunc2():
    if chk.get() == 0:
        showinfo("", "체크버튼 off")
    else:
        showinfo("", "체크버튼 on")

def myFunc3():
    value = myVar.get()

    if value == "사과":
        result.configure(text="사과")
    elif value == "망고":
        result.configure(text="망고")
    else:
        result.configure(text="앵두")

win = Tk()

# 메인
win.geometry('500x200')

# 버튼 생성
btn1 = Button(win, text='클릭하세요', command=myFunc)

# 체크박스
# IntVar()
# BooleanVar()
chk = IntVar()
cb1 = Checkbutton(win, text='클릭해', variable=chk, command=myFunc2)

# 라디오 버튼
# 예외적인 상황
# 1. 처음 시작했을 때 전체 선택
#       StringVar() 괄호 안에 어떤 설정
# 2. deselect()
myVar = StringVar()
rb1 = Radiobutton(win, text="사과", variable=myVar, value="사과", command=myFunc3)
rb2 = Radiobutton(win, text="망고", variable=myVar, value="망고", command=myFunc3)
rb3 = Radiobutton(win, text="앵두", variable=myVar, value="앵두", command=myFunc3)

result = Label(win, text="선택한 과일:")

# 윈도우에 추가
# pack() 왼쪽, 오른쪽 정렬 가능
# (side=LEFT, RIGHT, TOP, BOTTOM)
# padx, y = 픽셀 단위 (상하좌우 패딩)
btn1.pack()
cb1.pack()
rb1.pack()
rb2.pack()
rb3.pack()
result.pack()

win.mainloop()