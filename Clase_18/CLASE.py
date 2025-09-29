import pandas as pd
from pandasgui import show 

censo2024 = pd.read_excel('/home/hp-pavilion/clases_atrapaideas/Clase_18/P7_Educacion.xlsx', sheet_name='2')
censo2024.columns = censo2024.iloc[2] #Renombrar columnas
censo2024 = censo2024.drop([0,1,2]) #Eliminar filas
censo2024 = censo2024.reset_index(drop=True) #Reiniciar indices
# print(censo2024.tail())
censo2024 = censo2024.drop([347,348.349])

show(censo2024) #Mostrar df via pandasGUI
