import re 
from collections import Counter

def buscar_coincidencias(products):
    # Contar la frecuencia de las palabras en la lista
    conteo_palabras = Counter(products)
    
    # Encontrar la palabra más común
    palabra_comun = conteo_palabras.most_common(1)
    
    return palabra_comun[0] if palabra_comun else None
    
