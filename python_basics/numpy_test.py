import numpy as np
arr = np.array([1,2,3,6, np.nan, 9])
print(np.isnan(arr))

print(np.nan_to_num(arr, nan=30))