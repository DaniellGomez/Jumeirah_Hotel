import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect("JUMEIRAH.db", isolation_level=None)
        return con
    except Error:
        print(Error)

def sql_insert_habitacion(num_hab,capacidad,acomodacion,bano):
    strsql="INSERT INTO habitaciones (num_hab,hab_capacidad,hab_acomodacion,hab_bano) VALUES('"+num_hab+"' , '"+capacidad+"', '"+acomodacion+"', '"+bano+"');"
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

def sql_select_habitacion(num_hab):
    strsql="SELECT * FROM habitaciones WHERE num_habitacion = '"+num_hab+"';"
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql)
    habitacion=cursor_Obj.fetchall()
    con.close()
    return habitacion

def sql_edit_habitacion(num_hab,capacidad,acomodacion,bano):
    strsql="UPDATE habitaciones SET hab_capacidad = '"+capacidad+"' , SET hab_acomodacion = '"+acomodacion+"' , SET hab_bano = '"+bano+"' WHERE num_habitacion = '"+num_hab+"';"
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

def sql_delete_habitacion(num_hab):
    strsql="DELETE FROM habitaciones WHERE num_habitacion = '"+num_hab+"';"
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()
    