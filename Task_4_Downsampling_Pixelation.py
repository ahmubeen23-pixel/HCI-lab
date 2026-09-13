# HCI & Computer Graphics - Lab 1
# Task 4: Spatial Downsampling & Pixelation via Striding
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = np.array(Image.open("sample.jpg").convert("RGB"))
N = 8

downsampled = img[::N, ::N, :]
reexpanded = np.repeat(np.repeat(downsampled, N, axis=0), N, axis=1)
reexpanded = reexpanded[:img.shape[0], :img.shape[1], :]

print("--- DOWNSAMPLING ANALYSIS ---")
print("Original Shape:", img.shape)
print("Original Memory:", img.nbytes, "bytes")
print("Downsampled Shape:", downsampled.shape)
print("Downsampled Memory:", downsampled.nbytes, "bytes")
print("Re-expanded Shape:", reexpanded.shape)

dimension_reduction = (1 - downsampled.shape[0] / img.shape[0]) * 100
memory_reduction = (1 - downsampled.nbytes / img.nbytes) * 100
print(f"Dimension Reduction: {dimension_reduction:.2f}% per axis")
print(f"Memory Savings: {memory_reduction:.2f}%")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].imshow(img); axes[0].set_title(f"Original {img.shape}"); axes[0].axis("off")
axes[1].imshow(reexpanded); axes[1].set_title(f"Pixelated / Re-expanded {reexpanded.shape}"); axes[1].axis("off")
plt.tight_layout()
plt.show()
