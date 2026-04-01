import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# img = mpimg.imread('ttt.png')
# plt.imshow(img)
# plt.axis('off') # Скрыть оси
# plt.show()

# Стиль MATLAB (процедурное программирование, читаем чисто по коду сверху вниз: "Написал код - нарисовал")
# x = np.linspace(0, 10, 100)
#
# plt.subplot(2, 1, 1) # Разобьем область рисования на кол-во строк и столбцов
# # таким образом обозначаем место для рисования
# plt.plot(x, np.sin(x))
#
# plt.subplot(2, 1, 2)
# plt.plot(x, np.cos(x))
#
# print(plt.gcf())
# print(plt.gca())
#
# fig, ax = plt.subplots(2)
# print(fig)
# print(ax[0])

# Стиль ОО (Объекто-ориентированный)
# fig, ax = plt.subplots(2) # fig - сам график, ax - оси, две системы координат
# ax[0].plot(x, np.sin(x))
# ax[1].plot(x, np.cos(x))
# В данном случае обратится к графику легко, это по сути ссылка на график: ax[0].plot(x, np.sin(x)),
# и с таким стилем проще его вызывать в любом месте кода

# Оба данных подхода взаимозаменяемые

# x = np.linspace(0, 10, 1000)
# ax = plt.gca()
#
# # Как задавать цвета: color - именованный атрибут
#
# ax.plot(x, np.sin(x), color='blue')
# ax.plot(x, np.sin(x - 1), color='g', linestyle='solid') # -
# ax.plot(x, np.sin(x - 2), color='0.75', linestyle='dashed') # --
# ax.plot(x, np.sin(x - 3), color='#FFDDAA', linestyle='dashdot') # -.
# ax.plot(x, np.sin(x - 4), color=(1.0, 0.2, 0.3), linestyle='dotted') # RGB, :
# ax.plot(x, np.sin(x - 5), color='salmon')
# ax.plot(x, np.sin(x - 6), '--g')

# Нарисуем 5 графиков, идущих один за другим
# fig, ax = plt.subplots(5)
#
# ax[0].plot(x, np.sin(x))
# ax[1].plot(x, np.sin(x))
# ax[2].plot(x, np.sin(x))
# ax[3].plot(x, np.sin(x))
# ax[4].plot(x, np.sin(x))

# Настроим пределы осей

# ax[1].set_xlim(-2, 12)
# ax[1].set_ylim(-1.5, 1.5)
#
# ax[2].set_xlim(12, -2)
# ax[2].set_ylim(1.5, -1.5)
#
# # ax[3].axis('tight') # autoscale - более правильный
# ax[3].autoscale(tight=True) # Здесь tight - уже название атрибута
#
# ax[4].axis('equal')

# Настроим отображение title и legend

# plt.subplot(3, 1, 1)
# plt.plot(x, np.sin(x))
# plt.title("Синус")
# plt.xlabel("x")
# plt.ylabel("sin(x)") # Можно также писать в формате Latex: $\sqrt{2}$
#
# plt.subplot(3, 1, 2)
# plt.plot(x, np.sin(x), '-g', label='sin(x)')
# plt.plot(x, np.cos(x), ':b', label='cos(x)')
# plt.title("Синус и Косинус")
# plt.xlabel("x")
# plt.legend()
#
# plt.subplot(3, 1, 3)
# plt.plot(x, np.sin(x), '--k', label='$\sin x$')
# plt.plot(x, np.cos(x), '-r', label='$\cos x$')
# plt.title("Синус и Косинус - 2")
# plt.xlabel("x")
# plt.legend()
#
# plt.subplots_adjust(hspace=0.5)

# ВИДЫ ДИАГРАММ

# Диаграммы рассеивания

# На графиках сплошная линия получается за счёт того, что 1000 точек соединяются (np.linspace(0, 10, 1000)),
# образуя гладкую кривую

# В диаграмме рассеивания мы точки не соединяем, а просто их рисуем, и можем их описывать не как точки,
# а как какие-то фигуры

# x = np.linspace(0, 10, 100) # При разбиении в 30 видно, что точки соединяются линиями,
# # из-за того, что их мало - график получается не гладким
# y = np.sin(x)

# plt.plot(x,y)

# Чтобы точки вообще не соединялись линиями, нам нужно обозначить, что у нас точки обозначены, например, кружочками
# plt.plot(x,y, "o") # Это диаграмма рассеивания
# Вместо "o" м.б. ".", "x", "+", "v", "s", "d" - определенное представление точек графика

# Можно одновременно вводить и линии и точки
# plt.plot(x,y, "--o", markersize=15, linewidth=4,
#          markerfacecolor="red", markeredgecolor="blue", markeredgewidth=3, color="black")

# rng = np.random.default_rng(1)
#
# colors = rng.random(100)
# sizes = 1000 * rng.random(100)
#
# # Другой способ задания, все точки можно индивидуально менять
# plt.scatter(x, y, c=colors, s=sizes, alpha=0.3)
# plt.colorbar() # Говорит о значениях, которые соответствуют каждому цвету

# from sklearn.datasets import load_iris
#
# iris = load_iris(as_frame=True)
#
# print(iris.frame.head())
#
# plt.scatter(
#     iris.frame["sepal length (cm)"],
#     iris.frame["sepal width (cm)"],
#     s = 100 * iris.frame["petal length (cm)"],
#     c = iris.frame["target"],
#     alpha=0.3
# )

# rng = np.random.default_rng(1)
#
# x = np.linspace(0, 10, 100)
# dy = 0.5
# y = np.sin(x) + dy * rng.random(100)
#
# plt.plot(x, y, "-k")
# plt.errorbar(x,y, yerr=dy, fmt=".r") # Показывает дельту для каждой точки и как она меняется
# # это дискретная погрешность, и бывают и непрерывные погрешности:
# plt.fill_between(x, y - dy, y + dy, color="0.75", alpha=0.3)

# Графики плотности и контурные графики (на 2D изображают как бы 3D)

# x = np.linspace(0, 6, 50)
# y = np.linspace(0, 5, 40)
#
# X, Y = np.meshgrid(x, y)
# print(X.shape)
# print(Y.shape)
#
# print(X)
# print(Y)
# # Получили две матрицы
#
# def f(x,y):
#     return np.sin(x) ** 4 + np.cos(y + x * 30) * np.sin(y)
#
# Z = f(X, Y)
# print(Z)
#
# # plt.contour(X, Y, Z, colors="black") # Получаем набор изолиний
# #plt.contour(X, Y, Z, 10, cmap="RdGy")  # 10 - Кол-во интервалов между равными промежутками, чем значение больше,
# cnt = plt.contour(X, Y, Z, 10, colors="black")
# plt.clabel(cnt, inline=True)
# # тем картина насыщеннее
# # Это дискретная картина, чтобы она стала градиентной, нужно добавить
# #plt.contour(X, Y, Z, 10, cmap="RdGy_r")
#
# # Можно сделать интерполяцию
# plt.imshow(
#     Z,
#     extent=[0, 6, 0, 5],
#     origin="lower",
#     cmap="RdGy",
#     #interpolation="gaussian",
#     aspect="equal",
#     alpha=0.5
# )
# plt.colorbar()

# Гистограммы

rng = np.random.default_rng(1)
# data = rng.normal(size=1000)
#
# plt.hist(data, bins=30, density=True) # bins - основной параметр

# x1 = rng.normal(0, 0.8, 1000)
# x2 = rng.normal(-2, 1, 1000)
# x3 = rng.normal(3, 2, 1000)
#
# p = dict(alpha=0.3, bins=40)
#
# plt.hist(x1, **p)
# plt.hist(x2, **p)
# plt.hist(x3, **p)

#plt.show()
#print(np.histogram(x1, bins=1)) # Посмотреть, что там происходит

# Двумерные гистограммы

mean = [0,0]
cov = [[1,1], [1,3]]
x,y = rng.multivariate_normal(mean, cov, 10000).T

#plt.hist2d(x,y,bins=40)
plt.hexbin(x,y,gridsize=30)
plt.colorbar()

plt.show()

#print(np.histogram2d(x, y, bins=2))