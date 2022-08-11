import re

class Reservas:
# Atributos de la clase
    # Constructor vacío
    def __init__(self):
        self.__codigo_reserva = ""
        self.__doc_cliente = 0
        self.__fecha_inicio = "01/01/1600"
        self.__fecha_fin = "01/01/1600"
        self.__num_habitacion = 0

    # Constructor
    def __init__(self, codigo_reserva, doc_cliente, fecha_inicio, fecha_fin, num_habitacion):
        self.__codigo_reserva = codigo_reserva
        self.__doc_cliente = doc_cliente
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__num_habitacion = num_habitacion
    
# Getters
    def get_codigo_reserva(self):
        return self.__codigo_reserva

    def get_doc_cliente(self):
        return self.__doc_cliente

    def get_fecha_inicio(self):
        return self.__fecha_inicio

    def get_fecha_fin(self):
        return self.__fecha_fin

    def get_num_habitacion(self):
        return self.__num_habitacion

# Setters
    def set_codigo_reserva(self, codigo_reserva):
        codigo_reserva = str(codigo_reserva)
        regex_codigo = '^[a-zA-Z0-9\-]+$'
        if bool(re.search(regex_codigo,codigo_reserva)) == True:
            self.__codigo_reserva = codigo_reserva
        else:
            mensaje = "La fecha de inicio ingresada no es válida. No se realizaron cambios."
            # print(mensaje)
            return mensaje

    def set_doc_cliente(self, doc_cliente):
        if type(doc_cliente) is int:
            self.__doc_cliente = doc_cliente
        else:
            mensaje = "El documento del cliente ingresado no es válido. No se realizaron cambios."
            # print(mensaje)
            return mensaje

    def set_fecha_inicio(self, fecha_inicio):
        fecha_inicio = str(fecha_inicio)
        # regex_fecha = '^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
        regex_fecha = '^(0?[1-9]|[12][0-9]|3[01])[\/](0?[1-9]|1[012])[\/]\d{4}$'
        if bool(re.search(regex_fecha,fecha_inicio)) == True:
            self.__fecha_inicio = fecha_inicio
        else:
            mensaje = "La fecha de inicio ingresada no es válida. No se realizaron cambios."
            # print(mensaje)
            return mensaje

    def set_fecha_fin(self, fecha_fin):
        fecha_fin = str(fecha_fin)
        regex_fecha = '^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
        if bool(re.search(regex_fecha,fecha_fin)) == True:
            self.__fecha_fin = fecha_fin
        else:
            mensaje = "La fecha de fin ingresada no es válida. No se realizaron cambios."
            # print(mensaje)
            return mensaje

    def set_num_habitacion(self, num_habitacion):
        if type(num_habitacion) is int:
            self.__num_habitacion = num_habitacion
        else:
            mensaje = "El número de habitación ingresado no es válido. No se realizaron cambios."
            # print(mensaje)
            return mensaje


# Metodos adicionales de la clase


# PRUEBAS
# reserv = Reservas("XYZ11258", 1145, "01/01/0001", "31/12/2099", 401)
# print(reserv.get_codigo_reserva())
# reserv.set_codigo_reserva(8116)
# reserv.set_codigo_reserva("Letras Y Numeros")
# print(reserv.get_codigo_reserva())
# reserv.set_codigo_reserva("uno8seis2")
# print(reserv.get_codigo_reserva())
# reserv.set_codigo_reserva("Letras y Numeros")
# print(reserv.get_codigo_reserva())
# reserv.set_codigo_reserva("Letras-y-Numeros")
# print(reserv.get_codigo_reserva())


# print(reserv.get_num_habitacion())
# reserv.set_num_habitacion(8116)
# print(reserv.get_num_habitacion())
# reserv.set_num_habitacion("uno8seis2")
# print(reserv.get_num_habitacion())

# print(reserv.get_doc_cliente())
# reserv.set_doc_cliente("unodostres")
# print(reserv.get_doc_cliente())

# print(reserv.get_fecha_fin())
# reserv.set_codigo_reserva("JC2022")
# print(reserv.get_codigo_reserva())

# print(reserv.get_fecha_fin())
# finfin = "11/05/2002"
# reserv.set_fecha_fin(finfin)
# print(reserv.get_fecha_fin())
# finfin = 11011991
# reserv.set_fecha_fin(finfin)
# print(reserv.get_fecha_fin())
# finfin = "DD/A5/2K02"
# reserv.set_fecha_fin(finfin)
# print(reserv.get_fecha_fin())

# print(reserv.get_fecha_inicio())
# valor_prueba = 11011991
# reserv.set_fecha_inicio(valor_prueba)
# print(reserv.get_fecha_inicio())
# valor_prueba = "29/09/1991"
# reserv.set_fecha_inicio(valor_prueba)
# print(reserv.get_fecha_inicio())
# valor_prueba = "20-05-2015"
# reserv.set_fecha_inicio(valor_prueba)
# print(reserv.get_fecha_inicio())
# valor_prueba = "A1/05/2k02"
# reserv.set_fecha_inicio(valor_prueba)
# print(reserv.get_fecha_inicio())