import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

iris = sns.load_dataset("iris")

x = iris[iris["species"] != "virginica"].iloc[:, 0:2].to_numpy()
y = iris[iris["species"] != "virginica"].iloc[:, 4]

y1 = np.full(50, 1)
y2 = np.full(50, 2)
y = np.ravel([y1, y2])

# Метод k-средних (KMeans)
model = KMeans(n_clusters=2, random_state=42) # задаем количество кластеров
model.fit(x) # обучаем модель только на x (без учителя)

xx, yy = np.meshgrid(
    np.linspace(x[:, 0].min(), x[:, 0].max(), 100),
    np.linspace(x[:, 1].min(), x[:, 1].max(), 100),
)

x_0 = iris[iris["species"] == "setosa"].iloc[:, 0].to_numpy()
y_0 = iris[iris["species"] == "setosa"].iloc[:, 1].to_numpy()

x_1 = iris[iris["species"] == "versicolor"].iloc[:, 0].to_numpy()
y_1 = iris[iris["species"] == "versicolor"].iloc[:, 1].to_numpy()

plt.scatter(x_0, y_0, color="red", alpha=0.5, label="setosa")
plt.scatter(x_1, y_1, color="green", alpha=0.5, label="versicolor")

Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

ax = plt.gca()
ax.contourf(xx, yy, Z, alpha=0.3, levels=[-0.5, 0.5, 1.5])
# KMeans нумерует кластеры с 0, т.к. обучает модель только на x, и не получает вектор y при обучении
plt.legend()

plt.title("Метод k-средних (KMeans)")
plt.show()