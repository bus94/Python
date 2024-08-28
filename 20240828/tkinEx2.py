# 파일명: tkinEx2.py

from tkinter import *

win = Tk()
win.geometry("500x200") # 창 크기를 설정하지 않으면 컴포넌트 크기에 맞춰서 자동으로 크기가 지정된다.

# 라벨
# 문자를 표현할 수 있는 컨트롤을 의미함
# Label(어디 윈도우, 옵션...)
label1 = Label(win, text="python")

# 배치 윈도우 창에 추가
label1.pack()

label2 = Label(win, text="python 열심히", font=("궁서체", 30), fg="red")
label2.pack()

label3 = Label(win, text="python 코딩 중", bg="blue", width=20, height=5)
label3.pack()

# pack()
# 한줄에 하나씩 가운데 정렬
# x버튼을 클릭할 때까지 반복한다.
win.mainloop()