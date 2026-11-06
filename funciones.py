from datetime import datetime
from base_de_datos import database
import base_de_datos as bd
from base_de_datos import database
#funciones para guardado de la base de datos

#funciones para los administradores y superadministrador
def registrar_dueño():
    print("\n--- REGISTRAR NUEVO DUEÑO ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    pas = input("cree una contraseña: ")
    dueño = {"user_name": nombre,"apellido": apellido,"telefono": telefono,"direccion": direccion,"password":pas,"rol":"cliente"}
    
    database["usuarios"].append(dueño)
    bd.guardar_datos()
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
    
    elegido = cliente[int(input("¿Cuál?: "))-1]
    print("Si no quiere editar un dato, dejelo en blanco")
    elegido["user_name"] = input(f"Nuevo nombre ({elegido['user_name']}): ") or elegido["user_name"]
    elegido["apellido"] = input(f"Nuevo apellido ({elegido['apellido']}): ") or elegido["apellido"]
    elegido["telefono"] = input(f"Nuevo telefono ({elegido['telefono']}): ") or elegido["telefono"]
    elegido["direccion"] = input(f"Nueva direccion ({elegido['direccion']}): ") or elegido["direccion"]
    elegido["password"] = input("Nueva contraseña: ") or elegido['password']
    bd.guardar_datos()
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
    bd.guardar_datos()
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
    bd.guardar_datos()
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
    bd.guardar_datos()
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
    bd.guardar_datos()
    print("Eliminado con exito.")

#parte de los clientes/dueños

def ver_perfil():
    print("\n=== MI PERFIL ===")
    # Buscar al usuario actual en la base de datos
    usuario = None
    for u in database["usuarios"]:
        if u["user_name"] == bd.usuario_actual:
            usuario = u
            break
    
    if usuario:
        print(f"""| Nombre: {usuario.get('user_name','-')}
| Apellido: {usuario.get('apellido','-')} 
| Telefono: {usuario.get('telefono','-')} 
| Direccion: {usuario.get('direccion','-')}
| Rol: {usuario.get('rol','-')}
""")
    else:
        print("No se pudo encontrar el perfil.")

def mis_mascotas():
    print("\n--- MIS MASCOTAS ---")
    lista = [m for m in database["mascotas"] if m.get("dueño") == bd.usuario_actual]
    if not lista:
        print("No tienes mascotas registradas.")
    else:
        for i, m in enumerate(lista, 1):
            print(f"{i}. {m['nombre']} - {m['especie']} ({m['raza']}) - {m['edad']} años")
    
    reg = input("\n¿Quieres registrar una nueva mascota? (s/n): ").lower().strip()
    if reg == 's':
        nombre = input("Nombre de la mascota: ").strip()
        especie = input("Especie (perro/gato/otro): ").strip()
        raza = input("Raza: ").strip()
        edad = input("Edad: ").strip()

        ya_existe = False
        for m in database["mascotas"]:
            if m.get("dueño") == bd.usuario_actual and m.get("nombre", "").lower().strip() == nombre.lower():
                ya_existe = True
                break
        
        if ya_existe:
            print(f"Ya tienes registrada una mascota llamada '{nombre}'. No puedes registrarla dos veces.")
            return 

        database["mascotas"].append({"nombre": nombre, "especie": especie, "raza": raza, "edad": edad, "dueño": bd.usuario_actual})
        bd.guardar_datos()
        print(f"¡{nombre} registrada con éxito!")

def eliminar_mascota():
    print("\n--- ELIMINAR MASCOTA ---")
    lista = [m for m in database["mascotas"] if m.get("dueño") == bd.usuario_actual]
    
    if not lista:
        print("No tienes mascotas para eliminar.")
        return

    for i, m in enumerate(lista, 1):
        print(f"{i}. {m['nombre']} - {m['especie']} ({m['raza']})")

    try:
        opcion = int(input("\n¿Qué número quieres eliminar? (0 para cancelar): ").strip())
    except:
        print("Tienes que poner un número.")
        return

    if opcion == 0:
        print("Cancelado.")
        return

    if opcion < 1 or opcion > len(lista):
        print("Ese número no existe.")
        return

    mascota_a_borrar = lista[opcion - 1]
    
    confirmar = input(f"¿Seguro que quieres eliminar a {mascota_a_borrar['nombre']}? (s/n): ").lower().strip()
    if confirmar != 's':
        print("No se eliminó nada.")
        return

    # La borramos de la base de datos general
    database["mascotas"].remove(mascota_a_borrar)
    bd.guardar_datos()
    print(f"¡{mascota_a_borrar['nombre']} eliminada con éxito!")

def agendar_servicio():
    print("\n--- AGENDAR SERVICIO ---")
    mis_mascotas_list = [m for m in database["mascotas"] if m.get("dueño") == bd.usuario_actual]
    if not mis_mascotas_list:
        print("Primero registra una mascota.")
        return
    
    print("\n¿Para qué mascota quieres agendar?")
    for i in range(len(mis_mascotas_list)):
        print(f"{i+1}. {mis_mascotas_list[i]['nombre']}")

    while True:
        opcion = input("Elige el número de tu mascota: ").strip()
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(mis_mascotas_list):
                nombre_mascota = mis_mascotas_list[opcion-1]["nombre"]
                break
            else:
                print("Ese número no existe, intenta de nuevo.")
        else:
            print("Solo pon el número, por ejemplo: 1")

    print(f"Agendando para {nombre_mascota}...")


    # Pedimos hasta que ponga una fecha buena
    while True:
        fecha_texto = input("¿Qué día? (DD/MM/YYYY) Ejemplo: 10/11/2026: ")
        hora_texto = input("¿Qué hora? (HH:MM) Ejemplo: 14:30: ")

        try:
            fecha_cita = datetime.strptime(fecha_texto + " " + hora_texto, "%d/%m/%Y %H:%M")
        except:
            print("Fecha o hora inexistente. Intente denuevo")
            continue

        if fecha_cita < datetime.now():
            print("No puedes agendar una cita en el pasado.")
            continue
        
        break
    servicio = input("¿Que servicio desea?: Baño /Corte /Veterinario: ").strip()
    database["citas"].append({
        "mascota": nombre_mascota,
        "dueño": bd.usuario_actual,
        "fecha": fecha_cita.strftime("%d/%m/%Y %H:%M"),
        "servicio": servicio,
        "estado": "pendiente"
        })
    bd.guardar_datos()
    print(f"¡Cita agendada para {nombre_mascota} el {fecha_cita.strftime('%d/%m/%Y a las %H:%M')}!")

def ver_historial_mascotas():
    print("\n--- HISTORIAL DE MIS MASCOTAS ---")
    mis_citas = [c for c in database["citas"] if c.get("dueño") == bd.usuario_actual]

    if not mis_citas:
        print("Aún no tienes historial.")
        return

    for c in mis_citas:
        print(f"{c.get('fecha')} | {c.get('mascota')} | {c.get('servicio')} | Estado: {c.get('estado')}")
        
def cancelar_cita():
    print("\n--- CANCELAR CITA ---")
    mis_citas = [c for c in database["citas"] if c.get("dueño") == bd.usuario_actual and c.get("estado") == "pendiente"]

    if not mis_citas:
        print("No tienes citas pendientes para cancelar.")
        return

    print("\n¿Cúal cita quieres cancelar?")
    for i in range(len(mis_citas)):
        print(f"{i+1}. {mis_citas[i].get('fecha')} | {mis_citas[i].get('mascota')} | {mis_citas[i].get('servicio')}")

    while True:
        opcion = input("Elige el número de la cita: ").strip()
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(mis_citas):
                cita_elegida = mis_citas[opcion-1]
                break
            else:
                print("Ese número no existe, intenta de nuevo.")
        else:
            print("Solo pon el número, por ejemplo: 1")

    confirmar = input(f"¿Seguro que quieres cancelar la cita de {cita_elegida.get('mascota')} el {cita_elegida.get('fecha')}? (SI/NO): ").strip().upper()

    if confirmar == "SI":
        cita_elegida["estado"] = "Cancelada"
        bd.guardar_datos()
        print("¡Cita cancelada!")
    else:
        print("No se canceló nada.")