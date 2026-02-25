# Pandas - удобная надстройка над NumPy. В основе тот же NumPy массив, в котором хранятся значения одного и того же
# типа, и достаточно быстро совершает различные операции. В основе лежат универсальные функции, которые позволяют
# параллельно производить векторизованные операции над каждым элементом.
# Основные элементы в массиве Pandas:
# 1. Series - обертка для NumPy массива, где индексы мб не только числовыми
# 2. DataFrame - набор Series (т.е. матрица, где в качестве индексов строк мб метки разного типа)
# 3. Index
# В Pandas индексы могут быть не только числового типа, работа с отсутствующими данными (пробелы и т.д.), можно делать
# что-то а-ля SQL - графики, сводные таблицы

import numpy as np
import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0]) # экземпляр класса Series (передаем в него список из действительных чисел)
print(data)

print(data.values)
print(type(data.values))

print(data.index) # экземпляр класса RangeIndex из библиотеки Pandas
print(type(data.index))

print(data[1])
print(data[1:3])
# в NumPy неявно задаются целочисленные индексы начиная с нуля, а в Series все индексы определены явно
# Пример:
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=["a", "b", "c", "d"])
print(data)

print(type(data.index[0]))
print(data["a"])
print(data["b":"d"])

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[1, 10, 7, "d"])
print(data)

print(data.index)
print(type(data.index))
print(type(data.index[0]))
print(type(data.index[3]))

print(data[1])
print(data["d"])
print(data[10:"d"])

dict = {
    'A': 10,
    'B': 20,
    'C': 30,
    'D': 40,
    'E': 50,
}

data_dict = pd.Series(dict)
print(data_dict)
print(data_dict['B'])
print(data_dict['B':'D'])

# Итак, как можно создать объект Series
# 1. Через списки
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)

data = pd.Series(5, index=[10, 20, 30])
print(data)

# 2. Через словарь
# Ключи поедут в метки, значение элементов массива - значение в словаре
data_dict = pd.Series(dict, index=["A", "D"])
print(data_dict)

# DataFrame - всегда двумерный массив с явно определяемыми индексами (можно представить, что это несколько объектов
# типа Series, сложенных вместе

dict1 = {
    'A': 10,
    'B': 20,
    'C': 30,
    'D': 40,
    'E': 50,
   # 'F': 60,
}

data_dict1 = pd.Series(dict1) # создали Series
print(data_dict1)

dict2 = {
    'A': 11,
    'B': 21,
    'C': 31,
    'D': 41,
    'E': 51,
   # 'H': 71,
}

data_dict2 = pd.Series(dict2) # создали Series
print(data_dict2)

df = pd.DataFrame({"dict_01": data_dict1, "dict_02":data_dict2}) # создали DataFrame
print(df)

print(df.values)
print(type(df.values))

print(df.columns) # метки столбцов
print(type(df.columns))

print(df.index) # метки строк
print(type(df.index))

print(df["dict_01"])
print(df["dict_02"])

print(type(df["dict_01"]))

df = pd.DataFrame({"dict_01": data_dict1}) # Series - не вектор строка, а DataFrame уже вектор строка, у него две размерности
print(df)

print(df.values)

print(data_dict1)
df = pd.DataFrame(data_dict1, columns=["rrr"])
print(df)

print(pd.DataFrame([{"a": i, "b": 2 * i} for i in range(4)]))

# Если ключи не совпадают, появяться значения типа NaN - Not a Number

# Двумерный массив тоже можно использовать в качестве начальных значений для создания DataFrame
print(pd.DataFrame(np.zeros(3)))

# Index - способ сослаться (reference) на данные в Series или в DataFrame

index = pd.Index([2, 5, 3, 5, 71])
print(index)
print(type(index))

print(index[1])
print(index[::2])

# Важно! index[1] = 21 - индексы менять нельзя

# Индексы очень похожи на множества
index1 = pd.Index([2, 5, 3, 5, 71])
index2 = pd.Index([1, 2, 51, 71, 4])

print(index1.intersection(index2))
print(index1.union(index2))
print(index1.symmetric_difference(index2))

# Как можно из Series и DataFrame выбирать данные
# В NumPy могли выбирать данные след. образом:
# 1. Простая индексация: arr[1,2]
# 2. Срезы: arr[:, 1:4]
# 3. Маскирование: arr[arr > 5]
# 4. Прихотливая индексация: arr[0, [1,5]]; arr[:, [1,5]]

# В Pandas:
# Series
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=["a", "b", "c", "d"])
print(data)

# print(data["a"])
#
# print("a" in data) # уточняем, есть ли эта метка в data
# print("a1" in data)
#
# # Можно вынимать данные в виде списка кортежей (первый элемент кортежа - метка, второй - значение)
# print(list(data.items()))
#
# print(data)
#
# # Изменение и добавление данных по индексу
# data["a"] = 99
# print(data)
#
# data["a1"] = 990
# print(data)
#
# # срезы
# print(data["c": "a1"])
#
# print(data[2:4])
# print(data[2:])

# маскирование

print(data[(data > 0.3) & (data < 0.8)])

print(data.loc[["c", "a"]])

print(data.iloc[[2, 0]])

# loc, iloc - атрибуты-индексаторы; нужны для того, чтобы понимать, что подразумевается: значение ключа или номер индекса
# loc - название ключей
# iloc - название индексов

# DataFrame
dict1 = {
    'A': 10,
    'B': 20,
    'C': 30,
    'D': 40,
    'E': 50,
   # 'F': 60,
}

data_dict1 = pd.Series(dict1)
print(data_dict1)

dict2 = {
    'A': 11,
    'B': 21,
    'C': 31,
    'D': 41,
    'E': 51,
   # 'H': 71,
}

data_dict2 = pd.Series(dict2)
print(data_dict2)

df = pd.DataFrame({"dict_01": data_dict1, "dict_02":data_dict2})
print(df)

# print(df["dict_01"]) # доступ к столбцу
# print(df.dict_01) # сокращение (если нет никаких проблем)

df["new"] = df["dict_01"] # добавление нового столбца
print(df)

df["new1"] = df["dict_01"] / df["dict_02"] # поэлементные операции, универсальные функции, всё здесь работает
print(df)

# Теперь работаем с DataFrame не как со словарем, а как с двумерным массивом
print(df.values)

# print(df.T) # транспонирование

print(df["dict_01"]) # столбец
print(df.values[0]) # строка (перешли в NumPy режим)

# атрибуты-индексаторы здесь тоже работают (лучше через них указать, что хотим использовать)

print("sssssssssssssss")
print(df)

print(df.loc["A":"C", :"dict_02"])
print(df.iloc[:3, :2])

print(df.loc[df.dict_02 > 30, ["new1", "dict_01"]])

df.loc[df.dict_02 > 30, ["new1", "dict_01"]] = 36
print(df)

# операции над каждым элементом массива, совмещение индексов
# Пример:

rng = np.random.default_rng(1)
s = pd.Series(rng.integers(0, 10, 6))

print(s)

print(np.exp(s))

# индексация сохранится: взяли элемент из Pandas (Series), но используем функции NumPy, хотя NumPy про Series ничего не знает

# Пример с DataFrame:
df = pd.DataFrame(rng.integers(0, 10, (3, 4)), columns=["A", "B", "C", "D"])
print(df)

print(np.sin(df * 4))

# более того, индексы не просто сохраняются, но и согласовываются (т.е. даже если есть элементы, которые не присутствуют
# в одном из массивов (словарей) - индексы объединяются (появляются NaN)
dict1 = {
    'A': 10,
    'B': 20,
    'C': 30,
    'D': 40,
    'E': 50,
    'F': 60,
}

data_dict1 = pd.Series(dict1)
print(data_dict1)

dict2 = {
    'A': 11,
    'B': 21,
    'C': 31,
    'D': 41,
    'E': 51,
    'H': 71,
}

data_dict2 = pd.Series(dict2)
print(data_dict2)

df = pd.DataFrame({"dict_01": data_dict1, "dict_02":data_dict2})
print(df)

# то же самое и в Series
print(data_dict1 + data_dict2)

print(np.add(data_dict1,data_dict2))

print(data_dict1.add(data_dict2, fill_value=5)) # fill_value - значение, на которое мы заменим отсутствующее


dict1 = {
    'A': 10,
    'B': 20,
    'C': 30,
    'D': 40,
    'E': 50,
}

data_dict1 = pd.Series(dict1)
print(data_dict1)

dict2 = {
    'A': 11,
    'B': 21,
    'C': 31,
    'D': 41,
    'E': 51,
}

data_dict2 = pd.Series(dict2)
print(data_dict2)

df = pd.DataFrame({"dict_01": data_dict1, "dict_02":data_dict2})
print(df)

df1 = pd.DataFrame({"dict_10": data_dict1, "dict_02":data_dict2})
print(df + df1)

print(df.add(df1, fill_value=0))

# fill_value - мб не только числом, но и функцией
print(df.add(df1, fill_value=df.values.sum()))

# Итак, это всё было про согласованность индексов - никакие индексы никуда не пропадут (ВАЖНО при работе с данными)

# Транслирование: здесь в качестве массивов разных размеров используется Series(одномерный массив) DataFrame(двумерный)
A = rng.integers(10, size=(3, 4)) # массив NumPy
print(A)

print(A[0]) # 0 - строка

print(A - A[0])

# В Pandas
df = pd.DataFrame(A, columns=["A", "B", "C", "D"])
print(df)

print(df - df.iloc[0]) # построчное вычитание в DataFrame (Pandas)

print(df.subtract(df["A"], axis=0)) # вычитание по столбцам
# df["A"] - это столбцы в DataFrame

# и при этих операциях происходит согласование индексов - т.е. мы не теряем ни столбцы, ни метки строчек, NaN говорит о
# том, что в другом аргументе этой функции, которую мы использовали, этого значения просто нет