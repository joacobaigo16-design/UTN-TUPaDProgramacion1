print("--- BIENVENIDO A LA ARENA ---")


#PASO 1: Configuracion del personaje (con validacion estricta)

nombre_gladiador = ""  
nombre_valido = False  

while not nombre_valido:
    nombre_gladiador = input("Nombre del Gladiador: ")
    if nombre_gladiador.isalpha():
        nombre_valido = True
    else:
        print("Error: Solo se permiten letras.")

#PASO 2: Inicializacion de estadisticas

vida_gladiador = 100         
vida_enemigo = 100            
pociones = 3                  
danio_ataque_pesado = 15      
danio_enemigo = 12            
turno_gladiador = True        
juego_activo = True          

print("\n=== INICIO DEL COMBATE ===")

#PASO 3: Ciclo de combate

while vida_gladiador > 0 and vida_enemigo > 0 and juego_activo:

    print(f"\n{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    #Validacion del menu
    opcion_valida = False  
    opcion = ""             

    while not opcion_valida:
        opcion = input("Opción: ")
        if opcion.isdigit():
            if opcion == "1" or opcion == "2" or opcion == "3":
                opcion_valida = True
            else:
                print("Error: Debe elegir una opción entre 1 y 3.")
        else:
            print("Error: Ingrese un número válido.")

    opcion_num = int(opcion) 

    perdio_turno = False       #boolean, para el caso de "Curar" sin pociones

    #Accion A: Ataque Pesado
    if opcion_num == 1:
        danio_final = float(danio_ataque_pesado)  

        if vida_enemigo < 20:
            danio_final = danio_ataque_pesado * 1.5   #golpe critico (float)
            print(">> ¡GOLPE CRÍTICO!")

        vida_enemigo -= danio_final
        print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

    #Accion B: Rafaga Veloz (usa for)
    elif opcion_num == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for golpe in range(3):
            vida_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")

    #Accion C: Curar
    elif opcion_num == 3:
        if pociones > 0:
            vida_gladiador += 30
            pociones -= 1
            print(">> Usaste una poción y recuperaste 30 puntos de vida.")
        else:
            print("¡No quedan pociones!")
            perdio_turno = True

    #Turno del enemigo
    if vida_enemigo > 0:
        vida_gladiador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

    print("\n=== NUEVO TURNO ===")

#PASO 4: Fin del juego

if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")