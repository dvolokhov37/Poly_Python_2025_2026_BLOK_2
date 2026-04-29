import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# Описание трехмерной поверхности (функции)
def f(x,y):
    return np.sin(np.sqrt(x**2 + y**2))

# x = np.linspace(-6, 6, 30)
# y = np.linspace(-10, 10, 50)
#
# X, Y = np.meshgrid(x, y)
#
# Z = f(X, Y)
#
# fig = plt.figure()
# ax = plt.axes(projection="3d")

# ax.scatter3D(X, Y, Z, c=Z)

## Каркасный график:
# ax.plot_wireframe(X, Y, Z)

## Поверхностный каркасный график:
# ax.plot_surface(X, Y, Z, cmap="viridis")

# Срез поверхности на графике: для этого нужно нарисовать нашу трехмерную функцию через полярные координаты
# через угол поворота и радиус

# angle = np.linspace(0, 2 * np.pi, 50)
# r = np.linspace(0, 6, 30)
#
# R, Angle = np.meshgrid(r, angle)
#
# X = R * np.sin(Angle)
# Y = R * np.cos(Angle)
# Z = f(X,Y)
#
# ax.plot_surface(X, Y, Z, cmap="viridis")

# Для среза нужно определить убираемую часть
# angle = np.linspace(0, 1.5 * np.pi, 50)
# r = np.linspace(0, 6, 30)
#
# R, Angle = np.meshgrid(r, angle)
#
# X = R * np.sin(Angle)
# Y = R * np.cos(Angle)
# Z = f(X,Y)
#
# ax.plot_surface(X, Y, Z, cmap="viridis")

## Триангуляция
# angle = 1.5 * np.pi * np.random.random(1000)
# r = np.linspace(0, 6, 1000)
#
# R, Angle = np.meshgrid(r, angle)
#
# X = R * np.sin(Angle)
# Y = R * np.cos(Angle)
# Z = f(X,Y)
#
# x = r * np.sin(angle)
# y = r * np.cos(angle)
# z = f(x,y)
#
# # ax.scatter3D(X, Y, Z, c=Z)
#
# # ax.plot_surface(X, Y, Z, cmap="viridis")
# ax.plot_trisurf(x, y, z, cmap="viridis")
#
# plt.show()

#### Seaborn: построено поверх mpl, работает НЕ через numpy (как mpl), а напрямую через dataframe

import seaborn as sns

sns.set_style('darkgrid')
cars = pd.read_csv('./data/cars.csv')

print(cars.head())

# В dataset могут параметры либо числовые, либо категориальные

### Числовые данные ###

## Парная диаграмма
# sns.pairplot(cars)

# sns.pairplot(data=cars, hue='transmission')

## Диаграмма: Тепловая карта (показывает корреляцию между параметрами)

# cars_corr=cars[["year", "selling_price", "seats", "mileage"]]
#
# sns.heatmap(cars_corr.corr(), cmap='viridis', annot=True)

## Диаграмма рессеяния
# sns.scatterplot(x="seats", y="mileage", data=cars, hue='fuel')
# sns.scatterplot(x="year", y="selling_price", data=cars)

## Диаграмма рессеяния + линейная регрессия
# sns.regplot(x="seats", y="mileage", data=cars)

# sns.relplot(x="seats", y="mileage", data=cars, kind="scatter", hue='fuel')

# sns.relplot(x="seats", y="mileage", data=cars, kind="scatter", col='transmission', col_wrap=2, hue="fuel")

# sns.relplot(x="seats", y="mileage", data=cars, kind="line", col='transmission', col_wrap=2, hue="fuel")

## Диаграмма рессеяния + линейная регрессия
# sns.lmplot(x="seats", y="mileage", data=cars, col='transmission', col_wrap=2, hue="fuel")

# Линейный график
# sns.lineplot(x="seats", y="mileage", data=cars, hue="fuel")

## Сводная диаграмма

# sns.jointplot(x="year", y="selling_price", data=cars)

# sns.jointplot(x="year", y="selling_price", data=cars, kind='kde')

## Сводная диаграмма + лин. регрессия
# sns.jointplot(x="year", y="selling_price", data=cars, kind='reg')

# sns.jointplot(x="year", y="selling_price", data=cars, kind='hex')

# sns.jointplot(x="year", y="selling_price", data=cars, hue='transmission')


### Категориальные данные ###

## Категории и числа

# sns.barplot(x="fuel", y="selling_price", data=cars, estimator=sum)

# sns.barplot(x="fuel", y="selling_price", data=cars, estimator=np.mean, hue="transmission")

# sns.catplot(x="fuel", y="selling_price", data=cars, estimator=np.mean, hue="transmission", kind="bar",
#             col="seller_type", col_wrap=2)

# sns.pointplot(x="fuel", y="selling_price", data=cars, estimator=np.mean, hue="transmission")

## Диаграмма boxplot: "ящик с усами", квартили, помогает понять как распределены данные

# sns.boxplot(x="fuel", y="selling_price", data=cars, hue="transmission")

## Скрипичная диаграмма: как boxplot, только ещё и показывает распределение
# sns.violinplot(x="fuel", y="selling_price", data=cars, hue="transmission")

# sns.stripplot(x="fuel", y="selling_price", data=cars, hue="transmission") # точки

## Совмещение двух диаграмм на одном рисунке

g = sns.catplot(x="fuel", y="selling_price", data=cars, kind='box')

sns.stripplot(x="fuel", y="selling_price", data=cars, ax=g.ax)

plt.show()