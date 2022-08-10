import sqlite3
from sqlite3 import Error
import db_config.DB_Connection as db

def sql_insert_huesped(doc, nombre, email, rol, password):
    try:
        strsql="INSERT INTO pass_role(num_doc, password, user_role)VALUES('"+ doc +"', '" + password + "', '"+ rol+"');"
        print(strsql)
        cur, conn = db.slq_connection()
        cur.execute(strsql)
        conn.commit()
        strsql="INSERT INTO huespedes(num_doc, nombre, email)VALUES('"+ doc +"','"+ nombre +"','"+ email +"' );"
        print(strsql)
        cur.execute(strsql)
        conn.commit()
        conn.close()
    except Error:
        print(Error)

def sql_get_huesped():
    try:
        strsql="SELECT * FROM huespedes;"
        print(strsql)
        cur, conn = db.slq_connection()
        cur.execute(strsql)
        supAdministrators = cur.fetchall()
        conn.close()
        return supAdministrators
    except Error:
        print(Error)
    

def sql_edit_huesped(doc, nombre, email):
    try:
        strsql="UPDATE huespedes SET nombre = '"+ nombre +"', email = '"+ email +"' WHERE num_doc = '"+ doc +"';"
        print(strsql)
        cur, conn = db.slq_connection()
        cur.execute(strsql)
        conn.commit()
        conn.close()
    except Error:
        print(Error)

def sql_delete_huesped(doc):
    try:
        strsql="DELETE FROM huespedes WHERE num_doc = '"+ doc +"';"
        print(strsql)
        cur, conn = db.slq_connection();
        cur.execute()
        conn.commit()
        conn.close()
    except Error:
        print(Error)