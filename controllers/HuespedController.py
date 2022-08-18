#import sqlite3
#from sqlite3 import Error
import db_config.DB_Connection as db



def sql_insert_huesped(doc, nombre, email, rol, password):
    # try:
        strsql="INSERT INTO pass_role(num_doc, password, user_role) VALUES(?,?,?)"
        val=(doc,password,rol) #'"+ doc +"', '" + password + "', '"+ rol+"');"
        print(strsql)
        conn, cur = db.slq_connection()
        cur.execute(strsql,val)
        conn.commit()
        strsql="INSERT INTO huespedes(num_doc, nombre, email) VALUES(?,?,?)"
        val=(doc, nombre, email)#+ doc +"','"+ nombre +"','"+ email +"' );"
        print(strsql)
        cur.execute(strsql,val)
        conn.commit()
        conn.close()
    # except Error:
    #     print(Error)

def sql_get_huesped():
    # try:
        strsql="SELECT * FROM huespedes;"
        print(strsql)
        conn, cur = db.slq_connection()
        cur.execute(strsql)
        huespedes = cur.fetchall()
        conn.close()
        return huespedes
    # except Error:
    #     print(Error)
    

def sql_edit_huesped(doc, nombre, email):
    # try:
        strsql="UPDATE huespedes SET nombre = ?, email = ? WHERE num_doc = ?"
        val=(nombre,email,doc)
        print(strsql)
        conn, cur = db.slq_connection()
        cur.execute(strsql,val)
        conn.commit()
        conn.close()
    # except Error:
    #     print(Error)

def sql_delete_huesped(doc):
    # try:
        strsql="DELETE FROM huespedes WHERE num_doc = ?"
        val=(doc)
        print(strsql)
        conn, cur = db.slq_connection();
        cur.execute(strsql,[val])
        conn.commit()
        conn.close()
    # except Error:
    #     print(Error)

def sql_get_email_huesped(email):
    # try:
        strsql="SELECT email FROM huespedes WHERE email = ?"
        val=(email)
        print(strsql)
        conn, cur = db.slq_connection()
        cur.execute(strsql,[val])
        email = cur.fetchall()
        conn.close()
        return email

def sql_get_password_huesped(email):
    # try:
        strsql="SELECT password FROM pass_role WHERE num_doc in (SELECT num_doc from huespedes WHERE email = ?)"
        val=(email)
        print(strsql)
        conn, cur = db.slq_connection()
        cur.execute(strsql,[val])
        password = cur.fetchall()
        conn.close()
        passw=" ".join(map(str,password[0]))
        return passw.encode('utf-8')

def sql_get_password_admin(email):
    # try:
        strsql="SELECT password FROM pass_role WHERE num_doc in (SELECT num_doc from huespedes WHERE email = ?)"
        val=(email)
        print(strsql)
        conn, cur = db.slq_connection()
        cur.execute(strsql,[val])
        password = cur.fetchall()
        conn.close()
        passw=" ".join(map(str,password[0]))
        return passw.encode('utf-8')

def sql_get_password_sadmin(email):
    # try:
        strsql="SELECT password FROM pass_role WHERE num_doc in (SELECT num_doc from huespedes WHERE email = ?)"
        val=(email)
        print(strsql)
        conn, cur = db.slq_connection()
        cur.execute(strsql,[val])
        password = cur.fetchall()
        conn.close()
        passw=" ".join(map(str,password[0]))
        return passw.encode('utf-8')