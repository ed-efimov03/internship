import math
import numpy as np
import random

data = list()
PI = math.pi
n = 10_000
amplitude = 30

for i in range(n):
    y = math.sin((PI/50)*i) * amplitude
    y = round(y, 2) + round(random.uniform(-5, 5), 2)
    data.append(y)

data = np.array(data)

mean = round(data.mean(), 3)

print(f'Средняя температура: {mean}')
print(f'Стандартное отклонение: {np.std(data):.3f}')
print(f'Минимальная температура: {np.min(data):.2f}, его индекс: {np.argmin(data)}')
print(f'Максимальная температура: {np.max(data):.2f}, его индекс: {np.argmax(data)}')

c = 0
c_max = c
for i in data:
    if i < mean:
        c += 1
    elif c > c_max:
        c_max = c
        c = 0

print(f'Максимальное кол-во дней, когд атемпература была меньше средней: {c_max}')
    




