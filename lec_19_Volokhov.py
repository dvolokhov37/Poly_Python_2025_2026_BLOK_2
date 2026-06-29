# Рассмотрим несклько приложения к методам машинного обучения для разных задач
# 1) Фильтрация спама (имеем задачу бинарной классификации). Эти текстовые данные преобразовать должны
# в числа, т.к. модели не умеют работать с текстом, только с числами
# Это метод Векторизации:
# столбцы = слова (в тексте)
# строки = образцы текста
# ячейка = кол-во данных слов в данном тексте

# очистка данных: переводят символы в строчные, удаляются знаки препинания, стоп-слова, и далее заполняем эту матрицу

import numpy as np
import pandas as pd

data = pd.read_csv("spam.csv")
print(data.head())

data["Spam"] = data["Category"].apply(lambda x: 1 if x == "spam" else 0)

print(data.columns)

# Есть столбцы-категории и столбцы с сообщениями (message)

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["Message"])
w = vectorizer.get_feature_names_out()

# print(w)
# print(w[1000])
#
# print(X)
#
# print(X[:, 1000])

from sklearn.model_selection import train_test_split

X_tr, X_tst, y_tr, y_tst = train_test_split(data["Message"], data["Spam"], test_size=0.25)

from sklearn.naive_bayes import MultinomialNB

from sklearn.pipeline import Pipeline

md = Pipeline([("vectorizer", CountVectorizer()), ("nb", MultinomialNB())])

md.fit(X_tr, y_tr) # обучение

texts = [
    "Hi! How are you?", # 0
    "Win the lottery", # 0
    "Free subscription", # 1
    "Black Friday big discount shop offer", # 1
    "Nice to meet you" # 0
]

print(md.predict(texts))










