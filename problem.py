k = 5
#res = ''
lst = [5, 10, 0, 200]
res = [x + k for x in lst]
print(res)

# %%
lst = [1, 2, 3, 'text', True, 3+2j]

import numpy as np

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
