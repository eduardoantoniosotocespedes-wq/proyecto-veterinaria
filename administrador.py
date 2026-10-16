def administrator():
    while True:
        print("""
============= MENU DE ADMINISTRADOR ==============
1.-Registrar usuario
2.-Mostrar usuarios
3.-Buscar usuario
4.-Modificar usuario
5.-Eliminar usuario
6.-Cerrar sesión
""")
        option = input("Responda aqui: ")
        if option.isdigit():
            option = int(option)
            match option:
                case 1:
                    print("register_user()")
                case 2:
                    print("show_user()")
                case 3:
                    print("search_user()")
                case 4:
                    print("modify_user()")
                case 5:
                    print("delete_user()")
                case 6:
                    print("===Saliendo...")
                    break
                case _:
                    print("xd")
        else:
            print("opcion no reconocida")

