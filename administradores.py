from funciones import registrar_dueño, ver_dueños, editar_dueño, eliminar_dueño,registrar_administrador, ver_administrador, editar_administrador, eliminar_administrador
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
= Gestion de administradores = 
5.- Registrar Administrador
6.- Ver Administradores
7.- Editar Administrador
8.- Eliminar Administrador
9.- Cerrar Sesión 
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
                registrar_administrador()
            case "6":
                ver_administrador()
            case "7":
                editar_administrador()
            case "8":
                eliminar_administrador()
            case "9":
                print("Cerrando sesión de administrador...")
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")