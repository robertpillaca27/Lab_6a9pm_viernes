# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 20:23:39 2023

@author: USUARIO
"""

import random
import string

def generar_contrasena_segura(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_caracter_especial = False
    
    while True:
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
        
        for char in contrasena:
            if char.isupper():
                tiene_mayuscula = True
            elif char.islower():
                tiene_minuscula = True
            elif char.isdigit():
                tiene_numero = True
            elif char in string.punctuation:
                tiene_caracter_especial = True
        
        if (
            len(contrasena) >= 8 and
            #Debe incluir al menos una letra mayúscula 
            tiene_mayuscula and
            #Debe incluir al menos una letra minúscula.
            tiene_minuscula and
            tiene_numero and
            tiene_caracter_especial
        ):
            return contrasena

longitud_deseada = 8
contrasena_segura = generar_contrasena_segura(longitud=longitud_deseada)
print("Contraseña segura generada:", contrasena_segura)