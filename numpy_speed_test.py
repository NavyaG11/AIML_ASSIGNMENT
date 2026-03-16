import numpy as np
import time

size = 1000000

# Python list
start = time.time()
list_numbers = [i for i in range(size)]
list_squared = [i*i for i in list_numbers]
end = time.time()

print("Python List Time:", end - start)

# NumPy array
start = time.time()
array_numbers = np.arange(size)
array_squared = array_numbers ** 2
end = time.time()

print("NumPy Array Time:", end - start)