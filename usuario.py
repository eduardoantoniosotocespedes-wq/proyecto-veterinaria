def ejecutar_menu_usuarios():
    while True:
        print("\n==============================")
        print("  MENÚ DE USUARIOS ")
        print("==============================")
        print("1. Ver Dueños registrados (Modo lectura)")
        print("2. [Espacio para que Persona 2 y 3 agreguen funciones de Mascotas/Citas]")
        print("3. Cerrar sesión (Volver al menú principal)")
        
        opcion = input("Elige una opción: ")
        
        match opcion:
            case "1":
                from funciones import ver_dueños
                ver_dueños()
            case "2":
                print("Funciones en desarrollo por mis compañeras...")
            case "3":
                print("Cerrando sesión de usuario...")
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")