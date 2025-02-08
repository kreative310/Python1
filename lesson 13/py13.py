import numpy as np
import pandas as pd

arr_2d = np.array([[1,2,3,4,5,], [6,7,8,9,10]])
print(arr_2d)

element = arr_2d[1,2]
print(element)

dimension = arr_2d.ndim
print(dimension)

arr_size = arr_2d.size
print(arr_size)


products = ['apples', 'cherry', 'oranges', 'tangerines']

sales = ['200', '470', '221', '55']

sales_series = pd.series(sales, index=idxmax)

best_selling_product = sales_series.idxmax()
print(best_selling_products)

