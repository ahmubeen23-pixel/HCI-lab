Task 1 — Display Pixel Density (PPI/DPI) Calculator

import math

def calculate_ppi(width, height, diagonal_inches):
    diagonal_pixels = math.sqrt(width**2 + height**2)
    ppi = diagonal_pixels / diagonal_inches
    total_pixels = width * height
    aspect = math.gcd(width, height)
    aspect_ratio = f"{width // aspect}:{height // aspect}"
    return total_pixels, aspect_ratio, ppi

# Desktop Monitor
desktop = calculate_ppi(1920, 1080, 24)
print("Desktop Monitor")
print("Total Pixels:", desktop[0])
print("Aspect Ratio:", desktop[1])
print("PPI/DPI: {:.2f}".format(desktop[2]))

# Smartphone
phone = calculate_ppi(1170, 2532, 6.1)
print("\nSmartphone")
print("Total Pixels:", phone[0])
print("Aspect Ratio:", phone[1])
print("PPI/DPI: {:.2f}".format(phone[2]))
