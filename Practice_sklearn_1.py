import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

iris = sns.load_dataset("iris")

x = iris[iris["species"] != "virginica"].iloc[:, 0:4].to_numpy() # берем все 4 признака чтобы было, что сжимать
y = iris[iris["species"] != "virginica"].iloc[:, 4]

y1 = np.full(50, 1) # setosa
y2 = np.full(50, 2) # versicolor
y = np.ravel([y1, y2])

# Метод главных компонент (PCA) - это метод снижения размерности (обучение без учителя)
model = PCA(n_components=2) # снизим размерность с 4D до 2D (до 2 главных компонент)

# в PCA мы обучаем модель и трансформируем данные
x_pca = model.fit_transform(x)

# setosa
x_0 = x_pca[y == 1, 0]
y_0 = x_pca[y == 1, 1]

# versicolor
x_1 = x_pca[y == 2, 0]
y_1 = x_pca[y == 2, 1]

# 5. Визуализация решения
plt.scatter(x_0, y_0, color="red", alpha=0.5, label="setosa")
plt.scatter(x_1, y_1, color="green", alpha=0.5, label="versicolor")

plt.title("Метод главных компонент (PCA)")
plt.xlabel("Главная компонента 1")
plt.ylabel("Главная компонента 2")
plt.legend()
plt.show()