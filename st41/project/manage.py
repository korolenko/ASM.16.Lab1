import sqlite3
import sys
sys.path.append("./project/database");
import db
try: db.crete_users_table()
except sqlite3.OperationalError: print (u"manage: USERS table..OK")
else: print(u"manage: Table USERS created ")
db.all_users()
def menu(func):
    print ("""
    1.11111
    2.dod elem
    3.gt sp
    4.wr sr fl
    5.rd sp in fl
    6.del sp
    """)
    return func