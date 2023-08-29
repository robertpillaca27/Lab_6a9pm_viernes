import string

def limpiar_cadena(cadena):
    cadena = cadena.lower()
    caracteres_validos = string.ascii_lowercase + string.digits
    cadena_limpia = ''.join(caracter for caracter in cadena if caracter in caracteres_validos)
    return cadena_limpia

def es_palindromo(cadena):
    cadena_limpia = limpiar_cadena(cadena)
    return cadena_limpia == cadena_limpia[::-1]

frase = input('ingresar frase:')
if es_palindromo(frase):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")

