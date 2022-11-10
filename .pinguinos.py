import pandas as pd
from palmerpenguins import load_penguins

#Ejercicio 1
penguins = load_penguins()
print(penguins)
#Primero haremos una pequeña inspección general de los datos que tenemos
penguins.shape
penguins.describe()
penguins.info()

#Ejercicio 2
#Vamos a eliminar todas las filas que contengan alguna valor NaN
penguins2=penguins.dropna()
print(penguins2)
NaN_check=penguins2.isna()

#Verificamos que efectivamente no queda ningún NaN
check_for_any_nan= penguins2.isna().values.any()
total_nan_values = penguins2.isna().sum().sum()
print("NaN Presence:"+str(check_for_any_nan))
print ("Total Number of NaN values:"+str(total_nan_values))

#Ejercicio 3
#Para calcular cuantos individuos hay de cada tipo:
penguins2["sex"].value_counts()

#Agrupamos según el sexo y sacamos la media de la longitud del pico para cada grupo
medias=penguins2.groupby(["sex"]).mean("bill_length_mm")
print(medias.bill_length_mm)

#Ejercicio 4 
penguins3= penguins2.assign(bill_area=penguins2["bill_depth_mm"]*penguins2["bill_length_mm"])
print(penguins3)
#Hemos usado la función assign para añadir una nueva columna que contenga el área del pico de los pinguinos

#Ejercicio 5
#Agrupamos en función de sexo y de la especie mostrando la longitud media del pico para cada subgrupo:
group=penguins3.groupby(["sex","species"])["bill_length_mm"].mean()
print(group)
#queremos seleccionar solamente females:
group_female=group["female"]
print(group_female)

#Ejercicio 6
#Finalmente eliminaremos crearemos una columna con el peso en KG y eliminaremos la columna que tenía el peso en gramos:
penguins4=penguins3.assign(body_mass_kg=penguins3["body_mass_g"]/1000)
penguins5=penguins4.drop(["body_mass_g"],axis=1)
print(penguins5)



