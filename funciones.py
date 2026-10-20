# Base de datos central compartida
database = {
    "usuarios": [],     # username, password, rol
    "dueños": [],       # id, nombre, apellido, telefono, direccion)
    "mascotas": [],     
    "veterinarios": [], 
    "citas": [],        
    "tratamientos": []  
}

#LOGIN Y REGISTRO 
def registrar_usuario():
    print("\n--- REGISTRO DE USUARIO ---")
    username = input("Crea un usuario: ")
    
    # 🔍 Validar si el usuario ya existe en la base de datos
    for u in database["usuarios"]:
        if u["username"] == username:
            print("Ese nombre de usuario ya está en uso. Intenta con otro.")
            return  # Detiene el registro y vuelve al menú
            
    password = input("Crea una contraseña: ")
    
    print("¿Qué rol tendrá este usuario?")
    print("1. Administrador")
    print("2. Usuario normal")
    tipo = input("Elige (1 o 2): ")
    
    rol = "admin" if tipo == "1" else "usuario"
    
    database["usuarios"].append({
        "username": username,
        "password": password,
        "rol": rol
    })
    print(f"¡Usuario registrado con éxito como '{rol}'!")

def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    username = input("Usuario: ")
    password = input("Contraseña: ")
    
    for u in database["usuarios"]:
        if u["username"] == username and u["password"] == password:
            print(f"¡Bienvenido, {username}!")
            return u  # Retorna el diccionario del usuario incluyendo su rol
            
    print("Usuario o contraseña incorrectos.")
    return None


# CRUD DE DUEÑOS 
def registrar_dueño():
    print("\n--- REGISTRAR NUEVO DUEÑO ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    
    nuevo_id = len(database["dueños"]) + 1
    
    dueño = {
        "id": nuevo_id,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "direccion": direccion
    }
    
    database["dueños"].append(dueño)
    print(f"Dueño registrado con el ID: {nuevo_id}")

def ver_dueños():
    print("\n--- LISTA DE DUEÑOS ---")
    if not database["dueños"]:
        print("No hay dueños registrados.")
        return
    
    for d in database["dueños"]:
        print(f"ID: {d['id']} | Nombre: {d['nombre']} {d['apellido']} | Tel: {d['telefono']} | Dir: {d['direccion']}")

def editar_dueño():
    ver_dueños()
    if not database["dueños"]: return
        
    try:
        id_buscar = int(input("\nID del dueño a editar: "))
        for d in database["dueños"]:
            if d["id"] == id_buscar:
                print(f"Editando a {d['nombre']} {d['apellido']}. Deje en blanco para no cambiar el dato:")
                
                nuevo_nombre = input(f"Nuevo nombre [{d['nombre']}]: ")
                nuevo_apellido = input(f"Nuevo apellido [{d['apellido']}]: ")
                nuevo_telefono = input(f"Nuevo teléfono [{d['telefono']}]: ")
                nueva_direccion = input(f"Nueva dirección [{d['direccion']}]: ")
                
                # Actualizar solo si se escribió algo nuevo
                if nuevo_nombre: d["nombre"] = nuevo_nombre
                if nuevo_apellido: d["apellido"] = nuevo_apellido
                if nuevo_telefono: d["telefono"] = nuevo_telefono
                if nueva_direccion: d["direccion"] = nueva_direccion
                
                print("Dueño actualizado correctamente.")
                return
                
        print("ID no encontrado.")
    except ValueError:
        print("Ingrese un número válido.")

def eliminar_dueño():
    ver_dueños()
    if not database["dueños"]: return
        
    try:
        id_buscar = int(input("\nID del dueño a eliminar: "))
        for d in database["dueños"]:
            if d["id"] == id_buscar:
                database["dueños"].remove(d)
                print("Dueño eliminado.")
                return
        print("ID no encontrado.")
    except ValueError:
        print("Ingrese un número válido.")