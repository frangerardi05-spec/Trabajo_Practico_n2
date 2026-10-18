#---------------------------- Trabajo Práctico 2 de Francisco Gerardi ----------------------------#
# TP n°2: 1era entrega

# Consultas para Fausto o el profe: Buenos días, tardes o noches profe, les paso mi trabajo práctico, y tengo una duda
# en concreto, cómo puedo hacer para que la primera carta de la banca aparezca oculta a exepción del final. Sacando eso,
# ¿El resto estaría bien?.

# Desde ya, muchas gracias, espero que tenga/n buen día, tarde y/o noche.

# Importo el módulo con las funciones a utilizar:
import modulo_tragamonedas
import modulo_blackjack

from modulo_tragamonedas import iniciar_tragamonedas_virtual
from modulo_blackjack import iniciar_blackjack
from modulo_blackjack import limpiar_teclado_os


#-----------------------------------------------------#
# Declaro el saldo inicial
saldo = 100

#-----------------------------------------------------#
# Interfaz y operaciones del juego:
print("#-----------------------------------------------------#")
print(f"""            ⚠ Avisos antes de jugar ⚠

> Su <[apuesta_ingresada]> no debe ser mayor al 
  saldo que posee.
> Su <[apuesta_ingresada]> no debe ser menor a {1}.
> Cuando su <[saldo]> llegue a {0} se terminará 
  el programa.
> Podrá salir del programa luego de una ronda en 
  cada juego o en el menú principal.
> No se guardará el "progreso" una vez cerrado 
  el programa.""")
print("#-----------------------------------------------------#")

opcion_continuar = input("Presionar el botón {Enter} para ingresar al menú: ")
limpiar_teclado_os()

#-----------------------------------------------------#
# Bucle while que encierra a todas las funciones para que se repitan hasta salir del programa:
while True and saldo > 0:

#-----------------------------------------------------#
# Interfaz del menú principal:
    print("#----------------------------------------#\n")
    print("     Bienvenido al menú principal")
    print("\n#----------------------------------------#")
    print("Modos de juego seleccionables...\n")
    print("[1] Tragamonedas Virtual")
    print("[2] Black Jack")
    print("[3] Salir del programa")
    print("\n#----------------------------------------#")
    print(f"Su saldo actual es de [{saldo}]\n#----------------------------------------#")
    juego_select = int(input("Modo de juego seleccionado: "))

    match juego_select:

# Juego del Black Jack:
        case 1:
            limpiar_teclado_os()
            saldo = iniciar_tragamonedas_virtual(saldo)

# Juego del Tragramonedas virtual:
        case 2: 
            limpiar_teclado_os()
            saldo = iniciar_blackjack(saldo)
            limpiar_teclado_os()

# Salir del programa desde el menú principal:
        case 3:
            limpiar_teclado_os()
            print("Saliendo del programa...")
            print("\n#-----------------------------------------------------#\n")
            print("Fin del programa")
            print("\n#-----------------------------------------------------#\n")
            break

# En caso de que el usuario coloque otro valor distinto a 1, 2 o 3:
        case _:
            print("\nSeleccionar una opción válida.")
            print("#----------------------------------------#\n")
            print("[1] Tragamonedas Virtual")
            print("[2] Black Jack")
            print("[3] Salir del programa")
            print("#----------------------------------------#\n")
            juego_select = int(input("Modo de juego seleccionado: "))
