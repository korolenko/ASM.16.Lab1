import sqlite3
import sys
sys.path.append("./project");
import db
try: db.crete_users_table()
except sqlite3.OperationalError: print (u"manage: USERS table..OK")
else: print(u"manage: Table USERS created ")
db.all_users()
def menu():
    """TODO"""
    print ("""
    1.Add
    2.Edit
    3.Delite
    4.ALL
    5.rd sp in fl
    6.clean table
    """)
    return