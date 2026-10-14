print("==============================")
print("  VETCARE ")
print(" Sistema de Gestión Veterinaria")
print("==============================")
usuario_correcto = "admin"
contrasena_correcta = "1234"
intentos = 3
while intentos > 0:
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        print("\n¡Bienvenido al sistema VetCare!")
        print("Inicio de sesión exitoso.")
        break
    else:
        intentos = intentos - 1
        print("Usuario o contraseña incorrectos.")
        print("Intentos restantes:", intentos)
if intentos == 0:
    print("Acceso bloqueado. Intente nuevamente más tarde.")
    print("tengo pelos en los pesones, lo digo yo carolina, esta es la rama carolina por ende yo carolina tengo pelos en los pesones XD")