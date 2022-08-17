import sqlite3
from sqlite3 import Error
import db_config.DB_Connection as db

def sql_insert_supAdmin(doc, nombre, email, rol, password):
    try:
        strsql="INSERT INTO pass_role(num_doc, password, user_role) VALUES(?,?,?)"
        val=(doc,password,rol)
        print(strsql)
        conn, cur = db.slq_connection()
        cur.execute(strsql,val)
        conn.commit()
        strsql="INSERT INTO superadministradores(num_doc, nombre, email) VALUES(?,?,?)"
        val=(doc,nombre,email)
        print(strsql)
        cur.execute(strsql,val)
        conn.commit()
        conn.close()
    except Error:
        print(Error)

def sql_get_supAdmin():
    try:
        strsql="SELECT * FROM superadministradores;"
        print(strsql)
        conn, cur = db.slq_connection()
        cur.execute(strsql)
        supAdministrators = cur.fetchall()
        conn.close()
        return supAdministrators
    except Error:
        print(Error)
    

def sql_edit_supAdmin(doc, nombre, email):
    try:
        strsql="UPDATE superadministradores SET nombre = ?, email = ? WHERE num_doc = ?"
        val=(nombre,email,doc)
        print(strsql)
        conn, cur = db.slq_connection()
        cur.execute(strsql,val)
        conn.commit()
        conn.close()
    except Error:
        print(Error)

def sql_delete_supAdmin(doc):
    try:
        strsql="DELETE FROM superadministradores WHERE num_doc = ?"
        val=(doc)
        print(strsql)
        print(val)
        conn, cur = db.slq_connection();
        cur.execute(strsql, [val])
        conn.commit()
        conn.close()
    except Error:
        print(Error)

def sql_get_password_sadmin(email):
    # try:
        strsql="SELECT password FROM pass_role WHERE num_doc in (SELECT num_doc from superadministradores WHERE email = ?)"
        val=(email)
        print(strsql)
        conn, cur = db.slq_connection()
        cur.execute(strsql,[val])
        password = cur.fetchall()
        conn.close()
        passw=" ".join(map(str,password[0]))
        return passw.encode('utf-8')
        
    