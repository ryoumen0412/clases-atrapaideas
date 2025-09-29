from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

nombres = ['Ruben', 'Tabita', 'Alejandro', 'Pablo']
edades = [29, 27, 23, 28]

#primera serie

monster = pd.Series(edades, index=nombres) #se pueden definir los valores de los indices
print(monster)

print('='*30)

print(monster['Alejandro'])
print(type(monster))
print(f'Longitud: {len(monster)}')

print('='*30)

losCasablanca = monster>28 #'monster' se transforma en Series de booleanos
print(losCasablanca)

print('='*30)

monsterFiltrada = monster[losCasablanca]
print(monsterFiltrada) #se filtran los campos menores a un numero n definido en la variable losCasablanca, quedando solo los valores True

print('='*30)

print(monster.min()) #method .min() muestra el valor mas bajo del arreglo
print(monster.max()) #method .max() muestra el valor mas alto del arreglo
print(monster.mean()) #method .mean() muestra el valor promedio del arreglo

print('='*30)

