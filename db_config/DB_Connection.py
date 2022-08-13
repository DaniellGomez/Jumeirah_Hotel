import sqlite3
from sqlite3 import Error

def slq_connection():
    try:
        conn = sqlite3.connect('./Jumeirah_Hotel/database/JUMEIRAH.db', isolation_level=None)
        cur = conn.cursor()
        return conn , cur
    except Error:
        print(Error)
    
