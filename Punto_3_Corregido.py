#----- Ejercicio 3 -----#

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

#----- Nombre del operador -----#

operador = input("Ingrese el nombre del operador: ")
while not operador.isalpha():
    print("Error. El nombre debe contener únicamente letras.")
    operador = input("Ingrese nuevamente el nombre del operador: ")

#----- Menú principal -----#

opcion = ""
while opcion != "5":
    print("\n----- AGENDA DE TURNOS -----")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Ingrese una opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error. Debe ingresar una opción del 1 al 5.")
        opcion = input("Ingrese nuevamente la opción: ")

#----- Opción 1: reservar turno -----#

    if opcion == "1":
        print("\n1. Lunes")
        print("2. Martes")
        dia = input("Ingrese el día: ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error. Debe ingresar 1 o 2.")
            dia = input("Ingrese nuevamente el día: ")

        paciente = input("Ingrese el nombre del paciente: ")
        while not paciente.isalpha():
            print("Error. El nombre debe contener únicamente letras.")
            paciente = input("Ingrese nuevamente el nombre del paciente: ")

        reservado = False

        if dia == "1":
            if (paciente == lunes1 or paciente == lunes2 or
                    paciente == lunes3 or paciente == lunes4):
                print("El paciente ya tiene turno el lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                reservado = True
            elif lunes2 == "":
                lunes2 = paciente
                reservado = True
            elif lunes3 == "":
                lunes3 = paciente
                reservado = True
            elif lunes4 == "":
                lunes4 = paciente
                reservado = True
            else:
                print("No hay turnos disponibles para el lunes.")

        else:
            if (paciente == martes1 or paciente == martes2 or
                    paciente == martes3):
                print("El paciente ya tiene turno el martes.")
            elif martes1 == "":
                martes1 = paciente
                reservado = True
            elif martes2 == "":
                martes2 = paciente
                reservado = True
            elif martes3 == "":
                martes3 = paciente
                reservado = True
            else:
                print("No hay turnos disponibles para el martes.")

        if reservado:
            print("Turno reservado correctamente.")

#----- Opción 2: cancelar turno -----#

    elif opcion == "2":
        print("\n1. Lunes")
        print("2. Martes")
        dia = input("Ingrese el día: ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error. Debe ingresar 1 o 2.")
            dia = input("Ingrese nuevamente el día: ")

        paciente = input("Ingrese el paciente que desea cancelar: ")
        while not paciente.isalpha():
            print("Error. El nombre debe contener únicamente letras.")
            paciente = input("Ingrese nuevamente el nombre del paciente: ")

        cancelado = False

        if dia == "1":
            if paciente == lunes1:
                lunes1 = ""
                cancelado = True
            elif paciente == lunes2:
                lunes2 = ""
                cancelado = True
            elif paciente == lunes3:
                lunes3 = ""
                cancelado = True
            elif paciente == lunes4:
                lunes4 = ""
                cancelado = True
            else:
                print("El paciente no tiene turno el lunes.")

        else:
            if paciente == martes1:
                martes1 = ""
                cancelado = True
            elif paciente == martes2:
                martes2 = ""
                cancelado = True
            elif paciente == martes3:
                martes3 = ""
                cancelado = True
            else:
                print("El paciente no tiene turno el martes.")

        if cancelado:
            print("Turno cancelado correctamente.")

#----- Opción 3: ver agenda del día-----#

    elif opcion == "3":
        print("\n1. Lunes")
        print("2. Martes")
        dia = input("Ingrese el día: ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error. Debe ingresar 1 o 2.")
            dia = input("Ingrese nuevamente el día: ")

        if dia == "1":
            print("\n----- AGENDA DEL LUNES -----")
            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", lunes1)
            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", lunes2)
            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", lunes3)
            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print("Turno 4:", lunes4)

        else:
            print("\n----- AGENDA DEL MARTES -----")
            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", martes1)
            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", martes2)
            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", martes3)

#----- Opción 4: resumen general -----#

    elif opcion == "4":
        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print("\n----- RESUMEN GENERAL -----")
        print("Lunes:", ocupados_lunes, "ocupados y", disponibles_lunes, "disponibles")
        print("Martes:", ocupados_martes, "ocupados y", disponibles_martes, "disponibles")

        if ocupados_lunes > ocupados_martes:
            print("El lunes tiene más turnos ocupados.")
        elif ocupados_martes > ocupados_lunes:
            print("El martes tiene más turnos ocupados.")
        else:
            print("Hay empate entre lunes y martes.")

# Opción 5: cerrar sistema --
    else:
        print("Sistema cerrado.")
