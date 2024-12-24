import re
import numpy as np

string = input()
regex = re.compile(r'[^\d]+')
shape =  re.split(regex, string)

matrix = np.random.randint(1, 101, size=(int(shape[0]), int(shape[1])))
res = matrix.sum(axis=1)
print(matrix)
print(res)
