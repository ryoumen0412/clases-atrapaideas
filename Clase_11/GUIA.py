import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

dataMinimarket = pd.read_excel('./Data_MiniMarket.xlsx')

minimarket = pd.DataFrame(dataMinimarket)

print(minimarket)

print('=' * 90)

print('a.')

print(f'Hay {len(minimarket)} productos tabulados...')

print('='*90)

print('b.')

categorias = minimarket['Categoría'].nunique()

print(f'Hay {categorias} categorias unicas')

print('='*90)

print('c.')

precioMin = minimarket['Precio'].min()

print(f'El producto mas barato cuesta {precioMin}')

print('='*90)

print('d.')

print(minimarket[minimarket['Precio'] == precioMin])

print('='*90)

print('e.')

precioMax = minimarket['Precio'].max()
print(f'El producto mas caro cuesta {precioMax}')

print('='*90)

print('f.')

print(minimarket[minimarket['Precio'] == precioMax])

print('='*90)

print('g.')

isNaranja = minimarket['Producto'].str.contains('Naranja', case=False)

contieneNaranja = isNaranja.any()

if contieneNaranja == True:
    print('Si hay Naranjas')
else:
    print('No hay Naranjas')

print('='*90)

print('h.')

isHallulla = minimarket['Producto'].str.contains('Hallulla')

contieneHallulla = isHallulla.any()

if contieneHallulla == True:
    print('Si hay hallulla')
else:
    print('No hay hallulla')
    
print('='*90)

print('i.')

print('='*90)

print('j.')

print('='*90)

print('k.')

mayorStock = minimarket['Stock'].max()
prodMayorStock = minimarket[minimarket['Stock'] == mayorStock]
print(prodMayorStock)

print('='*90)

print('l.')

stockBajo = minimarket[minimarket['Stock'] < 20]

print(stockBajo)










##################

nuevoDataFrame = minimarket[['Categoría', 'Precio']].groupby(by='Categoría').mean()

otroMinimarket = pd.concat([minimarket, minimarket])
otroMinimarket = otroMinimarket.reset_index()
otroMinimarketOrdenado = otroMinimarket.sort_index()
print(otroMinimarketOrdenado)