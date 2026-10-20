from funciones import registrar_mascota, ver_mascotas, editar_mascota, eliminar_mascota,registrar_veterinario, ver_veterinarios, editar_veterinario, eliminar_veterinario 
from funciones import crear_cita, ver_citas, modificar_cita, cancelar_cita, registrar_tratamiento, ver_tratamientos_mascota
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
                print("\n==============================")
                print(" MENU DE CITAS")
                print("==============================")
                print("1. crear cita")                   
                print("2. ver citas")
                print("3. editar citas")
                print("4. cancelar citas")
                print("5.- salir")
                res = int(input("Reponda aqui: "))
                match res:
                    case 1:
                        crear_cita()
                    case 2:
                        ver_citas()
                    case 3:
                        modificar_cita()
                    case 4:
                        cancelar_cita()
                    case 5:
                        print("Cerrando sesión de administrador...")
                        break
            case "2":
                print("\n==============================")
                print(" MENU DE TRATAMIENTO")
                print("==============================")
                print("1. registrar tratamiento")                   
                print("2. ver trataiento de mascotas")
                print("4.- salir")
                res = int(input("Reponda aqui: "))
                match res:
                    case 1:
                        registrar_tratamiento()
                    case 2:
                        ver_tratamientos_mascota()
                    case 3:
                        print("Cerrando sesión de administrador...")
                        break
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