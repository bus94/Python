import requests
from bs4 import BeautifulSoup
from tkinter import *
import tkinter.ttk


html = requests.get("https://finance.naver.com/")
soup = BeautifulSoup(html.text, 'html.parser')
# print(html)

tab_area = soup.find('ul', class_='tab_area').find_all('span')
for tab in tab_area:
    print(f"{tab.text}")

print(f"{tab_area[0].text}")
topItems1 = soup.find('tbody', id='_topItems1').find_all('th')
for i in range(0, 10):
    print(f"{topItems1[i].text}")

print(f"{tab_area[1].text}")
topItems2 = soup.find('tbody', id='_topItems2').find_all('th')
for i in range(0, 10):
    print(f"{topItems2[i].text}")

print(f"{tab_area[2].text}")
topItems3 = soup.find('tbody', id='_topItems3').find_all('th')
for i in range(0, 10):
    print(f"{topItems3[i].text}")

print(f"{tab_area[3].text}")
topItems4 = soup.find('tbody', id='_topItems4').find_all('th')
for i in range(0, 10):
    print(f"{topItems4[i].text}")


# tkinter
win = Tk()

win.title("주식 Top 종목")
win.geometry("800x600")

notebook = tkinter.ttk.Notebook(win, width=700, height=400)
notebook.pack(pady=50)

# 거래상위 탭
tab1 = Frame(win)
notebook.add(tab1, text=f"{tab_area[0].text}")
for i, items in enumerate(topItems1):
    label = Label(tab1, text=f"{items.text}")
    label.pack(pady=10, anchor="w")

# 상승 탭
tab2 = Frame(win)
notebook.add(tab2, text=f"{tab_area[1].text}")
for i, items in enumerate(topItems2):
    label = Label(tab2, text=f"{items.text}")
    label.pack(pady=10, anchor="w")

# 하락 탭
tab3 = Frame(win)
notebook.add(tab3, text=f"{tab_area[2].text}")
for i, items in enumerate(topItems3):
    label = Label(tab3, text=f"{items.text}")
    label.pack(pady=10, anchor="w")

# 시가총액 상위 탭
tab4 = Frame(win)
notebook.add(tab4, text=f"{tab_area[3].text}")
for i, items in enumerate(topItems4):
    label = Label(tab4, text=f"{items.text}")
    label.pack(pady=10, anchor="w")

win.mainloop()