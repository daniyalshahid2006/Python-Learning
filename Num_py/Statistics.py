# import numpy as np
#
# numbers = np.array([10, 20, 30, 40, 50])
#
# # print(np.mean(numbers))
# # print(np.median(numbers))
# # print(np.min(numbers))
# # print(np.max(numbers))
# # print(np.sum(numbers))
#
#
# print(np.std(numbers))
# print(np.var(numbers))


# import numpy as np
#
# numbers = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])
#
# print(np.mean(numbers, axis=0))
# print(np.mean(numbers, axis=1))

#
# import numpy as np
#
# numbers = np.array([10, 20, 30, 40, 50])
#
# print(np.percentile(numbers, 40))


import numpy as np

hours = np.array([1, 2, 3, 4, 5])
marks = np.array([20, 40, 60, 80, 100])

print(np.corrcoef(hours, marks))