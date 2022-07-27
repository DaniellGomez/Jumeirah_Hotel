function iniciarSesion() {
    var rol = document.getElementById("userRol").value;
    var email = document.getElementById("emailUser").value;
    var password = document.getElementById("passwordUser").value;

    if (rol == "huesped" && email == "huesped" && password == "huesped") {
        window.location.href = "../views/UserMain.html";
    } else if (rol == "admin" && email == "admin" && password == "admin") {
        window.location.href = "../views/menu_admin.html";
    } else if (rol == "superadmin" && email == "superadmin" && password == "superadmin") {
        window.location.href = "../views/menu_SAdmin.html";
    }
}

function registro() {
    window.location.href = "../views/registro.html";
}