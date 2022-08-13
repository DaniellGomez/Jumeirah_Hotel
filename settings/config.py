import os

class configuracion():
    SECRET_KEY = os.environ.get("SECRET_KEY") or "contraseña"