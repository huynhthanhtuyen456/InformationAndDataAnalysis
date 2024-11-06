import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Store the CSV file into a data frame
df = pd.read_csv('Week8/Vehicles.csv')

# Print the dataset on the screen
D = df.to_string()
print(D)

# Print the dimensions of the dataset
print('Number of Rows: ', df.shape[0])
print('Number of Columns: ', df.shape[1])

# Save the dataset as NumPy array
MyArray = df.to_numpy()

# Change textual data to numerical
for i in range(0, MyArray.shape[0]):
    for j in range(0, MyArray.shape[1]):
        if MyArray[i, j] == 'Japan':
            MyArray[i, j] = int(1)
        if MyArray[i, j] == 'US':
            MyArray[i, j] = int(2)
        if MyArray[i, j] == 'Europe':
            MyArray[i, j] = int(3)

# Declare new array of type float
MyData = np.empty(shape=(MyArray.shape[0], MyArray.shape[1]), dtype=float)

# Assign new values to array
for i in range(0, MyData.shape[0]):
    for j in range(0, MyData.shape[1]):
        MyData[i, j] = float(MyArray[i, j])


# Normalise the year
for i in range(0, MyData.shape[0]):
    MyData[i, 6] = float(MyArray[i, 6] - 1970.0)

# Find the maximum values per column
Maximum = np.amax(MyData, axis=0)

# Normalise to interval 0 .. 100
for i in range(0, MyData.shape[0]):
    for j in range(0, MyData.shape[1]):
        MyData[i, j] = float(MyData[i, j]*(100.0/Maximum[j]))

# Spine names
name = ['MPG', 'Cyl', 'Engine', 'HP', 'Weight', '0to60', '1970\nYear', 'Origin']

# Test for random RGB in hex
k = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
MyC = '#'
for i in range(0, 6):
    s = np.random.choice(k)
    MyC = MyC + s
print(MyC)

# Spines
for i in range(0, MyData.shape[1]):
    plt.vlines(i, 0, 100, '#808080')

# Vehicles from Japan
for i in range(0, MyData.shape[0]):
    if MyData[i, 7] < float(40.0):
        MyC = '#'
        for j in range(0, 6):
            s1 = np.random.choice(k)
            s2 = np.random.choice(k)
            MyC = '#' + s1 + s2 + '0000'
        plt.plot(name, MyData[i], '#FF0000')

# Vehicles from US
for i in range(0, MyData.shape[0]):
    if 40. < MyData[i, 7] < 80.0:
        MyC = '#'
        for j in range(0, 6):
            s1 = np.random.choice(k)
            s2 = np.random.choice(k)
            MyC = '#' + '00' + s1 + s2 + '00'
        plt.plot(name, MyData[i], '#00FF00')

# Vehicles from Europe
for i in range(0, MyData.shape[0]):
    if 90.0 < MyData[i, 7]:
        MyC = '#'
        for j in range(0, 6):
            s1 = np.random.choice(k)
            s2 = np.random.choice(k)
            MyC = '#' + '0000' + s1 + s2
        plt.plot(name, MyData[i], '#0000FF')

plt.text(0, 101, round(Maximum[0]))
plt.text(1, 101, round(Maximum[1]))
plt.text(2, 101, round(Maximum[2]))
plt.text(3, 101, round(Maximum[3]))
plt.text(4, 101, round(Maximum[4]))
plt.text(5, 101, round(Maximum[5]))
plt.text(6, 101, round(Maximum[6]+1970))

plt.text(7.4, 33, 'Japan')
plt.text(7.4, 66, 'US')
plt.text(7.4, 99, 'EU')

plt.yticks([])

plt.show()