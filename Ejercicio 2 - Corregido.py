usuario = "alumno"
clave = "python123"

intentos = 1
maximo_intentos = 3

#inicio de sesion
while intentos <= maximo_intentos:

    ingrese_usuario = input(f"Intento {intentos}/3 - Usuario: ")
    ingrese_contrasena = input("Clave: ")

    if ingrese_usuario == usuario and ingrese_contrasena == clave:
        print("Acceso concedido.")
        break
    else:
        print("Error: credenciales inválidas.")

        if intentos == maximo_intentos:
            print("Cuenta bloqueada.")
            break

        intentos = intentos + 1


#si las credenciales son correctas, se muestra el menu
if ingrese_usuario == usuario and ingrese_contrasena == clave:

    while True:

        print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")

        texto_seleccion = input("Opción: ")

        if not texto_seleccion.isdigit():
            print("Error: ingrese un número válido.")

        else:
            seleccion = int(texto_seleccion)

            if seleccion < 1 or seleccion > 4:
                print("Error: opción fuera de rango.")

            elif seleccion == 1:
                print("Estado: Inscripto")

            elif seleccion == 2:

                nueva_clave = input("Nueva clave: ")

                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")

                else:
                    confirmacion_clave = input("Confirme la nueva clave: ")

                    if nueva_clave != confirmacion_clave:
                        print("Error: las contraseñas no coinciden.")
                    else:
                        clave = nueva_clave
                        print("Clave cambiada correctamente.")

            elif seleccion == 3:
                print("Programación 1")
                print("TECNICATURA UNIVERSITARIA")
                print("EN PROGRAMACIÓN")

            elif seleccion == 4:
                print("Cerrando sesión...")
                break