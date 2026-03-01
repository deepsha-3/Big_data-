import numpy as np
import time

# Python list vs NumPy array performance comparison
py_list = list(range(1000000))
np_array = np.arange(1000000)

# Python list operation
start = time.time()
py_result = [x * 2 for x in py_list]
py_time = time.time() - start

# NumPy array operation
start = time.time()
np_result = np_array * 2
np_time = time.time() - start

print(f"Python list time: {py_time:.4f} seconds")
print(f"NumPy array time: {np_time:.4f} seconds")
print(f"NumPy is {py_time/np_time:.2f}x faster!")

