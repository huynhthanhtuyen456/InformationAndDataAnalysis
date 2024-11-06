import numpy as np
import matplotlib.pyplot as plt

Dimension = int(6)
NumberOfSamples = int(50)
Scale = int(1000)
MyArray = np.zeros(shape=(NumberOfSamples, Dimension), dtype=int)

# Dimension 1: Random values
for i in range(0, NumberOfSamples):
    MyArray[i, 0] = int(np.random.randint(0, Scale))

# Dimension 2: Equally spaced values
for i in range(0, NumberOfSamples):
    MyArray[i, 1] = int(i*(Scale/NumberOfSamples))

# Dimension 3: Inverse the values around the middle of the scale
for i in range(0, NumberOfSamples):
    if MyArray[i, 1] <= Scale/2:
        MyArray[i, 2] = int(MyArray[i, 1]+int(Scale/2))
    if MyArray[i, 1] > Scale/2:
        MyArray[i, 2] = int(MyArray[i, 1]-int(Scale/2))

# Dimension 4: values equal to Dimension 3
for i in range(0, NumberOfSamples):
    MyArray[i, 3] = int(MyArray[i, 2])

# Dimension 5: all values are in the middle of the scale
for i in range(0, NumberOfSamples):
    MyArray[i, 4] = int(Scale/2)

# Dimension 6: Round the values to the closest hundred
for i in range(0, NumberOfSamples):
    MyArray[i, 5] = int((np.trunc(MyArray[i, 3]/100)*100))

# Print the values
for j in range(0, Dimension):
    print(MyArray[i][j], ' ', end='')
print(' ')

# Spine names, must be the same number as Dimension
Name = ['a', 'b', 'c', 'd', 'e', 'f']

# Test for random RGB in hex
k = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
MyC = '#'
for i in range(0, 6):
    s = np.random.choice(k)
    MyC = MyC + s
print(MyC)

# Spines
for i in range(0, Dimension):
    plt.vlines(i, 0, Scale, '#808080')

# Generate the parallel coordinates
for i in range(0, NumberOfSamples):
    MyC = '#'
    for j in range(0, 6):
        s = np.random.choice(k)
        MyC = MyC + s
    plt.plot(Name, MyArray[i], MyC)

plt.show()