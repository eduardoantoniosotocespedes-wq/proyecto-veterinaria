from funciones import ver_perfil
from base_de_datos import database
import base_de_datos as bd
from datetime import datetime

#esta menu, o apartado cliente pueden tocarlo ambas, no arruinen el codigo, cambien cosas sensillas
def ejecutar_menu_clientes():
    while True:
        print("""\n==============================
  MENÚ DE DUEÑO / CLIENTE

1. Ver mi perfil
2. Mis mascotas
3. Agendar servicio / Cita para mi mascota
4. Ver historial de mis mascotas
5. Cerrar sesión""")
        opcion = input("Elige una opción: ")
        
        match opcion:
            case "1":
                ver_perfil()
            
            case "2":
                print("\n--- MIS MASCOTAS ---")
                mascotas = database.get("mascotas", [])
                # Filtrar solo las del usuario actual
                mis_mascotas = [m for m in mascotas if m.get("dueño") == bd.usuario_actual]

                if not mis_mascotas:
                    print("Aún no tienes mascotas registradas.")
                else:
                    for i, m in enumerate(mis_mascotas, 1):
                        print(f"{i}. {m['nombre']} - {m['especie']} - {m['edad']} años - Raza: {m.get('raza','-')}")

                reg = input("\n¿Quieres registrar una nueva mascota? (s/n): ").lower()
                if reg == 's':
                    nombre = input("Nombre de la mascota: ")
                    especie = input("Especie (perro/gato/otro): ")
                    raza = input("Raza: ")
                    edad = input("Edad: ")
                    database["mascotas"].append({
                        "nombre": nombre,
                        "especie": especie,
                        "raza": raza,
                        "edad": edad,
                        "dueño": bd.usuario_actual
                    })
                    print(f"Mascota {nombre} registrada con éxito.")

            case "3":
                print("\n--- AGENDAR CITA / SERVICIO ---")
                mis_mascotas = [m for m in database["mascotas"] if m.get("dueño") == bd.usuario_actual]
                if not mis_mascotas:
                    print("Primero debes registrar una mascota en la opción 2.")
                    continue
                
                print("Tus mascotas:")
                for i, m in enumerate(mis_mascotas, 1):
                    print(f"{i}. {m['nombre']}")

                try:
                    idx = int(input("Elige el número de tu mascota: ")) - 1
                    mascota_elegida = mis_mascotas[idx]
                except:
                    print("Selección inválida.")
                    continue

                print("\nServicios: 1. Consulta general | 2. Vacunación | 3. Baño | 4. Emergencia")
                servicios_map = {"1":"Consulta general","2":"Vacunación","3":"Baño","4":"Emergencia"}
                cod_serv = input("Elige servicio (1-4): ")
                servicio = servicios_map.get(cod_serv, "Consulta general")
                fecha = input("Fecha (ej: 2026-11-10): ")
                hora = input("Hora (ej: 15:00): ")

                cita = {
                    "mascota": mascota_elegida["nombre"],
                    "dueño": bd.usuario_actual,
                    "servicio": servicio,
                    "fecha": fecha,
                    "hora": hora,
                    "estado": "pendiente"
                }
                database["citas"].append(cita)
                print(f"Cita de {servicio} agendada para {mascota_elegida['nombre']} el {fecha} a las {hora}.")

            case "4":
                print("\n--- HISTORIAL CLÍNICO ---")
                mis_citas = [c for c in database["citas"] if c.get("dueño") == bd.usuario_actual]
                if not mis_citas:
                    print("Aún no hay historial ni citas registradas.")
                else:
                    for c in mis_citas:
                        print(f"- {c['fecha']} {c['hora']} | {c['mascota']} | {c['servicio']} | Estado: {c['estado']}")

            case "5":
                print("Cerrando sesión...")
                bd.usuario_actual = None
                break
            case _:
                print("Opción inválida.")