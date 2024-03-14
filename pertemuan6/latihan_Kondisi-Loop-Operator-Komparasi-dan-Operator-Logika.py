import numpy as np
import matplotlib.pyplot as plt

# Create a 2D array of random integers
arr = np.random.randint(0, 3, size=(10, 10))

# Define the center and radius of the circle
center = [4, 4]
radius = 3

# Loop over each element in the array
for i in range(10):
    for j in range(10):
        # Check if the current element is within the circle using logical operators
        if (i - center[0])**2 + (j - center[1])**2 <= radius**2 and (i - center[0])**2 + (j - center[1])**2 >= (radius - 1)**2:
            # Set the element to yellow if it's on the boundary
            arr[i, j] = 2
        elif (i - center[0])**2 + (j - center[1])**2 < (radius - 1)**2:
            # Set the element to white if it's inside the circle
            arr[i, j] = 1
        else:
            # Set the element to black if it's outside the circle
            arr[i, j] = 0

# Create a colormap for the array
cmap = {'0': 'black', '1': 'white', '2': 'yellow'}

# Plot the array as an image using a built-in colormap
plt.imshow(arr, cmap='gray')
plt.show()
