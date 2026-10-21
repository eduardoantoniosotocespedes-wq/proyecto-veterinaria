from funciones import registrar_dueño, ver_dueños, editar_dueño, eliminar_dueño

def ejecutar_menu_administradores():
    while True:
        print("\n==============================")
        print(" MENÚ DE ADMINISTRADORES ")
        print("==============================")
        print("1. Registrar Dueño")
        print("2. Ver Dueños")
        print("3. Editar Dueño")
        print("4. Eliminar Dueño")
        print("5. Cerrar sesión (Volver al menú principal)")
        print("==============================")
        
        opcion = input("Elige una opción: ")
        
        match opcion:
            case "1":
                registrar_dueño()
            case "2":
                ver_dueños()
            case "3":
                editar_dueño()
            case "4":
                eliminar_dueño()
            case "5":
                print("Cerrando sesión de administrador...")
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")