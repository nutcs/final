import sqlite3

# เชื่อม DB
conn = sqlite3.connect('db/ณัฐพล_1650704388.db')
cursor = conn.cursor()

#ดูข้อมูล
def listenDB():
    # คำสั่ง sql หาข้อจาก table students
    sql = 'select * from login'
    # รัน sql
    cursor.execute(sql)
    # โชว์ข้อมูล
    showDb = cursor.fetchall()
    print(showDb,'\n')

#เพิ่มข้อมูล
def addData_DB():
    sql = "insert into login values(?,?,?,?,?,?)"
    cursor.execute(sql,[1650704388, 'Nutthapon1 Salangsing1', 1, 3.08,'nut2', 'n2'])
    conn.commit()

#อัปเดตข้อมูล
def updateDB():
    # std_id  /  first_name  /  lastname  /  gender  /  year  /  username  / password
    #update students set password=? username=? where std_id=?;
    sql = """
    update students set password=? where std_id=?;
    """
    cursor.execute(sql,['ng',1])
    conn.commit()

#ลบข้อมูล
def deleteDB():
    sql = "delete from students where std_id=?;"
    cursor.execute(sql,[1])
    conn.commit()


#listenDB()
#updateDB()
#deleteDB()
addData_DB()
listenDB()
conn.close()