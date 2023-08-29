# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 19:55:41 2023

@author: USUARIO
"""

def paises_mas_poblados(countries, num_paises=20):
    paises_ordenados_por_poblacion = sorted(countries, key=lambda x: x['population'], reverse=True)
    top_paises = paises_ordenados_por_poblacion[:num_paises]
    return top_paises

from countries_data import countries  

top_paises = paises_mas_poblados(countries, num_paises=20)

print("Los 10 o 20 países más poblados del mundo:")
for identificacion, pais in enumerate(top_paises, start=1):
    print(f"{identificacion}. {pais['name']}: {pais['population']}")