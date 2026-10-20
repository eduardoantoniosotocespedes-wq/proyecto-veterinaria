from funciones import registrar_mascota, ver_mascotas, editar_mascota, eliminar_mascota,registrar_veterinario, ver_veterinarios, editar_veterinario, eliminar_veterinario 
def ejecutar_menu_mascotas():
    while True:
        print("\n==============================")
        print(" MENÚ para mascotas ")
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
                print("\n==============================")
                print(" Registro de mascotas")
                print("==============================")
                print("1. registrar mascota")                   
                print("2. ver mascota")
                print("3. editar mascotas")
                print("4. eliminar mascota")
                print("5.- salir")
                res = int(input("Reponda aqui: "))
                match res:
                    case 1:
                        registrar_mascota()
                    case 2:
                        ver_mascotas()
                    case 3:
                        editar_mascota()
                    case 4:
                        eliminar_mascota()
                    case 5:
                        print("Cerrando sesión de administrador...")
                        break
            case "4":
                print("\n==============================")
                print(" Registro de mascotas")
                print("==============================")
                print("1. registrar veterinario")                 
                print("2. ver veterinarios")
                print("3. editar veterinario")
                print("4. eliminar veterinario")
                print("5.- salir")
                res = int(input("Reponda aqui: "))
                match res:
                    case 1:
                        registrar_mascota()
                    case 2:
                        ver_mascotas()
                    case 3:
                        editar_mascota()
                    case 4:
                        eliminar_mascota()
                    case 5:
                        print("Cerrando sesión de administrador...")
                        break
            case "5":
                print("Cerrando sesión de administrador...")
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")