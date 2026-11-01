from funciones import registrar_dueño, ver_dueños, editar_dueño, eliminar_dueño
#menu para administradires, solo con acceso solo administradores
def ejecutar_menu_administradores():
    while True:
        print("""\n==============================
 MENÚ DE ADMINISTRADORES 
==============================
1. Registrar Dueño
2. Ver Dueños
3. Editar Dueño
4. Eliminar Dueño
5. Cerrar sesión (Volver al menú principal)
==============================""")
        
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

#menu para superadministradir, unico con acceso a todo
def ejecutar_menu_super_admin():
    while True:
        print("""\n==============================
 MENÚ DE SUPERADMINISTRADOR 
==============================
===== Gestion de dueños ====== 
1.- Registrar Dueño
2.- Ver Dueños
3.- Editar Dueño
4.- Eliminar Dueño

===== Gestion de dueños ====== 
5.- Registrar Administrador
6.- Ver Administradores
7.- Editar editar administrador
8.- Eliminar Administrador
9.- Cerrar sesión 
==============================""")
        
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
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                pass
            case "9":
                pass 
                print("Cerrando sesión de administrador...")
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")