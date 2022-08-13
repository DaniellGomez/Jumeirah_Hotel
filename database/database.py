import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect("./Jumeirah_Hotel/database/JUMEIRAH.db", isolation_level=None)
        return con
    except Error:
        print(Error)


#habitaciones

def sql_insert_habitacion(num_hab,capacidad,acomodacion,bano):
    strsql="INSERT INTO habitaciones (num_habitacion,hab_capacidad,hab_acomodacion,hab_bano) VALUES(?,?,?,?)"
    val=(num_hab,capacidad,acomodacion,bano)
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,val)
    con.commit()
    con.close()

def sql_select_habitacion(num_hab):
    strsql="SELECT * FROM habitaciones WHERE num_habitacion = ?"
    val=(num_hab)
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,[val])
    habitacion=cursor_Obj.fetchall()
    con.close()
    return habitacion

def sql_edit_habitacion(num_hab,capacidad,acomodacion,bano):
    strsql="UPDATE habitaciones SET hab_capacidad = ? , SET hab_acomodacion = ? , SET hab_bano = ? WHERE num_habitacion = ?"
    val=(capacidad,acomodacion,bano,num_hab)
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,val)
    con.commit()
    con.close()

def sql_delete_habitacion(num_hab):
    strsql="DELETE FROM habitaciones WHERE num_habitacion = ?"
    val=(num_hab)
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,[val])
    con.commit()
    con.close()


#reservas

def sql_insert_reserva(num_doc,fecha_inicio,fecha_fin,num_hab):
    strsql="INSERT INTO reservaciones (num_doc,fecha_inicio,fecha_fin,num_habitacion) VALUES(?,?,?,?)"
    val=(num_doc,fecha_inicio,fecha_fin,num_hab)
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,val)
    con.commit()
    con.close()

def sql_select_reserva(codigo_reserva):
    strsql="SELECT * FROM reservaciones WHERE codigo_reserva = ?"
    val=(codigo_reserva)
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,[val])
    reserva=cursor_Obj.fetchall()
    con.close()
    return reserva

def sql_edit_reserva(num_doc,fecha_inicio,fecha_fin,num_hab,codigo_reserva):
    strsql="UPDATE reservaciones SET num_doc = ? , SET fecha_inicio = ? , SET fecha_fin = ?, SET num_habitacion WHERE codigo_reserva = ?"
    val=(num_doc,fecha_inicio,fecha_fin,num_hab,codigo_reserva)
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,val)
    con.commit()
    con.close()

def sql_delete_reserva(codigo_reserva):
    strsql="DELETE FROM reservaciones WHERE codigo_reserva = ?"
    val=(codigo_reserva)
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,[val])
    con.commit()
    con.close()

##contacto

def sql_insert_contacto(num_doc,nombre,email,comentario):
    strsql="INSERT INTO contacto (num_doc,nombre,email,comentario) VALUES(?,?,?,?)"
    val=(num_doc,nombre,email,comentario)
    #strsql="INSERT INTO contacto(num_doc, nombre, email, comentario) VALUES('" + num_doc + "', '" + nombre + "', '" + email + "', '" + comentario + "')"
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,val)
    con.commit()
    con.close()

#__________Pruebas__________
#sql_insert_contacto("12435687","John Smith","johnsmith@gmail.com","This is a good hotel")

def sql_select_contacto(num_doc):
    strsql="SELECT * FROM contacto WHERE num_doc = ?"
    val=(num_doc)
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,[val])
    contacto=cursor_Obj.fetchall()
    con.close()
    return contacto

def sql_delete_contacto(id_contacto):
    strsql="DELETE FROM contacto WHERE id_contacto = ?"
    val=(id_contacto)
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,[val])
    con.commit()
    con.close()


##calificaciones

def sql_insert_calificacion(num_doc,num_habitacion,codigo_reserva,comentarios,calificacion):
    strsql="INSERT INTO calificaciones (num_doc,num_habitacion,codigo_reserva,comentarios,calificacion) VALUES(?,?,?,?,?)"
    val=(num_doc,num_habitacion,codigo_reserva,comentarios,calificacion)
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,val)
    con.commit()
    con.close()

def sql_select_calificaciones(num_doc,codigo_reserva):
    strsql="SELECT * FROM calificaciones WHERE num_doc = ? AND codigo_reserva = ?"
    val=(num_doc,codigo_reserva)
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,val)
    calificaciones=cursor_Obj.fetchall()
    con.close()
    return calificaciones

def sql_delete_calificaciones(id_calificacion):
    strsql="DELETE FROM calificaciones WHERE id_calificacion = ?"
    val=(id_calificacion)
    print(strsql)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,[val])
    con.commit()
    con.close()
    