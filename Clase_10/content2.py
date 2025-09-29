from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from content1 import monster, nombres, edades

ocupacion = ['Trabajador', 'Contador auditor', 'Programador', 'Contador Auditor']
diccionario = {
    'Nombre': nombres,
    'Edad': edades,
    'Ocupacion': ocupacion
}

tabla = pd.DataFrame(diccionario)

print(tabla)

print('='*30)

print(tabla['Nombre']) #cuando se selecciona una columna del dataframe, el datatype es series

print('='*30)

seriesBools = tabla['Edad'] < 25
tablaFiltrada = tabla[seriesBools]

print(tablaFiltrada)

print('='*30)

fila = tabla.loc[0]

print(fila)

print(type(fila)) #.loc[] tambien convierte la variable en series

print('='*30)

unicos = tabla['Ocupacion'].unique()

print(unicos)
print(type(unicos))
print(len(unicos)) #los valores se guardan en un arreglo de numpy
