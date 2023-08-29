conjunto_interseccion = {10}
conjunto_union = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
conjunto_diferencia = {1, 2, 3, 4, 5, 6, 7, 8, 9}

tupla_interseccion = tuple(conjunto_interseccion)
tupla_union = tuple(conjunto_union)
tupla_diferencia = tuple(conjunto_diferencia)

suma_interseccion = tupla_interseccion[0] + tupla_interseccion[-1]
suma_union = tupla_union[0] + tupla_union[-1]
suma_diferencia = tupla_diferencia[0] + tupla_diferencia[-1]

print(suma_diferencia)
print(suma_union )
print(suma_diferencia)
