#Create an array of even numbers from 10 to 50.
import numpy as np

arr = np.arange(10, 51, 2) # start, stop, step

print(arr)

print(np.all(arr % 2 == 0))
