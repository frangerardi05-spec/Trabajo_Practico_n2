#---------#     Módulo que contiene el Black Jack para el TP_2 de Programación I   #---------#

# Módulos que importo
import random
import modulo_tragamonedas
from modulo_tragamonedas import validar_apuesta_min_max

# Función principal para el Black Jack
def iniciar_blackjack(saldo:int)->None:
    """
    Función que inicia el juego de Black Jack.

    Recibe el parámetro:
        saldo (int)
    """
    # Declaro las variables
    victoria_bj = None
    total_mano_banca = 0
    total_mano_jugador = 0

    # Declaro las listas
    mazo_cartas_figuras_comodin = ["J", "Q", "K", "A"]
    mazo_cartas_numericos = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    mazo_cartas_completo = mazo_cartas_figuras_comodin + mazo_cartas_numericos
    mano_banca = []
    mano_jugador = []

    # Muestra el menú del Black Jack
    print("#----------------------------------------#\n")
    print("     ¡¡Bienvenido al Black Jack!!")
    print("\n#----------------------------------------#")
    print(f"Su Puntaje inicial es de {saldo}.\n")
    print(f"Apuesta personalizada:\n -> Apuesta Mínima = 1\n -> Apuesta Máxima = {saldo}")
    print("\nApuesta por defecto = 10\n -> [Seleccionar '0']")
    print("\n#----------------------------------------#")

    while True:
        # Validación de apuesta
        apuesta = int(input("Ingrese total a apostar: "))
        if apuesta == 0:
            apuesta = 10
        limpiar_teclado_os()
        validar_apuesta_min_max(apuesta, saldo)

        print(f"Tu apuesta es de {apuesta}.")
        print("\nReparto las cartas...\n")
        mano_jugador = repartir_cartas_jugador(mazo_cartas_completo, mano_jugador)
        mano_banca = repartir_cartas_banca(mazo_cartas_completo, mano_banca)
        mano_jugador = repartir_cartas_jugador(mazo_cartas_completo, mano_jugador)
        mano_banca = repartir_cartas_banca(mazo_cartas_completo, mano_banca)

        total_mano_banca = definir_valores_mano(mano_banca)
        total_mano_jugador = definir_valores_mano(mano_jugador)
        
        mostrar_jugador_interfaz_BlackJack(mano_jugador) 
        mostrar_banca_interfaz_BlackJack(mano_banca)

        while True:
            print("\n#----------------------------------------#")
            print("Viendo tus cartas. Elegí...\n")
            print("[1] Seguis jugando.")
            print("[0] Te plantas.")
            eleccion = int(input("\nQue elegís: "))

            limpiar_teclado_os()
            print("#----------------------------------------#")

        # Dos condicionales por si el jugador sigue jugando o se planta
            if eleccion == 1:
                print("Sigo Jugando...\n")
                mano_jugador = repartir_cartas_banca(mazo_cartas_completo, mano_jugador)
                total_mano_jugador = definir_valores_mano(mano_jugador)
                mostrar_jugador_interfaz_BlackJack(mano_jugador)
                mostrar_banca_interfaz_BlackJack(mano_banca)
                if total_mano_jugador >= 21:
                    victoria_bj = False
                continue

            elif eleccion == 0:
                while total_mano_banca < 17:
                    print("Me planto.")
                    mano_banca = repartir_cartas_banca(mazo_cartas_completo, mano_banca)
                    total_mano_banca = definir_valores_mano(mano_banca)
                    mostrar_jugador_interfaz_BlackJack(mano_jugador)
                    mostrar_banca_interfaz_BlackJack(mano_banca)
                    break

            # En caso de calcular resultados
            limpiar_teclado_os()
            mostrar_jugador_interfaz_BlackJack(mano_jugador)
            mostrar_banca_interfaz_BlackJack(mano_banca)
            # Condicional en caso de victoria
            if (((total_mano_jugador <= 21) and (total_mano_banca < total_mano_jugador)) or
                ((total_mano_jugador <= 21) and (total_mano_banca > 21))):
                print(f"Gana el Jugador. Ganaste {apuesta * 2}.")
                apuesta = apuesta * 2
                saldo += apuesta
                victoria_bj = True
                break
            # Condicional en caso de derrota
            elif (((total_mano_jugador > 21) and (total_mano_banca <= 21)) or
                    (total_mano_banca == total_mano_jugador)):
                print(f"Gana la Banca. Perdiste {apuesta}.")
                saldo = saldo - apuesta
                victoria_bj = False
                break
            # Condicional en caso de empate
            else:
                print("Ambos perdieron. Empate. ","Push")
                victoria_bj = None
                saldo = saldo
                break

        # Condicional para cerrar el programa por si el saldo llega a 0
        if saldo == 0:
            print("\nTu saldo = 0... Fin del juego.")
            print("#----------------------------------------#")
            break

        print("#----------------------------------------#")
        print(f"Tu saldo actual es de {saldo}.\n")
        print("[1] Seguir jugando al Black Jack\n[0] Volver al menú principal\n")
        eleccion = input("¿Desea seguir jugando?: ")
        if eleccion == "1":
            continue
        elif eleccion == "0":
            break
        else:
            limpiar_teclado_os()
            while eleccion != 1 and eleccion != 0:
                print("Por favor, seleccionar una opción válida.\n")
                print(f"Tu saldo actual es de {saldo}.\n")
                print("[1] Seguir jugando al Black Jack\n[0] Volver al menú principal\n")
                eleccion = input("¿Desea seguir jugando?: ")
        limpiar_teclado_os()
    return saldo
    # Termina el programa.
#-------------------------------------------------------#
# Función para calcular el valor del As
def definir_valores_mano(mano:list, total_mano:int = 0)->int:
    """
    Función para asignarle un valor al "As
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
            continue

    for As in lista_Ases:
        if total_mano <= 10:
            As = 11
            total_mano += As
        elif total_mano > 10:
            As = 1
            total_mano += As

    for Figuras in lista_Figuras:
        Figuras = 10
        total_mano += Figuras

    return total_mano

# Función para repartir las primeras dos cartas a la banca
def repartir_cartas_banca(mazo_cartas_completo:list, mano_banca:list)->list:
    """
    Función para repartir las primeras dos cartas al jugador.

    Recibe dos parámetros:
        mazo_cartas_completo (list)     |     mano_banca (list)
    
    Retorna la mano_banca
    """
    carta_banca = mazo_cartas_completo [random.randint(0, len(mazo_cartas_completo)- 1)]
    mano_banca += [carta_banca]

    return mano_banca

# Función para repartir las primeras dos cartas al jugador
def repartir_cartas_jugador(mazo_cartas_completo:list, mano_jugador:list)->list:
    """
    Función para repartir las primeras dos cartas al jugador.

    Recibe dos parámetros:
        mazo_cartas_completo (list)     |     mano_jugador (list)
    
    Retorna la mano_jugador
    """
    carta_jugador = mazo_cartas_completo [random.randint(0, len(mazo_cartas_completo)- 1)]
    mano_jugador += [carta_jugador]
    return mano_jugador

# Función para mostrar las cartas de la banca
def mostrar_banca_interfaz_BlackJack(m_b:list)->None:
    """
    Función que sirve para mostrar la interfaz de las rondas de la banca.

    Los parámetros que utilizare serán: m_b (list) | m_j (list)
    """
    cantidad_cartas_mazo = len(m_b)
    contador = 0     

    print("--------Banca--------")
    while contador < cantidad_cartas_mazo:
        if contador + 1 < cantidad_cartas_mazo:
            print(f"     {m_b[contador]}        {m_b[contador + 1]} ")
        
        else:
            print(f"          {m_b[contador]}       ")
        contador += 2
    print("---------------------")

# Función para mostrar las cartas del jugador
def mostrar_jugador_interfaz_BlackJack(m_j:list)->None:
    """
    Función que sirve para mostrar la interfaz de las rondas del jugador.

    Los parámetros que utilizare serán: m_b (list) | m_j (list)
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
