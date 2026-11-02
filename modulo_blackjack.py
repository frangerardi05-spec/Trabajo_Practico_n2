#---------#     Módulo que contiene el Black Jack para el TP_2 de Programación I   #---------#

# Módulos que importo
import random
from modulo_tragamonedas import validar_apuesta_min_max
from modulo_tragamonedas import preguntar_seguir_jugando

# Función principal para el Black Jack
def iniciar_blackjack(saldo:int, apuesta:int)->int:
    """
    Función que inicia el juego de Black Jack.

    Recibe el parámetro:
        saldo (int)     |     apuesta(int)
    
    Retorna el saldo modificado
    """
    # Declaro las variables
    total_mano_banca = 0
    total_mano_jugador = 0
    continua_juego = True

    # Creo el mazo de cartas completo
    mazo_cartas_completo = crear_mazo_cartas()

    # Muestra el menú del Black Jack
    print("#----------------------------------------#\n")
    print("     ¡¡Bienvenido al Black Jack!!")
    print("\n#----------------------------------------#")
    print(f"Su Saldo es de {saldo}$.")
    print(f"Su Apuesta Actual es de {apuesta}$.")
    print("#----------------------------------------#")

    input("Presionar el botón {Enter} para empezar a jugar: ")

    limpiar_teclado_os()
 
    while True:
        # Vacío las manos para las partidas nuevas posteriores a haber jugado al menos una vez.
        mano_banca = []
        mano_jugador = []

        # Validación de apuesta
        apuesta = validar_apuesta_min_max(apuesta, saldo)

        # Resto la apuesta ya validada
        saldo = saldo - apuesta

        print(f"Tu apuesta es de {apuesta}.")
        print("#----------------------------------------#\n")
        print("Reparto las cartas...\n")

        mano_jugador = repartir_cartas(mazo_cartas_completo, mano_jugador)
        mano_jugador = repartir_cartas(mazo_cartas_completo, mano_jugador)
        mano_banca = repartir_cartas(mazo_cartas_completo, mano_banca)
        mano_banca = repartir_cartas(mazo_cartas_completo, mano_banca)

        total_mano_banca = definir_valores_mano(mano_banca)
        total_mano_jugador = definir_valores_mano(mano_jugador)

        mostrar_jugador_interfaz_BlackJack(mano_jugador) 
        mostrar_banca_interfaz_BlackJack(mano_banca, False)

        while True:
            continua_juego = preguntar_seguir_jugando(continua_juego, True)

            # Dos condicionales por si el jugador sigue jugando o se planta
            if continua_juego == True:
                limpiar_teclado_os()
                mano_jugador = repartir_cartas(mazo_cartas_completo, mano_jugador)
                total_mano_jugador = definir_valores_mano(mano_jugador)
                mostrar_jugador_interfaz_BlackJack(mano_jugador)
                mostrar_banca_interfaz_BlackJack(mano_banca, False)
                if total_mano_jugador > 21: 
                    continua_juego = False
                    limpiar_teclado_os()
                    print("Me pasé de 21...")
                else:
                    continue

            elif continua_juego == False:
                while True:
                    limpiar_teclado_os()
                    if total_mano_banca < 17:
                        mano_banca = repartir_cartas(mazo_cartas_completo, mano_banca)
                        mostrar_jugador_interfaz_BlackJack(mano_jugador)
                        mostrar_banca_interfaz_BlackJack(mano_banca)
                        total_mano_banca = definir_valores_mano(mano_banca)
                    elif total_mano_banca >= 17:
                        break

            mostrar_jugador_interfaz_BlackJack(mano_jugador)
            mostrar_banca_interfaz_BlackJack(mano_banca)

            # Variable para definir el resultado de la partida
            resultado = definir_resultados_blacjack(total_mano_jugador, total_mano_banca)
            
            if resultado == "victoria":
                print(f"Gana el Jugador. Ganaste {apuesta}$.")
                saldo = saldo + apuesta * 2

            elif resultado == "derrota":
                print(f"Gana la Banca. Perdiste {apuesta}$.")

            else:
                print("Empate. Push: se te devuelve la apuesta.")
                saldo = saldo + apuesta

            break

        # Condicional para cerrar el programa por si el saldo llega a 0
        if saldo == 0:
            print("\nTu saldo es de 0... Fin del juego.")
            print("#----------------------------------------#")
            break

        print("#----------------------------------------#")
        print(f"Tu saldo actual es de {saldo}$.")
        print("#----------------------------------------#")

        continua_juego = preguntar_seguir_jugando(continua_juego)
        if continua_juego == False:
            break

        limpiar_teclado_os()

        print("#----------------------------------------#")
        print(f"-> Tu Apuesta es de {apuesta}$.\n")
        print(f"-> Tu Saldo Actual es de {saldo}$.")
        print("#----------------------------------------#")

    return saldo

#-------------------------------------------------------#
# Función para calcular el valor del As
def definir_valores_mano(mano:list, total_mano:int = 0)->int:
    """
    Función para asignarle un valor a las cartas de la mano del jugador y de la banca.

    Recibe como parámetros: 
        mano (list)    |   total_mano (int)

    Retorna el total de la mano sumada.
    """
    lista_Ases = []
    lista_Figuras = []

    for carta in mano:
        if carta == "A":
            lista_Ases += carta
        elif carta == "J":
            lista_Figuras += carta
        elif carta == "Q":
            lista_Figuras += carta
        elif carta == "K":
            lista_Figuras += carta
        else:
            total_mano += carta

    for Figuras in lista_Figuras:
        Figuras = 10
        total_mano += Figuras

    for As in lista_Ases:
        As = 1
        if total_mano <= 10:
            As = 11
        total_mano += As

    return total_mano

# Función para repartir las cartas
def repartir_cartas(mazo_cartas_completo:list, mano:list)->list:
    """
    Función que reparte una carta al azar del mazo a la mano del jugador o de la banca.
    Las cartas repartidas quedan marcadas con "X" para que no vuelvan a salir.
    Si todas las cartas están usadas, vuelve a armar el mazo.

    Recibe dos parámetros:
        mazo_cartas_completo (list)     |     mano (list)

    Retorna la mano con la carta nueva agregada.
    """
    if cuantificar_cartas_usadas(mazo_cartas_completo) == len(mazo_cartas_completo):
        mazo_nuevo = crear_mazo_cartas()
        posicion_indice = 0
        while posicion_indice < len(mazo_cartas_completo):
            mazo_cartas_completo[posicion_indice] = mazo_nuevo[posicion_indice]
            posicion_indice += 1

    indice = random.randint(0, len(mazo_cartas_completo) - 1)
    while mazo_cartas_completo[indice] == "X":
        indice = random.randint(0, len(mazo_cartas_completo) - 1)

    carta = mazo_cartas_completo[indice]
    marcar_carta_usada(mazo_cartas_completo, indice)
    
    mano += [carta]

    return mano

# Función que determina los resultado de la partida de Black Jack
def definir_resultados_blacjack(total_jugador: int, total_banca: int)->str:
    """
    Función que declara si en el resultado de la partida de Blackjack el jugador salió con una victoria, derrota o empate.

    Recibe como parámetros:
        total_jugador (int)     |      total_banca (int)

    Retorna como mensaje el resultado de la partida para el jugador.
    """
    if total_jugador > 21:     
        resultado = "derrota"
    elif total_banca > 21:          
        resultado = "victoria"
    elif total_jugador > total_banca:  
        resultado = "victoria"
    elif total_jugador < total_banca:
        resultado = "derrota"
    else:                       
        resultado = "empate"
    return resultado

# Función que crea el mazo de cartas completo cuando no hay cartas
def crear_mazo_cartas()->list:
    """
    Función que crea el mazo de cartas completo cuando no hay cartas.

    Retorna el mazo de cartas completo.
    """
    mazo_cartas_completo = []
    mazo_cartas_figuras_comodin = ["J", "Q", "K", "A"] * 4
    mazo_cartas_numericos = [2, 3, 4, 5, 6, 7, 8, 9, 10] * 4

    mazo_cartas_completo = mazo_cartas_figuras_comodin + mazo_cartas_numericos

    return mazo_cartas_completo

# Función que remueve las cartas utilizadas
# Función que marca (tacha) una carta usada
def marcar_carta_usada(mazo_cartas_completo:list, indice:int)->None:
    """
    Función que tacha con "X" la carta que está en la posición indicada del mazo.

    Recibe como parámetros:
        mazo_cartas_completo (list)   |   indice (int)
    """
    mazo_cartas_completo[indice] = "X"

# Función que marca las cartas que ya salieron 
def cuantificar_cartas_usadas(mazo_cartas_completo:list)->int:
    """
    Función que se encarga de contar la cantidad de cartas usadas.

    Recibe como parámetro:
        mazo_cartas_completo (list)

    Retorna la cantidad de cartas utilizadas.
    """
    contador_cartas_usadas = 0
    for elemento in mazo_cartas_completo:
        if elemento == "X":
            contador_cartas_usadas += 1

    return contador_cartas_usadas

# Función para mostrar las cartas de la banca
def mostrar_banca_interfaz_BlackJack(m_b:list, muestro_carta:bool = True)->None:
    """
    Función que sirve para mostrar la interfaz de la mano de la banca. Tiene un parámetro opcional, que define si la banca muestra o no su primera carta (True = Si | False = No)

    Los parámetros que a utilizar son: 
        m_b (list)     |    muestro_carta (bool)
    """
    cantidad_cartas_mazo = len(m_b)
    contador = 0     

    print("--------Banca--------")
    while contador < cantidad_cartas_mazo and muestro_carta == True:
        if contador + 1 < cantidad_cartas_mazo:
            print(f"     {m_b[contador]}        {m_b[contador + 1]} ")
        
        else:
            print(f"          {m_b[contador]}       ")
        contador += 2
    while contador < cantidad_cartas_mazo and muestro_carta == False:
        if contador + 1 < cantidad_cartas_mazo:
            print(f"     ?        {m_b[contador + 1]} ")
        
        else:
            print(f"          {m_b[contador]}       ")
        contador += 2
    print("---------------------")

# Función para mostrar las cartas del jugador
def mostrar_jugador_interfaz_BlackJack(m_j:list)->None:
    """
    Función que sirve para mostrar la interfaz de las rondas del jugador.

    Recibo como parámetro: 
        m_j (list)
    """
    cantidad_cartas_mazo = len(m_j)
    contador = 0     

    print("-------Jugador-------")
    while contador < cantidad_cartas_mazo:
        if contador + 1 < cantidad_cartas_mazo:
            print(f"     {m_j[contador]}        {m_j[contador + 1]} ")
        
        else:
            print(f"          {m_j[contador]}       ")
        contador += 2
    print("---------------------")

# Función para limpiar el teclado de la terminal:
def limpiar_teclado_os()->None:
    """
    Objetivo: Función con el {import os} que al convocarlo sirve para limpiar el teclado según el OS del usuario sin necesidad de repetir código.
    """
    import os 

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
