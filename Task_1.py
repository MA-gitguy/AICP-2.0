import numpy as np

#1
even_num = np.arange(30, 70, 2)
print("Even numbers b/w 30 & 70 is are: \n", even_num)

#2
random_num = np.random.randn(15)
print("\n15 Random numbers from SND: \n", random_num)

#3
M_1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
M_2 = np.array([[9,8,7], [6,5,4], [3,2,1]])
C_Matrix = np.cross(M_1, M_2)
print("\nCross Product of 2 Matrices is: \n", C_Matrix)

#4
D_array = np.array([[2,3], [4,5]])
result = np.linalg.det(D_array)
print("\n\nThe Determinent of the metrix is: ", result)

#5
R_3x3 = np.random.random((3,3,3))
print("\n3x3x3 array metrices with random values: \n", R_3x3)

#6
R_5x5 = np.random.random((5, 5))
print("\n5x5 array metrices with random value: \n", R_5x5)
print("\nMinimum value is: ", np.min(R_5x5))
print("Maximum value is: ", np.max(R_5x5))

#7
arr = np.array([[1,2], [4,5]])
mean_arr = np.mean(arr, axis=1)
std_arr = np.std(arr, axis=1)
variance_arr = np.var(arr, axis=1)
print("On Second axis: \n Mean = \t\t", mean_arr)
print("Standard Deviation =    ", std_arr)
print("Variance = \t\t", variance_arr)