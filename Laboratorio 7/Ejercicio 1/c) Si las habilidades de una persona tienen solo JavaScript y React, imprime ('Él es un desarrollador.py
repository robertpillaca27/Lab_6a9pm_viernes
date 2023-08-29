# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 15:24:23 2023

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

habilidades = persona.get('skills', [])

if habilidades == ['JavaScript', 'React']:
    print("Él es un desarrollador frontend.")
elif 'Node' in habilidades and 'Python' in habilidades and 'MongoDB' in habilidades:
    print("Él es un desarrollador backend.")
elif 'React' in habilidades and 'Node' in habilidades and 'MongoDB' in habilidades:
    print("Él es un desarrollador fullstack.")
else:
    print("Título desconocido.")