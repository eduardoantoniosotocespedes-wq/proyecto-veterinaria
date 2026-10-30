from funciones import iniciar_sesion, registrar_usuario, verificar, dueños
from administrador import ejecutar_menu_administradores
from usuario import ejecutar_menu_usuarios

def main():
    while True:
        print("""\n
==================================")
  VETCARE — SISTEMA VETERINARIO  
==================================
INICIAR SESIÓN COMO:
1. Dueño
2. Administrador
3. Usuario
4. Salir del sistema""")
        
        opcion = input("Elige una opción: ")
        
        match opcion:
            case "1":
                verificar()
            case "2":
                pass
            case "3":
                print("\n¡Gracias por usar VetCare! Hasta luego. ")
                break
            case "4":
                print("\n¡Gracias por usar VetCare! Hasta luego. ")
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()