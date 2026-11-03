from funciones import ver_perfil
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
                ver_perfil()
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                print("Cerrando sesión de usuario...")
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")