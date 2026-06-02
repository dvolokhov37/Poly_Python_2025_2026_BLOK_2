import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

iris = sns.load_dataset("iris")

x = iris[iris["species"] != "virginica"].iloc[:, 0:2].to_numpy()
y = iris[iris["species"] != "virginica"].iloc[:, 4]

y1 = np.full(50, 1) # setosa
y2 = np.full(50, 2) # versicolor
y = np.ravel([y1, y2])

# Метод Случайные леса (Random Forest)
model = RandomForestClassifier(n_estimators=100, random_state=42) # задаем гиперпараметры (кол-во деревьев)
model.fit(x, y)

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
ax.contourf(xx, yy, Z, alpha=0.3, levels=[0, 1.5, 3])

plt.title("Random Forest")
plt.legend()
plt.show()