k = 5
#res = ''
lst = [5, 10, 0, 200]
res = [x + k for x in lst]
print(res)

# %%
lst = [1, 2, 3, 'text', True, 3+2j]

import numpy as np
from numpy.lib.shape_base import put_along_axis

arr = np.array(lst)

print(type(arr[0]), type(arr[2]),type(arr[5]))


# %%
lst = [56, 45, 12, 6]

import numpy as np

arr = np.array(lst)
print(arr.nbytes)
# %%
arr = np.array([2,5,6,8], dtype= int)
print(arr)
print(type(arr))
print(np.result_type(arr))
# %%
lst1 = [5, 10, 0, 200]
import numpy as np

arr = np.array(lst1)

print(arr + 5)

# %%
lst2= [1,2,3, 'jchjhfjh', 'True', 3+2j]

#import numpy as np

#arr = np.array(lst2)

#print(type(arr[3]), type(arr[5]))
# %%
lst3 = [56, 48, 16, 6]

import numpy as np

arr = np.array(lst3)

print(arr.nbytes)
# %%
import numpy as np

Narr = np.random.rand((6))

print((Narr))
# %%
import numpy as np

arr1 = np.array( [25, 56, 12, 85, 34,75])

print(arr1.dtype)

arr1 = arr1.astype(complex)

print(arr1.dtype)

print(arr1)

# %%
import numpy as np
print(np.array([5,6,8,45,12,52]).reshape(2,3))

# %%
print(np.matrix([[1,2],
                [3,4]]))
                
# %%
print(np.eye(3))


# %%
print(np.zeros((4,3)))
# %%
print(np.ones((3,3), dtype = np.float64))
# %%
import numpy as np
arr1 =np.array([25, 56, 12, 85, 34, 75])
arr2 = np.array([42, 3, 86, 32, 856, 46])

arr1_mat = np.array(arr1).reshape(2,3)
arr2_mat = np.array(arr2).reshape(2,3)
print(arr1_mat)
print(arr2_mat)
Trans_arr1 = (arr1_mat*arr1_mat - arr2_mat*arr2_mat)
print(Trans_arr1)
Trans_arr2 = (arr1_mat - arr2_mat)
print(Trans_arr2)
#final_arr = Trans_arr.astype(complex)
result_arr = Trans_arr1 / Trans_arr2
result_arr = result_arr.astype(complex)
print(result_arr)
# %%

import numpy as np

arr1 = np.ones(10)
arr2 = np.arange(10, dtype = np.float64)
arr3 = arr1 + arr2 
print(np.result_type(arr1))
print(np.result_type(arr3))
# %%

import numpy as np
arr = np.arange(4)
print(arr)
arr.reshape(2,2)
print(arr.shape)
# %%
import numpy as np

arr = np.arange(4).reshape(4, 1)
print(arr)
print(arr.shape)
# %%
import numpy as np
S_X = np.array([[2, 5, 6, 5], [4, 8, 6, 5]])

print(S_X)

S_Y = np.array([[6, 7, 5, 9], [7, 5, 6, 4]])

print(S_Y)

print(S_Y - S_X)

print(S_X < 2)

twos_mat = np.ones((2, 4)) * 2
print(twos_mat)
print(np.less(S_Y, twos_mat))
# %%
import numpy as np 

mat = (np.zeros((4, 4), dtype = int))
print(mat)
diag_parent = np.diag([4, 5, 6], 1)
print(diag_parent)

# %%
import numpy as np

arr = np.arange(11)
print(arr)

m = (arr > 6)
arr[m] *= -1
print(arr)
# %%
import numpy as np
mat = np.array([['abc', 'A'], ['def', 'B'], ['ghi', 'C'], ['jkl', 'D'] ])
arr = np.array(['abc', 'def', 'ghi', 'kjl'])

print(mat)
print(arr)

print(np.mat(4) = arr

# %%
import numpy as np
print(np.__version__)
np.show_config()
Z = np.zeros(10)
print(Z)
# %%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
# %%
fileHandle = open('test1.txt')
print(fileHandle.read())
fileHandle.close()

# %%
x = 4
z = 3

x, z = z, x
print(z, x)

# %%

# %%
