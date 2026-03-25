import numpy as np
import pandas as pd

# Пример: Список дат и управление через временные периоды
# print(pd.date_range("2026-01-01", periods=4, freq="ME"))
#
# print(pd.date_range("2026-01-01", periods=4, freq="MS"))
#
# print(pd.date_range("2026-01-01", periods=4, freq="QE"))
#
# print(pd.date_range("2026-01-01", periods=4, freq="QS"))
#
# print(pd.date_range("2026-01-01", periods=4, freq="W"))
#
# print(pd.date_range("2026-01-01", periods=4, freq="W-MON"))

# ind = pd.read_csv("./data/index.csv", sep=';', parse_dates=["Date"])
#
# print(ind.head())
#
# print(type(ind))
# print(ind.dtypes)
#
# index = pd.DatetimeIndex(ind["Date"])
#
# ind.index = index
# ind = ind["Close"]
# print(ind.head())
#
# import matplotlib.pyplot as plt
#
# ind.plot()
# plt.show()

# Следующий пример:
# Чтобы здесь распарсить дату, нужно сделать следующее
# (не просто parse_dates=["Date"])
df = pd.read_csv("./data/FremontBridge.csv",
                 index_col="Date",
                 parse_dates=True,
                 #date_format="%Y-%m-%d %I:%M:%S %p"
                 date_format="%m/%d/%Y %I:%M:%S %p")
# Важно правильно представить дата-формат (чтобы корректно распарсилось)
print(df.head())
print(df.dtypes)

print(df.columns)
df.columns=["Total", "East", "West"]
print(df.head())

print(df.describe())
# Удалим те данные, которые неопределены, дропнув их
print(df.dropna().describe())

import matplotlib.pyplot as plt

# df.plot()
# plt.ylabel("Кол-во велосипедистов (в час)")
# plt.show()

# Вместо часовой даты делаем недельную
# weekly = df.resample("W").sum()
# weekly.plot(style=["-", ":", "--"])
# plt.ylabel("Кол-во велосипедистов (по неделям)")
# plt.show()

# На данные повесим некоторое скользящее окно, которое охватывает некоторое
# кол-во элементов, и высвечивать на каждую дату среднее значение
# т.е. использовать Скользящее среднее

# Изначально в дате - часы; складываем все часы одного дня, чтобы была дата по дням
# daily = df.resample("D").sum()
# # center = False -> берутся прошлые значения от выбранного
# # center = True -> берутся прошлые и будущие значения от выбранного
# daily.rolling(30, center=True).mean().plot(style=["-", ":", "--"])
# # Среднемесячное - т.к. в rolling поставили значение 30, если бы поставили 7 - было бы средненедельное
# plt.ylabel("Средне месячное кол-во велосипедистов (скользящее окно)")
# plt.show()

# Способы сглаживания данных
# daily = df.resample("D").sum()
# daily.rolling(30, center=True, win_type="gaussian").mean(std=5).plot(style=["-", ":", "--"])
# plt.ylabel("Средне месячное кол-во велосипедистов (скользящее окно)")
# plt.show()

# До этого показывали даты в различных периодах

# Если хочется построить такой же график в зависимости от времени суток

# График по часам
# timely = df.groupby(df.index.time).mean()
# ticks = 60 * 60 * 4 * np.arange(6) # Управление рисочками на графике
# # print(ticks)
# timely.plot(xticks=ticks)
# plt.show()

# График по дням недели
# weekly = df.groupby(df.index.dayofweek).mean()
# weekly.plot()
# plt.show()

# Сравнительный график в выходные и в будни по часам

# w1 = np.where(df.index.weekday < 5, "Будни", "Выходные") # т.к. на графике индексы дней недели от 0 до 6
# # получили массив из слов - "будни" или "выходные"
# # Теперь должны сгруппироваться не только времени, но вторым индексом идёт "будни" или "выходные"
# t1 = df.groupby([w1, df.index.time]).mean()
#
fig,ax = plt.subplots(1, 2)
# ax[0].set_ylim(0,600)
# t1.loc["Будни"].plot(ax=ax[0], title="Будни")
#
# ax[1].set_ylim(0,600)
# t1.loc["Выходные"].plot(ax=ax[1], title="Выходные")
# plt.show()


# НОВЫЙ БЛОК: Matplotlib

# pip instal matplotlib
# pip instal pyqt5

import matplotlib.pyplot as plt

plt.style.use('classic') # цветовая схема

# Как отображаются графики
plt.show() # !должно быть в единственном экземпляре
# Как plt.show работае: Ищутся все активные фигуры и по очереди показываются

# Можно запускать из оболочки ipython
# Модуль IPython д.б. установлен
# $ python -m IPython

# In [1]: %matplotlib
# Using matplotlib backend: qtagg
#
# In [2]: import numpy as np
#
# In [3]: import matplotlib.pyplot as plt
#
# In [4]: x = np.linspace(0, 10, 100)
#
# In [5]: plt.plot(x, np.sin(x))
# Out[5]: [<matplotlib.lines.Line2D at 0x7f871bffb050>]

# И также можно через Jupyter Notebook:
# Здесь всё проще и никаких plt.show не нужно

# %matplotlib inline
# import numpy as np
# x = np.linspace(0, 10, 100)
# plt.plot(x, np.sin(x))

# Для сохранения картинки потребуется fig
# fig.savefig('ttt.png')

# Если хотим картинку нарисовать
# from IPython.display import Image
# Image('ttt.png')

# Стандарты форматов графических файлов
print(fig.canvas.get_supported_filetypes())
# {'eps': 'Encapsulated Postscript', 'jpg': 'Joint Photographic Experts Group', 'jpeg': 'Joint Photographic Experts Group', 'pdf': 'Portable Document Format',
# 'pgf': 'PGF code for LaTeX', 'png': 'Portable Network Graphics', 'ps': 'Postscript', 'raw': 'Raw RGBA bitmap', 'rgba': 'Raw RGBA bitmap',
# 'svg': 'Scalable Vector Graphics', 'svgz': 'Scalable Vector Graphics', 'tif': 'Tagged Image File Format', 'tiff': 'Tagged Image File Format', 'webp': 'WebP Image Format'}