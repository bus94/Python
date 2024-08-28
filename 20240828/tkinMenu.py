# 파일명: tkinMenu.py

# 윈도우창에 메뉴 만들기

from tkinter import *
from tkinter import messagebox, filedialog

# askopenfilename(속성)
# parent = 윈도우창 or 프레임
# filetypes=(("모든 파일", "*.*"), ("텍스트 파일", "*.txt")) 튜플 형태
def open_file(event=None):
    file = filedialog.askopenfilename()

    if file:
        messagebox.showinfo("파일열기", f"선택된 파일: {file}")

def quit_app(event=None):
    root.quit() # root.mainloop() 중지시킴
    # destory() 위에 quit() 메서드와 차이점!

root = Tk()
root.geometry("400x400")

# 메뉴바를 생성한다.
mainMenu = Menu(root)
root.config(menu=mainMenu)

# 상위메뉴
fileMenu = Menu(mainMenu, tearoff=False) # tearoff=False 또는 0 모두 적용 가능!
mainMenu.add_cascade(label="파일", menu=fileMenu)

editMenu = Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="편집", menu=editMenu)

viewMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="보기", menu=viewMenu)

# 하위메뉴
fileMenu.add_command(label="열기", accelerator="Ctrl+O")
fileMenu.add_separator() # 선
fileMenu.add_command(label="종료")

editMenu.add_command(label="잘라내기")
editMenu.add_separator()
editMenu.add_command(label="복사")
editMenu.add_separator()
editMenu.add_command(label="붙여넣기")

viewMenu.add_command(label="확대/축소")
viewMenu.add_separator()
viewMenu.add_command(label="상태 표시줄")
viewMenu.add_separator()
viewMenu.add_command(label="자동 줄 바꿈")

# 이벤트
# 모든 컴포넌트 실행 중에도 단축키를 사용할 수 있도록
# 단축키 이벤트!
root.bind_all("<Control-o>", open_file)
root.bind_all("<Control-q>", quit_app)

root.mainloop()
