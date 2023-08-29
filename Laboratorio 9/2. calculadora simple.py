# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 19:12:33 2023

@author: USUARIO
"""

def resta(a, b):
    return a - b

def suma(a,b):
    return a+b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def main():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ")

        if operacion == "+":
            resultado = suma(num1, num2)
        elif operacion == "-":
            resultado = resta(num1, num2)
        elif operacion == "*":
            resultado = multiplicacion(num1, num2)
        elif operacion == "/":
            resultado = division(num1, num2)
        else:
            print("Operación no válida. Por favor ingrese +, -, *, o /.")
            return

        print(f"El resultado es: {resultado:.2f}")

    except ValueError:
        print("Entrada incorrecta. Por favor ingrese números válidos.")

    except ZeroDivisionError as e:
        print(e)

if __name__ == "__main__":
    main()
