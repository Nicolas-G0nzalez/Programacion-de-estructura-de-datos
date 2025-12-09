#Punto 1
#Cargue el dataset disponible en
#https://www.datos.gov.co/Econom-a-y- Finanzas/Tasa-de-Cambio-Representativa-del-Mercado-TRM/32sa-8pi3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sodapy import Socrata
cliente=Socrata('www.datos.gov.co', None)
result=cliente.get("32sa-8pi3")
df=pd.DataFrame.from_records(result)
df.head()

df.info()

#columna_numerica = pd.to_numeric(datos['limite_menor_cuantia'], errors='coerce')
#columna_numerica = columna_numerica.dropna().astype(float)
valor=pd.to_numeric(df['valor'],errors='coerce')
print(valor)

#Punto 2
#Calcular
#a. Media
#b. Mediana
#c. Desviación estándar
#d. Máximo
#e. Mínimo
#f. Máximo
#g. Rango
print('El valor de la media es: ',round(np.mean(valor),3))
print('El valor de la mediana es: ',round(np.median(valor),3))
print('El valor de la desviacion estandar es: ',round(np.std(valor),3))
print('El valor del máximo es: ',round(np.max(valor),3))
print('El valor del mínimo es: ',round(np.min(valor),3))
print('El valor del rango es: ',round(np.max(valor),3)-round(np.min(valor),3))

#Punto 3
#Presentar el resumen de los datos numéricos
df.info()

df['Valor_n']=valor
df

df.describe()

#Punto 4
#Presentar la información general del dataset
df.info()

#Punto 5
#Hacer dos representaciones graficas que sean acordes a la naturaleza de los datos
df.hist(bins=10)
plt.title('Histograma de la variación del Dolar')
plt.xlabel('Pesos')
plt.show()

df.plot()
plt.title('Grafica de la variación del dolar sin ordenar')
plt.xlabel('Tiempo')
plt.ylabel('Pesos')
plt.grid()
plt.show()

#Ordenar las fechas y valores del data Frame
data_o=df.sort_values(by=['vigenciadesde'])
valores=list(data_o['Valor_n'])
plt.plot(valores,'r--')
plt.title('Variación hitorica del dolar')
plt.xlabel('Tiempo')
plt.ylabel('Pesos')
plt.grid()
plt.show()

print(data_o.head(1))

print(data_o.tail())

#Punto 6
#Usando Socrata, Cargue un dataset que se encuentre en el portal de datos públicos
#de Colombia
#se usa un data set del paruqe automotor del departamento de Boyaca
cliente2=Socrata('www.datos.gov.co', None)
result=cliente2.get("874t-i57z")
df_auto=pd.DataFrame.from_records(result)
df_auto.head()

#Punto 7
#Realice las tareas de limpieza y transformación necesarias
#Liempiza Quitar datos nulos
df_auto.info()

#Eliminar filas con dato nulos
df_auto=df_auto.dropna(axis=0, how='any')
df_auto.info()

df_auto.describe()

df_auto.head()

#Revisar si hay registros duplicados
print(df_auto.duplicated())

df_auto.drop_duplicates(inplace = True)
df_auto

df_auto.info()

#Punto 8
#Presentar el dataset, mostrando datos estadísticos y gráficas
df_auto.head()
var=list((df_auto['modelo']))
modelo=[]
for i in range(len(var)):
    modelo.append(int(var[i]))

modelo_a=np.array(modelo)
print('La media de los modelos es: ', np.mean(modelo_a))

#Grafica del histograma de modelos
plt.hist(modelo_a, bins=10)
plt.axvline(np.mean(modelo_a), ymin=0.0, ymax=0.9,color='r')
plt.title('Histograma de los modelos del parque automotor')
plt.grid()
plt.show()

#Graficas el diagrama de caja de los modelos
plt.boxplot(modelo_a)
plt.title('Diagram de caja para el modelo')
plt.ylabel('Años')
plt.grid()
plt.show()

#Analisis de las clases del parque automotor
df_clase=df_auto[['clase']]
df_clase.head()

df_clase.info()

df_clase.tail()

lista_clase=list(df_clase['clase'])
for i in lista_clase:
    print(i)

df_clase.describe()

#Vamos a contar las diferentes clases de automoviles
def contar(n, vec):
    '''Para esta funcion n es el numero a contar y vec es la lista donde contar '''
    count=0
    for i in vec:
        if i==n:
            count+=1
    return count

print('AUTOMOVIL aparece: ',contar('AUTOMOVIL', lista_clase))
print('CAMPERO aparece: ',contar('CAMPERO', lista_clase))
print('CAMIONETA aparece: ',contar('CAMIONETA', lista_clase))
print('CAMION aparece: ',contar('CAMION', lista_clase))
print('MOTOCICLETA aparece: ',contar('MOTOCICLETA', lista_clase))
print('VOLQUETA aparece: ',contar('VOLQUETA', lista_clase))
print('BUSETA aparece: ',contar('BUSETA', lista_clase))
print('MICRO BUS aparece: ',contar('MICRO BUS', lista_clase))

aux=[contar('AUTOMOVIL', lista_clase), contar('CAMPERO', lista_clase),contar('CAMIONETA', lista_clase),
    contar('CAMION', lista_clase),contar('MOTOCICLETA', lista_clase), contar('VOLQUETA', lista_clase),
    contar('BUSETA', lista_clase) , contar('MICRO BUS', lista_clase)]
print('La suma total es de: ', sum(aux))

num_clase=[]
for i in range(len(lista_clase)):
    num_clase.append(contar(lista_clase[i],lista_clase))

print(num_clase)
print(len(num_clase))

#Diagrama de Barras
categoria=['AUTO','CAM','CAMI','CAMIO', 'MOTO','VOL','BUS','MICRO']
plt.bar(categoria,aux,width=0.8, color='lime')
plt.xlabel('Clases')
plt.ylabel('Veces que se repiten')
plt.title('Análisi sobre las clases de automotores')
plt.grid()
plt.show()

len(num_clase)

#Punto 9
#Se debe incluir mínimo una tabla pivote y una agrupación
df_auto.head()

df_auto.pivot_table(values='modelo', index='municipio', columns=['servicio'], aggfunc='count')

df_auto.groupby(df_auto['municipio']).count()[['importado']]

df_auto.groupby(df_auto['municipio']).count()['marca']

lis=list(df_auto['municipio'])
for i in lis:
    print(i)

#Punto 10
#Todas las graficas deben ser explicadas
#Diagrama de Barras
categoria=['AUTO','CAM','CAMI','CAMIO', 'MOTO','VOL','BUS','MICRO']
plt.bar(categoria,aux,width=0.8, color='silver')
plt.xlabel('Clases')
plt.ylabel('Veces que se repiten')
plt.title('Análisi sobre las clases de automotores')
plt.grid()
plt.show()

print(aux)
print(categoria)

#Graficas el diagrama de caja de los modelos
plt.boxplot(modelo_a)
plt.title('Diagrama de caja para el modelo')
plt.ylabel('Años')
plt.grid()
plt.show()

#Grafica del histograma de modelos
plt.hist(modelo_a, bins=10)
plt.axvline(np.mean(modelo_a), ymin=0.0, ymax=0.9,color='r')
plt.title('Histograma de los modelos del parque automotor')
plt.grid()
plt.show()