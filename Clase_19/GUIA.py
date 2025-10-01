import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

notas = pd.read_csv('~/clases_atrapaideas/Clase_19/notas.csv')

# plt.scatter(notas['Tiempo_estudio'], notas['Nota'])
# plt.show()

promedio_curso = notas['Nota'].mean()
print(promedio_curso)

#=============================================================
'''
x = np.linspace(-10, 20, 3000)
pendiente = 5
interseccion = -100
y = x*pendiente + interseccion

plt.plot(x,y)

pendiente = 2
interseccion = -100
y = x*pendiente + interseccion

plt.plot(x,y)

pendiente = -10
interseccion = -100
y = x*pendiente + interseccion

plt.plot(x,y)

pendiente = 0
interseccion = -100
y = x*pendiente + interseccion

plt.plot(x,y)
'''
plt.grid()
# plt.show()

modelo = LinearRegression()
x = np.array(notas['Tiempo_estudio']).reshape(-1,1)
y = np.array(notas['Nota'])
modelo.fit(x,y)

plt.scatter(notas['Tiempo_estudio'], notas['Nota'])
plt.xlabel('Horas de estudio')
plt.ylabel('Nota obtenida')

y_modelo = modelo.predict(x)
plt.plot(x,y_modelo, color='red')
# plt.show()

pendiente_modelo = modelo.coef_[0]
interseccion_modelo = modelo.intercept_
print(pendiente_modelo)
print(interseccion_modelo)
ec_recta = pendiente_modelo*5+interseccion_modelo
print(f'Ecuacion de la recta en 5 horas es {ec_recta:.2f}')

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
mse = mean_squared_error(y, y_modelo)
print(mse)

rmse = mse**(1/2)

print(rmse)

mae = mean_absolute_error(y, y_modelo)

print(mae)

r2 = r2_score(y, y_modelo)

print(r2)

nota10 = modelo.predict(np.array(10).reshape(-1,1))
nota0 = modelo.predict(np.array(0).reshape(-1,1))
nota25 = modelo.predict(np.array(25).reshape(-1,1))

if nota25>7:
    nota25=[7]

print(f'{nota10}, {nota0}, {nota25}')

data_flojos = notas[notas['Tiempo_estudio'] <=10]
print(data_flojos.head())


notaMariaC = modelo.predict(np.array(4.6).reshape(-1,1))
notaRaul = modelo.predict(np.array(0.7).reshape(-1,1))
notaMariaF = modelo.predict(np.array(6.8).reshape(-1,1))
notaGabriela = modelo.predict(np.array(5.2).reshape(-1,1))
notaBea = modelo.predict(np.array(2.9).reshape(-1,1))

print(f'{notaMariaC},{notaRaul},{notaMariaF},{notaGabriela},{notaBea}')