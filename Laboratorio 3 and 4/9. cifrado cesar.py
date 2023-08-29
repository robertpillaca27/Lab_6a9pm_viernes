palabra = input('Ingrese una palabra o frase: ')

lista_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
texto_cifrado = []

for letra in palabra: 
        if letra in lista_letras:
            indice = lista_letras.index(letra)
            indice_siguiente = indice + 3
            texto_cifrado.append(lista_letras[indice_siguiente])

print('Texto cifrado: ')
print(''.join(texto_cifrado))
