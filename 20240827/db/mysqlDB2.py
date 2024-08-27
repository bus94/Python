# 폴더명: db
# 파일명: mysqlDB2.py

# from 파일명 import * (전부)
# from 파일명 import 함수명, 필요한 클래스명

from random import randint

import pymysql as p

# 1. mysql 연결하기 connect()
conn = p.connect(host='localhost', user='root', password='1234', db='pythonTest', charset='utf8')

# 2. DB 조작 cursor()
cur = conn.cursor()

# select 일 경우에는 저장할 필요x
cur.execute('''
select * from userTable
''')

# fetchall()
# sql에서 조회된 모든 내용을 가져오는 메서드
for row in cur.fetchall():
    # print(row) # 튜플 자료형으로 가져온다. (여러 데이터들을)
    print("아이디 | 이름 | 이메일 | 생년월일")
    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    print()

conn.close()

# 오라클 디비 연결
# pip install oracledb
# import oracledb
# user, password, dsn(Database Source Name)
# dsn = "호스트이름:port/DB명"

