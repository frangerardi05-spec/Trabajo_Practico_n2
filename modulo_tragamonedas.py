#---------#     Módulo que contiene el Tragamonedas para el TP_2 de Programación I   #---------#

# Módulos que importo
import random

#--------------------------------------------------------#
def iniciar_tragamonedas_virtual(saldo:int, apuesta:int = 10)->int:
    """
    Objetivo: Función que contiene el juego de "tragamonedas virtual".

    Parámetros: saldo (int) | apuesta (int)

    Retorno: El juego de tragamonedas hasta que el usuario no quiera jugar más o pierda todos los puntos.
    """

    # Declaro las variables a utilizar:
    apuesta_defecto = 10
    apuesta_min = 1

    # Utilizaré esta variable para el bucle while
    cont_juego = 1

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
    print(" Bienvenido al tragamonedas virtual")
    print("\n#----------------------------------------#")
    print(f"""Su saldo inicial es de {saldo}

Apuesta personalizada: 
    -> Apuesta Mínima = 1 
    -> Apuesta Máxima = {saldo}

Apuesta por defecto = 10 
    -> [Seleccionar '0']""")
    print("#----------------------------------------#")
    apuesta = int(input("Ingrese total a apostar: "))

    print("\n#----------------------------------------#\n")
    limpiar_teclado_os()
    while cont_juego == 1:

    # Función para cuando la apuesta es menor a la puesta mínima o cuando la apuesta es mayor a tu saldo
        apuesta = validar_apuesta_min_max(apuesta, saldo)

    #Las siglas son por como estaban puestas antes: pri_char_pantalla | seg_char_pantalla | ter_char_pantalla
        p_c_p = list_char [random.randint(0, len(list_char)- 1)]
        s_c_p = list_char [random.randint(0, len(list_char)- 1)]
        t_c_p = list_char [random.randint(0, len(list_char)- 1)]
        
        print("|",p_c_p,"|",s_c_p,"|",t_c_p,"|")

        result += [p_c_p]
        result += [s_c_p]
        result += [t_c_p]

        saldo = calcular_coincidencias(result, saldo, apuesta)
        result = []

        print("\n#----------------------------------------#")
        print("\nTu saldo es:", saldo)

    # Condicional para cerrar el programa por si el saldo llega a 0
        if saldo == 0:
            print("\nTu saldo es 0... Fin del juego.")
            print("\n#----------------------------------------#")
            break

    # Utilizo la variable cont_juego para consultar si se sigue jugando o no:
        print("Seguir jugando...\n\n[1] Si\n[0] No\n")
        cont_juego = preguntar_seguir_jugando(cont_juego)
        if cont_juego == 0:
            limpiar_teclado_os()
            break
    # Si el saldo > 0, se sigue el código con normalidad:
        limpiar_teclado_os()
        print("#----------------------------------------#")
        print("\nTu saldo es: ", saldo)
        print(f"Apuesta personalizada:\n -> Apuesta Mínima = 1\n -> Apuesta Máxima = {saldo}")
        print("\nApuesta por defecto = 10\n -> [Seleccionar '0']")
        print("\n#----------------------------------------#")

        apuesta = int(input("Ingrese total a apostar: "))
        print("\n#----------------------------------------#")
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
                print("\n¡¡Triple 7!! Saldo actual:", saldo)
            case "0":
                saldo = apuesta * 0
                print("\nPerdiste todo. Saldo actual:", saldo)
            case _:
                saldo = saldo + apuesta * 5
                print("\n¡¡Triple Coincidencia!! Saldo actual:", saldo)

    #Para las 2/3 coincidencias:
    elif result[0] == result[1] or result[0] == result[2] or result[1] == result[2]:
        saldo = saldo + apuesta * 2
        print("\n¡¡Doble Coincidencia!! Saldo actual:", saldo)

    #Para cuando no hay ninguna coincidencia:
    elif result[0] != result[1] and result[0] != result[2] and result[1] != result[2]:
        saldo = saldo - apuesta * 1
        print("\nNada... Saldo actual:", saldo)

    return saldo

#--------------------------------------------------------#
def validar_apuesta_min_max(apuesta:int, saldo:int,apuesta_min:int = 0)->int:
    """
    Función para cuando la apuesta es menor a la puesta mínima o cuando la apuesta es mayor a tu saldo se produzca un bucle while()
    hasta que se ingrese una apuesta válida.

    Recibe como parámetros:
        apuesta (int)   |   saldo (int)    |    apuesta_min (int) = 0

    Retorna la apuesta
    """
    while apuesta < apuesta_min or apuesta > saldo:
        if apuesta < apuesta_min:
            print("La apuesta mínima es de: 1\n")
            print("Tu saldo es:", saldo)
            apuesta = int(input("\nIngrese nuevamente un total a apostar: "))
            print("\n#----------------------------------------#")
            limpiar_teclado_os()
        elif apuesta > saldo:
            print("La apuesta máxima no puede ser mayor a tu saldo.\n")
            print("Tu saldo es:", saldo)
            apuesta = int(input("\nIngrese nuevamente un total a apostar: "))
            print("\n#----------------------------------------#")
            limpiar_teclado_os()
        else:
            break
    return apuesta

#--------------------------------------------------------#
def preguntar_seguir_jugando(cont_juego:str)->str:
    """"""
    # Utilizo la variable cont_juego para consultar si se sigue jugando o no:
    cont_juego = int(input("------>: "))
    print("\n#----------------------------------------#")

    match cont_juego:
        case 0:
            print("\nFin del Juego.")
            print("\n#----------------------------------------#")

        case 1:
            cont_juego = 1

        case _:
            while cont_juego != 0 and cont_juego != 1:
                print("Seleccionar las opciones válidas")
                print("Seguir jugando...\n[1] Si\n[0] No")
                cont_juego = input("------>: ")

    return cont_juego

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
