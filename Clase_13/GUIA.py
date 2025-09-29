from matplotlib import pyplot as pt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris


iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target_names[iris.target]

num_species = iris_df['species'].nunique()

# Lista de especies distintas
species_list = iris_df['species'].unique()

# Cantidad de registros por cada especia
num_perspecies = iris_df['species'].value_counts()

# Cantidad de flores medidas
num_flores = len(iris_df)

print("Número de especies distintas:", num_species)
print("Especies encontradas:", species_list)
print(num_perspecies)
print(f'Se midieron {num_flores} flores.')

# Encontrar el valor mínimo de petal width
min_petal_width = iris_df["petal width (cm)"].min()

# Filtrar las filas que tienen ese valor mínimo
min_rows = iris_df[iris_df["petal width (cm)"] == min_petal_width]

print("Menor ancho de pétalo medido:", min_petal_width)
print("Especie(s) correspondiente(s):")
print(min_rows[["species", "petal width (cm)"]])

# Encontrar el valor mínimo de sepal length
min_sepal_length = iris_df["sepal length (cm)"].min()

# Filtrar las filas con ese valor
min_rows = iris_df[iris_df["sepal length (cm)"] == min_sepal_length]

print("Menor largo de sépalo medido:", min_sepal_length)
print("Especie(s) correspondiente(s):")
print(min_rows[["species", "sepal length (cm)"]])

# Calcular el promedio del ancho de pétalo por especie
mean_petal_width = iris_df.groupby("species")["petal width (cm)"].mean()

# Mostrar resultados
print(mean_petal_width)

# Encontrar la especie con el mayor promedio
max_species = mean_petal_width.idxmax()
max_value = mean_petal_width.max()

print("\nLa especie con los pétalos más anchos en promedio es:", max_species)
print("Promedio de ancho de pétalo:", max_value)

# Calcular el promedio del largo de sépalo por especie
mean_sepal_length = iris_df.groupby("species")["sepal length (cm)"].mean()

# Mostrar resultados
print(mean_sepal_length)

# Encontrar la especie con el mayor promedio
max_species = mean_sepal_length.idxmax()
max_value = mean_sepal_length.max()

print("\nLa especie con los sépalos más largos en promedio es:", max_species)
print("Promedio de largo de sépalo:", max_value)

# Filtrar filas donde el ancho de pétalo sea mayor o igual a 0.4
filtered = iris_df[iris_df["petal width (cm)"] >= 0.4]

# Contar cuántas filas cumplen la condición
num_flowers = len(filtered)

print("Número de flores con pétalos de 0.4 cm o más de ancho:", num_flowers)

# Filtrar filas donde el ancho de sépalo sea mayor o igual a 4
filtered = iris_df[iris_df["sepal width (cm)"] >= 4.0]

# Contar cuántas filas cumplen la condición
num_flowers = len(filtered)

print("Número de flores con sépalos de 4 cm o más de ancho:", num_flowers)

import matplotlib.pyplot as plt

# Definir colores para cada especie
colors = {"setosa": "red", "versicolor": "green", "virginica": "blue"}

# Crear el gráfico de dispersión
plt.figure(figsize=(8,6))

for species in iris_df["species"].unique():
    subset = iris_df[iris_df["species"] == species]
    plt.scatter(
        subset["sepal length (cm)"], 
        subset["sepal width (cm)"], 
        c=colors[species], 
        label=species,
        edgecolor='k',  # borde negro para mejor visibilidad
        s=80           # tamaño de los puntos
    )

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Scatter plot del ancho y largo de sépalos por especie")
plt.legend()
plt.grid(True)
plt.show()
