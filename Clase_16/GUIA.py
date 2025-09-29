import numpy as np
import plotly as pl
import pandas as pd
import random as rd

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def numVerif(num):
    
    if num < 0: # Si es negativo
        return False
    else:       # Si es positivo
        return True
    
num1 = numVerif(float(input('Ingrese un numero real..... ')))

if num1 == True:
    print('Su numero es positivo...')
else:
    print('Su numero es negativo...')

print('+'*90)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def numPar(num):
    numVer = num%2
    if numVer == 0:
        return True
    else:
        return False

num2 = numPar(float(input('Ingrese un numero real..... ')))

if num2 == True:
    print('Su numero es par...')
else:
    print('Su numero es impar...')

print('+'*90)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def esPalindromo(palabra):
    palabraLimpia = ''.join(palabra.lower().split())
    palabraSuperLimpia = normalize(palabraLimpia)
    
    if palabraSuperLimpia == palabraSuperLimpia[::-1]:
        return True
    else:
        return False
    
palindromo = esPalindromo('Holaaloh')

print(palindromo)

noPalindromo = esPalindromo('aeiou')

print(noPalindromo)

print('+'*90)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def esFrasePalindromo(palabra):
    palabraLimpia = ''.join(palabra.lower().split())
    palabraSuperLimpia = normalize(palabraLimpia)
    
    if palabraSuperLimpia == palabraSuperLimpia[::-1]:
        return True
    else:
        return False
    
frasePalindromo = esFrasePalindromo('Ale es grande y ednarg se elA')

print(frasePalindromo)

noFrasePalindromo = esFrasePalindromo('Esto definitivamente no es un palindromo :3')

print(noFrasePalindromo)

print('+'*90)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def contarVocales(texto):
    
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    textoLower = texto.lower()
    
    con = {}
    for vocal in vocales:
        con[vocal] = textoLower.count(vocal)
    
    print(con)
    
    return pd.Series(con)

vocalesSeries = contarVocales('''HOLA QUE TAL COMO ESTAS YO BIEN GRACIAS
                              RESULTA QUE ALFKDSJLFJSDLFK Y LUEGO LSDFJLSDF
                              PERO IMAGINATE QUE ASDPQWOIHNEFU XDXDD''')

print(vocalesSeries)

print('+'*90)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def maxMinMeanStd(df: pd.DataFrame, col: str):
    
    if col not in df.columns:
        return f'ERROR: LA COLUMNA "{col}" NO EXISTE EN EL DATAFRAME'
    
    if not pd.api.types.is_numeric_dtype(df[col]):
        return 'ERROR: LA COLUMNA ENTREGADA DEBE SER NUMERICA'
    
    dfMax = df[col].max()
    dfMin = df[col].min()
    dfMean = df[col].mean()
    dfStd = df[col].std()
    
    results = {
        'maximo': dfMax,
        'minimo': dfMin,
        'promedio': dfMean,
        'variacion estandar': dfStd
    }
    
    return results

print('NO VOY A HACER UN DF AHORA PARA PROBAR ESTA FUNCION, QUIZAS DESPUES')
print('+'*90)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def tiradas(n):
    n = int(n)
    lista = []
    for i in range(n):
        i = rd.randint(1, 6)
        lista.append(i)
    
    return lista

letsGoGambling = tiradas(input('Cuantas veces tiras? '))

print(letsGoGambling)