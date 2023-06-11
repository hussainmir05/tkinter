import sqlite3

def create_db():
    con=sqlite3.connect(database='rms.db')
    cur=con.cursor()


    # cid,name,duration,charges,description
    cur.execute('CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text, charges text,description text)')
    con.commit()
    # rollnbr,name,email,gender,dob,contact,admission,course,state,city,pin,adress
    cur.execute('CREATE TABLE IF NOT EXISTS student(rollnbr INTEGER PRIMARY KEY AUTOINCREMENT ,name  text,email  text,gender  text,dob  text,contact  text,admission  text,course  text,state  text,city  text,pin  text,adress text)')
    con.commit()
    

    cur.execute('CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT ,rollnbr  text,name  text,course text,ob_marks text,total_marks text,per text)')
    con.commit()
create_db()