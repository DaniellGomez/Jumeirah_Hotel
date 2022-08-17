from database.database import *
from controllers.HuespedController import *
from controllers.AdminController import *
from controllers.SupAdminController import *
import bcrypt

class informacion:
    @staticmethod
    def setContacto(nombre, id, email, comentario):
        #Esto debe ser reemplazado por una orden para introducir dicha info en una tabla de la base de datos
        sql_insert_contacto(id,nombre,email,comentario)

    @staticmethod
    def setRegistro(nombre, id, email, password):
        #Esto debe ser reemplazado por una orden para introducir dicha info en una tabla de la base de datos
        
        #Encode password into a readable utf-8 byte code: 
        password = password.encode('utf-8')
        # Hash the ecoded password and generate a salt: 
        hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt(5))
        print(hashedPassword)
        hashedPassword=hashedPassword.decode('utf-8')
        sql_insert_huesped(id, nombre, email, "huesped", hashedPassword)

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