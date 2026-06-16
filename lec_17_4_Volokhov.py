# Метод главных компонент (алгоритм без учителя)
# и им можно понизить размерности, чтобы использовать самые влиятельные из размерностей

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

iris = sns.load_dataset("iris")

data = iris[["sepal_length", "petal_length", "species"]]
data_setosa = data[data["species"] == "setosa"]

print(data_setosa.head())

X = data_setosa["sepal_length"]
Y = data_setosa["petal_length"]

data_setosa = data_setosa.drop(columns = ["species"])
print(data_setosa.head())

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca.fit(data_setosa)

print("1")

print(pca.components_)

print(pca.mean_) # точка, от которой идем (середина)
print(pca.explained_variance_) # взаимный вес (дисперсия) этих компонент

plt.scatter(X, Y)

plt.scatter(pca.mean_[0], pca.mean_[1])

# 1ая компонента
plt.plot(
    [pca.mean_[0], pca.mean_[0] + pca.components_[0][0] * np.sqrt(pca.explained_variance_[0])], # из точки A
    [pca.mean_[1], pca.mean_[1] + pca.components_[0][1] * np.sqrt(pca.explained_variance_[0])] # в точку B
)

# 2ая компонента
plt.plot(
    [pca.mean_[0], pca.mean_[0] + pca.components_[1][0] * np.sqrt(pca.explained_variance_[1])], # из точки A
    [pca.mean_[1], pca.mean_[1] + pca.components_[1][1] * np.sqrt(pca.explained_variance_[1])] # в точку B
)

# получившаяся система координат больше соответствует расположению точек, чем исходная

pca1 = PCA(n_components=1)
pca1.fit(data_setosa)

X_pca1 = pca1.transform(data_setosa) # трансформация данных, изменение размерности

print(data_setosa.shape)
print(X_pca1.shape)

X_new = pca1.inverse_transform(X_pca1)

plt.scatter(X_new[:, 0], X_new[:, 1])

# наиболее распределенные данный вносят наибольший вклад в результирующее решение
# и именно они остаются

# Минус: достаточно чувствителен к выбросам и аномальным значениям

plt.show()