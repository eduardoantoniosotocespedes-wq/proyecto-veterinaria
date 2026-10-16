clientes = []
mascotas = []
citas = []
historiales = []
pagos = []
veterinarios = []
inventario = []


def registrar_cliente():
    print("\n--- REGISTRAR CLIENTE ---")
    nombre = input("Nombre del dueño: ").strip()
    telefono = input("Teléfono: ").strip()
    direccion = input("Dirección: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    cliente = {
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion
    }

    clientes.append(cliente)
    print("Cliente registrado correctamente.")


def mostrar_clientes():
    print("\n--- LISTA DE CLIENTES ---")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return

    for i, cliente in enumerate(clientes, start=1):
        print(f"\nCliente {i}")
        print("Nombre:", cliente["nombre"])
        print("Teléfono:", cliente["telefono"])
        print("Dirección:", cliente["direccion"])


def registrar_mascota():
    print("\n--- REGISTRAR MASCOTA ---")
    nombre = input("Nombre de la mascota: ").strip()
    especie = input("Especie: ").strip()
    raza = input("Raza: ").strip()
    edad = input("Edad: ").strip()
    dueño = input("Nombre del dueño: ").strip()

    if not nombre or not especie or not dueño:
        print("Completa el nombre, la especie y el dueño.")
        return

    mascota = {
        "nombre": nombre,
        "especie": especie,
        "raza": raza,
        "edad": edad,
        "dueño": dueño
    }

    mascotas.append(mascota)
    print("Mascota registrada correctamente.")


def mostrar_mascotas():
    print("\n--- LISTA DE MASCOTAS ---")

    if not mascotas:
        print("No hay mascotas registradas.")
        return

    for i, mascota in enumerate(mascotas, start=1):
        print(f"\nMascota {i}")
        print("Nombre:", mascota["nombre"])
        print("Especie:", mascota["especie"])
        print("Raza:", mascota["raza"])
        print("Edad:", mascota["edad"])
        print("Dueño:", mascota["dueño"])


def buscar_mascota():
    print("\n--- BUSCAR MASCOTA ---")
    nombre = input("Nombre que deseas buscar: ").strip().lower()
    encontrada = False

    for mascota in mascotas:
        if mascota["nombre"].lower() == nombre:
            print("\nMascota encontrada")
            print("Nombre:", mascota["nombre"])
            print("Especie:", mascota["especie"])
            print("Raza:", mascota["raza"])
            print("Edad:", mascota["edad"])
            print("Dueño:", mascota["dueño"])
            encontrada = True

    if not encontrada:
        print("No se encontró esa mascota.")


def actualizar_mascota():
    print("\n--- ACTUALIZAR MASCOTA ---")
    nombre = input("Nombre de la mascota: ").strip().lower()

    for mascota in mascotas:
        if mascota["nombre"].lower() == nombre:
            print("Deja vacío un campo si no quieres cambiarlo.")

            nuevo_nombre = input("Nuevo nombre: ").strip()
            nueva_especie = input("Nueva especie: ").strip()
            nueva_raza = input("Nueva raza: ").strip()
            nueva_edad = input("Nueva edad: ").strip()

            if nuevo_nombre:
                mascota["nombre"] = nuevo_nombre
            if nueva_especie:
                mascota["especie"] = nueva_especie
            if nueva_raza:
                mascota["raza"] = nueva_raza
            if nueva_edad:
                mascota["edad"] = nueva_edad

            print("Datos actualizados.")
            return

    print("Mascota no encontrada.")


def eliminar_mascota():
    print("\n--- ELIMINAR MASCOTA ---")
    nombre = input("Nombre de la mascota: ").strip().lower()

    for mascota in mascotas:
        if mascota["nombre"].lower() == nombre:
            confirmar = input("¿Eliminar esta mascota? (s/n): ").lower()

            if confirmar == "s":
                mascotas.remove(mascota)
                print("Mascota eliminada.")
            else:
                print("Operación cancelada.")
            return

    print("Mascota no encontrada.")


def registrar_cita():
    print("\n--- REGISTRAR CITA ---")
    mascota = input("Nombre de la mascota: ").strip()
    fecha = input("Fecha (DD/MM/AAAA): ").strip()
    hora = input("Hora: ").strip()
    motivo = input("Motivo de la consulta: ").strip()

    cita = {
        "mascota": mascota,
        "fecha": fecha,
        "hora": hora,
        "motivo": motivo,
        "estado": "Pendiente"
    }

    citas.append(cita)
    print("Cita registrada correctamente.")


def mostrar_citas():
    print("\n--- LISTA DE CITAS ---")

    if not citas:
        print("No hay citas registradas.")
        return

    for i, cita in enumerate(citas, start=1):
        print(f"\nCita {i}")
        print("Mascota:", cita["mascota"])
        print("Fecha:", cita["fecha"])
        print("Hora:", cita["hora"])
        print("Motivo:", cita["motivo"])
        print("Estado:", cita["estado"])


def cambiar_estado_cita():
    mostrar_citas()

    if not citas:
        return

    try:
        numero = int(input("\nNúmero de cita: "))
        if numero < 1 or numero > len(citas):
            print("Número de cita inválido.")
            return
    except ValueError:
        print("Debes ingresar un número.")
        return

    print("1. Pendiente")
    print("2. Atendida")
    print("3. Cancelada")

    estado = input("Selecciona el nuevo estado: ")

    estados = {
        "1": "Pendiente",
        "2": "Atendida",
        "3": "Cancelada"
    }

    if estado in estados:
        citas[numero - 1]["estado"] = estados[estado]
        print("Estado actualizado.")
    else:
        print("Opción inválida.")


def registrar_historial():
    print("\n--- HISTORIAL CLÍNICO ---")
    mascota = input("Nombre de la mascota: ").strip()
    sintomas = input("Síntomas: ").strip()
    diagnostico = input("Diagnóstico: ").strip()
    tratamiento = input("Tratamiento indicado: ").strip()
    fecha = input("Fecha de atención: ").strip()

    historial = {
        "mascota": mascota,
        "sintomas": sintomas,
        "diagnostico": diagnostico,
        "tratamiento": tratamiento,
        "fecha": fecha
    }

    historiales.append(historial)
    print("Historial registrado.")


def mostrar_historiales():
    print("\n--- HISTORIALES CLÍNICOS ---")

    if not historiales:
        print("No hay historiales registrados.")
        return

    for i, historial in enumerate(historiales, start=1):
        print(f"\nHistorial {i}")
        print("Mascota:", historial["mascota"])
        print("Síntomas:", historial["sintomas"])
        print("Diagnóstico:", historial["diagnostico"])
        print("Tratamiento:", historial["tratamiento"])
        print("Fecha:", historial["fecha"])


def registrar_pago():
    print("\n--- REGISTRAR PAGO ---")
    cliente = input("Nombre del cliente: ").strip()
    concepto = input("Concepto del pago: ").strip()

    try:
        monto = float(input("Monto en Bs: "))
        if monto < 0:
            print("El monto no puede ser negativo.")
            return
    except ValueError:
        print("Ingresa un monto válido.")
        return

    pago = {
        "cliente": cliente,
        "concepto": concepto,
        "monto": monto
    }

    pagos.append(pago)
    print(f"Pago registrado: Bs {monto:.2f}")


def mostrar_pagos():
    print("\n--- REGISTRO DE PAGOS ---")

    if not pagos:
        print("No hay pagos registrados.")
        return

    total = 0

    for i, pago in enumerate(pagos, start=1):
        print(f"\nPago {i}")
        print("Cliente:", pago["cliente"])
        print("Concepto:", pago["concepto"])
        print(f"Monto: Bs {pago['monto']:.2f}")
        total += pago["monto"]

    print(f"\nTotal registrado: Bs {total:.2f}")


def registrar_veterinario():
    print("\n--- REGISTRAR VETERINARIO ---")
    nombre = input("Nombre del veterinario: ").strip()
    especialidad = input("Especialidad: ").strip()
    telefono = input("Teléfono: ").strip()

    if not nombre:
        print("El nombre es obligatorio.")
        return

    veterinario = {
        "nombre": nombre,
        "especialidad": especialidad,
        "telefono": telefono
    }

    veterinarios.append(veterinario)
    print("Veterinario registrado.")


def mostrar_veterinarios():
    print("\n--- LISTA DE VETERINARIOS ---")

    if not veterinarios:
        print("No hay veterinarios registrados.")
        return

    for i, veterinario in enumerate(veterinarios, start=1):
        print(f"\nVeterinario {i}")
        print("Nombre:", veterinario["nombre"])
        print("Especialidad:", veterinario["especialidad"])
        print("Teléfono:", veterinario["telefono"])


def registrar_producto():
    print("\n--- INVENTARIO ---")
    nombre = input("Nombre del producto: ").strip()

    try:
        cantidad = int(input("Cantidad disponible: "))
        precio = float(input("Precio por unidad en Bs: "))

        if cantidad < 0 or precio < 0:
            print("Los valores no pueden ser negativos.")
            return
    except ValueError:
        print("Ingresa una cantidad y un precio válidos.")
        return

    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }

    inventario.append(producto)
    print("Producto agregado al inventario.")


def mostrar_inventario():
    print("\n--- PRODUCTOS DISPONIBLES ---")

    if not inventario:
        print("El inventario está vacío.")
        return

    for i, producto in enumerate(inventario, start=1):
        print(f"\nProducto {i}")
        print("Nombre:", producto["nombre"])
        print("Cantidad:", producto["cantidad"])
        print(f"Precio: Bs {producto['precio']:.2f}")


def reporte_general():
    print("\n========== REPORTE GENERAL ==========")
    print("Clientes registrados:", len(clientes))
    print("Mascotas registradas:", len(mascotas))
    print("Citas registradas:", len(citas))
    print("Historiales clínicos:", len(historiales))
    print("Veterinarios registrados:", len(veterinarios))
    print("Productos en inventario:", len(inventario))

    total = sum(pago["monto"] for pago in pagos)
    print(f"Total de pagos registrados: Bs {total:.2f}")
    print("=====================================")


def menu_encargado():
    while True:
        print("""
========================================
             VETCARE
       SISTEMA VETERINARIO
========================================
          MENÚ DEL ENCARGADO

  1. Registrar cliente
  2. Mostrar clientes
  3. Registrar mascota
  4. Mostrar mascotas
  5. Buscar mascota
  6. Actualizar mascota
  7. Eliminar mascota
  8. Registrar cita
  9. Mostrar citas
 10. Cambiar estado de una cita
 11. Registrar historial clínico
 12. Mostrar historiales clínicos
 13. Registrar pago
 14. Mostrar pagos
 15. Registrar veterinario
 16. Mostrar veterinarios
 17. Agregar producto al inventario
 18. Mostrar inventario
 19. Reporte general
  0. Cerrar sesión
========================================
""")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            registrar_mascota()
        elif opcion == "4":
            mostrar_mascotas()
        elif opcion == "5":
            buscar_mascota()
        elif opcion == "6":
            actualizar_mascota()
        elif opcion == "7":
            eliminar_mascota()
        elif opcion == "8":
            registrar_cita()
        elif opcion == "9":
            mostrar_citas()
        elif opcion == "10":
            cambiar_estado_cita()
        elif opcion == "11":
            registrar_historial()
        elif opcion == "12":
            mostrar_historiales()
        elif opcion == "13":
            registrar_pago()
        elif opcion == "14":
            mostrar_pagos()
        elif opcion == "15":
            registrar_veterinario()
        elif opcion == "16":
            mostrar_veterinarios()
        elif opcion == "17":
            registrar_producto()
        elif opcion == "18":
            mostrar_inventario()
        elif opcion == "19":
            reporte_general()
        elif opcion == "0":
            print("Cerrando sesión del encargado...")
            break
        else:
            print("Opción incorrecta. Intenta nuevamente.")


if __name__ == "_main_":
    menu_encargado()