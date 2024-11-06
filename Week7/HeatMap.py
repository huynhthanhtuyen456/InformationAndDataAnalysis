# Heat map optimised for PyCharm in full-screen mode

import numpy as np
import matplotlib.pyplot as plt


# This subroutine encapsulates the 'plot' method, as the most suitable for raster rendering
def DrawBox(x, y, size, r, g, b):
    for i in range(0, int(size)):
        if r < 0:
            r = int(0)
        if r > 255:
            r = int(255)
        if g < 0:
            g = int(0)
        if g > 255:
            g = int(255)
        if b < 0:
            b = int(0)
        if b > 255:
            b = int(255)
        plt.plot([x, x + size], [y + i, y + i], '#{:02x}{:02x}{:02x}'.format(r, g, b))


# Initialise NumPy arrays containing the average monthly temperatures for 7 cities
City1 = np.array([6, 8, 11, 16, 21, 25, 27, 26, 23, 17, 10, 6], dtype=int)
City2 = np.array([4, 6, 12, 17, 21, 25, 28, 27, 23, 17, 11, 6], dtype=int)
City3 = np.array([9, 11, 13, 15, 18, 21, 23, 23, 21, 17, 13, 9], dtype=int)
City4 = np.array([-2, 1, 5, 9, 14, 20, 23, 21, 17, 10, 3, -2], dtype=int)
City5 = np.array([-2, 1, 4, 10, 15, 21, 24, 23, 19, 12, 7, 1], dtype=int)
City6 = np.array([1, 2, 6, 12, 17, 22, 25, 24, 20, 14, 8, 3], dtype=int)
City7 = np.array([15, 17, 19, 22, 25, 27, 27, 27, 26, 23, 20, 17], dtype=int)

# Initialise a two-dimensional array containing the average monthly temperatures
Cities = np.array([City1, City2, City3, City4, City5, City6, City7], dtype=int)

# Extract the minimum and the maximum values
Min = np.min(Cities)
Max = np.max(Cities)

# Setup the plotting area
plt.axis([0, 600, 0, 400])
plt.xticks([])
plt.yticks([])

# Initialise box size and offsets
BoxSize = int(40)
OffsetX = int(15)
OffsetY = int(12)

# Visualise the heat map
for i in range(0, Cities.shape[0]):
    for j in range(0, Cities.shape[1]):
        ColourCode = int(((Cities[i, j]-Min)/(Max-Min))*255)
        DrawBox(60+BoxSize*j, 300-BoxSize*i, BoxSize, ColourCode, 0, 0)
        plt.text(OffsetX+60+BoxSize*j, OffsetY+300-BoxSize*i, str(Cities[i, j]), color='#FFFFFF')

# Visualise the colour scale
for i in range(0, 280):
    plt.plot([560, 580], [i + 60, i + 60], '#{:02x}{:02x}{:02x}'.format(int((i / 280) * 255), 0, 0))
    
plt.text(585, 58, str(Min))
plt.text(585, 335, str(Max))

# Print the months
plt.text(72, 20, 'Jan')
plt.text(112, 20, 'Feb')
plt.text(152, 20, 'Mar')
plt.text(192, 20, 'Apr')
plt.text(232, 20, 'May')
plt.text(272, 20, 'Jun')
plt.text(312, 20, 'Jul')
plt.text(352, 20, 'Aug')
plt.text(392, 20, 'Sep')
plt.text(432, 20, 'Oct')
plt.text(472, 20, 'Nov')
plt.text(512, 20, 'Dec')

# Print the names of the cities
plt.text(5, 315, 'Phoenix')
plt.text(5, 275, 'Little Rock')
plt.text(5, 235, 'Sacramento')
plt.text(5, 195, 'Denver')
plt.text(5, 155, 'Hartford')
plt.text(5, 115, 'Dover')
plt.text(5, 75, 'Tallahassee')

# Generate the chart
plt.show()