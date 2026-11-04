from base_de_datos import database
from administradores import ejecutar_menu_super_admin, ejecutar_menu_administradores
from cliente import ejecutar_menu_clientes
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
            import base_de_datos as bd
            bd.usuario_actual = user_found["user_name"]
            print(f"\nBienvenido {user_found['user_name']} - Rol: {user_found['rol']}")
            if user_found["rol"] == "superadmin":
                    ejecutar_menu_super_admin()
    
            elif user_found["rol"] == "admin":
                    ejecutar_menu_administradores()
    
            elif user_found["rol"] == "cliente":
                    ejecutar_menu_clientes()
            else:
                print("error de roll, usuario agregado de manera incorrecta comunicarse con dios")
        else:
            print("""
///Usuario o contraseña incorrecta, intente denuevo///
            """)
main()