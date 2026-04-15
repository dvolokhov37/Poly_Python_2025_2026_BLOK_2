import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl

# Начнем с того, как можно распологать графики на нашей фигуре (fig)

# Субграфики (как на одном рисунке расположить несколько элементов)

# x = np.linspace(0,10,50)

# ax1 = plt.axes()
# ax1.plot(np.sin(x))
# # (нижний, левый) - фиксируют точку начала координат, от этой точке задаем (ширина, высота) прямоугольника
# # 0.4 - 40% ширины рисунка (И ВСЕ ЧЕТЫРЕ ПАРАМЕТРА: нижний, левый, ширина, высота, ЗАДАЮТСЯ В ПРОЦЕНТАХ)
# ax2 = plt.axes([0.4, 0.3, 0.2, 0.1]) # четыре параметра новой СК задают внутри начальной, которая охватывает всю фигуру
# ax2.plot(np.cos(x))

# fig = plt.figure()
# ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax2 = fig.add_axes([0.4, 0.3, 0.2, 0.1])
# ax1.plot(np.sin(x))
# ax2.plot(np.cos(x))

# ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4])
# ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4])
# ax1.plot(np.sin(x))
# ax2.plot(np.cos(x))

# Будем использовать сетки: графики, которые уже выравнены по строкам и столбцам

# ax1 = fig.add_subplot(2,3,1)
# ax1.plot(np.sin(x + np.pi / 4))

# for i in range(1, 7):
#     ax = fig.add_subplot(2,3,i)
#     ax.plot(np.sin(x + np.pi / 4 * i))

# разнесение графиков четко по строкам и столбцам
# fig, ax = plt.subplots(2, 3, sharex="col", sharey="row") # приведение к одному масштабу
#
# x1 = np.linspace(0,10,50)
# x2 = np.linspace(0,20,100)
#
# # ax[0,0].plot(np.sin(x + np.pi / 4))
#
# for i in range(2):
#     for j in range(3):
#         if i % 2 == 0:
#             ax[i,j].plot(np.sin(x1 + np.pi / 4 * (i*2 + j)))
#         else:
#             ax[i,j].plot(np.sin(x2 + np.pi / 4 * (i*2 + j)))

# Гриды (сетки)

# grid = plt.GridSpec(2, 3, wspace=0.1, hspace=0.1)
# #   0 1 2
# # 0 X Y Y
# # 1 X X X
#
# plt.subplot(grid[0, 0])
# plt.subplot(grid[0, 1:])
# plt.subplot(grid[1, :2])
# plt.subplot(grid[1, 2])

#   0 1 2
# 0 X Y K
# 1 Z Z X

# plt.subplot(grid[0, 0])
# plt.subplot(grid[0, 1])
# plt.subplot(grid[:, 2])
# plt.subplot(grid[1, :2])

# Построим график нормального двумерного распределения

# grid = plt.GridSpec(4, 4, wspace=0.2, hspace=0.2)
#
# # Z X X X
# # Z X X X
# # Z X X X
# #   Y Y Y
#
# rng = np.random.default_rng(1)
# x, y = rng.multivariate_normal([0,0], [[1, 2], [3, 4]], 1000).T
#
# main_axes = plt.subplot(grid[:3, 1:], yticklabels=[]) # X-составляющая
# # вместо "3" везде можно написать "-1" как эквивалентную запись (т.к. 3 - последний элемент)
# y_axes = plt.subplot(grid[:3, 0])  # Y
# x_axes = plt.subplot(grid[3, 1:])  # Z
#
# main_axes.plot(x,y, 'ok', alpha=0.2) # получили нормальное распределение с взаимной ковариацией
# y_axes.hist(y, 40, orientation="horizontal", color="grey")
# y_axes.invert_xaxis()
#
# x_axes.hist(x, 40, color="grey")
# x_axes.invert_yaxis()

# births = pd.read_csv("./data/births-1969.csv")
#
# births['day'] = births['day'].astype(int)
#
# births.index = pd.to_datetime(births["year"] * 10000 + births["month"] * 100 + births["day"], format="%Y%m%d")
#
# print(births)
#
# births_dom = births.pivot_table("births", index=[births.month, births.day])
#
# from datetime import datetime
#
# births_dom.index = [datetime(1969, month, day) for (month, day) in births_dom.index]
#
# fig, ax = plt.subplots()
# births_dom.plot(ax=ax)
#
# ax.text('1969-1-1', 5500, "Новый год")
#
# ax.xaxis.set_major_locator(mpl.dates.MonthLocator(bymonthday=15))
# ax.xaxis.set_major_formatter(mpl.dates.DateFormatter("%h"))
#
# # Аннотации на графике
#
# ax.annotate("Текст аннотации",xy=('1969-1-1', 5500), xytext=('1969-12-1', 4500),
#             #arrowprops=dict(facecolor='black'),
#             arrowprops=dict(arrowstyle="->", facecolor='black', connectionstyle="angle3,angleA=10,angleB=45"))

fig = plt.figure()
ax1 = plt.axes()
ax1.set_xlim(0,2)
ax2 = plt.axes([0.4, 0.3, 0.2, 0.1])

ax1.text(0.6, 0.8, "#1_1", transform=ax1.transData)
ax2.text(0.6, 0.8, "#2_1", transform=ax2.transData)

ax1.text(0.5, 0.1, "#1_2", transform=ax1.transAxes)
ax2.text(0.5, 0.1, "#2_2", transform=ax2.transAxes)

ax1.text(0.05, 0.05, "#1_3", transform=fig.transFigure)
ax2.text(0.2, 0.2, "#2_3", transform=fig.transFigure)

plt.show()