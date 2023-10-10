import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2023)

a = np.random.randint(1, 100, 20)

plt.plot(a, color='green')


index1 = 0
index = 1
deepNumberLeft = 0

for i in range(len(a) - 1):
    difference = (abs((a[i] - a[i+1])))
    b = i+1
    if difference > deepNumberLeft and a[b] < a[b+1] > 0:
        deepNumberLeft = difference
        index1 = i


lastPoint = 0


for i in range(len(a) - 1):
    if i == index1:
        lastPoint = i + 1
        index = index
        plt.plot([i, lastPoint], [a[i], a[lastPoint]], 'r-', linewidth=2)
print(a)



while (lastPoint + index) < len(a) and a[lastPoint] < a[lastPoint + index]:
    print(lastPoint, index)
    plt.plot([lastPoint, (lastPoint + index)], [a[lastPoint], a[(lastPoint + index)]], 'r-', linewidth=2)
    lastPoint = lastPoint + 1

plt.show()