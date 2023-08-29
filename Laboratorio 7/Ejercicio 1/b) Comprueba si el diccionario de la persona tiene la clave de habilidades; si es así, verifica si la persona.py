# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 15:24:22 2023

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

if 'skills' in persona and 'Python' in persona['skills']:
    print("La persona tiene la habilidad 'Python'.")
else:
    print("La persona no tiene la habilidad 'Python'.")
