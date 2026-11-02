from base_de_datos import database

#funciones de superadministrador y algunas de administradores 
def registrar_dueño():
    print("\n--- REGISTRAR NUEVO DUEÑO ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    pas = input("cree una contraseña: ")
    dueño = {"user_name": nombre,"apellido": apellido,"telefono": telefono,"direccion": direccion,"password":pas,"rol":"cliente"}
    
    database["usuarios"].append(dueño)
    print(f"El dueño ha sido registrado con exito")

def ver_dueños():
    print("\n=== Lista de dueños ===")
    dueños = [u for u in database["usuarios"]if u["rol"]== "cliente" ]
    if not dueños:
        print("No hay dueños registrados")
    for d in dueños:
        print(f"| Nombre: {d["user_name"]} {d["apellido"]} | Tel: {d["telefono"]} | Dir: {d["direccion"]}")

def editar_dueño():
    cliente = [u for u in database["usuarios"] if u["rol"] == "cliente"]
    if not cliente: 
        print("No hay dueños")
        return

    for i, a in enumerate(cliente, 1): 
        print(f"{i}. {a['user_name']}")
    
    elegido = cliente[int(input("¿Cuál? "))-1]
    print("Si no quiere editar un dato, dejelo en blanco")
    elegido["user_name"] = input(f"Nuevo nombre ({elegido["user_name"]}): ") or elegido["user_name"]
    elegido["apellido"] = input(f"Nuevo apellido ({elegido["apellido"]}): ") or elegido["apellido"]
    elegido["telefono"] = input(f"Nuevo telefono ({elegido["telefono"]}): ") or elegido["telefono"]
    elegido["direccion"] = input(f"Nueva direccion ({elegido["direccion"]}): ") or elegido["direccion"]
    elegido["password"] = input("Nueva contraseña: ") or elegido["password"]
    print("Editado con exito.")

def eliminar_dueño():
    clientes = [u for u in database["usuarios"] if u["rol"] == "cliente"]
    if not clientes: 
        print("No hay dueños registrados")
        return
    for i, a in enumerate(clientes, 1): 
            print(f"{i}. {a['user_name']}")
    elegido = clientes[int(input("¿Cuál? "))-1]
    database["usuarios"].remove(elegido)
    print("Eliminado con exito.")

def registrar_administrador():
    print("=== REGISTRO DE ADMINISTRADOR ===")
    username = input("Crea un usuario: ")
    for u in database["usuarios"]:
        if u["user_name"] == username:
            print("Ese nombre de usuario ya está en uso. Intenta con otro.")
            return     
    password = input("Crea una contraseña: ")
    database["usuarios"].append({
        "user_name": username,
        "password": password,
        "rol": "admin"})
    print(f"¡Administrador {username} registrado con éxito!")

def ver_administrador():
    print("\n--- LISTA DE ADMINISTRADORES ---")
    
    admins = []
    for u in database["usuarios"]:
        if u["rol"] == "admin":
            admins.append(u)
    if not admins:
        print("No hay administradores registrados.")
        return
    for a in admins:
        print(f"Usuario: {a['user_name']} | Rol: {a['rol']}")

def editar_administrador():
    admins = [u for u in database["usuarios"] if u["rol"] == "admin"]
    if not admins: 
        print("No hay administradores")
        return

    for i, a in enumerate(admins, 1): 
        print(f"{i}. {a['user_name']}")
    
    elegido = admins[int(input("¿Cuál? "))-1]
    elegido["user_name"] = input(f"Nuevo nombre ({elegido['user_name']}): ") or elegido["user_name"]
    elegido["password"] = input("Nueva pass: ") or elegido["password"]
    print("Editado con exito.")

def eliminar_administrador():
    admins = [u for u in database["usuarios"] if u["rol"] == "admin"]
    if not admins: 
        print("No hay administradores")
        return
    for i, a in enumerate(admins, 1): 
            print(f"{i}. {a['user_name']}")
    elegido = admins[int(input("¿Cuál? "))-1]
    database["usuarios"].remove(elegido)
    print("Eliminado con exito.")

















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


#  modulo de veterinaria

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


def crear_cita():
    print("\n--- CREAR NUEVA CITA ---")
    if not database["mascotas"]:
        print(" No hay mascotas registradas. Debe registrar una mascota primero.")
        return
    if not database["veterinarios"]:
        print(" No hay veterinarios registrados. Debe registrar un veterinario primero.")
        return
    try:
        id_mascota = int(input("ID de la mascota: "))
        mascota_encontrada = next((m for m in database["mascotas"] if m["id"] == id_mascota), None)
        if not mascota_encontrada:
            print(" Error: No existe ninguna mascota registrada con ese ID.")
            return
        id_veterinario = int(input("ID del veterinario: "))
        vet_encontrado = next((v for v in database["veterinarios"] if v["id"] == id_veterinario), None)
        if not vet_encontrado:
            print(" Error: No existe ningún veterinario registrado con ese ID.")
            return
        fecha = input("Fecha de la cita (ej. DD/MM/AAAA): ")
        hora = input("Hora de la cita (ej. 10:30 AM): ")
        motivo = input("Motivo de la consulta: ")
        id_cita = len(database["citas"]) + 1
        database["citas"].append({
            "id": id_cita,
            "id_mascota": id_mascota,
            "id_veterinario": id_veterinario,
            "fecha": fecha,
            "hora": hora,
            "motivo": motivo
        })
        print(f" Cita #{id_cita} agendada con éxito para '{mascota_encontrada['nombre']}' con Dr/a. {vet_encontrado['nombre']} {vet_encontrado['apellido']}.")
    except ValueError:
        print(" Ingrese un número válido para los IDs.")

def ver_citas():
    print("\n--- LISTA DE CITAS PROGRAMADAS ---")
    if not database["citas"]:
        print("No hay citas programadas.")
        return

    for c in database["citas"]:
        mascota = next((m for m in database["mascotas"] if m["id"] == c["id_mascota"]), None)
        nombre_mascota = mascota["nombre"] if mascota else "Desconocida"

        vet = next((v for v in database["veterinarios"] if v["id"] == c["id_veterinario"]), None)
        nombre_vet = f"Dr/a. {vet['nombre']} {vet['apellido']}" if vet else "Desconocido"

        print(f"ID Cita: {c['id']} | Fecha: {c['fecha']} - {c['hora']} | Mascota: {nombre_mascota} (ID: {c['id_mascota']}) | Atiende: {nombre_vet} (ID: {c['id_veterinario']}) | Motivo: {c['motivo']}")

def modificar_cita():
    ver_citas()
    if not database["citas"]: return
    try:
        id_buscar = int(input("\nID de la cita a modificar: "))
        for c in database["citas"]:
            if c["id"] == id_buscar:
                print(f"Modificando Cita #{c['id']}. Deje en blanco para mantener el dato actual:")
                nueva_fecha = input(f"Nueva fecha [{c['fecha']}]: ")
                nueva_hora = input(f"Nueva hora [{c['hora']}]: ")
                nuevo_motivo = input(f"Nuevo motivo [{c['motivo']}]: ")
                if nueva_fecha: c["fecha"] = nueva_fecha
                if nueva_hora: c["hora"] = nueva_hora
                if nuevo_motivo: c["motivo"] = nuevo_motivo
                print(" Cita modificada correctamente.")
                return
        print(" ID de cita no encontrado.")
    except ValueError:
        print("Ingrese un número válido.")

def cancelar_cita():
    ver_citas()
    if not database["citas"]: return
    try:
        id_buscar = int(input("\nID de la cita a cancelar: "))
        for c in database["citas"]:
            if c["id"] == id_buscar:
                database["citas"].remove(c)
                print("Cita cancelada y eliminada correctamente.")
                return
        print(" ID de cita no encontrado.")
    except ValueError:
        print(" Ingrese un número válido.")

def registrar_tratamiento():
    print("\n--- REGISTRAR TRATAMIENTO MÉDICO ---")
    if not database["mascotas"]:
        print(" No hay mascotas registradas en la base de datos.")
        return
    try:
        id_mascota = int(input("ID de la mascota que recibe el tratamiento: "))
        mascota_encontrada = next((m for m in database["mascotas"] if m["id"] == id_mascota), None)
        if not mascota_encontrada:
            print(" Error: No existe ninguna mascota registrada con ese ID.")
            return
        descripcion = input("Descripción del caso / diagnóstico: ")
        medicamento = input("Medicamento recetado y dosis: ")
        fecha = input("Fecha del tratamiento (ej. DD/MM/AAAA): ")
        id_tratamiento = len(database["tratamientos"]) + 1
        database["tratamientos"].append({
            "id": id_tratamiento,
            "id_mascota": id_mascota,
            "descripcion": descripcion,
            "medicamento": medicamento,
            "fecha": fecha
        })
        print(f"Tratamiento registrado con éxito para la mascota '{mascota_encontrada['nombre']}'.")
    except ValueError:
        print(" Ingrese un número válido para el ID de la mascota.")

def ver_tratamientos_mascota():
    print("\n--- CONSULTAR HISTORIAL MÉDICO ---")
    if not database["mascotas"]:
        print("No hay mascotas registradas.")
        return
    try:
        id_mascota = int(input("Ingrese el ID de la mascota a consultar: "))
        mascota = next((m for m in database["mascotas"] if m["id"] == id_mascota), None)
        if not mascota:
            print(" Error: No existe ninguna mascota registrada con ese ID.")
            return
        print(f"\nHistorial Médico de: {mascota['nombre']} ({mascota['especie']} - {mascota['raza']})")
        print("-" * 55)
        tratamientos = [t for t in database["tratamientos"] if t["id_mascota"] == id_mascota]
        if not tratamientos:
            print("No hay tratamientos registrados para esta mascota.")
            return
        for t in tratamientos:
            print(f"Fecha: {t['fecha']} | Diagnóstico: {t['descripcion']} | Medicamento: {t['medicamento']}")
    except ValueError:
        print(" Ingrese un número válido.")