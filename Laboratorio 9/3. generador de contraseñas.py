# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 19:15:25 2023

@author: USUARIO
"""
import string
import random

def generar_contrasena(longitud, mayusculas, minusculas, numeros, especiales):
    caracteres = ""
    if mayusculas: caracteres += string.ascii_uppercase
    if minusculas: caracteres += string.ascii_lowercase
    if numeros: caracteres += string.digits
    if especiales: caracteres += string.punctuation

    if not caracteres or longitud <= 0:
        raise ValueError("Parámetros inválidos")

    return ''.join(random.choice(caracteres) for _ in range(longitud))

def main():
    try:
        longitud = int(input("Longitud de la contraseña: "))
        mayusculas = input("Incluir mayúsculas (si/no): ").lower() == 'si'
        minusculas = input("Incluir minúsculas (si/no): ").lower() == 's'
        numeros = input("Incluir números (s/n): ").lower() == 's'
        especiales = input("Incluir caracteres especiales (s/n): ").lower() == 's'

        contrasena = generar_contrasena(longitud, mayusculas, minusculas, numeros, especiales)
        print(f"Contraseña generada: {contrasena}")

    except ValueError:
        print("Entrada inválida. Por favor, ingrese valores válidos.")

if __name__ == "__main__":
    main()
