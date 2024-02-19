# pip install numpy
# pip install matplotlib
# pip install msvc-runtime
# pip install pandas
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# ar = np.array(a)
# ar2 = np.array([[10, 23, 4],
#                 [7, 5, 6],
#                 [3, 7, 11]])
# print(ar2[1, 1])
# print(ar2[0:2, 0:4])
# print(ar)
# print(ar + 2)
# print(ar * 4)
# print(ar * ar2)
# print(np.dot(ar, ar2))
# print(ar.T)

# turn_matrix = np.zeros((28, 28))
# for i in range(28):
#     turn_matrix[i, i] = 1
# turn_matrix[0:2, 0:2] = [[0.5, -math.sqrt(3)/2],
#                          [math.sqrt(3)/2, 0.5]]
# print(turn_matrix)
#
#
# with open('mnist_test.csv', 'r') as file:
#     number = np.fromstring(file.readlines()[100], sep=',', dtype=int)
#     number = number[1:].reshape((28, 28))
#
#
# turned = np.dot(number, turn_matrix)
# plt.imshow(turned, cmap='gray')
# plt.show()
# plt.imshow(number, cmap='gray')
# plt.show()


data1 = pd.DataFrame([[1, 2, 3, 4], [5, 6, 7, 8]], columns=['a', 'b', 'c', 'd'])
print(data1)
data = pd.read_csv('vhi_id_2_00-44-34_22.09.2023.csv', skiprows=0, header=1, index_col=False)
print(data[(data['year'] == 2020) & (data['VHI'] > 30)])
# pd.concat()
print(data['VHI'].min())
print(data['VHI'].max())
print(data['VHI'].std())
