import sys

from calculadora import sumar, restar

arguments = sys.argv

if len(arguments) != 4:
    print("Por favor ingresa los argumentos correctos")
elif arguments[1] == "restar":
    print(f"La resta da {restar(int(arguments[2]), int(arguments[3]))}")
elif arguments[1] == "sumar":
    print(f"La suma da {sumar(int(arguments[2]), int(arguments[3]))}")