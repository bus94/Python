from tkinter import *

# ListBox

root = Tk()
root.geometry("500x500")

list1 = Listbox(root, bg="yellow", width=50, height=20)
list1.pack()

# listbox 추가할 때는 insert()
for i in range(10): # 0~9까지
    # 데이터 값을 맨 마지막에 추가
    # END : 맨 마지막 인덱스
    # insert(index, value)
    list1.insert(END, i)

# 문자열 추가하기
strings = ['python', 'Tkinter', 'listbox']
for string in strings:
    list1.insert(END, string)

root.mainloop()

# 1. listbox 이용해서 데이터를 저장
# 2. treeview 컴포넌트
# 3. tkinter 모듈 안에 ttk 라이브러리로 포함
