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

#funciones para los clientes
def ver_perfil():
    print("\n=== MI PERFIL ===")
    print(f"""| Nombre: {["user_name"]}
| Apellido: {["apellido"]} 
| Telefono: {["telefono"]} 
| Direccion: {["direccion"]}
""")

def mis_mascotas():
    pass

def agendar_servicio():
    pass

def ver_historial_mascotas():
    pass 