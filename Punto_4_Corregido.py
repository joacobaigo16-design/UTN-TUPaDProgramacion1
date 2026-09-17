# ----- Ejercicio 4 -----#
 
#----- Nombre del agente -----#

nombre = input("Ingrese el nombre del agente: ")

while not nombre.isalpha():
    print("Error. El nombre debe contener solamente letras.")
    nombre = input("Ingrese nuevamente el nombre del agente: ")

#----- Variables iniciales -----#

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

#----- Variables de control -----#

forzar_seguidas = 0
bloqueado = False

print()
print("----- ESCAPE ROOM: LA BÓVEDA -----")
print("Bienvenido, agente", nombre)

#----- Ciclo principal del juego -----#

while (energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado):

    print()
    print("----- ESTADO ACTUAL -----")
    print("Energía:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)

    if alarma:
        print("Alarma: ACTIVADA")
    else:
        print("Alarma: DESACTIVADA")

    print()
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Ingrese una opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error. Debe ingresar una opción del 1 al 3.")
        opcion = input("Ingrese nuevamente la opción: ")

#----- Opción 1: forzar cerradura -----#

    if opcion == "1":
        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        print()
        print("Perdiste 20 puntos de energía y 2 de tiempo.")

#----- Regla contra tres intentos seguidos -----#

        if forzar_seguidas >= 3:
            alarma = True
            print("La cerradura se trabó.")
            print("La alarma se activó y no abriste la cerradura.")

        else:
             
#----- Riesgo de alarma cuando la energía es menor que 40 -----#

            if energia < 40 and not alarma:
                riesgo = input("Energía baja. Ingrese un número del 1 al 3: ")

                while (not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3):
                    print("Error. Debe ingresar un número del 1 al 3.")
                    riesgo = input("Ingrese nuevamente un número del 1 al 3: ")

                if riesgo == "3":
                    alarma = True
                    print("La alarma se activó.")

#----- Abre solamente si la alarma está desactivada -----#

            if not alarma:
                cerraduras_abiertas += 1
                print("Abriste una cerradura.")
            else:
                print("No pudiste abrir la cerradura por la alarma.")

#----- Opción 2: hackear panel -----#

    elif opcion == "2":
        energia -= 10
        tiempo -= 3
        forzar_seguidas = 0

        print()
        print("Comenzaste a hackear el panel.")

        for paso in range(1, 5):
            codigo_parcial += "A"
            print("Paso", paso, "de 4")
            print("Código parcial:", codigo_parcial)

        print("Perdiste 10 puntos de energía y 3 de tiempo.")

        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("El código alcanzó 8 caracteres.")
                print("Abriste una cerradura automáticamente.")

#----- Opción 3: descansar -----#

    elif opcion == "3":
        forzar_seguidas = 0
        energia += 15
        tiempo -= 1

#----- La energía no puede superar 100 -----#

        if energia > 100:
            energia = 100

        print()
        print("Recuperaste energía y perdiste 1 de tiempo.")

#----- Penalización si la alarma está activada -----#

        if alarma:
            energia -= 10
            print("La alarma te hizo perder 10 puntos de energía extra.")

#----- Comprobar el bloqueo por alarma -----#

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True
        print()
        print("El sistema se bloqueó por la alarma.")

#----- Resultado final -----#

print()
print("----- FIN DEL JUEGO -----")

if cerraduras_abiertas == 3:
    print("¡VICTORIA!")
    print("Agente", nombre, "abrió las 3 cerraduras.")

elif bloqueado:
    print("DERROTA.")
    print("La bóveda se bloqueó por la alarma.")

else:
    print("DERROTA.")
    print("Te quedaste sin energía o sin tiempo.")