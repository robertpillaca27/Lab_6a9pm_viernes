# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 15:24:21 2023

@author: USUARIO
"""

persona = {
 'first_name': 'Edem',
 'last_name': 'Terraza',
 'age': 31,
 'country': 'Peru',
 'is_married': True, #
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '02210'
 }
}

if 'skills' in persona:
    habilidades = persona['skills']
    cantidad_habilidades = len(habilidades)
    if cantidad_habilidades > 0:
        habilidad_del_medio = habilidades[cantidad_habilidades // 2]
        print("Habilidad del medio:", habilidad_del_medio)
    else:
        print("No se encontraron habilidades.")