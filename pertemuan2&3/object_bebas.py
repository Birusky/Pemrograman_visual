import numpy as np
import matplotlib.pyplot as plt

def draw_diamond(image, center, width, height, color):
    pr, pg, pb = color
    hdw = int(width / 2)
    hdh = int(height / 2)

    for i in range(center[0] - hdw, center[0] + hdw + 1):
        for j in range(center[1] - hdh, center[1] + hdh + 1):
            if (i - center[0]) * height + (j - center[1]) * width <= 0 and (i - center[0]) * height - (j - center[1]) * width >= 0:
                image[j, i, 0] = pr
                image[j, i, 1] = pg
                image[j, i, 2] = pb

row, col = 500, 500
Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)

diamond_center = (250, 250)
diamond_width = 100
diamond_height = 150
diamond_color = [255, 0, 255]  # Magenta color

draw_diamond(Gambar, diamond_center, diamond_width, diamond_height, diamond_color)

plt.figure('Layang-layang')
plt.imshow(Gambar)
plt.show()
