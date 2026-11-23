import pandas as pd

df = pd.DataFrame({'column1': [1, 2, 3], 'column2': [4, 5, 6]})
print(df)

import numpy as np
array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)

array2 = np.zeros((3, 3))
print(array2)

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)
plt.title('Sample Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()