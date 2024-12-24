import numpy as np

matrix = np.random.uniform(low=1.01, high=9.9, size=(10,10))
matrix = np.around(matrix, decimals=2)

print("Матрица 10х10:", matrix, sep='\n')

print("Главная диагональ:", np.diag(matrix), sep = '\n')

print(f'Среднее значение: {np.mean(matrix):.2f}')
print(f'Максимальное значение: {np.max(matrix):.2f}')
print(f'Минимальное значение: {np.min(matrix):.2f}')
print(f'Медианное значение: {np.median(matrix):.2f}')
print(f'Дисперсия: {np.var(matrix):.2f}')
print(f'Стандартное отклонения {np.std(matrix):.2f}')