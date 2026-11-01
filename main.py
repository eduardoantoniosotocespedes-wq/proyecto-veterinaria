from base_de_datos import database
from administradores import ejecutar_menu_super_admin
#creando el ligin de main(), esta funcion la llamare en la parte de main.py
def main():
    while True:
        print("""\n==================================
  VETCARE — SISTEMA VETERINARIO  
==================================
INICIAR SESIÓN""") 
        user = input("Ingrese su nombre de usuario: ")
        pas = input("Ingrese su contraseña: ")
        user_found = None
        for u in database["usuarios"]:
            if u["user_name"] == user and u["password"] == pas:
                user_found = u 
                break
        if user_found:
            print(f"\nBienvenido {user_found['user_name']} - Rol: {user_found['rol']}")
            if user_found["rol"] == "superadmin":
                    ejecutar_menu_super_admin()
    
            elif user_found["rol"] == "admin":
                    pass#administradires con acceso a todo menos a crear administradires
    
            elif user_found["rol"] == "cliente":
                    pass#el clientes solo tendra acceso a poder ver sus servicios
            else:
                print("error de roll, usuario agregado de manera incorrecta comunicarse con dios")
        else:
            print("""
///Usuario o contraseña incorrecta, intente denuevo///
            """)
main()