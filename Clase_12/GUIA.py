import pandas as pd

pelis = pd.read_excel('./Data_Pelis.xlsx')
directores = pd.read_excel('./Directores.xlsx')
extra = pd.read_excel('./Data_Extra.xlsx')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# a y b.

extraNoIndex = extra.drop('Unnamed: 0', axis=1)
 
pelis['Director'] = directores['Director']

pelisFull = pd.concat([pelis, extraNoIndex])

pelisFull = pelisFull.reset_index()

pelisFull = pelisFull.drop('index', axis=1)

print(pelisFull)

(print('+'*90))

# c.

print(f'c. En la base de datos hay {len(pelisFull)} peliculas. Puro cine...')

print('+'*90)

# d.

generosUnicos = pelisFull['Género'].nunique()
print(f'd. Hay {generosUnicos} generos unicos.')

print('+'*90)

# e.

duracionMasLarga = pelisFull['Duración_min'].max()
print(f'e. La pelicula mas larga dura {duracionMasLarga} minutos.')

print('+'*90)

# f.

peliMasLarga = pelisFull[pelisFull['Duración_min'] == duracionMasLarga]
print('f.')
print(peliMasLarga)

print('+'*90)

# g.

duracionMasCorta = pelisFull['Duración_min'].min()
print(f'g. La pelicula mas corta dura {duracionMasCorta} minutos.')

print('+'*90)

# h.

peliMasCorta = pelisFull[pelisFull['Duración_min'] == duracionMasCorta]
print('h.')
print(peliMasCorta)

print('+'*90)

# i.

anhoMasModerna = pelisFull['Año'].max()
print(f'i. La pelicula mas moderna es del año {anhoMasModerna}')

print('+'*90)

# j.

peliMasModerna = pelisFull[pelisFull['Año'] == anhoMasModerna]
print(f'j. La pelicula mas moderna es:')
print(peliMasModerna)

print('+'*90)

# k.

anhoMasAntigua = pelisFull['Año'].min()
print(f'k. La pelicula mas antigua es del año {anhoMasAntigua}')

print('+'*90)

# l.

peliMasAntigua = pelisFull[pelisFull['Año'] == anhoMasAntigua]
print(f'l. La pelicula mas antigua es:')
print(peliMasAntigua)

print('+'*90)

# m.

pelisSciFi = pelisFull[pelisFull['Género'] == 'Sci-Fi']
anhoPeliSciFiMasAntigua = pelisSciFi['Año'].min()
peliSciFiMasAntigua = pelisSciFi[pelisSciFi['Año'] == anhoPeliSciFiMasAntigua]
print('m. La pelicula Sci-Fi mas antigua es:')
print(peliSciFiMasAntigua)

print('+'*90)

# n.

pelisTerror = pelisFull[pelisFull['Género'] == 'Terror']
anhoPeliTerrorMasAntigua = pelisTerror['Año'].min()
peliTerrorMasAntigua = pelisTerror[pelisTerror['Año'] == anhoPeliTerrorMasAntigua]
print('n. La pelicula de Terror mas antigua es:')
print(peliTerrorMasAntigua)

print('+'*90)

# o.

pelisComedia = pelisFull[pelisFull['Género'] == 'Comedia']
anhoPeliComediaMasModerna = pelisComedia['Año'].max()
peliComediaMasModerna = pelisComedia[pelisComedia['Año'] == anhoPeliComediaMasModerna]
print('o. La pelicula de comedia mas moderna es:')
print(peliComediaMasModerna)

print('+'*90)

# p.

pelisSciFiDuracionPromedio = pelisSciFi['Duración_min'].mean()
print(f'p. Las pelis Sci-Fi duran en promedio {pelisSciFiDuracionPromedio} minutos.')

# q.

pelisAnimacion = pelisFull[pelisFull['Género'] == 'Animación']
pelisAnimacionDuracionPromedio = pelisAnimacion['Duración_min'].mean()
print(f'Las peliculas de animacion duran en promedio {pelisAnimacionDuracionPromedio} minutos.')

print('+'*90)

# r.

pelisJohnWick = pelisFull['Título'].__contains__('John Wick')