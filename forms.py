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