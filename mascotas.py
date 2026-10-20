def ejecutar_menu_administradores():
    while True:
        print("\n==============================")
        print(" MENÚ DE ADMINISTRADORES ")
        print("==============================")
        print("1. Menu de citas para mascotas")
        print("2. Tratamiento de mascota")
        print("3. Registro de mascotas")
        print("4. Ver veterinarios")
        print("5. Cerrar sesión (Volver al menú principal)")
        
        opcion = input("Elige una opción: ")
        
        match opcion:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                print("Cerrando sesión de administrador...")
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")