import numpy as np
import pandas as pd

# Строковые операции в Pandas

data = ["one one", "TWO TWO", "tHREE tHREE", "fOuR fOuR"]
print(data)

# Если захотим перевести эти элементы в вид, где только первый символ - заглавная буква:

print([s.capitalize() for s in data])

names = pd.Series(data)
print(names)

print(names.str.capitalize()) # атрибут str открывает доступ к функциям, работающим с data

# str -- открывает доступ к операциям, связанным со строками

print(names.str.lower()) # все элементы к нижнему регистру

print(names.str.len())

print(names.str.startswith('t'))

print(names.str.split())

# К строкам также можно применять различные операции, связанные с использованием регулярных выражений:

import re # модуль регулярных выражений (практически все методы из этого модуля есть в модуле Pandas)

data = ["one1 one2 one3", "two999 ddd ", "tHREE tHREE", "fOuR fOuR"]
names = pd.Series(data)

# сервис для проверки валидности регулярных выражений: https://regex101.com/

rgex = r"([a-z0-9]+\s)([a-z0-9]+\s).*" # - наше регулярное выражение
a = names.str.extract(rgex) # для каждого массива будет вызываться этот метод и возвращать подходящие
# группы, которые мы хотим здесь высветить, в виде строчек
# доступ к регулярным выражениям осуществляем так же через атрибут str

print(a) # на выходе получается dataframe

print(type(a))

rgex = r"([a-z0-9]+\s).*"
a = names.str.extract(rgex, expand=False)
print(a)

print(type(a))

data = ["one1 one2 one3", "two999 ddd ", "tHREE tHREE", "fOuR fOuR"]
names = pd.Series(data)

print(names.str.get(2)) # get самостоятельно индексирует все элементы
print(names.str[2])

print(names.str[0:3])
print(names.str.slice(0,3))

print(names.str[-1])

# ИНДИКАТОРНЫЕ ПЕРЕМЕННЫЕ

data = ["one1 one2 one3", "two999 ddd ", "tHREE tHREE", "fOuR fOuR"]
names = pd.DataFrame({"name": data, "info": ["A|B", "B|C", "A|B|C", "D"]}) # info - как битовая маска

# По сути здесь категориальные данные

print(names)

print(names['info'].str.get_dummies('|')) # узнать, как распределяются признаки по строчкам info

# https://github.com/jakevdp/open-recipe-data - здесь база рецептов, где каждая строчка - набор полей

# recipes = pd.read_json('./data/recipeitems.json', lines=True)
# print(recipes.head())
#
# print(recipes.shape)
#
# print(recipes.iloc[0])
#
# print(recipes.ingredients.str.len())
#
# print(recipes.ingredients.str.len().describe())
#
# print(recipes.name[np.argmax(recipes.ingredients.str.len())]) # хотим найти номер элемента с максимальной длиной
#
# print(recipes.description.str.contains('Breakfast').sum())
# print(recipes.description.str.contains('breakfast').sum())
#
# spices = ["salt", "pepper", "cream"]
#
# result = pd.DataFrame({i: recipes.ingredients.str.contains(i) for i in spices})
#
# print(result)
#
# select = result.query("salt & pepper & cream")
#
# print(select.index)
#
# print(recipes.name[select.index].head())

# ВАЖНО! В Pandas, когда работаем с Series и DataFrame, операции со строками ложатся на каждый элемент
# массива, т.е. всё это векторизуется, работает параллельно и достаточно быстро


# Заключительная тема по Pandas: РАБОТА С ВРЕМЕННЫМИ РЯДАМИ

# Существует три способа хранения временных данных в Pandas
# 1)  Конкретные моменты времени, т.е. абсолютные значения, например "1 января 2026 года 00:00"
# 2)  Периоды или временные интервалы - есть конечная и начальная точка (мб не абсолютным),
# например "март 2025 года" - это интервал, "24 часа", "7 дней" - периоды
# 3)  Продолжительность (временная дельта) = 15 минут

# Что есть в Python?
from datetime import datetime
import dateutil

d = datetime(year=2026, month=3, day=4)
print(d)
print(type(d))

d = dateutil.parser.parse("4th of March, 2026")
print(d)
print(type(d))

print(d.strftime("%A"))

# Что есть в Numpy?

d = np.array("2026-03-04", dtype=np.datetime64)
print(d)
print(d.dtype)

print(d + 1) # здесь базовая единица - день

d1 = np.array("2026-03-04 00:00", dtype=np.datetime64)
print(d1)
print(d1.dtype)

print(d1 + 1) # здесь базовая единица - минута

# Над датами в Numpy можно осуществлять векторизованные операции
d2 = d + np.arange(12)
print(d2)

t = np.array(12, dtype=np.timedelta64)
print(t)
print(t.dtype)

# В основе лежит базовая единица - time unit; кол-во элементов т.к. 64 битная 2^64 возможных значений, и
# в зависимости от базовых элементов различное количество дат и времен может храниться

d = np.datetime64("2026-03-04", "D")
print(d)
print(d + 1)

d = np.datetime64("2026-03-04", "Y")
print(d)
print(d + 1)

d = np.datetime64("2026-03-04", "W")
print(d)
print(d + 1)

d = np.datetime64("2026-03-04", "ns")
print(d)
print(d + 1)

t = np.timedelta64(1, "D")
print(t)
print(t + 1)

t1 = np.timedelta64(1, "M")
print(t1)
print(t1 + 1)

# print(t + t1) - так делать нельзя, unitы д.б. одинаковыми
# если есть совместимость unitов, то складывать можно

t = np.timedelta64(1, "s")
print(t)
print(t + 1)

t1 = np.timedelta64(100, "ms")
print(t1)
print(t1 + 1)

print(t + t1)

print(np.timedelta64(t + t1, "ns"))

# Базовые unitы: Y M W D h m s ms ns ...

# Что есть в Pandas?
# Timestamp (numpy.datetime64) - можно использовать как объект индексации

d = pd.to_datetime("4th of March, 2026")
print(d)
print(type(d))

print(d.strftime("%A"))

d2 = d + pd.to_timedelta(np.arange(30), "D")
print(d2)
print(type(d2))

index = d2
data = pd.Series(np.arange(30), index=index)

print(data)

print(data["2026-03-06": "2026-03-10"]) # помним про лексиграфический порядок

print(data["2026-04"])

# РАБОТА С ВРЕМЕННЫМИ РЯДАМИ

# Существует три способа хранения временных данных в Pandas
# 1)  Конкретные моменты времени, т.е. абсолютные значения, например "1 января 2026 года 00:00"
# В Pandas - это Timestamp (numpy.datetime64)
# 2)  Периоды или временные интервалы - есть конечная и начальная точка (мб не абсолютным),
# например "март 2025 года" - это интервал, "24 часа", "7 дней" - периоды
# Здесь в Pandas: Period (numpy.datetime64) - PeriodIndex
# 3)  Продолжительность (временная дельта) = 15 минут
# Здесь в Pandas: Timedelta (numpy.timedelta64) - TimedeltaIndex

# Timestamp (numpy.datetime64)
d = pd.to_datetime("4th of March, 2026")
print(d)
print(type(d))

ds = pd.to_datetime(["2026-03-04", "2026-03-05"])
print(ds)

# Period (numpy.datetime64) - PeriodIndex
p = ds.to_period("D")
print(p)
print(type(p))

# Timedelta (numpy.timedelta64)
delt = ds[1] - ds[0]
print(delt)
print(type(delt))

# TimedeltaIndex
idelt = ds - ds[0]
print(idelt)
print(type(idelt))

# Иногда нужно создать регулярные последовательности этих элементов

print(pd.date_range("2026-01-01", "2026-03-04"))

hh = pd.date_range("2026-01-01", periods=10, freq="h")
print(hh)
print(hh[0] + 2 * hh.freq)

print(pd.period_range("2026-01-01", periods=10, freq="M"))

print(pd.timedelta_range(0, periods=10, freq='h'))

# Периодичность и смещение дат
# Коды периодичности
# Месяц, квартал, год (показывают именно на конец этих элементов) - M Q A
# MS QS AS - показывают на начало этих элементов

p1 = pd.Period("2026Q1")
print(p1)
print(p1.month)
print(p1.day)

print(pd.timedelta_range(0, periods=10, freq='2h15min'))

# Иногда нужно учитывать не просто дни, а только рабочие дни
from pandas.tseries.offsets import BDay

hh = pd.date_range("2026-02-01", periods=20, freq=BDay())
print(hh)