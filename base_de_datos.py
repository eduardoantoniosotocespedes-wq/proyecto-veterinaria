#nueva base de datos con guardado automatico
import json
import os

ARCHIVO = "datos.json"

def datos_iniciales():
    return {
        "usuarios": [
            {"user_name": "superadmin", "password": "admin123", "rol": "superadmin"},
            {"user_name": "admin1", "password": "12345", "rol": "admin"},
            {"user_name": "eduardo", "apellido": "soto", "telefono": "64946952", "direccion": "villazon", "password": "eduardo123", "rol": "cliente"}
        ],
        "mascotas": [],
        "citas": [],
        "historial": []
    }

def cargar_datos():
    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                datos = json.load(f)
                base = datos_iniciales()
                for k in base:
                    if k not in datos:
                        datos[k] = base[k]
                return datos
        except:
            return datos_iniciales()
    else:
        datos = datos_iniciales()
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        return datos

def guardar_datos():
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(database, f, indent=4, ensure_ascii=False)

database = cargar_datos()

usuario_actual = None