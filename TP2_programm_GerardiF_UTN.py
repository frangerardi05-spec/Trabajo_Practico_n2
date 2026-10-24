#---------------------------- Trabajo Práctico 2 de Francisco Gerardi ----------------------------#
# TP n°2: 2da entrega

# Buenas Profe Fausto, ya hice las correcciones que me mandaste en la primer entrega, espero que ahora esté todo bien. 
# Saludos, muchas gracias, y que tenga un buen día, tarde o noche.

# Importo el módulo con las funciones a utilizar:
import modulo_tragamonedas
import modulo_blackjack

from modulo_tragamonedas import iniciar_tragamonedas_virtual
from modulo_tragamonedas import validar_apuesta_min_max
from modulo_blackjack import iniciar_blackjack
from modulo_blackjack import limpiar_teclado_os

#-----------------------------------------------------#
# Declaro el saldo y la apuesta inicial
saldo = 100
apuesta = 10

#-----------------------------------------------------#
# Interfaz y operaciones del juego:

# Bucle while que encierra a todas las funciones para que se repitan hasta salir del programa:
while True and saldo > 0:
    
#-----------------------------------------------------#
# Interfaz del menú principal:
  print("#----------------------------------------#\n")
  print("     Bienvenido al menú principal")
  print("\n#----------------------------------------#")
  print("Modos seleccionables:\n")
  print("[1] Tragamonedas Virtual.")
  print("[2] Black Jack.")
  print("[3] Cambiar Apuesta.")
  print("[4] Salir del programa.")
  print("\n#----------------------------------------#")
  print(f"Su saldo actual es de [{saldo}]$.")
  print(f"Su apuesta actual es de [{apuesta}]$.")
  print("#----------------------------------------#\n")

  juego_select = input("> Modo seleccionado: ")

  match juego_select:

# Juego del Black Jack:
      case "1":
          limpiar_teclado_os()
          saldo = iniciar_tragamonedas_virtual(saldo, apuesta)

# Juego del Tragramonedas virtual:
      case "2": 
          limpiar_teclado_os()
          saldo = iniciar_blackjack(saldo, apuesta)

# Cambiar apuesta para jugar
      case "3":
          print("\n#----------------------------------------#\n")
          apuesta = int(input("Cantidad de dinero a apostar: "))
          apuesta = validar_apuesta_min_max(apuesta, saldo)
          limpiar_teclado_os()

# Salir del programa desde el menú principal:
      case "4":
          limpiar_teclado_os()
          print("Saliendo del programa...")
          print("#----------------------------------------#\n")
          print("             Fin del programa")
          print("\n#----------------------------------------#")
          break

# En caso de que el usuario coloque otro valor distinto a 1, 2, 3 o 4:
      case _:
              limpiar_teclado_os()
              print("#----------------------------------------#")
              print("Por favor, seleccionar una opción válida.")
