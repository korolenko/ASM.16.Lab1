import sqlite3
import sys
sys.path.append("./project")
import user
database = "./project/dbfile"
connect = sqlite3.connect(database=database,isolation_level="EXCLUSIVE")
cc = connect.cursor()
def all_users():
    for row in cc.execute("select * from USERS"):
        print (row)
def crete_users_table():
    cc.execute("create table USERS (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, hash TEXT)")
    connect.commit()
    return
def chec_user_in_db(username):
    for row in cc.execute("SELECT * FROM USERS WHERE username=?", (username,)):
        if (row[1] == username):
            print ("db.chec_user_in_db: True")
            return  True
    print("db.chec_user_in_db: False")
    return False
def new_id_user():
    for row in cc.execute("SELECT MAX(id)  FROM USERS"):
        try:return row[0]+1
        except TypeError: return 1
        else: return row[0]+1
def add_user():
    username = input("Username: ")
    if  not(chec_user_in_db(username)):
        password = input("Password: ")
        newuser = user.User(username, password)
        cc.execute("insert into USERS values (?,?,?)", (newuser.id,newuser.username,newuser.hash))
        connect.commit()
        print("add_user: OK")
        newuser.info()
    else:
        print ("add_user: ERROR")
    return
def clean_table():
    cc.execute("DELETE FROM USERS  ")
    connect.commit()
    pass