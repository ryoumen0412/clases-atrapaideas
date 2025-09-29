import pandas as pd
from pandasgui import show 

censo2024 = pd.read_excel('/home/hp-pavilion/clases_atrapaideas/Clase_18/P7_Educacion.xlsx', sheet_name='2')
censo2024.columns = censo2024.iloc[2] #Renombrar columnas
censo2024 = censo2024.drop([0,1,2,3]) #Eliminar filas
censo2024 = censo2024.reset_index(drop=True) #Reiniciar indices
# print(censo2024.tail())
censo2024 = censo2024.drop([346,347,348]) #Eliminar tail

#Columnas de porcentajes
censo2024["Nunca asistió Porcentaje"] = (censo2024["Nunca asistió"] / censo2024["Población censada"])*100
censo2024["Diferencial Porcentaje"] = (censo2024["Diferencial"] / censo2024["Población censada"])*100
censo2024["Parvularia Porcentaje"] = (censo2024["Parvularia"] / censo2024["Población censada"])*100
censo2024["Básica Porcentaje"] = (censo2024["Básica"] / censo2024["Población censada"])*100
censo2024["Media Porcentaje"] = (censo2024["Media"] / censo2024["Población censada"])*100
censo2024["Superior Porcentaje"] = (censo2024["Superior"] / censo2024["Población censada"])*100
censo2024["Nivel educativo no declarado Porcentaje"] = (censo2024["Nivel educativo no declarado"] / censo2024["Población censada"])*100

censoArreglado = censo2024
# print(censo2024.info())
# show(censo2024) #Mostrar df via pandasGUI

'''
    PARTE 2
    
1.
'''
print(censoArreglado.info())

pobTemuco = censoArreglado[censoArreglado['Comuna'] == 'Temuco']
# show(pobTemuco)
print(f"La poblacion censada en temuco es de {pobTemuco["Población censada"].values} personas...")

'''
2.
'''
comunasChile = len(censoArreglado)
print(f'En chile hay {comunasChile} comunas.')

'''
3.
'''
maxPob = censoArreglado['Población censada'].max()
comunaMaxPob = censoArreglado[censoArreglado["Población censada"] == maxPob]
print(comunaMaxPob['Comuna'].values)

'''
4.
'''
edSuperiorTemucoPorcentaje = pobTemuco['Superior Porcentaje'].values
print(f'El porcentaje de poblacion con educacion superior es de {edSuperiorTemucoPorcentaje}%...')

'''
5.
'''
sinEdTemuco = pobTemuco['Nunca asistió'].values
print(f'En Temuco hay {sinEdTemuco} personas sin educacion...')

'''
6.
'''
edSuperiorMax = censoArreglado['Superior Porcentaje'].max()
edSuperiorMaxComuna = censoArreglado[censoArreglado["Superior Porcentaje"] == edSuperiorMax]
print(f'La comuna con mas porcentaje de ed superior es {edSuperiorMaxComuna['Comuna'].values}')

'''
7.
'''
sinEducacionMax = censoArreglado["Nunca asistió Porcentaje"].max()
sinEducacionMaxComuna = censoArreglado[censoArreglado["Nunca asistió Porcentaje"] == sinEducacionMax]
print(f'La comuna con mas porcentaje sin educacion es {sinEducacionMaxComuna['Comuna'].values}')

'''
8.
'''
git