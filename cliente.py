from funciones import ver_perfil, mis_mascotas, agendar_servicio, ver_historial_mascotas, eliminar_mascota, cancelar_cita
import base_de_datos as bd

#esta menu, o apartado cliente pueden tocarlo ambas, no arruinen el codigo, cambien cosas sensillas
def ejecutar_menu_clientes():
    while True:
        print("""\n==============================
  MENÚ DE DUEÑO / CLIENTE

1. Ver mi perfil
2. Mis mascotas
3. Elimina mascota
4. Agendar servicio / Cita para mi mascota
5. cancelar cita
6. Ver historial de mis mascotas
7. Cerrar sesión""")
        opcion = input("Elige una opción: ")
        
        match opcion:
            case "1":
                ver_perfil()
            
            case "2":
                mis_mascotas()

            case "3":
                eliminar_mascota()

            case "4":
                agendar_servicio()

            case "5":
                cancelar_cita()

            case "6":
                ver_historial_mascotas()
            
            case "7":
                print("Cerrando sesión...")
                bd.usuario_actual = None
                break
            case _:
                print("Opción inválida.")