import pandas as pd
from pandasgui import show as sh
from CLASE import censoArreglado

# print(censoArreglado.info())

pobTemuco = censoArreglado[censoArreglado['Comuna'] == 'Temuco']
print(pobTemuco)
