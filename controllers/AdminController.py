import sqlite3
from sqlite3 import Error
import db_config.DB_Connection as db

def sql_insert_admin(doc, nombre, email, rol, password):
    try:
        strsql="INSERT INTO pass_role(num_doc, password, user_role) VALUES(?,?,?)"
        val=(doc,password,rol)
        print(strsql)
        conn, cur = db.slq_connection()
        cur.execute(strsql,val)
        conn.commit()
        strsql="INSERT INTO administradores(num_doc, nombre, email) VALUES(?,?,?)"
        val=(doc,nombre,email)
        print(strsql)
        cur.execute(strsql,val)
        conn.commit()
        conn.close()
    except Error:
        print(Error)

def sql_get_admin():
    try:
        strsql="SELECT * FROM administradores;"
        print(strsql)
        conn, cur = db.slq_connection()
        cur.execute(strsql)
        supAdministrators = cur.fetchall()
        conn.close()
        return supAdministrators
    except Error:
        print(Error)
    

def sql_edit_admin(doc, nombre, email):
    try:
        strsql="UPDATE administradores SET nombre = ?, email = ? WHERE num_doc = ?"
        val=(nombre,email,doc)
        print(strsql)
        conn, cur = db.slq_connection()
        cur.execute(strsql,val)
        conn.commit()
        conn.close()
    except Error:
        print(Error)

def sql_delete_admin(doc):
    try:
        strsql="DELETE FROM administradores WHERE num_doc = ?"
        val=(doc)
        print(strsql)
        conn, cur = db.slq_connection();
        cur.execute(strsql,[val])
        conn.commit()
        conn.close()
    except Error:
        print(Error)