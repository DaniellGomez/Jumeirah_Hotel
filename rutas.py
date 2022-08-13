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

@app.route('/gestionhabitaciones', methods=['GET', 'POST'])
def habitacionesSuperAdmin():
    formulario1 = AgregarHabitaciones()
    formulario2 = BuscarHabitaciones()
    formulario3 = GestionHabitaciones()

    if request.method == "POST":
        
        num_habitacion = "";
        
        if request.form['button'] == 'Agregar Habitación':
        #if formulario1.agregarHabitacion.data and formulario1.validate:
            print("agregar")
            sql_insert_habitacion(formulario1.numHabitacion.data, request.form.get('room_capacity'),request.form.get('room_layout'), request.form.get('room_bath'))
        

        elif request.form['button'] == 'Buscar':
            #print(formulario2.buscar.data)
            habitacion = sql_select_habitacion(formulario2.buscar.data)
            #for row in habitacion:
                #print(row)
            num_habitacion = formulario2.buscar.data
            if request.form['button'] == 'Actualizar':
                print(num_habitacion)
                sql_edit_habitacion(num_habitacion, request.form.get('room_capacity3'),request.form.get('room_layout3'), request.form.get('room_bath3'))
            
            elif request.form['button'] == 'Eliminar':
                sql_delete_habitacion(formulario2.buscar.data)
            

    return render_template("habitacionesSAdmin.html", 
    form1 = formulario1, 
    form2 = formulario2, 
    form3 = formulario3, 
    data1 = [{'capacidad': 'Individual'}, {'capacidad': '2 personas'}, {'capacidad': '4 personas'}], 
    data2 = [{'acomodacion': '1 cama sencilla'}, {'acomodacion': '1 cama doble'}, {'acomodacion': '2 camas dobles'}], 
    data3 = [{'baño': 'Baño estándar'}, {'baño': 'Baño con Jacuzzi'}], 
    titulo = "Gestión Habitaciones", 
    logo_img = logo_path)

@app.route('/gestionusuarios')
def usuariosSuperAdmin():
    formulario1 = RegistrarUsuario()
    formulario2 = BuscarUsuario()
    formulario3 = GestionUsuario()
    return render_template("usuariosSAdmin.html", 
    form1 = formulario1,
    form2 = formulario2,
    form3 = formulario3,
    data = [{'rol': 'Huesped'}, {'rol': 'Administrador'}, {'rol': 'Superadministrador'}],
    titulo = "Gestión Usuarios", logo_img = logo_path)

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
    correo=formulario.email.data
    password=formulario.password.data

    if request.method== "POST":
        if request.form['iniciarSesion'] == 'Iniciar Sesión':
            correo=formulario.email.data
            password=formulario.password.data
            password = password.encode('utf-8')
            hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt(10))

            if correo == sql_get_email_huesped(correo) and hashedPassword == sql_get_password_huesped(correo):
                print("Inicio Sesión fue exitoso")
                session['usuario'] = correo
                return redirect("menuHuesped")
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

@app.route('/calificarreserva')
def calificarReserva():
    return render_template("calificarReserva.html", titulo = "Calificar reserva", logo_img = logo_path)