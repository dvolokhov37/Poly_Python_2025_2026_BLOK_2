import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# ГРАФИК 1: Два графика с маркерами
fig, ax = plt.subplots()
x = np.array([2, 5, 10, 15, 20])
y1 = np.array([1, 7, 3, 5, 11])
y2 = np.array([4, 3, 1, 8, 12])

ax.plot(x, y1, 'o-', color='red', linewidth=2, markersize=8, label='line 1')
ax.plot(x, y2, 'o-.', color='green', linewidth=2, markersize=8, label='line 2')

ax.legend(loc='upper left')
plt.show()

# ГРАФИК 2: Три графика с GridSpec
fig = plt.figure(figsize=(10, 6))
grid = plt.GridSpec(2, 2, hspace=0.4)

x_top = [1, 2, 3, 4, 5]
y_top = [1, 7, 6, 3, 5]

x_bl = [1, 2, 3, 4, 5]
y_bl = [9, 4, 2, 4, 9]

x_br = [1, 2, 3, 4, 5]
y_br = [-7, -4, 2, -4, -7]

# Верхний график
ax1 = fig.add_subplot(grid[0, :])
ax1.plot(x_top, y_top)

# Нижний левый
ax2 = fig.add_subplot(grid[1, 0])
ax2.plot(x_bl, y_bl)

# Нижний правый
ax3 = fig.add_subplot(grid[1, 1])
ax3.plot(x_br, y_br)

plt.show()

# ГРАФИК 3: Парабола со стрелкой
fig, ax = plt.subplots()
x = np.linspace(-5, 5, 15)
y = x**2
ax.plot(x, y)

ax.annotate('min',
            xy=(0, 0),
            xytext=(0, 10),
            fontsize=11,
            arrowprops=dict(
                facecolor='green',
                edgecolor='black',
                width=4,
                headwidth=12,
                headlength=15,
            ))

plt.show()

# ГРАФИК 4: Тепловая карта (heatmap)
fig, ax = plt.subplots()
data = np.random.randint(0, 11, size=(7, 7))
im = ax.imshow(data, cmap='viridis', aspect='equal')
ax.set_xticks(np.arange(7))
ax.set_yticks(np.arange(7))
plt.colorbar(im, ax=ax, shrink=0.5, anchor=(0, 0))
plt.show()

# ГРАФИК 5: График косинуса с заливкой
fig, ax = plt.subplots()
x = np.linspace(0, 5, 1000)
y = np.cos(np.pi * x)

ax.plot(x, y, 'r-', linewidth=2)
ax.fill_between(x, y, 0, color='blue', alpha=0.7)

plt.show()

# ГРАФИК 6: Косинусоида с разрывами (маскирование)
fig, ax = plt.subplots()
x = np.linspace(0, 5, 500)
y = np.cos(np.pi * x)

y_masked = np.where(y < -0.5, np.nan, y)

ax.plot(x, y_masked, linewidth=2)
ax.set_ylim(-1, 1)
ax.set_yticks(np.arange(-1.00, 1.01, 0.25))
ax.set_xticks([0, 1, 2, 3, 4])
plt.show()

# ГРАФИК 7: Три типа ступенчатых графиков
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
x = np.arange(7)
y = np.arange(7)

xlims = (-0.3, 6.25)
ylims = (-0.3, 6.25)

# Левый график: шаг до точки
axes[0].step(x, y, where='pre', color='green', marker='o', linewidth=1.5)
axes[0].grid(True)
axes[0].set_xlim(xlims)
axes[0].set_ylim(ylims)

# Средний график: шаг после точки
axes[1].step(x, y, where='post', color='green', marker='o', linewidth=1.5)
axes[1].grid(True)
axes[1].set_xlim(xlims)
axes[1].set_ylim(ylims)

# Правый график: шаг посередине
axes[2].step(x, y, where='mid', color='green', marker='o', linewidth=1.5)
axes[2].grid(True)
axes[2].set_xlim(xlims)
axes[2].set_ylim(ylims)

plt.show()

# ГРАФИК 8: Стек графиков (Stackplot)
fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)

y1 = x * (10 - x) * 0.2
y2 = x * (10 - x) * 0.4
y3 = x * (10 - x) * 0.45

ax.stackplot(x, y1, y2, y3, labels=['y1', 'y2', 'y3'])
ax.legend(loc='upper left')
ax.set_xlim(0, 10)
plt.show()

# ГРАФИК 9: Круговая диаграмма (Pie) с "выпавшим" куском
labels = ['Toyota', 'Ford', 'Jaguar', 'AUDI', 'BMV']
sizes = [10, 15, 25, 15, 35]
colors = ['#ff7f0e', '#1f77b4', '#9467bd', '#d62728', '#2ca02c']
explode = (0, 0, 0, 0, 0.1)

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, explode=explode,
       startangle=90, counterclock=False, autopct=None)
plt.show()

# ГРАФИК 10: Кольцевая диаграмма (Donut chart)
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors,
       startangle=90, counterclock=False,
       wedgeprops=dict(width=0.4, edgecolor='w'))
plt.show()