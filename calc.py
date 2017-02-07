#!/usr/bin/python3
import sys
if (len(sys.argv) != 4):
    sys.exit("Debes introducir solo tres parametros")

_,operacion,operando1,operando2 = sys.argv
try:
    operando1 = float(operando1)
    operando2 = float(operando2)
except ValueError:
    sys.exit("Deben ser floats")

if (operacion == 'suma'):
    print(operando1 + operando2)
elif (operacion == 'resta'):
    print(operando1 - operando2)
elif (operacion == 'multiplica'):
    print(operando1 * operando2)
elif (operacion == 'divide'):
    try:
        print(operando1 / operando2)
    except ZeroDivisionError:
        print("Indeterminacion")
