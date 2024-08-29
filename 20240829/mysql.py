import pymysql


def insertDB(id,name,email,year):
    
    conn=pymysql.connect(host='localhost',user='root',password='1234',db='pythonTest',charset='utf8')

    cur= conn.cursor()
    result=cur.execute(f"INSERT INTO listtable VALUES('{id}', '{name}', '{email}','{year}')")
    
    print('리턴값:',result)
    conn.commit()

    conn.close()
    return result


def selectDB():
    
    conn=pymysql.connect(host='localhost',user='root',password='1234',db='pythonTest',charset='utf8')

    cur= conn.cursor()
    cur.execute('select * from listtable')
    list=[]
    for row in cur.fetchall():
        list.append(row)
    conn.commit()

    conn.close()
    
    return list