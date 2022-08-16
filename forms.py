from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired, Length

class FormContacto(FlaskForm):
    nombre = StringField("Nombre", id="nombre", validators = [DataRequired(message = "Digite su nombre"), Length(min = 8, max = 30, message = "El usuario debe contar con al menos 8 caracteres y máximo 10 caracteres.")])
    numeroId = StringField("Número ID.", id="id", validators = [DataRequired(message = "Digite su número de ID")])
    email = EmailField("Email", id="email", validators = [DataRequired(message = "Digite un email valido")])
    comentario = TextAreaField("Comentario", id="comentarioField", validators = [DataRequired(message = "Digite su comentario")])
    enviar = SubmitField("Enviar formulario", id="buttonRegistro")

class FormRegistro(FlaskForm):
    nombre = StringField("Nombre", id="nombre", validators = [DataRequired(message = "Digite su nombre"), Length(min = 8, max = 30, message = "El usuario debe contar con al menos 8 caracteres y máximo 10 caracteres.")])
    numeroId = StringField("Número ID.", id="id", validators = [DataRequired(message = "Digite su número de ID")])
    email = EmailField("Email", id="email", validators = [DataRequired(message = "Digite un email valido")])
    password = PasswordField("Contraseña", id="contraseña", validators = [DataRequired(message = "Digite una contraseña valida")])
    confirmarPassword = PasswordField("Confirmar contraseña", id="confirmar", validators = [DataRequired(message = "Las contraseñas no coinciden")])
    enviar = SubmitField("Enviar formulario", id="buttonRegistro")

class FormHabitaciones(FlaskForm):
    eliminar = SubmitField("Eliminar", id="eliminar")
    editar = SubmitField("editar", id="editar")
    reserva = SubmitField("reserva", id="reserva")
    fechaInicio = DateField("Fecha de Inicio", format='%m/%d/%y', validators=[DataRequired(message = "Ingrese una fecha valida")])
    dias = IntegerField("Cantidad de días", id="dias")
    reservaId = StringField("Reserva ID.", validators = [DataRequired(message = "Digite el número ID. de la reserva")])
    buscar = SubmitField("Buscar", id="buscar")

class AgregarHabitacion(FlaskForm):
    numHabitacion = StringField("N° Habitación", validators = [DataRequired(message = "Digite el número de la habitación")])
    agregarHabitacion = SubmitField("Agregar Habitación", id = "agregar", name="button")

class EditarHabitacion(FlaskForm):
    numHabitacion = StringField("N° Habitación", id="room_number", validators = [DataRequired(message = "Digite el número de la habitación")])
    editarButton = SubmitField("Editar Habitación", id = "buscar", name="button")

class EliminarHabitacion(FlaskForm):
    numHabitacion = StringField("N° Habitación", id="room_number", validators = [DataRequired(message = "Digite el número de la habitación")])
    eliminar = SubmitField("Eliminar Habitación", id= "eliminar", name="button")

class RegistrarUsuario(FlaskForm):
    nombre = StringField("Nombre", validators = [DataRequired(message = "Digite el nombre del usuario")])
    numId = StringField("Número ID", validators = [DataRequired(message = "Digite el número de Id del usuario")])
    email = EmailField("Email", validators = [DataRequired(message = "Digite el email del usuario")])
    password = PasswordField("Asignar Contraseña", validators = [DataRequired(message = "Digite la contrseña del usuario")])
    agregarUsuario = SubmitField("Agregar Usuario", id="agregarUsuario", name="button")

class EditarUsuario(FlaskForm):
    nombre = StringField("Nombre", validators = [DataRequired(message = "Digite el nombre del usuario")])
    numId = StringField("Número ID", validators = [DataRequired(message = "Digite el número de Id del usuario")])
    email = EmailField("Email", validators = [DataRequired(message = "Digite el email del usuario")])
    password = PasswordField("Asignar Contraseña", validators = [DataRequired(message = "Digite la contrseña del usuario")])
    agregarUsuario = SubmitField("Editar Usuario", id="agregarUsuario", name="button")

class EliminarUsuario(FlaskForm):
    numId = StringField("Número ID", validators = [DataRequired(message = "Digite el número de Id del usuario")])
    eliminarUsuario = SubmitField("Eliminar Usuario", id="agregarUsuario", name="button")

class BuscarUsuario(FlaskForm):
    buscar = StringField("N° ID", id="buscarUsuario", validators = [DataRequired(message = "Digite el número de ID del usuario")])
    buscarButton = SubmitField("Buscar", id = "buscar")

class GestionUsuario(FlaskForm):
    nombre = StringField("Nombre", validators = [DataRequired(message = "Digite el nombre del usuario")])
    email = EmailField("Email", validators = [DataRequired(message = "Digite el email de usuario")])
    password = PasswordField("Contraseña", validators = [DataRequired(message = "Digite la contraseña del usuario")])
    eliminar = SubmitField("Eliminar", id="eliminar")
    actualizar = SubmitField("Actualizar", id="actualizar")

class ReservasDisponibles(FlaskForm):
    fechaInicio = DateField("Fecha de entrada", format='%m/%d/%y', validators = [DataRequired()])
    fechaFinal = DateField("Fecha de salida", format='%m/%d/%y', validators = [DataRequired()])
    buscarDisponibles = SubmitField("Buscar Disponibles", id = "buscar-disponibles")

class BuscarReserva(FlaskForm):
    buscar = StringField("Código de Reserva", validators = [DataRequired()])
    buscarButton = SubmitField("Buscar", id = "buscar")

class GestionReserva(FlaskForm):
    nombre = StringField("Nombre", validators = [DataRequired()])
    numHabitacion = StringField("N° Habitación", validators = [DataRequired()])
    fechaInicio = DateField("Fecha de entrada", format='%m/%d/%y', validators = [DataRequired()])
    fechaFinal = DateField("Fecha de salida", format='%m/%d/%y', validators = [DataRequired()])
    eliminar = SubmitField("Eliminar", id="eliminar")
    actualizar = SubmitField("Actualizar", id="actualizar")

class InicioSesion(FlaskForm):
    email = EmailField("Email", validators = [DataRequired()])
    password = PasswordField("Contraseña", validators = [DataRequired()])
    iniciarSesion = SubmitField("Iniciar Sesión", id = "iniciarSesion")