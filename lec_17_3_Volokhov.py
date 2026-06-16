# Bagging
# использует несколько моделей (ансамбль), усредняет результаты и получает некоторую оптимальную классификацию
# в случае деревьев это называется Random Forest

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Ансамблевые методы и метод главных компонент

iris = sns.load_dataset("iris")

print(iris.head())

# Будем заниматься проблемой классификации

species_int = [] # массив, в который кладем отображение сортов
for row in iris.values:
    match row[4]:
        case "setosa":
            species_int.append(1)
        case "versicolor":
            species_int.append(2)
        case "virginica":
            species_int.append(3)

# species_int_df = pd.DataFrame(species_int)
# print(species_int_df.head())

# Для нашей задачи выберем две хар-ки, соберем один датасет

data = iris[["sepal_length", "petal_length"]]
data["species"] = species_int

print(data.head())
print(data.shape)

# data_df = data[ (data["species"] == 3) | (data["species"] == 2)]
# print (data_df.shape)

data_of_setosa = data[data["species"] == 1]
data_of_versicolor = data[data["species"] == 2]
data_of_virginica = data[data["species"] == 3]


X = data[["sepal_length", "petal_length"]]
y = data["species"]

x1_p = np.linspace(min(data["sepal_length"]), max(data["sepal_length"]), 100)
x2_p = np.linspace(min(data["petal_length"]), max(data["petal_length"]), 100)

X1_p, X2_p = np.meshgrid(x1_p, x2_p)

print(X1_p.shape)

X_p = pd.DataFrame(np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"])

print(X_p.head())

# У классфикатора есть гиперпараметры, отвечающие за глубину поиска
from sklearn.tree import DecisionTreeClassifier

# max_depth = [[1, 2, 3, 4], [5, 6, 7, 8]]

fig, ax = plt.subplots(1, 3, sharex="col", sharey="row")

ax[0].scatter(data_of_setosa["sepal_length"], data_of_setosa["petal_length"])
ax[0].scatter(data_of_versicolor["sepal_length"], data_of_versicolor["petal_length"])
ax[0].scatter(data_of_virginica["sepal_length"], data_of_virginica["petal_length"])

ax[1].scatter(data_of_setosa["sepal_length"], data_of_setosa["petal_length"])
ax[1].scatter(data_of_versicolor["sepal_length"], data_of_versicolor["petal_length"])
ax[1].scatter(data_of_virginica["sepal_length"], data_of_virginica["petal_length"])

ax[2].scatter(data_of_setosa["sepal_length"], data_of_setosa["petal_length"])
ax[2].scatter(data_of_versicolor["sepal_length"], data_of_versicolor["petal_length"])
ax[2].scatter(data_of_virginica["sepal_length"], data_of_virginica["petal_length"])

model1 = DecisionTreeClassifier(max_depth=6)
model1.fit(X, y)
y1_p = model1.predict(X_p)

ax[0].contourf(X1_p, X2_p, y1_p.reshape(X1_p.shape), alpha=0.3, levels=[0, 1.5, 2.5, 3.5])

from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier

# Теперь начинается Bagging
model2 = DecisionTreeClassifier(max_depth=6)
bagging = BaggingClassifier(model2, n_estimators=10, max_samples=0.6, random_state=1)
bagging.fit(X, y) # обучаем

y2_p = bagging.predict(X_p) # предсказываем

ax[1].contourf(X1_p, X2_p, y2_p.reshape(X1_p.shape), alpha=0.3, levels=[0, 1.5, 2.5, 3.5])

# Далее Random Forest

model3 = RandomForestClassifier(max_depth=3, n_estimators=10, max_samples=0.6, random_state=1)
model3.fit(X, y) # обучаем

y3_p = model3.predict(X_p) # предсказываем

ax[2].contourf(X1_p, X2_p, y3_p.reshape(X1_p.shape), alpha=0.3, levels=[0, 1.5, 2.5, 3.5])


# # Демонстрация эффекта переобучения для деревьев решений
# for i in range(2):
#     j = 0
#     for md in max_depth[i]:
#
#         model = DecisionTreeClassifier(max_depth=md)
#         model.fit(X, y)
#
#         y_p = model.predict(X_p)
#
#         ax[i,j].scatter(data_of_setosa["sepal_length"], data_of_setosa["petal_length"])
#         ax[i,j].scatter(data_of_versicolor["sepal_length"], data_of_versicolor["petal_length"])
#
#         # Демонстрация работы метода классификации с помощью деревьев
#         ax[i,j].contourf(X1_p, X2_p, y_p.reshape(X1_p.shape), alpha=0.3, levels=[0, 2.5, 3.5])
#         j += 1

# Набор данных разделили на несколько частей, а затем эти части обучили отдельно
plt.show()

# Итоги по ансамблевым методам:
# Плюсы:
# Можно взять простые модели обучения (Дерево решений - это простая модель)
# Предсказания выполняются быстро (т.е. хорошо решается)
# Хорошо распараллеливаются (т.к. независимые вычисления)
# метод "голосование"
# непараметрическая модель - опирается на данные и исходя из данных принимают решения
# т.е. эффективная работа с данными
# Минусы:
# Сложно интерпретировать результат (осмысленные выводы сложно сделать)