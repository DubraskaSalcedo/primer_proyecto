import sys
import json

arguments = sys.argv
if len(arguments) != 4:
    print("Por favor ingresa los argumentos correctos")
else:
    print(f"Bienvenido {arguments[1]}")
    print(type(arguments[3]))
    lista = json.loads(arguments[3])
    print(type(lista))
    print(lista)