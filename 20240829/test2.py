from tkinter import * 
from tkinter.messagebox import showinfo
import pymysql
import tkinter.ttk

conn = pymysql.connect(host='localhost', user='root', password='1234', db='guitest', charset='utf8')
print(conn)
cur = conn.cursor()
def insertDB(id, name, email, year):
    cur.execute(f"INSERT INTO guitest VALUES({id}, {name}, {email}, {year})")
def selectDB():
    cur.execute("SELECT * FROM guitest")

def insert():
    id=entry.get()
    name=entry2.get()
    email=entry3.get()
    year=entry4.get()
    result= insertDB(id,name,email,year)
    if result > 0:
        showinfo('','입력성공')
    else:
        showinfo('','실패')
def select():
    treeValueList=[]
    treeValueList=selectDB()
    print("treeValueList:", treeValueList)
    for i in range(len(treeValueList)):
        treeview.insert("", "end", text="", values=treeValueList[i], iid=i)
        
    
win= Tk()
win.geometry('600x500')

entry=Entry(win,width=10)
entry.pack(pady=5,padx=20,side='left',anchor='n')
entry.insert(0,'ID입력')

entry2=Entry(win,width=10)
entry2.pack(pady=5,padx=20,side='left',anchor='n')
entry2.insert(0,'이름입력')

entry3=Entry(win,width=10)
entry3.pack(pady=5,padx=20,side='left',anchor='n')
entry3.insert(0,'이메일입력')

entry4=Entry(win,width=10)
entry4.pack(pady=5,padx=20,side='left',anchor='n')
entry4.insert(0,'출생년도입력')

btn = Button(win,text='입력',command=insert)
btn.pack(pady=5,padx=5,side='left',anchor='n')

btn2 = Button(win,text='조회',command=select)
btn2.pack(pady=5,padx=5,side='left',anchor='n')

listbox=Listbox(win,height=0,width=0)
listbox.place(x=50,y=50)

treeview = tkinter.ttk.Treeview(win, 
    column=["id", "name", "email","year"], 
    displaycolumns=["id", "name", "email","year"])
treeview.place(x=50,y=50)

treeview.column("id", width=100, anchor="center")
treeview.heading("id", text="사용자 ID", anchor="center")
 
treeview.column("name", width=100, anchor="center")
treeview.heading("name", text="사용자 이름", anchor="center")
 
treeview.column("email", width=100, anchor="center")
treeview.heading("email", text="이메일", anchor="center")

treeview.column("year", width=100, anchor="center")
treeview.heading("year", text="출생연도", anchor="center")
 
# 컬럼제목만
treeview["show"] = "headings"
win.mainloop()