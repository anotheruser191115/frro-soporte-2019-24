# Implementar la función es_palindromo(), que devuelva un booleano en base a
# si palabra se lee igual de corrido como al revés.


# Ejemplos: arenera, radar, ojo, oso, salas.
# Resolver sin utilizar loops (for/while), sino con slicing.
def es_palindromo(palabra):
    l=len(palabra)
    if palabra[:]==palabra[-1:-1*l-1:-1]:
        return True
    return False
assert es_palindromo('olo')== True
assert es_palindromo('elmono')==False