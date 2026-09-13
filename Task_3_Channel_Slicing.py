# HCI & Computer Graphics - Lab 1
# Task 3: Channel Slicing & Isolation
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = np.array(Image.open("sample.jpg").convert("RGB"))

red = img[:, :, 0]
green = img[:, :, 1]
blue = img[:, :, 2]

red_only = np.zeros_like(img)
green_only = np.zeros_like(img)
blue_only = np.zeros_like(img)

red_only[:, :, 0] = red
green_only[:, :, 1] = green
blue_only[:, :, 2] = blue

print("--- CHANNEL EXTRACTION SUMMARY ---")
print("Original Image Shape:", img.shape)
print("Red Channel Shape:", red.shape)
print("Green Channel Shape:", green.shape)
print("Blue Channel Shape:", blue.shape)

fig, axes = plt.subplots(2, 3, figsize=(12, 7))
axes[0, 0].imshow(red_only); axes[0, 0].set_title("Red-Only")
axes[0, 1].imshow(green_only); axes[0, 1].set_title("Green-Only")
axes[0, 2].imshow(blue_only); axes[0, 2].set_title("Blue-Only")
axes[1, 0].imshow(red, cmap="gray"); axes[1, 0].set_title("Red Intensity Map")
axes[1, 1].imshow(green, cmap="gray"); axes[1, 1].set_title("Green Intensity Map")
axes[1, 2].imshow(blue, cmap="gray"); axes[1, 2].set_title("Blue Intensity Map")

for ax in axes.ravel():
    ax.axis("off")

plt.tight_layout()
plt.show()
