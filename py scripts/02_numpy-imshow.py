import numpy as np
import matplotlib.pyplot as plt

arr = np.array(np.zeros((10,10)))  # create array of zeros
print("initial array of zeroes")
print(arr)

arr[3:7, 1] = 2  # set column 1 of rows 3 to 6 to 1
arr[1,:] = np.arange(0,1.0,0.1)  # set row 1 to values from 0 to 0.9
print("new array")
print(arr)

plt.imshow(arr, cmap='grey', vmin=0, vmax=2)  # display array as image
plt.colorbar(label='Value')  # add colorbar
plt.savefig("output/numpy_imshow.png", dpi=300)  # save figure
plt.show()