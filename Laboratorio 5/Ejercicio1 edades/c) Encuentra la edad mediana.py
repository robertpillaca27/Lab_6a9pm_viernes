
#Mediana:
edades = [19,22,19,24,20,25,26,24,25,24]
edades.sort()
longitud = len(edades)
if longitud % 2 == 1:
    mediana = edades[longitud//2]
    print(mediana)
else:
    mediana = (edades[longitud//2-1] + edades[longitud//2])/2
    print(mediana)





