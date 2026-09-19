import numpy as np
A = np.array([1,2,3,4,5,6,7,8,9])
print(A+10)
numbers = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
print(numbers + np.array([10, 20, 30]))
print(numbers + np.array([10, 20, 30]) + 10)
B = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9]])
print(B+np.array([10,20,30,40,50,60,70,80,90]))