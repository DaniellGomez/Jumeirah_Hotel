from flask import Flask, render_template, url_for, redirect, flash, request, session
import os
from forms import *
from settings.config import configuracion
from informacion import *
from flask_login import LoginManager

app=Flask(__name__)
app.run(port = 5000, debug = True)
images_folder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = images_folder
logo_path = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.webp')
app.config.from_object(configuracion)

@app.route('/')
@app.route('/home')
def home():
    offert_path = os.path.join(app.config['UPLOAD_FOLDER'], 'offertHome.png')
    comida_path = os.path.join(app.config['UPLOAD_FOLDER'], 'comidaHome.png')
    sauna_path = os.path.join(app.config['UPLOAD_FOLDER'], 'saunaHome.png')
    gym_path = os.path.join(app.config['UPLOAD_FOLDER'], 'gymHome.png')
    return render_template("home.html", titulo = "Home", logo_img = logo_path, offert = offert_path, comida = comida_path, sauna = sauna_path, gym = gym_path)

@app.route('/habitaciones', methods=['GET', 'POST'])
def habitaciones():
    formulario = FormHabitaciones();
    estandar_path = os.path.join(app.config['UPLOAD_FOLDER'], 'estandarReservaUser.png')

    

    return render_template("reservaHuesped.html", titulo = "Habitaciones", logo_img = logo_path, estandar = estandar_path, form = formulario)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    formulario = FormContacto()
    if request.method == "POST":
        flash("El formulario fue enviado con éxito")
        informacion.setContacto(formulario.nombre.data, formulario.numeroId.data, formulario.email.data, formulario.comentario.data)
        formulario.nombre.data = ""
        formulario.numeroId.data = ""
        formulario.email.data = ""
        formulario.comentario.data = ""
        return render_template("contactoForm.html", form = formulario, titulo = "Contacto", logo_img = logo_path)
    return render_template("contactoForm.html", form = formulario, titulo = "Contacto", logo_img = logo_path)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    formulario = FormRegistro()
    if request.method == "POST":
        informacion.setRegistro(formulario.nombre.data, formulario.numeroId.data, formulario.email.data, formulario.password.data)
        formulario.nombre.data = ""
        formulario.numeroId.data = ""
        formulario.email.data = ""
        formulario.password.data = ""
        formulario.confirmarPassword.data = ""
        return redirect("iniciosesion")
    return render_template("registroHuesped.html", form = formulario, titulo = "Registro", logo_img = logo_path)

@app.route('/menusuperadmin')
def menuSuperAdmin():
    return render_template("menuSAdmin.html", titulo = "Menú Superadmistrador", logo_img = logo_path)

@app.route('/agregarhabitacion', methods=['GET', 'POST'])
def agregarHabitacion():
    formulario1 = AgregarHabitacion()
    if request.method == "POST":
        if request.form['button'] == 'Agregar Habitación':
            sql_insert_habitacion(formulario1.numHabitacion.data, request.form.get('room_capacity'),request.form.get('room_layout'), request.form.get('room_bath'))

    return render_template("agregarHabitacion.html", 
    form1 = formulario1, 
    data1 = [{'capacidad': 'Individual'}, {'capacidad': '2 personas'}, {'capacidad': '4 personas'}], 
    data2 = [{'acomodacion': '1 cama sencilla'}, {'acomodacion': '1 cama doble'}, {'acomodacion': '2 camas dobles'}], 
    data3 = [{'baño': 'Baño estándar'}, {'baño': 'Baño con Jacuzzi'}], 
    titulo = "Agregar Habitación", 
    logo_img = logo_path)

@app.route('/editarhabitacion', methods=['GET', 'POST'])
def editarHabitacion():
    formulario1 = EditarHabitacion()
    if request.method == "POST":
        if request.form['button'] == 'Editar Habitación':
            sql_edit_habitacion(formulario1.numHabitacion.data, request.form.get('room_capacity'),request.form.get('room_layout'), request.form.get('room_bath'))

    return render_template("editarHabitacion.html", 
    form1 = formulario1, 
    data1 = [{'capacidad': 'Individual'}, {'capacidad': '2 personas'}, {'capacidad': '4 personas'}], 
    data2 = [{'acomodacion': '1 cama sencilla'}, {'acomodacion': '1 cama doble'}, {'acomodacion': '2 camas dobles'}], 
    data3 = [{'baño': 'Baño estándar'}, {'baño': 'Baño con Jacuzzi'}], 
    titulo = "Editar Habitación", 
    logo_img = logo_path)

@app.route('/eliminarhabitacion', methods=['GET', 'POST'])
def eliminarHabitacion():
    formulario1 = EliminarHabitacion()
    if request.method == "POST":
        if request.form['button'] == 'Eliminar Habitación':
            sql_delete_habitacion(formulario1.numHabitacion.data)

    return render_template("eliminarHabitacion.html", 
    form1 = formulario1, 
    titulo = "Eliminar Habitación", 
    logo_img = logo_path)

@app.route('/agregarusuario', methods=['GET', 'POST'])
def agregarUsuarioSA():
    formulario1 = RegistrarUsuario()
    
    if request.method == "POST":
        if request.form['button'] == 'Agregar Usuario':
            if request.form.get('user_rol') == 'Huesped':
                print("agregar Usuario")
                sql_insert_huesped(formulario1.numId.data, formulario1.nombre.data, formulario1.email.data, "Huesped", formulario1.password.data)
            elif request.form.get('user_rol') == 'Administrador':
                sql_insert_admin(formulario1.numId.data, formulario1.nombre.data, formulario1.email.data, "Administrador", formulario1.password.data)
            elif request.form.get('user_rol') == 'Superadministrador':
                sql_insert_supAdmin(formulario1.numId.data, formulario1.nombre.data, formulario1.email.data, "Superadministrador", formulario1.password.data)

    return render_template("agregarUsuario.html", 
    form1 = formulario1,
    data = [{'rol': 'Huesped'}, {'rol': 'Administrador'}, {'rol': 'Superadministrador'}],
    titulo = "Registrar Usuarios", logo_img = logo_path)

@app.route('/editarusuario', methods=['GET', 'POST'])
def editarUsuarioSA():
    formulario1 = EditarUsuario()
    
    if request.method == "POST":
        if request.form['button'] == 'Editar Usuario':
            if request.form.get('user_rol') == 'Huesped':
                sql_edit_huesped(formulario1.numId.data, formulario1.nombre.data, formulario1.email.data)
            elif request.form.get('user_rol') == 'Administrador':
                sql_edit_admin(formulario1.numId.data, formulario1.nombre.data, formulario1.email.data)
            elif request.form.get('user_rol') == 'Superadministrador':
                sql_edit_supAdmin(formulario1.numId.data, formulario1.nombre.data, formulario1.email.data)
    
    return render_template("editarUsuario.html", 
    form1 = formulario1,
    data = [{'rol': 'Huesped'}, {'rol': 'Administrador'}, {'rol': 'Superadministrador'}],
    titulo = "Editar Usuarios", logo_img = logo_path)

@app.route('/eliminarusuario', methods=['GET', 'POST'])
def eliminarUsuarioSA():
    formulario1 = EliminarUsuario()
    
    if request.method == "POST":
        if request.form['button'] == 'Eliminar Usuario':
            if request.form.get('user_rol') == 'Huesped':
                sql_delete_huesped(formulario1.numId.data)
            elif request.form.get('user_rol') == 'Administrador':
                sql_delete_admin(formulario1.numId.data)
            elif request.form.get('user_rol') == 'Superadministrador':
                sql_delete_supAdmin(formulario1.numId.data)
    
    return render_template("eliminarUsuario.html", 
    form1 = formulario1,
    data = [{'rol': 'Huesped'}, {'rol': 'Administrador'}, {'rol': 'Superadministrador'}],
    titulo = "Eliminar Usuarios", logo_img = logo_path)

@app.route('/menuadmin')
def menuAdmin():
    return render_template("menuAdmin.html", titulo = "Menú Administrador", logo_img = logo_path)

@app.route('/reservasadmin')
def reservasAdmin():
    formulario1 = ReservasDisponibles()
    formulario2 = BuscarReserva()
    formulario3 = GestionReserva()
    return render_template("reservasAdmin.html", 
    form1 = formulario1,
    form2 = formulario2,
    form3 = formulario3,
    data1 = [{'capacidad': 'Individual'}, {'capacidad': '2 personas'}, {'capacidad': '4 personas'}], 
    data2 = [{'acomodacion': '1 cama sencilla'}, {'acomodacion': '1 cama doble'}, {'acomodacion': '2 camas dobles'}], 
    data3 = [{'baño': 'Baño estándar'}, {'baño': 'Baño con Jacuzzi'}],
    titulo = "Gestión Reservas", 
    logo_img = logo_path)

@app.route('/habitacionesadmin')
def habitacionesAdmin():
    formulario1 = AgregarHabitaciones()
    formulario2 = BuscarHabitaciones()
    formulario3 = GestionHabitaciones()
    return render_template("habitacionesSAdmin.html", 
    form1 = formulario1, 
    form2 = formulario2, 
    form3 = formulario3, 
    data1 = [{'capacidad': 'Individual'}, {'capacidad': '2 personas'}, {'capacidad': '4 personas'}], 
    data2 = [{'acomodacion': '1 cama sencilla'}, {'acomodacion': '1 cama doble'}, {'acomodacion': '2 camas dobles'}], 
    data3 = [{'baño': 'Baño estándar'}, {'baño': 'Baño con Jacuzzi'}], 
    titulo = "Gestión Habitaciones", 
    logo_img = logo_path)

@app.route('/iniciosesion', methods=['GET', 'POST'])
def inicioSesion():
    formulario = InicioSesion()
    #correo=formulario.email.data
    #password=formulario.password.data

    if request.method== 'POST':
        if request.form['iniciarSesion'] == 'Iniciar Sesión':
            correo=formulario.email.data
            print(correo)
            password=formulario.password.data
            password = password.encode('utf-8')
            #print(password)
            #print(sql_get_password_huesped(correo))
            
            if request.form.get('userRol') == 'Huesped':
                if bcrypt.checkpw(password,sql_get_password_huesped(correo)): 
                    print("Inicio Sesión fue exitoso")
                    session['usuario'] = correo
                    return redirect("/menuhuesped")
            elif request.form.get('userRol') == 'Administrador':
                #if bcrypt.checkpw(password,sql_get_password_admin(correo)): 
                print("Inicio Sesión fue exitoso")
                session['usuario'] = correo
                return redirect("/menuadmin")
            elif request.form.get('userRol') == 'Superadministrador':
                #if bcrypt.checkpw(password,sql_get_password_sadmin(correo)): 
                print("Inicio Sesión fue exitoso")
                session['usuario'] = correo
                return redirect("/menusuperadmin")

            else:
                print("Password Incorrecto")
                return redirect("iniciosesion")

    return render_template("inicioSesion.html", 
    form = formulario,
    data = [{'rol': 'Seleccione su rol'}, {'rol': 'Huesped'}, {'rol': 'Administrador'}, {'rol': 'Superadministrador'}], 
    titulo = "Inicio de Sesión", 
    logo_img = logo_path)

@app.route('/menuhuesped')
def menuHuesped():
    return render_template("menuHuesped.html", titulo = "Menú Huespedes", logo_img = logo_path)

@app.route('/realizarreserva', methods=['GET', 'POST'])
def realizarReserva():
    formulario1 = RealizarReserva()
    estandar_path = os.path.join(app.config['UPLOAD_FOLDER'], 'estandarReservaUser.png')

    if request.method== "POST":
        if request.form['button'] == 'Realizar Reserva':
            print(type(formulario1.fechaInicio.data))
            sql_insert_reserva(formulario1.numId.data, formulario1.fechaInicio.data, formulario1.fechaFinal.data, formulario1.numHabitacion.data)
            reserva = sql_select_reserva(formulario1.numId.data)
            formulario1.codigoReserva.data = reserva[0][0]

    return render_template("realizarReserva.html", titulo = "Realizar Reserva", logo_img = logo_path, form = formulario1, estandar = estandar_path)

@app.route('/editarreserva', methods=['GET', 'POST'])
def editarReserva():
    formulario1 = EditarReserva()
    estandar_path = os.path.join(app.config['UPLOAD_FOLDER'], 'estandarReservaUser.png')

    if request.method== "POST":
        if request.form['button'] == 'Editar Reserva':
            print(type(formulario1.fechaInicio.data))
            sql_edit_reserva(formulario1.numId.data, formulario1.fechaInicio.data, formulario1.fechaFinal.data, formulario1.numHabitacion.data, formulario1.codigoReserva.data)

    return render_template("editarReserva.html", titulo = "Editar Reserva", logo_img = logo_path, form = formulario1, estandar = estandar_path)

@app.route('/eliminarreserva', methods=['GET', 'POST'])
def eliminarReserva():
    formulario1 = EliminarReserva()
    estandar_path = os.path.join(app.config['UPLOAD_FOLDER'], 'estandarReservaUser.png')

    if request.method== "POST":
        if request.form['button'] == 'Eliminar Reserva':
            sql_delete_reserva(formulario1.codigoReserva.data)

    return render_template("eliminarReserva.html", titulo = "Eliminar Reserva", logo_img = logo_path, form = formulario1, estandar = estandar_path)

@app.route('/calificarreserva', methods=['GET', 'POST'])
def calificarReserva():
    formulario1 = CalificarReserva()

    if request.method== "POST":
        if request.form['button'] == 'Calificar Reserva':
            sql_insert_calificacion(formulario1.numId.data, formulario1.numHabitacion.data, formulario1.codigoReserva.data, formulario1.comentario.data, request.form['calificacion'])

    return render_template("calificarReserva.html", titulo = "Calificar reserva", logo_img = logo_path, form = formulario1)