import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# Figure
# На графиках есть оси Axes - axis (x,y)

# grid = plt.GridSpec(1, 2)
#
# ax1 = plt.subplot(grid[0, 0])
# ax1.set_xscale("log")
# ax1.set_xlim(1, 1000)
# # Управление рисочками
# ax1.grid(True, which="major") # основные рисочки
#
# ax2 = plt.subplot(grid[0, 1])
# ax2.set_yscale('log')
# ax2.set(ylim=(1, 1000))
# ax2.grid(True, which="minor", axis="y") # промежуточные рисочки
#
# print(ax1.xaxis.get_major_locator()) # где ставится рисочка
# print(ax1.xaxis.get_major_formatter()) # как пишется значение рисочки
# print(ax1.xaxis.get_minor_locator())
# print(ax1.xaxis.get_minor_formatter())
#
# print(ax1.yaxis.get_major_locator())
# print(ax1.yaxis.get_major_formatter())
# print(ax1.yaxis.get_minor_locator())
# print(ax1.yaxis.get_minor_formatter())
#
# ax1.xaxis.set_major_formatter(plt.NullFormatter())
# ax2.xaxis.set_major_locator(plt.NullLocator())

# from sklearn.datasets import fetch_olivetti_faces
#
# faces = fetch_olivetti_faces().images
#
# fig, ax = plt.subplots(7, 7)
# fig.subplots_adjust(hspace=0, wspace=0)
#
# for i in range(7):
#     for j in range(7):
#         ax[i, j].xaxis.set_major_locator(plt.NullLocator())
#         ax[i, j].yaxis.set_major_locator(plt.NullLocator())
#         ax[i, j].imshow(faces[7 * i + j], cmap="binary_r")

# fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)

# for a in ax.flat:
#     a.xaxis.set_major_locator(plt.MaxNLocator(10)) # сделали количество интервалов по x = 10
#     a.yaxis.set_major_locator(plt.MaxNLocator(2))

# def ff(value, tick_number):
#     N = int(np.round(2 * value / np.pi)) # количество pi/2
#     if N == 0:
#         return 0
#     elif N == 1:
#         return r"$\frac{\pi}{2}$"
#     elif N == 2:
#         return r"$\pi$"
#     elif N % 2 == 0:
#         t = int(N / 2)
#         return f"{t}" + r"$\pi$"
#     else:
#         return f"{N}" + r"$\frac{\pi}{2}$"
#
#    # Такие будут значения: 0, pi/2, 3/2 pi, 2 pi, 5/2 pi, 3 pi, 7/2 pi, 4 pi
#     return value
#
# x = np.linspace(0, 4 * np.pi, 1000)
#
# fig, ax = plt.subplots()
#
# ax.plot(x, np.sin(x), label="Sinus")
# ax.plot(x, np.cos(x), label="Cosinus")
#
# ax.grid(True)
# ax.legend()
# ax.set_xlim(0, 4 * np.pi)
#
# ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 4))
#
# ax.xaxis.set_major_formatter(plt.FuncFormatter(ff)) # В качестве параметра к форматору передали функцию, которая форматирует
# # значения в зависимости от наших требований

# fig, ax = plt.subplots(8, 1)
#
# plt.subplots_adjust(hspace=0.5)
#
# x = np.linspace(0, 20, 10)
#
# for i in ax.flat:
#     i.plot(x, x * 0 + 2)
#
# # Локаторы влияющие на рисочки
# ax[0].xaxis.set_major_locator(plt.NullLocator())
# ax[1].xaxis.set_major_locator(plt.MultipleLocator(0.8))
# ax[2].xaxis.set_major_locator(plt.FixedLocator([1,3,8,9]))
# ax[3].xaxis.set_major_locator(plt.LinearLocator(numticks=4))
# ax[4].xaxis.set_major_locator(plt.IndexLocator(base=2, offset=1.3))
# ax[5].xaxis.set_major_locator(plt.AutoLocator())
# ax[6].xaxis.set_major_locator(plt.MaxNLocator(8))
# ax[7].xaxis.set_major_locator(plt.LogLocator(base=3))
#
# import matplotlib.ticker as mtick
#
# ax[1].xaxis.set_major_formatter(plt.NullFormatter())
# ax[2].xaxis.set_major_formatter(plt.FixedFormatter(['a', 'b', 'c', 'd']))
# ax[3].xaxis.set_major_formatter(plt.FormatStrFormatter('%.2f $m^2$'))
# ax[4].xaxis.set_major_formatter(mtick.PercentFormatter(xmax=4))

# Визуальная настройка графика (раскраска, например)

# plt.style.use('./lec_13.style') # сгрузили все стили в этот файл
# это ресурсный файл
# lec_13.style:
# figure.facecolor: "#921212"
# axes.facecolor: "#adadad"

# print(plt.style.available)
# exit()

# plt.style.use('grayscale')

# x = np.random.rand(1000)
#plt.figure(facecolor='#921212')
#plt.axes(facecolor='#adadad')

# plt.rc("figure", facecolor='#921212') # создали ресурс
# plt.rc("axes", facecolor='#adadad')
#
# plt.hist(x)

# 3D графика в Matplotlib

from mpl_toolkits import mplot3d

def f(x,y):
    return np.sin(np.sqrt(x**2 + y**2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-10, 10, 50)
# всего 1500 элементов т.к. 30*50

print(x.shape)
print(y.shape)

X, Y = np.meshgrid(x, y)

print(X.shape)
print(Y.shape)

print(X)
print(Y)

Z = f(X, Y)

print(Z.shape)
print(Z)

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.contour3D(X, Y, Z, 40) # чем больше числовой параметр, тем меньше расстояние меж элементами
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# Повороты самого 3D-представления
ax.view_init(30, 90)

plt.show()