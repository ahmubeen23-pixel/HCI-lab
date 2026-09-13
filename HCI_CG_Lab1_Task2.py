Task 2 — Synthetic Image Matrix Creation

import numpy as np
import matplotlib.pyplot as plt

# Create a 300 x 400 x 3 RGB image array
img = np.zeros((300, 400, 3), dtype=np.uint8)

# Fill four quadrants
img[:150, :200] = [255, 0, 0]       # Red
img[:150, 200:] = [0, 255, 0]       # Green
img[150:, :200] = [0, 0, 255]       # Blue
img[150:, 200:] = [255, 255, 255]   # White

# Display image
plt.imshow(img)
plt.title("300 x 400 Synthetic RGB Image")
plt.axis("off")
plt.show()

# Array information
print("Array Shape (H, W, C):", img.shape)
print("Data Type:", img.dtype)
print("Total Elements:", img.size)
print("Memory Footprint:", img.nbytes, "bytes")
print("Memory Footprint: {:.2f} KB".format(img.nbytes / 1024))
