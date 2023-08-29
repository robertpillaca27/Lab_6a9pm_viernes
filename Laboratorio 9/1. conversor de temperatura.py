# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 19:11:23 2023

@author: USUARIO
"""

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    try:
        temperatura = float(input("Ingrese la temperatura: "))
        unidad = input("Ingrese la unidad de temperatura (C o F): ").upper()

        if unidad == "C":
            temperatura_convertida = celsius_to_fahrenheit(temperatura)
            unidad_convertida = "Fahrenheit"
        elif unidad == "F":
            temperatura_convertida = fahrenheit_to_celsius(temperatura)
            unidad_convertida = "Celsius"
        else:
            print("Unidad de temperatura no válida. Por favor ingrese 'C' o 'F'.")
            return

        print(f"La temperatura convertida es: {temperatura_convertida:.2f} {unidad_convertida}")

    except ValueError:
        print("Entrada incorrecta. Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()
