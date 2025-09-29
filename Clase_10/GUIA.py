import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

datosCurso = pd.read_excel('/home/hp-pavilion/clases_atrapaideas/Clase_10/Datos Curso.xlsx')

excelDb = pd.DataFrame(datosCurso)

print(excelDb)

print('='*30)

print('1.')
print('a.')

menorEdad = excelDb['Edad'].min()
estudianteMenor = excelDb[excelDb['Edad'] == menorEdad]
print(estudianteMenor)

print(' ')

print('b.')

mayorEdad = excelDb['Edad'].max()
estudianteMayor = excelDb[excelDb['Edad'] == mayorEdad]
print(estudianteMayor)

print(' ')

print('c.')

print('NO APLICA')

print(' ')

print('d.')

ocupacion_count = {}

for ocupacion in excelDb['Ocupación']:
    if ocupacion in ocupacion_count:
        ocupacion_count[ocupacion] += 1
    else:
        ocupacion_count[ocupacion] = 1


max_count = 0
ocupacionMasRepetida = None
for ocupacion, count in ocupacion_count.items():
    if count > max_count:
        max_count = count
        ocupacionMasRepetida = ocupacion

print(ocupacion_count)
print(f'La ocupacion mas repetida es: {ocupacionMasRepetida}')

print('='*30)

datosOcup = excelDb.groupby(by='Ocupación').count()
print(datosOcup)

print(' ')

print('e.')

menorQueVeintiocho = excelDb[excelDb['Edad']>=28]


print(f'Hay {len(menorQueVeintiocho)} personas mayores de 28')

print(' ')

print('f.')

promedioEdad = excelDb['Edad'].mean()

print(f'Edad promedio: {promedioEdad}')

print(' ')

print('g.')


cantEst = excelDb[excelDb['Ocupación'] == 'Estudiante']
print(f'Hay {len(cantEst)} estudiantes')

print(' ')

print('h.')

seriesBool = excelDb['Apellido'].str.startswith(('A', 'E', 'I', 'O', 'U'))
apellidosVocal = excelDb[seriesBool]
print(f'Apellidos que comienzan con vocal: {len(apellidosVocal)}')

print('='*30)

seriesBool2 = excelDb['Nombres'].str.startswith(('A', 'E', 'I', 'O', 'U'))
nombresVocal = excelDb[seriesBool2]
print(f'Nombres que comienzan con vocal: {len(nombresVocal)}')