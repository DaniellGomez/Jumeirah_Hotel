class Habitaciones:
# Atributos de la clase
    lista_calificaciones = []
    # Constructor vacío
    def __init__(self):
        self.__num_habitacion = 0
        self.__hab_capacidad = 0
        self.__hab_acomodacion = ""
        self.__hab_bano = ""
        self.__calificacion_promedio = 0.0
        self.__hab_disponible = False
        # self.__lista_calificaciones = []

    # Constructor
    def __init__(self, num_habitacion, hab_capacidad, hab_acomodacion, hab_bano, calificacion_promedio, hab_disponible):
        self.__num_habitacion = num_habitacion
        self.__hab_capacidad = hab_capacidad
        self.__hab_acomodacion = hab_acomodacion
        self.__hab_bano = hab_bano
        self.__calificacion_promedio = calificacion_promedio
        self.__hab_disponible = hab_disponible
        # self.__lista_calificaciones = []

# Getters
    def get_num_habitacion(self):
        return self.__num_habitacion

    def get_hab_capacidad(self):
        return self.__hab_capacidad
    
    def get_hab_acomodacion(self):
        return self.__hab_acomodacion

    def get_hab_bano(self):
        return self.__hab_bano

    def get_calificacion_promedio(self):    
        return self.__calificacion_promedio
    
    def get_hab_disponible(self):    
        return self.__hab_disponible

    # def get_lista_calificaciones(self):
    #     return self.__lista_calificaciones

# Setters
    def set_num_habitacion(self, 
    num_habitacion):
        if type(num_habitacion) is int:
            self.__num_habitacion = num_habitacion
        else:
            mensaje = "El número de habitación ingresado no es válido. No se realizaron cambios."
            # print(mensaje)
            return mensaje

    def set_hab_capacidad(self, hab_capacidad):
        mensaje = "La información ingresada para la capacidad de la habitación no es válida. No se realizaron cambios."
        if type(hab_capacidad) is str:
            if hab_capacidad.lower() == "1 persona" or hab_capacidad == "1":
                self.__hab_capacidad = "1 persona"
            elif hab_capacidad.lower() == "2 personas" or hab_capacidad == "2":
                self.__hab_capacidad = "2 personas"
            elif hab_capacidad.lower() == "4 personas" or hab_capacidad == "4":
                self.__hab_capacidad = "4 personas"
            else:
                # print(mensaje)
                return mensaje
        elif type(hab_capacidad) is int:
            if hab_capacidad == 1:
                self.__hab_capacidad = "1 persona"
            elif hab_capacidad == 2:
                self.__hab_capacidad = "2 personas"
            elif hab_capacidad == 4:
                self.__hab_capacidad = "4 personas"
            else:
                # print(mensaje)
                return mensaje
        else:
            # print(mensaje)
            return mensaje
    
    def set_hab_acomodacion(self, hab_acomodacion):
        mensaje = "La información ingresada para la acomodación de la habitación no es válida. No se realizaron cambios."
        if type(hab_acomodacion) is str:
            if hab_acomodacion.lower() == "1 cama sencilla":
                self.__hab_acomodacion = hab_acomodacion.lower()
            elif hab_acomodacion.lower() == "1 cama doble":
                self.__hab_acomodacion = hab_acomodacion.lower()
            elif hab_acomodacion.lower() == "2 camas dobles":
                self.__hab_acomodacion = hab_acomodacion.lower()
            else:
                # print(mensaje)
                return mensaje
        else:
            # print(mensaje)
            return mensaje

    def set_hab_bano(self, hab_bano):
        mensaje = "La información ingresada para el baño de la habitación no es válida. No se realizaron cambios."
        if type(hab_bano) is str:
            if hab_bano.capitalize() == "Baño estándar" or hab_bano.capitalize() == "Baño estandar":
                self.__hab_bano = "Baño estándar"
            elif hab_bano.capitalize() == "Baño con jacuzzi":
                self.__hab_bano = "Baño con jacuzzi"
            elif hab_bano.capitalize() == "Baño doble con jacuzzi":
                self.__hab_bano = "Baño doble con jacuzzi"
            else:
                #print(mensaje)
                return mensaje
        else:
            #print(mensaje)
            return mensaje

    def set_calificacion_promedio(self, calificacion_promedio):
        mensaje = "El valor ingresado para la calificación promedio de la habitación no es válido. No se realizaron cambios."
        if type(calificacion_promedio) is float:
            if calificacion_promedio >= 0 and calificacion_promedio <= 5:
                self.__calificacion_promedio = calificacion_promedio
            else:
                return mensaje
        elif type(calificacion_promedio) is int:
            calificacion_promedio = float(calificacion_promedio)
            if calificacion_promedio >= 0 and calificacion_promedio <= 5:
                self.__calificacion_promedio = calificacion_promedio
            else:
                return mensaje
        else:
            # print(mensaje)
            return mensaje
    
    def set_hab_disponible(self, hab_disponible):
        mensaje = "El valor ingresado para la disponibilidad de la habitación no es válido. No se realizaron cambios."
        if type(hab_disponible) is bool:
            self.__hab_disponible = hab_disponible
        else:
            return mensaje

    # def set_lista_calificaciones(self, lista_calificacion):
    #     mensaje = "El valor de la calificación de la habitación no es válido. No se realizaron cambios."
    #     if type(lista_calificacion) is list:
    #         for element in lista_calificacion:
    #             if type(element) is int or type(element) is float:
    #                 self.__lista_calificaciones = self.__lista_calificaciones.append(float(element))
    #                 # self.calcular_promedio()
    #     else:
    #         return mensaje

# Metodos adicionales de la clase
    def calcular_promedio(self):
        if len(self.lista_calificaciones) > 0:
            self.__calificacion_promedio = sum(self.lista_calificaciones)/len(self.lista_calificaciones)    

    def nueva_calificacion(self, calificacion):
        mensaje = "El valor de la calificación de la habitación no es válido. No se realizaron cambios."
        if type(calificacion) is int or type(calificacion) is float:
            calificacion = float(calificacion)
            self.lista_calificaciones = self.lista_calificaciones.append(calificacion)
            # self.calcular_promedio()
        else:
            return mensaje
        
# PRUEBAS 
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PRUEBAS
valores_prueba = ["Baño doble con JAcuzzi", 2, "1 persona", "2 camas sencillas", 4.8, "baño estándar", "1 cama sencilla", True, 4, "2 camas dobles", False, "Baño doble con Jacuzzi", 10.5, "4 camas dobles", 1, "una cama sencilla", "Baño Estándar", -1, "4 personas", "1 cama doble", 3, "Baño con Jacuzzi", "baño doble con jacuzzi", "BAÑO ESTANDAR", "2", "1 CAMA SENCILLA",5.0]

hab401 = Habitaciones(401, "4 personas", "2 camas dobles", "Baño estándar", 4.0, False)

# print("Prueba num_habitacion")
# print(hab401.get_num_habitacion())
# hab401.set_num_habitacion("quinientos")
# print(hab401.get_num_habitacion())
# hab401.set_num_habitacion(401.40)
# print(hab401.get_num_habitacion())
# hab401.set_num_habitacion(5888)
# print(hab401.get_num_habitacion())

# print("Prueba hab_capacidad")
# print(hab401.get_hab_capacidad())
# for prueba in valores_prueba:
#     hab401.set_hab_capacidad(prueba)
#     print(hab401.get_hab_capacidad(), "/// valor:", prueba)

# print("Prueba hab_acomodacion")
# print(hab401.get_hab_acomodacion())
# for prueba in valores_prueba:
#     hab401.set_hab_acomodacion(prueba)
#     print(hab401.get_hab_acomodacion(), "/// valor:", prueba)

# print("Prueba hab_bano")
# print(hab401.get_hab_bano())
# for prueba in valores_prueba:
#     hab401.set_hab_bano(prueba)
#     print(hab401.get_hab_bano(), "/// valor:", prueba)

# print("Prueba calificacion_promedio")
# print(hab401.get_calificacion_promedio())
# for prueba in valores_prueba:
#     hab401.set_calificacion_promedio(prueba)
#     print(hab401.get_calificacion_promedio(), "/// valor:", prueba)


print(hab401.get_calificacion_promedio())
print(hab401.lista_calificaciones)
print("lenght",len(hab401.lista_calificaciones))
print("sumatory",sum(hab401.lista_calificaciones))
hab401.lista_calificaciones = [5.0, 4.7, 4.4]

hab401.calcular_promedio()

print(hab401.get_calificacion_promedio())
print(hab401.lista_calificaciones)
print("lenght",len(hab401.lista_calificaciones))
print("sumatory",sum(hab401.lista_calificaciones))
# promedio = (sum(hab401.lista_calificaciones)/len(hab401.lista_calificaciones))
# print(promedio)

# hab401.nueva_calificacion(2.3)
print(hab401.lista_calificaciones)
hab401.calcular_promedio()

print(hab401.get_calificacion_promedio())
print("lenght",len(hab401.lista_calificaciones))
print("sumatory",sum(hab401.lista_calificaciones))