#---------#     Módulo que contiene el Tragamonedas para el TP_2 de Programación I   #---------#

# Módulos que importo
import random

#--------------------------------------------------------#
def iniciar_tragamonedas_virtual(saldo:int, apuesta:int)->int:
    """
    Objetivo: Función que contiene el juego de "tragamonedas virtual".

    Parámetros: saldo (int) | apuesta (int)

    Retorno: El juego de tragamonedas hasta que el usuario no quiera jugar más o pierda todos los puntos.
    """

    # Declaro las variables a utilizar:
    apuesta_defecto = 10
    apuesta_min = 1

    # Utilizaré esta variable para el bucle while
    continua_juego = True

    # Declaro las listas que utilizaré:
    result = []
    list_char = ["A", "B", "C", "D", "E", "0", "7"]

    # Para aclarar los premios: 
        # Triple 7: 
            #   apuesta * 10
        # Triple carácter: 
            #   apuesta * 5
        # Triple 0: 
            #   apuesta * 0
        # Doble carácter:
            #   apuesta * 2
        # Ninguna coincidencia: 
            #   apuesta * 1
    
    # Interfaz y código del Tragamonedas:
    print("#----------------------------------------#\n")
    print(" ¡¡Bienvenido al Tragamonedas Virtual!!")
    print("\n#----------------------------------------#")
    print(f"Su Saldo es de {saldo}$.")
    print(f"Su Apuesta Actual es de {apuesta}$.")
    print("#----------------------------------------#")

    opcion_continuar = input("Presionar el botón {Enter} para empezar a jugar: ")
    print("#----------------------------------------#")
    limpiar_teclado_os()
    while continua_juego == True:

    # Función para cuando la apuesta es menor a la puesta mínima o cuando la apuesta es mayor a tu saldo
        apuesta = validar_apuesta_min_max(apuesta, saldo)

    #Las siglas son por como estaban puestas antes: pri_char_pantalla | seg_char_pantalla | ter_char_pantalla
        p_c_p = list_char [random.randint(0, len(list_char)- 1)]
        s_c_p = list_char [random.randint(0, len(list_char)- 1)]
        t_c_p = list_char [random.randint(0, len(list_char)- 1)]

        print("#----------------------------------------#")
        print("|",p_c_p,"|",s_c_p,"|",t_c_p,"|","\n")

        result += [p_c_p]
        result += [s_c_p]
        result += [t_c_p]

        saldo = calcular_coincidencias(result, saldo, apuesta)
        result = []

        print("#----------------------------------------#")
        print(f"-> Tu Apuesta es de {apuesta}$.\n")
        print(f"-> Tu Saldo Actual es de {saldo}$.")
        print("#----------------------------------------#")

    # Condicional para cerrar el programa por si el saldo llega a 0
        if saldo == 0:
            print("\nTu Saldo es 0... Fin del juego.")
            print("\n#----------------------------------------#")
            break

    # Utilizo la variable continua_juego para consultar si se sigue jugando o no:
        continua_juego = preguntar_seguir_jugando(continua_juego)
        if continua_juego == False:
            break

        limpiar_teclado_os()
    return saldo

#--------------------------------------------------------#
def calcular_coincidencias(result:list, saldo:int, apuesta:int)->int:
    """
    Función que tiene como objetivo el calcular las coincidencias del tragamonedas, actualizando el valor del saldo
    en base a la apuesta realizada.

    Recibe como parámetros:
        result (list)   |   saldo (int)   |   apuesta (int)
    
    Retorna el saldo
    """
    #Para las 3/3 coincidencias:
    if result[0] == result[1] and result[0] == result[2]:
        match result[0]:
            case "7":
                saldo = saldo + apuesta * 10
                print(f"¡¡Triple 7!! Saldo actual: +{apuesta*10}$")
            case "0":
                print("Perdiste todo.")
                print(f"Saldo anterior: {saldo}")
                saldo = apuesta * 0
                print(f"Saldo actual: {apuesta*0}$")
            case _:
                saldo = saldo + apuesta * 5
                print(f"¡¡¡Triple Coincidencia!!! Saldo actual: +{apuesta*5}$")

    #Para las 2/3 coincidencias:
    elif result[0] == result[1] or result[0] == result[2] or result[1] == result[2]:
        saldo = saldo + apuesta * 2
        print(f"¡¡Doble Coincidencia!! Saldo actual: +{apuesta*2}$")

    #Para cuando no hay ninguna coincidencia:
    elif result[0] != result[1] and result[0] != result[2] and result[1] != result[2]:
        saldo = saldo - apuesta * 1
        print("Nada...")

    return saldo

#--------------------------------------------------------#
def validar_apuesta_min_max(apuesta:int, saldo:int,apuesta_min:int = 1)->int:
    """
    Función para cuando la apuesta es menor a la puesta mínima o cuando la apuesta es mayor a tu saldo se produzca un bucle while()
    hasta que se ingrese una apuesta válida.

    Recibe como parámetros:
        apuesta (int)   |   saldo (int)    |    apuesta_min (int) = 0

    Retorna la apuesta
    """
    while apuesta < apuesta_min or apuesta > saldo:
        print("#----------------------------------------#")
        if apuesta < apuesta_min:
            print("La apuesta mínima es de: 1\n")
            print("Tu saldo es:", saldo)
            apuesta = int(input("\nIngrese nuevamente un total a apostar: "))
            print("\n#----------------------------------------#")
        elif apuesta > saldo:
            print("La apuesta máxima no puede ser mayor a tu saldo.\n")
            print("Tu saldo es:", saldo)
            apuesta = int(input("\nIngrese nuevamente un total a apostar: "))
            print("\n#----------------------------------------#")
        else:
            break
    limpiar_teclado_os()
    return apuesta

#--------------------------------------------------------#
def preguntar_seguir_jugando(continua_juego:bool, pregunta_partida:bool = False)->bool:
    """
    Función que tiene como objetivo el preguntar si se sigue jugando, si se vuelve al menú principal; o si te plantas o seguis jugando.

    Recibe dos parámetros, uno de ellos opcional:
        continua_juego (bool)      |    pregunta_partida (bool) = False

    Retorna como un booleano el si continuar el juego o no.
    """
    # Utilizo la variable cont_juego para consultar si se sigue jugando o no:
    if pregunta_partida == False:
        print("\n> Presionar {Enter} para continuar jugando")
        eleccion = input("  o ingresar 'S' para volver al menú principal: ")

        match eleccion:
            case "s":
                continua_juego = False
                limpiar_teclado_os()
                print("Volviendo al menú principal...")

            case "S":
                continua_juego = False
                limpiar_teclado_os()
                print("Volviendo al menú principal...")

            case _:
                continua_juego = True

    elif pregunta_partida == True:
        print("\n#----------------------------------------#")
        print("Viendo tus opciones. Elegí...")
        print("\n> Seguís jugando (Presionar {Enter})")
        eleccion = input("  o te plantas (Ingresar 'P'): ")
        print("\n#----------------------------------------#")

        match eleccion:
            case "p":
                continua_juego = False
                print("Me planto.")

            case "P":
                continua_juego = False
                print("Me planto")

            case _:
                continua_juego = True
                print("Sigo jugando. Dame otra carta.")

    return continua_juego

#--------------------------------------------------------#
def limpiar_teclado_os()->None:
    """
    Objetivo: Función con el {import os} que al convocarlo sirve para limpiar el teclado según el OS del usuario sin necesidad de repetir código.
    """
    import os 

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
