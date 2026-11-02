from mascotas import ejecutar_menu_mascotas
def ejecutar_menu_clientes():
    while True:
        print("""\n==============================
  MENÚ DE DUEÑO 
==============================
1. Ver mi perfil
2. Mis mascotas
3. Agendar servicio / Cita para mi mascota
4. Ver historial de mis mascotas
5. Cerrar sesión""")
        opcion = input("Elige una opción: ")
        
        match opcion:
            case "1":
                from funciones import ver_dueños
                ver_dueños()
            case "2":
                ejecutar_menu_mascotas()
            case "3":
                print("Cerrando sesión de usuario...")
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")