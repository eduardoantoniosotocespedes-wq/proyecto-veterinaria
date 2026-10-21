from mascotas import ejecutar_menu_mascotas
def ejecutar_menu_usuarios():
    while True:
        print("\n==============================")
        print("  MENÚ DE USUARIOS ")
        print("==============================")
        print("1. Ver Dueños registrados (Modo lectura)")
        print("2. Menu para servicios de mascotas")
        print("3. Cerrar sesión (Volver al menú principal)")
        
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