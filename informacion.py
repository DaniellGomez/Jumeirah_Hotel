from database.database import *
from controllers.HuespedController import *
from controllers.AdminController import *
from controllers.SupAdminController import *

class informacion:
    @staticmethod
    def setContacto(nombre, id, email, comentario):
        #Esto debe ser reemplazado por una orden para introducir dicha info en una tabla de la base de datos
        sql_insert_contacto(id,nombre,email,comentario)

    @staticmethod
    def setRegistro(nombre, id, email, password):
        #Esto debe ser reemplazado por una orden para introducir dicha info en una tabla de la base de datos
        sql_insert_huesped(id, nombre, email, "huesped", password)

    @staticmethod
    def setReserva(huespedId, reservaId, numeroCuarto, fechaIncio, dias):
        #Esto debe ser reemplazado por una orden para introducir dicha info en una tabla de la base de datos
        print(huespedId)
        print(fechaIncio)
        print(dias)

    @staticmethod
    def eliminarReserva(reservaId):
        #Esto debe ser reemplazado por una orden para introducir dicha info en una tabla de la base de datos
        print(reservaId)

    @staticmethod
    def getReserva(reservaId):
        #Esto debe ser reemplazado por una orden para introducir dicha info en una tabla de la base de datos
        print(reservaId)

    #@staticmethod
    #def getHabitaciones():
        #Esto debe ser reemplazado por una orden para introducir dicha info en una tabla de la base de datos