import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# lee datos
data = pd.read_csv('Cars93.csv')

# selecciona
cols = ['Price', 'MPG.city', 'EngineSize', 'Horsepower', 'RPM', 
                     'Fuel.tank.capacity', 'Length', 'Width', 'Turn.circle', 'Weight']
data_selecta = data[cols]

# normaliza
data_selecta = (data_selecta - data_selecta.mean())/data_selecta.std()

# covarianza
cov_matrix = np.cov(data_selecta.T)
# valores y vectores propios
values, vectors = np.linalg.eig(cov_matrix)

# Primer autovector y segundo autovector
vector_A = vectors[:,0]
vector_B = vectors[:,1]

# Grafica 
plt.figure(figsize=(12,12))

# Proyeccion de los modelos
for i in range(len(data)):
    model = data['Model'][i]
    v = np.array(data_selecta.iloc[i])
    x = np.dot(vector_A, v) # PRoducto punto con primer autovector
    y = np.dot(vector_B, v) # Producto punto con segundo autovector
    plt.text(x,y, model, fontsize=10, color='blue')
    plt.scatter(x, y, s=0.001)

# Proyeccion de los autovectores
for j in range(len(cols)):
    plt.arrow(0.0, 0.0, 5*vector_A[j], 5*vector_B[j], color='red', head_width=0.1)
    plt.text(5.5*vector_A[j], 5.5*vector_B[j], cols[j], color='red')

plt.xlabel('Primera Componente Principal')
plt.ylabel('Segunda Componente Principal')
plt.savefig('componentes_principales.png', bbox_inches='tight')