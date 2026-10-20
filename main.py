from funciones import iniciar_sesion, registrar_usuario
from administrador import ejecutar_menu_administradores
from usuario import ejecutar_menu_usuarios

def main():
    while True:
        print("\n==================================")
        print("🐾 VETCARE — SISTEMA VETERINARIO 🐾")
        print("==================================")
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Salir del Sistema")
        
        opcion = input("Elige una opción: ")
        
        match opcion:
            case "1":
                usuario_actual = iniciar_sesion()
                if usuario_actual:
                    if usuario_actual["rol"] == "admin":
                        ejecutar_menu_administradores()
                    else:
                        ejecutar_menu_usuarios()
            case "2":
                registrar_usuario()
            case "3":
                print("\n¡Gracias por usar VetCare! Hasta luego. ")
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()


#prueba para ver si mi terminal tiene algo malo