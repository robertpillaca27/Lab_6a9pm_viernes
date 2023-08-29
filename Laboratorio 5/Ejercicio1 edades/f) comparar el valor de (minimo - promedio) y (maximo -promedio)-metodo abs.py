
edades = [19,22,19,24,20,25,26,24,25,24]

edad_maxima = max(edades)
edad_minima = min(edades)

promedio_edades = sum(edades) / len(edades)

diferencia_minimo = abs(edad_minima - promedio_edades)
diferencia_maximo = abs(edad_maxima - promedio_edades)

# Comparar las diferencias utilizando el valor absoluto
if diferencia_minimo > diferencia_maximo:
    print("La diferencia entre mínimo y promedio es mayor.")
elif diferencia_maximo > diferencia_minimo:
    print("La diferencia entre máximo y promedio es mayor.")
else:
    print("Las diferencias son iguales.")


