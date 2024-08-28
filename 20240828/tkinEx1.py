# tkinEx1.py

# tkinter GUI 프로그래밍
# 파일명: tkinter.py 로 하면 tkinter 프로그래밍과 충돌이 나므로 해당 라이브러리를 가져오려면 파일명과 달라야한다.

from tkinter import *

# Tk() 기본적으로 윈도우창을 반환한다.
# 제일 아래에 깔리는 윈도우창 (자바 스윙과 비슷!)
root = Tk()

# 이 부분에서 컴포넌트들을 배치
root.title("처음 만든 윈도우")   # 제목
root.geometry("500x200")        # 창 크기
root.resizable(width=False, height=False)                # 자동조절

root.mainloop()

