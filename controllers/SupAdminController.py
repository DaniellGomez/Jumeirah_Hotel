import sqlite3
from sqlite3 import Error
import db_config.DB_Connection as db

def sql_insert_new(doc, nombre, email):
    strsql="INSERT INTO superadministradores(num_doc, nombre, email)VALUES('"+ doc +"','"+ nombre +"','"+ email +"' );"
    print(strsql)
    cur, conn = db.slq_connection()
    cur.execute(strsql)
    conn.commit()
    conn.close()

def sql_get():
    strsql="SELECT * FROM superadministradores;"
    print(strsql)
    cur, conn = db.slq_connection()
    cur.execute(strsql)
    supAdministrators = cur.fetchall()
    conn.close()
    return supAdministrators

def sql_edit_supAdmin(doc, nombre, email):
    strsql="UPDATE superadministradores SET nombre = "+ nombre +", email = "+ email +" WHERE num_doc = "+ doc +";"
