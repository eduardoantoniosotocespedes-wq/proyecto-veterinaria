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

# MÓDULO DE MASCOTAS

def registrar_mascota():
    print("\n--- REGISTRAR NUEVA MASCOTA ---")
    if not database["dueños"]:
        print("No hay dueños registrados. Debe registrar un dueño primero.")
        return

    try:
        id_dueño = int(input("ID del dueño: "))
        dueño_encontrado = None
        for d in database["dueños"]:
            if d["id"] == id_dueño:
                dueño_encontrado = d
                break
        
        if not dueño_encontrado:
            print(" Error: No existe ningún dueño registrado con ese ID.")
            return

        nombre = input("Nombre de la mascota: ")
        especie = input("Especie (ej. Perro, Gato): ")
        raza = input("Raza: ")
        edad = input("Edad: ")
        sexo = input("Sexo (M/F): ")

        id_mascota = len(database["mascotas"]) + 1

        database["mascotas"].append({
            "id": id_mascota,
            "nombre": nombre,
            "especie": especie,
            "raza": raza,
            "edad": edad,
            "sexo": sexo,
            "id_dueño": id_dueño
        })
        print(f" Mascota '{nombre}' registrada con éxito con ID {id_mascota} (Dueño: {dueño_encontrado['nombre']} {dueño_encontrado['apellido']}).")

    except ValueError:
        print(" Ingrese un número válido para el ID del dueño.")


def ver_mascotas():
    print("\n--- LISTA DE MASCOTAS ---")
    if not database["mascotas"]:
        print("No hay mascotas registradas.")
        return

    for m in database["mascotas"]:
        # Buscar el nombre del dueño asociado
        nombre_dueño = "Desconocido"
        for d in database["dueños"]:
            if d["id"] == m["id_dueño"]:
                nombre_dueño = f"{d['nombre']} {d['apellido']}"
                break

        print(f"ID: {m['id']} | Nombre: {m['nombre']} | Especie: {m['especie']} | Raza: {m['raza']} | Edad: {m['edad']} | Sexo: {m['sexo']} | Dueño: {nombre_dueño} (ID: {m['id_dueño']})")


def editar_mascota():
    ver_mascotas()
    if not database["mascotas"]: return

    try:
        id_buscar = int(input("\nID de la mascota a editar: "))
        for m in database["mascotas"]:
            if m["id"] == id_buscar:
                print(f"Editando a '{m['nombre']}'. Deje en blanco para mantener el dato actual:")

                nuevo_nombre = input(f"Nuevo nombre [{m['nombre']}]: ")
                nueva_especie = input(f"Nueva especie [{m['especie']}]: ")
                nueva_raza = input(f"Nueva raza [{m['raza']}]: ")
                nueva_edad = input(f"Nueva edad [{m['edad']}]: ")
                nuevo_sexo = input(f"Nuevo sexo [{m['sexo']}]: ")

                if nuevo_nombre: m["nombre"] = nuevo_nombre
                if nueva_especie: m["especie"] = nueva_especie
                if nueva_raza: m["raza"] = nueva_raza
                if nueva_edad: m["edad"] = nueva_edad
                if nuevo_sexo: m["sexo"] = nuevo_sexo

                print("Mascota actualizada correctamente.")
                return

        print("ID no encontrado.")
    except ValueError:
        print(" Ingrese un número válido.")


def eliminar_mascota():
    ver_mascotas()
    if not database["mascotas"]: return

    try:
        id_buscar = int(input("\nID de la mascota a eliminar: "))
        for m in database["mascotas"]:
            if m["id"] == id_buscar:
                database["mascotas"].remove(m)
                print("Mascota eliminada correctamente.")
                return
        print("ID no encontrado.")
    except ValueError:
        print("Ingrese un número válido.")


#  MÓDULO DE VETERINARIOS 

def registrar_veterinario():
    print("\n--- REGISTRAR NUEVO VETERINARIO ---")
    id_vet = len(database["veterinarios"]) + 1
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    especialidad = input("Especialidad: ")
    telefono = input("Teléfono: ")

    database["veterinarios"].append({
        "id": id_vet,
        "nombre": nombre,
        "apellido": apellido,
        "especialidad": especialidad,
        "telefono": telefono
    })
    print(f"Veterinario Dr/a. '{nombre} {apellido}' registrado con éxito con ID {id_vet}.")


def ver_veterinarios():
    print("\n--- LISTA DE VETERINARIOS ---")
    if not database["veterinarios"]:
        print("No hay veterinarios registrados.")
        return

    for v in database["veterinarios"]:
        print(f"ID: {v['id']} | Dr/a. {v['nombre']} {v['apellido']} | Especialidad: {v['especialidad']} | Teléfono: {v['telefono']}")


def editar_veterinario():
    ver_veterinarios()
    if not database["veterinarios"]: return

    try:
        id_buscar = int(input("\nID del veterinario a editar: "))
        for v in database["veterinarios"]:
            if v["id"] == id_buscar:
                print(f"Editando a Dr/a. {v['nombre']} {v['apellido']}. Deje en blanco para mantener el dato actual:")

                nueva_especialidad = input(f"Nueva especialidad [{v['especialidad']}]: ")
                nuevo_telefono = input(f"Nuevo teléfono [{v['telefono']}]: ")

                if nueva_especialidad: v["especialidad"] = nueva_especialidad
                if nuevo_telefono: v["telefono"] = nuevo_telefono

                print("Información de veterinario actualizada correctamente.")
                return

        print("ID no encontrado.")
    except ValueError:
        print("Ingrese un número válido.")


def eliminar_veterinario():
    ver_veterinarios()
    if not database["veterinarios"]: return

    try:
        id_buscar = int(input("\nID del veterinario a eliminar: "))
        for v in database["veterinarios"]:
            if v["id"] == id_buscar:
                database["veterinarios"].remove(v)
                print("Veterinario eliminado correctamente.")
                return
        print("ID no encontrado.")
    except ValueError:
        print("Ingrese un número válido.")