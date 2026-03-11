import numpy as np
import pandas as pd

rng = np.random.default_rng(1)

mi1 = pd.MultiIndex.from_product([["A1", "A2"], [2025, 2026]], names = ["property", "year"])
print(mi1)

mi2 = pd.MultiIndex.from_product([["B1", "B2", "B3"], ["jan", "feb"]], names = ["shop", "month"])
print(mi2)

data = rng.random((4,6))
print(data)

df = pd.DataFrame(data, index=mi1, columns=mi2)
# print(df)
#
# # Как осуществляется доступ к элементам набора данных df:
#
# # 1) Просто по индексам
# print(df["B2"]) # При обращении просто по индексам сначала идут столбцы
# print(df["B2", "feb"]) # Уточняем детализацию: нужен только февраль
#
# # 2) Прямым указанием индексов через iloc (конкретные номера строк и столбцов),
# # и так как это срезы, здесь сначало идут строки,а потом столбцы
# print(df.iloc[1:, 2:5])
# # 3) Если вместо iloc поставим loc, то в таком случае можем указывать уже названия
# print(df.loc[:, "B1"]) # Все строки захватим, а в качестве столбцов только по B1
#
# print(df.loc[:, ("B1", "jan")])
#
# print(df.loc[:, (["B1", "B2"], "jan")])
#
# ind1 = pd.IndexSlice[:, 2025]
# ind2 = pd.IndexSlice[:, "jan"]
#
# print(df.loc[ind1, ind2])

# Мультииндексирование - когда у столбцов и строк индекс может быть многоуровневым (в виде кортежа),
# т.е. два уровня - это не предел, и выбирать через срезы себы кусочки нужных данных

# ИТОГИ
# Как к мультииндексированному массиву можем обращаться:
data = {
    ("A1", 2025): 1,
    ("A1", 2026): 2,
    ("A1", 2027): 3,
    ("A2", 2025): 11,
    ("A2", 2026): 12,
    ("A2", 2027): 13,
    ("A3", 2025): 21,
    ("A3", 2026): 22,
    ("A3", 2027): 23,
} # Двойная индексация, где на первом уровне: три элемента, на втором тоже три

sr = pd.Series(data)
sr.index.names = ["property", "year"]

print(sr)
# Индексация (поиск) по нескольким индексам
print(sr["A1"])
print(sr["A1", 2027])
print(sr[:, 2027])

print(sr.loc["A2":"A3", 2025:2026]) # через loc с указанием элементов

print(sr[sr > 12]) # через булеву маску

print(sr.loc[["A1","A3"], 2025:2026])

# Индексы внутри начальной структуры (data) д.б. отсортированы по алфавиту или, в случае чисел, по возрастанию:
# Пример
# Отсортированный
index = pd.MultiIndex.from_product([["a", "b", "c"], [1,2]])

data = pd.Series(rng.random(6), index=index)
print(data)
print(data['a':'b'])
# Поэтому, когда делаем срезы - важен лексиграфический порядок, без него работать не будет

# Неотсортированный
index = pd.MultiIndex.from_product([["a", "c", "b"], [1,2]])

data = pd.Series(rng.random(6), index=index)
print(data)

# НО! Если что-то не так - данные всегда можно подправить сортировкой (и сортируются все уровни данных)
data = data.sort_index()
print(data)

print(data['a':'b'])

# Многоуровневые индексы на строках и столбцах могут перемещаться друг между другом (иногда это мб полезно)

data = {
    ("A1", 2025, 1): 1,
    ("A1", 2025, 2): 2,
    ("A1", 2026, 1): 3,
    ("A1", 2026, 2): 4,
    ("A1", 2027, 1): 5,
    ("A1", 2027, 2): 6,
    ("A2", 2025, 1): 11,
    ("A2", 2025, 2): 12,
    ("A2", 2026, 1): 13,
    ("A2", 2026, 2): 14,
    ("A2", 2027, 1): 15,
    ("A2", 2027, 2): 16,
    ("A3", 2025, 1): 21,
    ("A3", 2025, 2): 22,
    ("A3", 2026, 1): 23,
    ("A3", 2026, 2): 24,
    ("A3", 2027, 1): 25,
    ("A3", 2027, 2): 26,
} # Сделали трехуровневую структуру
sr = pd.Series(data)
print(sr)

# Способ перегруппировки индекса (т.о. появятся вместо одного - несколько столбцов)
print(sr.unstack()) # Переводит второй (третий) уровень "1 2" в название столбцов
print(sr.unstack(level=2)) # Делает то же самое, что и строчкой выше
print(sr.unstack(level=1)) # В столбцы уже переедут года
print(sr.unstack(level=0)) # Переехал в столбцы нулевой уровень

sr.index.names = ["product", "year", "count"]

print(sr)
print(type(sr))

df = sr.reset_index(name="value") # Сбросили мультииндекс, а значения, которые входили
# в этот мультииндекс мы превратили в соответствующие задаваемые столбцы "product", "year", "count", "value"
print(df)
print(type(df))

# Часто бывают ситуации, когда мы хотим, чтобы дата стала индексом (например, чтобы "product" стал индексом)
print(df.set_index("product")) # Становится индексом

# Индексом можно сделать ни один "product", а несколько элементов
print(df.set_index(["product", "count"]))

# Т.о. можем собрать свой индекс из линейных столбцов так, как хотим

# К данным в Pandas-конструкциях (Series, DataFrame) можем применить некоторые операции очень похожие на SQL-запросы

# НОВАЯ ТЕМА: СВОДНЫЕ ТАБЛИЦЫ
# представляют собой представление многомерных данных в виде двумерных таблиц
import seaborn as sns

# titanic = sns.load_dataset('titanic')
# print(type(titanic))
#
# print(titanic.head())
#
# print(titanic.groupby("sex")["survived"].mean())
#
# print(titanic.groupby(["sex", "class"])["survived"].mean())
#
# print(titanic.groupby(["sex", "class"])["survived"].mean().unstack())

births = pd.read_csv("./data/births.csv")

print(births.head())

# Собрать данные по десятилетиям
# Добавим в births.csv столбец "decade"

births["decade"] = 10 * (births["year"] // 10)

print(births.head())

# Делаем сводную таблицу с помощью функции pivot_table

print(births.pivot_table("births", index="decade", columns="gender", aggfunc="sum"))

import matplotlib.pyplot as plt

births_years = births.pivot_table("births", index="year", columns="gender", aggfunc="sum")
# births_years.plot()

# Построим теперь не просто график, а гистограмму
# plt.hist(births[births["year"] == 1969]["births"], bins=100)

# Удаляем выбросы в данных с помощью квартилей

q = np.percentile(births["births"], [25, 50, 75]) # все данные выстраивают по возрастанию, считают количество
# и делят на группу с одинаковым количеством элементов внутри; здесь 50 - это медиана

print(q)

m = q[1] # медиана
sig = 0.74 * (q[2] - q[0]) # сигма - корень из дисперсии; 0.74 - const (межквартильный размах)
# это делается для того, чтобы понять, где именно на этом колокольчике нужно обрезать данные

births = births.query("(births > @m - 5*@sig) & (births < @m + 5*@sig)")# теперь из датасета births хотим убрать часть элементов

# plt.hist(births[births["year"] == 1969]["births"], bins=100)

# plt.show()

print(births.dtypes)

print(births.index)

# Пример, когда в качестве индекса хочется взять дату
births['day'] = births['day'].astype(int)

births.index = pd.to_datetime(births["year"] * 10000 + births["month"] * 100 + births["day"], format="%Y%m%d") # собираем дату
# ВАЖНО: индекс собирается из элементов строки, по результатам каждая строка получает свой идентификатор, и потом
# это все лексикографически сортируется (в случае дат по увеличению даты)

print(births.index)

births["dayofweek"] = births.index.dayofweek

print(births.head())

# Пример: посмотрим рождения в зависимости от дней недели

births_dow = births.pivot_table("births", index="dayofweek", columns="decade", aggfunc="mean")

print(births_dow)

# Двумерный индекс
births_dom = births.pivot_table("births", index=[births.month, births.day]) # получился мультииндекс

print(births_dom)

from datetime import datetime

print(births.dtypes)

births_dom.index = [datetime(2012, month, day) for (month, day) in births_dom.index]

print(births_dom.head())

births_dom.plot()
plt.show()

# Сводные таблицы - это возможность самим создать индексы из элементов данных + использование SQL-подобных выражений