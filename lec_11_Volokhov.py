import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl

# Легенды на графиках

x = np.linspace(0, 10, 1000) # x - одномерный массив

# fig, ax = plt.subplots()
#
# ax.plot(x, np.sin(x), "-k", label="Синус")
# ax.plot(x, np.cos(x), "--r", label="Косинус")
# ax.axis("equal") # делает одинаковый масштаб по x и y
#
# ax.legend(frameon=True, shadow=True, borderpad=1, loc="lower center", ncol=2)
# # frameon=False - прямоугольник с легендой убрали

y = np.sin(x[:,np.newaxis] + np.pi * np.arange(0, 2, 0.5)) # чтобы всё работало, нужно добавить новую ось
# благодаря np.arange получили несколько графиков

# lines = plt.plot(x, y)
#
# # plt.legend(lines[:3], ["первая", "вторая", "третья"])
# plt.legend(lines, ["первая", "вторая", "третья", "четвертая"])

# plt.plot(x, y[:, 0], label="первый")
# plt.plot(x, y[:, 1], label="второй")
# plt.plot(x, y[:, 2:])
# plt.legend()

# cities = pd.read_csv("./data/california_cities.csv")
#
# latd = cities['latd'],
# longd = cities['longd'],
# population_total = cities['population_total'],
# area_total_km2 = cities['area_total_km2']
#
# plt.scatter(
#     latd,
#     longd,
#     c=np.log10(population_total),
#     s=area_total_km2,
#     alpha=0.5
# )
# plt.colorbar()
#
# # Легенда д.б. привязываться к графику
# # создадим фиктивную легенду (т.е. легенда создается за счёт фиктивных графиков, которые ничего не рисуют)
#
# plt.scatter([],[],s=100, c='k', alpha=0.5, label='100 $км^2$')
# plt.scatter([],[],s=300, c='k', alpha=0.5, label='300 $км^2$')
# plt.scatter([],[],s=500, c='k', alpha=0.5, label='500 $км^2$')
#
# plt.legend(frameon=False, labelspacing=2, title="Площадь")
#
# plt.axis("equal")

# Это был матлабовский способ
# а нам может понадобиться доступ к отдельным графикам:

# fig, ax = plt.subplots()
#
# lines = ax.plot(x, np.sin(x[:,np.newaxis] - np.pi/2 * np.arange(0, 4)))
# ax.axis("equal")
#
# # Хотим сделать различные легенды
# ax.legend(lines[:2], ['line A', 'line B'], loc='lower right')
#
# # ax.legend(lines[2:], ['line C', 'line D'], loc='upper right') # так сделать НЕ можем
#
# # Создаем легенду как объект
# leg = mpl.legend.Legend(ax, lines[2:], ['line C', 'line D'], loc='upper right')
# # теперь эту легенду можем разместить на новом слое
#
# ax.add_artist(leg) # принудительно эту легенду отображаем на новом слое
#
# leg2 = mpl.legend.Legend(ax, lines[2:], ['line C', 'line D'], loc='upper left')
#
# ax.add_artist(leg2)

# Цветовые шкалы

y = np.sin(x) * np.cos(x[:,np.newaxis])

# Есть три вида (схем) карт:
# 1) Последовательная - непрерывная последовательность цветов, дискретности не видно
# plt.imshow(y, cmap='binary')

# 2) Дивергентная - задаем два цвета, они переходят один в другой через третий цвет
# plt.imshow(y, cmap='RdGy')

# 3) Много цветов в некотором порядке
# plt.imshow(y, cmap='jet')

# В черно-белых вариантах всплески интенсивности разные
# И есть цветные схемы, которые хорошо отображаются в черно-белом варианте
# plt.imshow(y, cmap='jet')
# plt.imshow(y, cmap='viridis')
# plt.imshow(y, cmap='RdBu')
# plt.imshow(y, cmap='Set1') # пример дискретной шкалы
# plt.colorbar()

# Т.к. язык и библиотека объектно-ориентированные, мы можем обращаться к цветовым шкалам
# как к экземплярам некоторого класса

from sklearn.datasets import load_digits

digits = load_digits(n_class=6)

# fig, ax = plt.subplots(8,8)
# for i, ax_ in enumerate(ax.flat):
#     ax_.imshow(digits.images[i], cmap="binary")
#     ax_.set(xticks=[], yticks=[])

# Каждая цифра - это 64 атрибута (элемента) со значениями от 0 до 1
# Можем понизить их размерность, чтобы нарисовать их в двумерной плоскости

from sklearn.manifold import Isomap

iso = Isomap(n_components=2, n_neighbors=10)
prj = iso.fit_transform(digits.data)

plt.scatter(prj[:, 0], prj[:, 1], c=digits.target, cmap=plt.cm.get_cmap("jet",6))
plt.colorbar(ticks=range(6))
plt.clim(-0.5, 5.5)

# cmap можно управлять, и делать дискретным на какое-то кол-во элементов

plt.show()