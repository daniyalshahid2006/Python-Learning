# import numpy as np
#
# # A = np.array([1, 2, 3])
# # B = np.array([4, 5, 6])
# #
# # print(np.dot(A, B))
# #
# # A = np.array([
# #     [1, 2],
# #     [3, 4]
# # ])
# #
# # B = np.array([
# #     [5, 6],
# #     [7, 8]
# # ])
# #
# # # print(np.matmul(A, B))
# # print((A@B))
#
#
# A = np.array([
#     [1, 2],
#     [3,4,],
#     [ 5, 6]
# ])
#
# print(A.T)
#
#
#
# A = np.array([
#     [1, 2],
#     [3, 4]
# ])
#
# print(np.linalg.det(A))


import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

print(np.linalg.inv(A))
